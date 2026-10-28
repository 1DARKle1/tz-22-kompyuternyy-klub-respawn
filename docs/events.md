# События

Вызов `gtag('event', …)` один: `js/analytics.js`, строка 24, функция `track`. Кнопки с `data-event` доходят туда через обработчик клика на строке 56. Остальные события вызывают `RespawnTrack` из своих файлов. Автоматические события page_view, scroll, click, file_download, form_start и form_submit код не отправляет: их собирает расширенная статистика GA4.

| Событие | Где | Пример параметров |
|---|---|---|
| page_view | автоматически, любая страница | page_location, page_title |
| scroll | автоматически, прокрутка до 90 % | percent_scrolled = 90 |
| click | автоматически, внешняя ссылка | link_url, outbound = true |
| file_download | автоматически, ссылка на PDF в prices.html и tournament.html | file_name = club-rules.pdf |
| form_start | автоматически, первое поле формы lead-form | form_id = lead-form |
| form_submit | автоматически, отправка формы | form_id = lead-form |
| generate_lead | js/form.js, строка 234, только после ответа ok: true | lead_type = booking, lead_zone = vip, value = 525, currency = RUB |
| cta_click | клик по кнопке с data-event, например index.html герой | button_name = hero_booking, page_section = hero |
| zone_view | клик по карточке зоны, index.html и zones.html | zone = vip |
| booking_calc | js/calculator.js, строка 74, кнопка «Рассчитать» | zone = vip, seats = 1, hours = 3, time_band = weekday_day, total_price = 525 |
| package_select | кнопка «Выбрать» на prices.html | package_name = pack_3h_vip |
| game_search | js/games.js, строка 29, через 1 секунду после ввода | search_term = dota, results_count = 1 |
| tournament_view | index.html, кнопка «Открыть регламент»; tournament.html, «Подробнее о формате» | tournament_id = winter_cup_2026 |
| reaction_test_complete | js/reaction.js, строка 40, после пятой удачной попытки | reaction_ms = 240 |
| contact_click | телефон и почта в шапке и подвале | contact_type = phone |
| messenger_click | contacts.html, Telegram и WhatsApp | messenger = telegram |
| social_click | иконки в подвале и на thanks.html | network = vk, page_section = footer |
| form_error | js/form.js, строка 152 | field_name = phone, error_type = format |
| promo_copy | reaction.html, кнопка «Скопировать» | promo_code = REACT20 |
| video_play | index.html, кнопка «Смотреть видео» | video_title = club_tour |

Имена и параметры в нижнем регистре, короче 40 символов. Значения короче 100 символов. Имя, телефон и почта в параметрах и в адресе страницы не передаются.
