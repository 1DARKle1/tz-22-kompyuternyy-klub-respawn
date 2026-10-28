# -*- coding: utf-8 -*-
"""Собирает статические HTML-страницы клуба. Запуск: python scripts/build_pages.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("index.html", "Главная"),
    ("zones.html", "Зоны"),
    ("prices.html", "Цены"),
    ("games.html", "Игры"),
    ("tournament.html", "Турнир"),
    ("reaction.html", "Реакция"),
    ("contacts.html", "Бронь"),
]

GAMES = [
    ("Counter-Strike 2", "Шутер", "Стандарт, VIP"),
    ("Dota 2", "MOBA", "Стандарт, VIP"),
    ("Valorant", "Шутер", "Стандарт, VIP"),
    ("League of Legends", "MOBA", "Стандарт, VIP"),
    ("Apex Legends", "Королевская битва", "Стандарт, VIP"),
    ("Fortnite", "Королевская битва", "Стандарт, VIP"),
    ("PUBG: BATTLEGROUNDS", "Королевская битва", "Стандарт, VIP"),
    ("Rainbow Six Siege", "Шутер", "Стандарт, VIP"),
    ("Overwatch 2", "Шутер", "Стандарт, VIP"),
    ("Call of Duty: Warzone", "Шутер", "VIP"),
    ("Escape from Tarkov", "Шутер", "VIP"),
    ("Rust", "Выживание", "Стандарт, VIP"),
    ("DayZ", "Выживание", "Стандарт"),
    ("Minecraft", "Песочница", "Стандарт, VIP"),
    ("Grand Theft Auto V", "Экшен", "Стандарт, VIP"),
    ("Cyberpunk 2077", "RPG", "VIP"),
    ("The Witcher 3", "RPG", "Стандарт, VIP"),
    ("Elden Ring", "RPG", "Стандарт, VIP"),
    ("Baldur's Gate 3", "RPG", "Стандарт, VIP"),
    ("Diablo IV", "RPG", "Стандарт, VIP"),
    ("World of Warcraft", "MMO", "Стандарт, VIP"),
    ("EA Sports FC 25", "Спорт", "Стандарт, VIP"),
    ("Rocket League", "Спорт", "Стандарт, VIP"),
    ("Mortal Kombat 1", "Файтинг", "Стандарт, VIP"),
    ("Street Fighter 6", "Файтинг", "Стандарт, VIP"),
    ("Tekken 8", "Файтинг", "VIP"),
    ("Dead by Daylight", "Хоррор", "Стандарт, VIP"),
    ("Phasmophobia", "Хоррор", "Стандарт"),
    ("Lethal Company", "Хоррор", "Стандарт"),
    ("Helldivers 2", "Шутер", "Стандарт, VIP"),
    ("Marvel Rivals", "Шутер", "Стандарт, VIP"),
    ("War Thunder", "Симулятор", "Стандарт"),
    ("Euro Truck Simulator 2", "Симулятор", "Стандарт"),
    ("Assetto Corsa", "Гонки", "VIP"),
    ("Stardew Valley", "Казуальная", "Стандарт"),
    ("Among Us", "Пати", "Стандарт"),
    ("Hearthstone", "Карточная", "Стандарт"),
    ("World of Tanks", "Шутер", "Стандарт, VIP"),
    ("Warface", "Шутер", "Стандарт"),
    ("Genshin Impact", "RPG", "Стандарт, VIP"),
    ("Path of Exile", "RPG", "Стандарт, VIP"),
    ("Lost Ark", "MMO", "Стандарт"),
    ("Destiny 2", "Шутер", "Стандарт, VIP"),
    ("Warframe", "Шутер", "Стандарт"),
    ("Hunt: Showdown", "Шутер", "VIP"),
    ("The Finals", "Шутер", "Стандарт, VIP"),
    ("Red Dead Redemption 2", "Экшен", "VIP"),
    ("Fall Guys", "Пати", "Стандарт"),
    ("God of War Ragnarök", "Экшен", "PlayStation 5"),
    ("Marvel's Spider-Man 2", "Экшен", "PlayStation 5"),
    ("Horizon Forbidden West", "Экшен", "PlayStation 5"),
    ("Gran Turismo 7", "Гонки", "PlayStation 5"),
    ("EA Sports FC 25 (PS5)", "Спорт", "PlayStation 5"),
    ("NBA 2K25", "Спорт", "PlayStation 5"),
    ("Mortal Kombat 1 (PS5)", "Файтинг", "PlayStation 5"),
    ("Tekken 8 (PS5)", "Файтинг", "PlayStation 5"),
    ("Helldivers 2 (PS5)", "Шутер", "PlayStation 5"),
    ("Fortnite (PS5)", "Королевская битва", "PlayStation 5"),
    ("Rocket League (PS5)", "Спорт", "PlayStation 5"),
    ("Minecraft (PS5)", "Песочница", "PlayStation 5"),
]

assert len(GAMES) == 60

HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="img/og.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ru_RU">
  <link rel="icon" href="img/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Orbitron:wght@600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>
</head>
<body>
<a class="skip" href="#main">К содержанию</a>
<header class="site-header">
  <div class="wrap header-bar">
    <a class="logo" href="index.html">RE<span>SPAWN</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Меню</button>
    <nav id="site-nav" class="site-nav" aria-label="Страницы клуба">
      {nav}
    </nav>
    <a class="header-phone" href="tel:+79002220222" data-event="contact_click" data-contact-type="phone">+7 (900) 222-02-22</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="logo">RE<span>SPAWN</span></p>
      <p>ООО «Респаун»</p>
      <p>614 122, г. Новоозёрск, ул. Студенческая, д. 2, ТЦ «Орбита», 3 этаж</p>
      <p><a href="tel:+79002220222" data-event="contact_click" data-contact-type="phone">+7 (900) 222-02-22</a></p>
      <p><a href="mailto:book@respawn-club.example" data-event="contact_click" data-contact-type="email">book@respawn-club.example</a></p>
    </div>
    <div>
      <p>Мы в сети</p>
      <ul class="social-list">
        <li><a href="https://instagram.com/respawn.nov2026" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="instagram" data-page-section="footer">Instagram</a></li>
        <li><a href="https://vk.com/respawn_nov2026" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="vk" data-page-section="footer">ВКонтакте</a></li>
        <li><a href="https://t.me/respawn_events" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="telegram" data-page-section="footer">Telegram</a></li>
        <li><a href="https://youtube.com/@respawn_nov2026" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="youtube" data-page-section="footer">YouTube</a></li>
      </ul>
    </div>
    <div>
      <p><a href="privacy.html">Политика конфиденциальности</a></p>
      <p><a href="files/club-rules.pdf">Правила клуба (PDF)</a></p>
    </div>
  </div>
  <div class="wrap">
    <p class="legal">Круглосуточно с 2023 года. Вход с 14 лет. С 22:00 до 08:00 и на ночные пакеты — только с 18 лет.</p>
  </div>
</footer>
{scripts}
</body>
</html>
"""


