// Основа — приёмник темы 7. Столбцы и проверки взяты из ТЗ-22.
// Вставьте ID таблицы: между /d/ и /edit в адресе Google Таблицы.
const SPREADSHEET_ID = 'PASTE_YOUR_SPREADSHEET_ID';
const HEADERS = [
  'request_id', 'created_at', 'name', 'phone', 'email', 'lead_type', 'zone',
  'slot', 'seats', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'status'
];

function doGet() {
  return jsonResponse({ok: true, service: 'respawn-leads'});
}

function doPost(e) {
  const payload = readPayload(e);
  const clean = key => String(payload[key] == null ? '' : payload[key]).trim();
  const requestId = clean('request_id');
  const name = clean('name');
  const phone = clean('phone');
  const email = clean('email');
  const leadType = clean('lead_type');
  const zone = clean('zone');
  const seats = Number(clean('seats'));
  let slot = clean('slot');

  if (!/^REQ-[A-F0-9]{8}-[A-F0-9]{4}-4[A-F0-9]{3}-[89AB][A-F0-9]{3}-[A-F0-9]{12}$/i.test(requestId)) {
    return jsonResponse({ok: false, error: 'invalid_request_id'});
  }
  if (name.length < 2 || name.length > 60) return jsonResponse({ok: false, error: 'invalid_name'});
  if (!/^\+7\d{10}$/.test(phone)) return jsonResponse({ok: false, error: 'invalid_phone'});
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return jsonResponse({ok: false, error: 'invalid_email'});
  }
  if (leadType !== 'booking' && leadType !== 'tournament') {
    return jsonResponse({ok: false, error: 'invalid_lead_type'});
  }
  if (['standard', 'vip', 'bootcamp', 'ps5'].indexOf(zone) === -1) {
    return jsonResponse({ok: false, error: 'invalid_zone'});
  }
  if (!Number.isInteger(seats) || seats < 1 || seats > 5) {
    return jsonResponse({ok: false, error: 'invalid_seats'});
  }
  if (zone === 'ps5' && seats > 4) return jsonResponse({ok: false, error: 'invalid_seats'});
  if (zone === 'bootcamp' && seats !== 5) return jsonResponse({ok: false, error: 'invalid_seats'});
  if (leadType === 'tournament') {
    slot = '';
    if (seats !== 5) return jsonResponse({ok: false, error: 'invalid_seats'});
  } else if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/.test(slot)) {
    return jsonResponse({ok: false, error: 'invalid_slot'});
  }
  const texts = [name, phone, email, leadType, zone, slot, clean('utm_source'), clean('utm_medium'), clean('utm_campaign'), clean('utm_content')];
  if (texts.some(value => value.length > 200)) return jsonResponse({ok: false, error: 'value_too_long'});

  const source = clean('utm_source') || 'direct';
  const medium = clean('utm_medium') || 'none';
  const campaign = clean('utm_campaign') || 'not_set';
  const content = clean('utm_content') || 'not_set';

  const lock = LockService.getScriptLock();
  if (!lock.tryLock(10000)) return jsonResponse({ok: false, error: 'busy_retry'});
  try {
    const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName('leads');
    if (!sheet || sheet.getRange(1, 1, 1, HEADERS.length).getValues()[0].join('|') !== HEADERS.join('|')) {
      return jsonResponse({ok: false, error: 'invalid_sheet_schema'});
    }
    const duplicate = sheet.getRange('A:A').createTextFinder(requestId)
      .matchEntireCell(true).matchCase(false).useRegularExpression(false).findNext();
    if (duplicate) return jsonResponse({ok: false, error: 'duplicate_request_id'});
    // status из браузера не читаем: новую строку всегда ставит приёмник.
    sheet.appendRow([
      requestId,
      new Date(),
      textCell(name),
      textCell(phone),
      textCell(email),
      leadType,
      zone,
      textCell(slot),
      seats,
      textCell(source),
      textCell(medium),
      textCell(campaign),
      textCell(content),
      'new'
    ]);
    SpreadsheetApp.flush();
    return jsonResponse({ok: true, request_id: requestId});
  } catch (error) {
    return jsonResponse({ok: false, error: 'storage_error'});
  } finally {
    lock.releaseLock();
  }
}

function setupSheet() {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  let sheet = ss.getSheetByName('leads');
  if (!sheet) sheet = ss.insertSheet('leads');
  sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]).setFontWeight('bold');
  sheet.setFrozenRows(1);
  sheet.getRange('B2:B1000').setNumberFormat('dd.MM.yyyy HH:mm');
  sheet.getRange('D2:D1000').setNumberFormat('@');
  const statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['new', 'confirmed', 'paid', 'came', 'cancelled'], true)
    .setAllowInvalid(false)
    .build();
  sheet.getRange('N2:N1000').setDataValidation(statusRule);
  sheet.clearConditionalFormatRules();
  const empty = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied('=AND($A2<>"";OR(C2="";D2="";F2="";G2="";I2="";J2="";K2="";L2="";M2="";N2=""))')
    .setBackground('#f4c7c3')
    .setRanges([sheet.getRange('A2:N1000')])
    .build();
  const duplicate = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied('=AND($A2<>"";COUNTIF($A$2:$A$1000;$A2)>1)')
    .setBackground('#fce8b2')
    .setRanges([sheet.getRange('A2:A1000')])
    .build();
  sheet.setConditionalFormatRules([empty, duplicate]);
}

function readPayload(e) {
  if (e && e.postData && e.postData.contents) {
    try {
      return JSON.parse(e.postData.contents);
    } catch (error) {
      return e.parameter || {};
    }
  }
  return (e && e.parameter) || {};
}

function textCell(value) {
  return /^[=+@-]/.test(value) ? "'" + value : value;
}

function jsonResponse(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
