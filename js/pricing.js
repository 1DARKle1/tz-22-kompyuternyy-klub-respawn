/* Тариф считает время начала. Пакет и скидка 30% не складываются. */
(function () {
  var RATES = { standard: 150, vip: 250, bootcamp: 1100, ps5: 400 };
  var BAND_LABEL = {
    weekday_day: "дневные будни",
    evening: "вечер",
    night: "ночь"
  };

  function timeBand(date) {
    var day = date.getDay();
    var minutes = date.getHours() * 60 + date.getMinutes();
    var night = minutes >= 23 * 60 || minutes < 8 * 60;
    if (night) return "night";
    var weekday = day >= 1 && day <= 5;
    var morning = minutes >= 8 * 60 && minutes < 14 * 60;
    if (weekday && morning) return "weekday_day";
    return "evening";
  }

  function perSeat(zone) {
    return zone === "standard" || zone === "vip";
  }

  function quote(opts) {
    var zone = opts.zone;
    var seats = Number(opts.seats);
    var hours = Number(opts.hours);
    var start = opts.start instanceof Date ? opts.start : new Date(opts.start);
    var packageName = opts.packageName || "";
    var band = timeBand(start);
    var total;
    var formula;

    if (packageName === "pack_3h_standard" || packageName === "pack_3h_vip") {
      var unit = packageName === "pack_3h_standard" ? 400 : 650;
      zone = packageName === "pack_3h_standard" ? "standard" : "vip";
      hours = 3;
      total = unit * seats;
      formula = seats + " × " + unit + " ₽ = " + total + " ₽. Пакет «3 часа», скидка 30% не применяется.";
    } else if (packageName === "pack_night_standard" || packageName === "pack_night_vip") {
      var nightUnit = packageName === "pack_night_standard" ? 700 : 1100;
      zone = packageName === "pack_night_standard" ? "standard" : "vip";
      total = nightUnit * seats;
      formula = seats + " × " + nightUnit + " ₽ = " + total + " ₽. Ночной пакет 23:00–08:00.";
    } else if (band === "night" && perSeat(zone)) {
      var flat = zone === "standard" ? 700 : 1100;
      total = flat * seats;
      formula = "Ночной пакет: " + seats + " × " + flat + " ₽ = " + total + " ₽.";
    } else if (band === "weekday_day") {
      var rate = RATES[zone];
      var base = rate * hours * (perSeat(zone) ? seats : 1);
      total = Math.round((base * 70) / 100);
      if (perSeat(zone) && seats === 1) {
        formula = hours + " × " + rate + " × 0,7 = " + total + " ₽";
      } else if (perSeat(zone)) {
        formula = hours + " × " + rate + " × " + seats + " × 0,7 = " + total + " ₽";
      } else {
        formula = hours + " × " + rate + " × 0,7 = " + total + " ₽";
      }
    } else {
      var full = RATES[zone];
      total = full * hours * (perSeat(zone) ? seats : 1);
      formula = perSeat(zone)
        ? hours + " × " + full + " × " + seats + " = " + total + " ₽"
        : hours + " × " + full + " = " + total + " ₽. Цена за комнату или приставку, не за игрока.";
    }

    return {
      zone: zone,
      seats: seats,
      hours: hours,
      total: total,
      timeBand: band,
      bandLabel: BAND_LABEL[band],
      formula: formula,
      packageName: packageName
    };
  }

  window.RespawnPricing = { quote: quote, timeBand: timeBand };
})();