def nav(current):
    parts = []
    for href, label in NAV:
        mark = ' aria-current="page"' if href == current else ""
        parts.append(f'<a href="{href}"{mark}>{label}</a>')
    return "\n      ".join(parts)


def scripts(names):
    tags = ['<script src="js/analytics.js"></script>', '<script src="js/ui.js"></script>']
    tags.extend(f'<script src="js/{name}"></script>' for name in names)
    return "\n".join(tags)


def write(filename, title, description, body, extra):
    html = HEAD.format(
        title=title,
        description=description,
        nav=nav(filename),
        body=body,
        scripts=scripts(extra),
    )
    (ROOT / filename).write_text(html, encoding="utf-8")
    print(filename, len(html))


INDEX = """
<section class="hero">
  <div class="wrap">
    <p class="discount">Будни до 14:00 −30 %</p>
    <h1>Компьютерный клуб «Респаун»</h1>
    <p class="lead">52 игровых места рядом с двумя вузами и колледжем. Днём в будни зал свободнее: приходи до 14:00 и бери скидку 30 %. Вечером место лучше забронировать.</p>
    <div class="actions">
      <a class="btn" href="contacts.html?lead_type=booking" data-event="cta_click" data-button-name="hero_booking" data-page-section="hero">Забронировать</a>
      <a class="btn btn-ghost" href="prices.html">Считать стоимость</a>
    </div>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Зоны</h2>
    <ul class="zone-grid">
      <li class="zone-card"><a href="zones.html#standard" data-event="zone_view" data-zone="standard"><img src="img/zone-standard.jpg" width="960" height="640" alt="Иллюстрация зоны Стандарт: монитор и системный блок"><h3>Стандарт</h3><p>RTX 4060, монитор 165 Гц. 40 мест в общем зале.</p><p class="price">150 ₽/час</p></a></li>
      <li class="zone-card"><a href="zones.html#vip" data-event="zone_view" data-zone="vip"><img src="img/zone-vip.jpg" width="960" height="640" alt="Иллюстрация зоны VIP: широкий монитор и кресло"><h3>VIP</h3><p>RTX 4080, монитор 240 Гц, кресло премиум. 12 мест.</p><p class="price">250 ₽/час</p></a></li>
      <li class="zone-card"><a href="zones.html#bootcamp" data-event="zone_view" data-zone="bootcamp"><img src="img/zone-bootcamp.jpg" width="960" height="640" alt="Иллюстрация комнаты bootcamp на пять мест"><h3>Bootcamp</h3><p>Отдельная комната на 5 человек. Цена за комнату.</p><p class="price">1 100 ₽/час</p></a></li>
      <li class="zone-card"><a href="zones.html#ps5" data-event="zone_view" data-zone="ps5"><img src="img/zone-ps5.jpg" width="960" height="640" alt="Иллюстрация зоны PlayStation 5 с большим телевизором"><h3>PlayStation 5</h3><p>Телевизор 65 дюймов, до 4 игроков.</p><p class="price">400 ₽/час</p></a></li>
    </ul>
  </div>
</section>
<section class="block">
  <div class="wrap panel">
    <h2>Турнир «Зимний кубок»</h2>
    <p>CS2, пять на пять. Отборочные онлайн 28 ноября – 13 декабря, финал в клубе 19 декабря. Взнос 2 500 ₽ с команды, призовой фонд 60 000 ₽.</p>
    <a class="btn" href="tournament.html" data-event="tournament_view" data-tournament-id="winter_cup_2026" data-button-name="tournament_open" data-page-section="tournament">Открыть регламент</a>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Видео клуба</h2>
    <div class="player">
      <img src="img/video-poster.jpg" width="1280" height="720" alt="Иллюстрация общего зала компьютерного клуба Респаун">
      <div id="video-frame" class="video-frame" hidden></div>
      <button id="video-play" class="btn" type="button" data-event="video_play" data-video-title="club_tour">Смотреть видео</button>
    </div>
  </div>
</section>
"""

ZONES = """
<section class="block">
  <div class="wrap">
    <h1>Зоны</h1>
    <p class="lead">Характеристики указаны как в зале: видеокарта и частота монитора. Жми на карточку, потом бронируй выбранную зону.</p>
    <ul class="zone-grid">
      <li class="zone-card" id="standard"><a href="#standard" data-event="zone_view" data-zone="standard" data-zone-pick="standard"><img src="img/zone-standard.jpg" width="960" height="640" alt="Иллюстрация зоны Стандарт: монитор и системный блок"><h2>Стандарт</h2></a><p>Бери это место, если хочешь играть в общем зале. RTX 4060 и монитор 165 Гц. Таких мест сорок, час — 150 ₽ за место.</p></li>
      <li class="zone-card" id="vip"><a href="#vip" data-event="zone_view" data-zone="vip" data-zone-pick="vip"><img src="img/zone-vip.jpg" width="960" height="640" alt="Иллюстрация зоны VIP: широкий монитор и кресло"><h2>VIP</h2></a><p>Бери VIP, если важен каждый кадр. RTX 4080, монитор 240 Гц и кресло премиум. 12 мест, 250 ₽ в час за место.</p></li>
      <li class="zone-card" id="bootcamp"><a href="#bootcamp" data-event="zone_view" data-zone="bootcamp" data-zone-pick="bootcamp"><img src="img/zone-bootcamp.jpg" width="960" height="640" alt="Иллюстрация комнаты bootcamp на пять мест"><h2>Bootcamp</h2></a><p>Закройтесь впятером и не делите эфир с залом. Комната на 5 мест, 1 100 ₽ в час за всю комнату.</p></li>
      <li class="zone-card" id="ps5"><a href="#ps5" data-event="zone_view" data-zone="ps5" data-zone-pick="ps5"><img src="img/zone-ps5.jpg" width="960" height="640" alt="Иллюстрация зоны PlayStation 5 с большим телевизором"><h2>PlayStation 5</h2></a><p>Садитесь к одному экрану до четырёх человек. PlayStation 5 и телевизор 65 дюймов, 400 ₽ в час.</p></li>
    </ul>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <a id="zone-book" class="btn" href="contacts.html?lead_type=booking" data-event="cta_click" data-button-name="zones_booking" data-page-section="zones">Забронировать</a>
  </div>
</section>
"""

PRICES = """
<section class="block">
  <div class="wrap">
    <h1>Цены</h1>
    <form id="calculator" class="panel calc-grid">
      <div>
        <label for="calc-zone">Зона</label>
        <select id="calc-zone" name="zone">
          <option value="">Выбери зону</option>
          <option value="standard">Стандарт — 150 ₽/час</option>
          <option value="vip">VIP — 250 ₽/час</option>
          <option value="bootcamp">Bootcamp — 1 100 ₽/час за комнату</option>
          <option value="ps5">PlayStation 5 — 400 ₽/час</option>
        </select>
      </div>
      <div>
        <label for="calc-seats">Места</label>
        <input id="calc-seats" name="seats" type="number" min="1" max="5" value="1">
      </div>
      <div>
        <label for="calc-start">Начало</label>
        <input id="calc-start" name="start" type="datetime-local">
      </div>
      <div>
        <label for="calc-hours">Часы</label>
        <input id="calc-hours" name="hours" type="number" min="1" max="12" value="3">
      </div>
      <div class="wide">
        <button class="btn" type="submit">Рассчитать</button>
        <p id="calc-error" class="field-error" role="status"></p>
        <p id="calc-result" class="formula" aria-live="polite"></p>
        <p id="calc-formula" class="hint"></p>
        <p class="hint">Для проверки приёмки: VIP, 1 место, ближайший будний день, 11:00, 3 часа, без пакета. Ожидается 3 × 250 × 0,7 = 525 ₽ и тариф weekday_day.</p>
        <a id="calc-book" class="btn" href="contacts.html?lead_type=booking" data-event="cta_click" data-button-name="calculator_booking" data-page-section="prices">Забронировать</a>
      </div>
    </form>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Пакеты</h2>
    <p>Скидки и пакеты не суммируются. Кнопка «Выбрать» подставляет пакет в калькулятор.</p>
    <ul class="pack-grid">
      <li class="pack-card"><h3>3 часа, Стандарт</h3><p class="price">400 ₽</p><p>За одно место. Дешевле, чем три часа по 150 ₽.</p><button class="btn" type="button" data-event="package_select" data-package-name="pack_3h_standard">Выбрать</button></li>
      <li class="pack-card"><h3>3 часа, VIP</h3><p class="price">650 ₽</p><p>За одно место. Дешевле, чем три часа по 250 ₽.</p><button class="btn" type="button" data-event="package_select" data-package-name="pack_3h_vip">Выбрать</button></li>
      <li class="pack-card"><h3>Ночь, Стандарт</h3><p class="price">700 ₽</p><p>23:00–08:00, за одно место.</p><button class="btn" type="button" data-event="package_select" data-package-name="pack_night_standard">Выбрать</button></li>
      <li class="pack-card"><h3>Ночь, VIP</h3><p class="price">1 100 ₽</p><p>23:00–08:00, за одно место.</p><button class="btn" type="button" data-event="package_select" data-package-name="pack_night_vip">Выбрать</button></li>
    </ul>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Правила клуба</h2>
    <p><a class="btn" href="files/club-rules.pdf">Скачать правила (PDF)</a></p>
  </div>
</section>
"""

TOURNAMENT = """
<section class="block">
  <div class="wrap">
    <h1>Турнир «Зимний кубок»</h1>
    <p>Собирай пятёрку по CS2. Отборочные идут онлайн, финал играете у нас в клубе.</p>
    <ul class="plain-list">
      <li>Формат: 5 × 5</li>
      <li>Отборочные онлайн: 28 ноября – 13 декабря</li>
      <li>Финал в клубе: 19 декабря</li>
      <li>Взнос: 2 500 ₽ с команды</li>
      <li>Призовой фонд: 60 000 ₽</li>
    </ul>
    <details>
      <summary data-event="tournament_view" data-tournament-id="winter_cup_2026">Подробнее о формате</summary>
      <p>Регистрацию оставляет капитан. В заявке пять игроков, время брони для турнира не спрашиваем. Правила файла ниже написаны для участника на «вы».</p>
    </details>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Регламент PDF</h2>
    <p><a class="btn" href="files/winter-cup.pdf">Скачать регламент (PDF)</a></p>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <a class="btn" href="contacts.html?lead_type=tournament" data-event="cta_click" data-button-name="tournament_register" data-page-section="tournament">Зарегистрировать команду</a>
  </div>
</section>
"""

REACTION = """
<section class="block">
  <div class="wrap">
    <h1>Тест реакции</h1>
    <p>Нажми, когда экран станет зелёным. Пять попыток, пауза перед сигналом от 1 до 4 секунд. Раннее нажатие — фальстарт, попытка начинается заново и в среднее не входит.</p>
    <button id="reaction-pad" class="reaction-pad" type="button">Нажми, чтобы начать</button>
    <p id="reaction-note" class="hint" aria-live="polite"></p>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Таблица результатов</h2>
    <table class="result-table" id="reaction-table">
      <caption class="visually-hidden">Пять попыток и среднее время</caption>
      <thead><tr><th>Попытка</th><th>Миллисекунды</th></tr></thead>
      <tbody>
        <tr><th>1</th><td data-attempt="1">—</td></tr>
        <tr><th>2</th><td data-attempt="2">—</td></tr>
        <tr><th>3</th><td data-attempt="3">—</td></tr>
        <tr><th>4</th><td data-attempt="4">—</td></tr>
        <tr><th>5</th><td data-attempt="5">—</td></tr>
        <tr><th>Среднее</th><td id="reaction-average">—</td></tr>
      </tbody>
    </table>
  </div>
</section>
<section class="block">
  <div class="wrap panel">
    <h2>Промокод</h2>
    <p class="promo-code">REACT20</p>
    <p>Промокод на утреннюю бронь. Назови его администратору. Скидка и пакеты не суммируются.</p>
    <button id="promo-copy" class="btn" type="button" data-event="promo_copy" data-promo-code="REACT20">Скопировать</button>
    <p id="promo-status" class="hint" aria-live="polite"></p>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <a class="btn" href="contacts.html?lead_type=booking" data-event="cta_click" data-button-name="reaction_booking" data-page-section="reaction">Забронировать</a>
  </div>
</section>
"""

CONTACTS = """
<section class="block">
  <div class="wrap">
    <h1>Бронь и контакты</h1>
    <form id="lead-form" action="#" method="post" novalidate>
      <div class="form-grid">
        <div>
          <label for="lead_type">Тип заявки</label>
          <select id="lead_type" name="lead_type">
            <option value="booking">Бронь места</option>
            <option value="tournament">Регистрация команды</option>
          </select>
          <span id="error-lead_type" class="field-error"></span>
        </div>
        <p id="quote-summary" class="hint">Если посчитать стоимость на странице «Цены», сумма подставится сюда.</p>
        <div>
          <label for="name">Имя</label>
          <input id="name" name="name" type="text" autocomplete="name" minlength="2" maxlength="60">
          <span id="error-name" class="field-error"></span>
        </div>
        <div>
          <label for="phone">Телефон</label>
          <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="+79002220222" maxlength="20">
          <span id="error-phone" class="field-error"></span>
        </div>
        <div>
          <label for="email">Почта, если есть</label>
          <input id="email" name="email" type="email" autocomplete="email" maxlength="200">
          <span id="error-email" class="field-error"></span>
        </div>
        <div>
          <label for="zone">Зона</label>
          <select id="zone" name="zone">
            <option value="">Выбери зону</option>
            <option value="standard">Стандарт</option>
            <option value="vip">VIP</option>
            <option value="bootcamp">Bootcamp</option>
            <option value="ps5">PlayStation 5</option>
          </select>
          <span id="error-zone" class="field-error"></span>
        </div>
        <div id="slot-wrap">
          <label for="slot">Начало брони</label>
          <input id="slot" name="slot" type="datetime-local">
          <span id="error-slot" class="field-error"></span>
        </div>
        <div id="seats-wrap">
          <label for="seats">Места</label>
          <select id="seats" name="seats">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
          <span id="error-seats" class="field-error"></span>
        </div>
        <label class="consent" for="consent">
          <input id="consent" name="consent" type="checkbox">
          <span>Я соглашаюсь на обработку персональных данных и принимаю <a href="privacy.html" target="_blank" rel="noopener noreferrer">политику конфиденциальности</a>.</span>
        </label>
        <span id="error-consent" class="field-error"></span>
        <input id="request_id" name="request_id" type="hidden">
        <button id="submit-lead" class="btn" type="submit">Отправить заявку</button>
        <p id="form-status" role="status"></p>
      </div>
    </form>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Мессенджеры</h2>
    <div class="messengers">
      <a class="btn" href="https://t.me/respawn_events" target="_blank" rel="noopener noreferrer" data-event="messenger_click" data-messenger="telegram">Telegram</a>
      <a class="btn btn-ghost" href="https://wa.me/79002220222" target="_blank" rel="noopener noreferrer" data-event="messenger_click" data-messenger="whatsapp">WhatsApp</a>
    </div>
  </div>
</section>
"""

THANKS = """
<section class="block">
  <div class="wrap panel">
    <h1>Заявка принята</h1>
    <p>Номер брони: <strong id="thanks-id">—</strong></p>
    <p>Зона: <strong id="thanks-zone">—</strong></p>
    <p>Время: <strong id="thanks-time">—</strong></p>
    <p>Бронь держится 15 минут после начала.</p>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Ссылки на соцсети</h2>
    <ul class="social-list">
      <li><a href="https://instagram.com/respawn.nov2026" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="instagram" data-page-section="thanks">Instagram</a></li>
      <li><a href="https://vk.com/respawn_nov2026" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="vk" data-page-section="thanks">ВКонтакте</a></li>
      <li><a href="https://t.me/respawn_events" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="telegram" data-page-section="thanks">Telegram</a></li>
      <li><a href="https://youtube.com/@respawn_nov2026" target="_blank" rel="noopener noreferrer" data-event="social_click" data-network="youtube" data-page-section="thanks">YouTube</a></li>
    </ul>
  </div>
</section>
"""

PRIVACY = """
<article class="block policy">
  <div class="wrap">
    <h1>Политика конфиденциальности</h1>
    <p>Настоящий текст описывает, как ООО «Респаун» обрабатывает персональные данные посетителей сайта. Формулировки даны на «вы».</p>
    <h2>Оператор</h2>
    <p>ООО «Респаун», 614 122, г. Новоозёрск, ул. Студенческая, д. 2, ТЦ «Орбита», 3 этаж. ИНН 9922 220 022, КПП 992201001, ОГРН 1239900022002. Телефон +7 (900) 222-02-22, почта book@respawn-club.example.</p>
    <h2>Какие данные вы передаёте</h2>
    <p>Имя или название команды, телефон, почту по желанию, выбранную зону, время начала брони, число мест и тип заявки: бронь места или регистрация команды. Технические метки источника перехода (UTM) сохраняются вместе с заявкой. Паспорт, платёжные реквизиты и фотографии через эту форму не запрашиваются.</p>
    <h2>Зачем они нужны</h2>
    <p>Чтобы подтвердить бронь, удержать место 15 минут после начала, связаться с вами и отделить регистрацию команды на «Зимний кубок» от обычной брони. Отдельная цель — понять, из какого размещения на сайте вы пришли. Для этой цели имя, телефон и почта в систему веб-аналитики не передаются.</p>
    <h2>На каком основании</h2>
    <p>Основание — ваше согласие. Флажок в форме по умолчанию не отмечен. Без него заявка не отправляется. Ссылка на эту страницу стоит рядом с флажком.</p>
    <h2>Сколько храним</h2>
    <p>Заявка хранится в таблице клуба до визита и ещё 12 месяцев после даты заявки, чтобы сверить бронь и обращение. Затем строка удаляется, если закон не требует хранить её дольше.</p>
    <h2>Кому передаём</h2>
    <p>Данные видит сотрудник клуба, который ведёт таблицу заявок. Хостинг сайта не получает содержимое формы: браузер отправляет заявку в веб-приложение таблицы. Рекламным сетям имя, телефон и почта не отдаются.</p>
    <h2>Ваши права</h2>
    <p>Вы можете запросить сведения об обработке, попросить исправить ошибку или удалить заявку и отозвать согласие. Напишите на book@respawn-club.example или позвоните по телефону из шапки сайта. Отзыв согласия не отменяет обработку, которая уже была законной до отзыва.</p>
  </div>
</article>
"""

NOT_FOUND = """
<section class="not-found">
  <div class="wrap">
    <h1>Такой страницы нет</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a class="btn" href="index.html">На главную</a>
  </div>
</section>
"""


def games_body():
    items = []
    for name, genre, zone in GAMES:
        search = f"{name} {genre} {zone}".replace('"', "")
        items.append(
            f'<li class="game" data-search="{search}"><span class="game-name">{name}</span>'
            f'<span class="meta">{genre}</span><span class="meta">{zone}</span></li>'
        )
    listing = "\n".join(items)
    return f"""
<section class="block">
  <div class="wrap">
    <h1>Игры</h1>
    <label for="game-search">Поиск по играм</label>
    <input id="game-search" type="search" maxlength="100" placeholder="Название или жанр">
    <p id="game-count" class="hint" aria-live="polite">Найдено: 60</p>
  </div>
</section>
<section class="block">
  <div class="wrap">
    <h2>Список из 60 игр</h2>
    <ul id="game-list" class="game-list">
{listing}
    </ul>
  </div>
</section>
"""


def main():
    write("index.html", "Главная — компьютерный клуб «Респаун»", "Круглосуточный компьютерный клуб в Новоозёрске: зоны, бронь мест и турнир «Зимний кубок». В будни до 14:00 скидка 30 %.", INDEX, ["video.js"])
    write("zones.html", "Зоны — компьютерный клуб «Респаун»", "Стандарт на RTX 4060, VIP на RTX 4080, комната bootcamp и PlayStation 5. Цены и характеристики зон клуба «Респаун».", ZONES, ["zones.js"])
    write("prices.html", "Цены и калькулятор брони — «Респаун»", "Калькулятор брони: зона, места, начало и часы. Пакет «3 часа», ночной пакет и правила клуба.", PRICES, ["pricing.js", "calculator.js"])
    write("games.html", "Игры — компьютерный клуб «Респаун»", "Шестьдесят игр на ПК и PlayStation 5 в клубе «Респаун». Поиск по названию и жанру.", games_body(), ["games.js"])
    write("tournament.html", "Турнир «Зимний кубок» — «Респаун»", "«Зимний кубок» по CS2: отборочные 28 ноября – 13 декабря, финал 19 декабря, взнос 2 500 ₽, призовой фонд 60 000 ₽.", TOURNAMENT, [])
    write("reaction.html", "Тест реакции — компьютерный клуб «Респаун»", "Пять попыток на реакцию, среднее время в миллисекундах и промокод REACT20 на утреннюю бронь.", REACTION, ["reaction.js"])
    write("contacts.html", "Бронь и контакты — «Респаун»", "Форма брони места или регистрации команды на турнир. Телефон, Telegram и WhatsApp клуба «Респаун».", CONTACTS, ["config.js", "pricing.js", "form.js"])
    write("thanks.html", "Заявка принята — «Респаун»", "Номер брони, зона и время. Бронь в клубе «Респаун» держится 15 минут после начала.", THANKS, ["thanks.js"])
    write("privacy.html", "Политика конфиденциальности — «Респаун»", "Какие данные собирает ООО «Респаун», зачем, сколько хранит и как отозвать согласие.", PRIVACY, [])
    write("404.html", "Страница не найдена — «Респаун»", "Запрошенной страницы на сайте компьютерного клуба «Респаун» нет.", NOT_FOUND, [])


if __name__ == "__main__":
    main()
