# -*- coding: utf-8 -*-
"""Картинки, правила, регламент, QR и афиша. После адреса Vercel поменяйте SITE и запустите снова."""
from pathlib import Path
import pymupdf
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://tz-22-kompyuternyy-klub-respawn.vercel.app"
QR_URL = (
    SITE
    + "/prices.html?utm_source=campus_qr&utm_medium=qr"
    + "&utm_campaign=respawn_nov_2026&utm_content=campus_flyer"
)
FONT = Path(r"C:\Windows\Fonts\arial.ttf")
FONT_B = Path(r"C:\Windows\Fonts\arialbd.ttf")
BG = (15, 14, 23)
CYAN = (41, 211, 245)
PURPLE = (123, 47, 242)
WHITE = (244, 246, 251)


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_B if bold else FONT), size)


def save_jpeg(image, path):
    image.save(path, "JPEG", quality=78, optimize=True)
    print(path.name, path.stat().st_size)


def poster(path, title, subtitle, monitors):
    image = Image.new("RGB", (960, 640), BG)
    draw = ImageDraw.Draw(image)
    draw.polygon([(0, 0), (220, 0), (0, 220)], fill=PURPLE)
    draw.rectangle((36, 36, 924, 604), outline=CYAN, width=3)
    gap = 700 // max(monitors, 1)
    for index in range(monitors):
        left = 80 + index * gap
        draw.rounded_rectangle((left, 230, left + gap - 28, 430), radius=6, outline=CYAN, width=5)
        draw.rectangle((left + (gap - 28) // 2 - 8, 430, left + (gap - 28) // 2 + 8, 468), fill=CYAN)
    draw.text((56, 70), title, font=font(54, True), fill=WHITE)
    draw.text((56, 520), subtitle, font=font(28), fill=CYAN)
    save_jpeg(image, path)


def make_images():
    img = ROOT / "img"
    img.mkdir(exist_ok=True)
    poster(img / "zone-standard.jpg", "СТАНДАРТ", "RTX 4060 · 165 Гц · 150 ₽/час", 3)
    poster(img / "zone-vip.jpg", "VIP", "RTX 4080 · 240 Гц · 250 ₽/час", 1)
    poster(img / "zone-bootcamp.jpg", "BOOTCAMP", "Комната на 5 · 1 100 ₽/час", 5)
    poster(img / "zone-ps5.jpg", "PLAYSTATION 5", "Телевизор 65\" · 400 ₽/час", 1)
    hero = Image.new("RGB", (1280, 720), BG)
    draw = ImageDraw.Draw(hero)
    draw.polygon([(900, 0), (1280, 0), (1280, 420)], fill=PURPLE)
    draw.text((70, 220), "RESPAWN", font=font(92, True), fill=WHITE)
    draw.text((70, 340), "Будни до 14:00 −30 %", font=font(42, True), fill=CYAN)
    save_jpeg(hero, img / "video-poster.jpg")
    og = hero.resize((1200, 630))
    save_jpeg(og, img / "og.jpg")
    icon = Image.new("RGB", (64, 64), BG)
    idraw = ImageDraw.Draw(icon)
    idraw.rectangle((4, 4, 59, 59), outline=CYAN, width=3)
    idraw.text((16, 14), "R", font=font(36, True), fill=WHITE)
    icon.save(img / "favicon.png", "PNG")


def write_pdf(path, title, paragraphs):
    doc = pymupdf.open()

    def new_page():
        page = doc.new_page()
        page.insert_font(fontname="arial", fontfile=str(FONT))
        page.insert_font(fontname="arialbd", fontfile=str(FONT_B))
        return page

    def wrap(text, limit=78):
        lines, line = [], ""
        for word in text.split():
            trial = word if not line else line + " " + word
            if len(trial) > limit:
                if line:
                    lines.append(line)
                line = word
            else:
                line = trial
        if line:
            lines.append(line)
        return lines

    page = new_page()
    y = 64
    page.insert_text((56, y), title, fontname="arialbd", fontsize=16)
    y += 28
    for paragraph in paragraphs:
        for line in wrap(paragraph):
            if y > 780:
                page = new_page()
                y = 64
            page.insert_text((56, y), line, fontname="arial", fontsize=12)
            y += 16
        y += 10
    doc.save(path, deflate=True, garbage=4)
    doc.close()
    print(path.name, path.stat().st_size)


def subset_font(src, text, dest):
    from fontTools.subset import Subsetter, Options
    from fontTools.ttLib import TTFont
    options = Options()
    font = TTFont(src)
    subsetter = Subsetter(options=options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    font.save(dest)


def make_pdfs():
    global FONT, FONT_B
    files = ROOT / "files"
    files.mkdir(exist_ok=True)
    rules = [
        "Оператор: ООО «Респаун», 614 122, г. Новоозёрск, ул. Студенческая, д. 2, ТЦ «Орбита», 3 этаж. Телефон +7 (900) 222-02-22.",
        "Вход в клуб разрешён с 14 лет. С 22:00 до 08:00 и на ночные пакеты пускаем только с 18 лет.",
        "Бронь оформляет посетитель от 18 лет или родитель. Бронь держится 15 минут после времени начала. Если гость не пришёл, место освобождается.",
        "В будни с 08:00 до 14:00 действует скидка 30 % на почасовую оплату. Пакет «3 часа»: 400 ₽ за место «Стандарт» и 650 ₽ за место VIP. Ночь 23:00–08:00: 700 ₽ за место «Стандарт» и 1 100 ₽ за место VIP.",
        "Скидки и пакеты не суммируются. Время начала брони определяет тариф.",
        "Комната bootcamp оплачивается за комнату: 1 100 ₽ в час. PlayStation 5 — 400 ₽ в час, до 4 игроков.",
    ]
    cup = [
        "Турнир по CS2, формат 5 × 5. Отборочные проходят онлайн с 28 ноября по 13 декабря. Финал проводится в клубе «Респаун» 19 декабря.",
        "Взнос составляет 2 500 ₽ с команды. Призовой фонд — 60 000 ₽.",
        "Заявку подаёт капитан через форму на сайте. В составе команды 5 игроков. Время брони места в заявке на турнир не указывается.",
        "Участник финала соблюдает правила клуба: вход с 14 лет, ночной формат — с 18 лет. Бронь места, если она нужна отдельно от турнира, держится 15 минут после начала.",
    ]
    afisha = "Сканируйте код: дневная скидка и цены. Кампания respawn_nov_2026. tz-22-kompyuternyy-klub-respawn.vercel.app +7 (900) 222-02-22"
    alphabet = afisha + "RESPAWNБудни до 14:00 −30 %Стандарт VIP · ₽/часТЦ «Орбита» этаж " + "".join(rules + cup)
    regular = ROOT / "files" / "arial-subset.ttf"
    bold = ROOT / "files" / "arialbd-subset.ttf"
    subset_font(FONT, alphabet, regular)
    subset_font(FONT_B, alphabet, bold)
    FONT, FONT_B = regular, bold
    write_pdf(files / "club-rules.pdf", "Правила клуба «Респаун»", rules)
    write_pdf(files / "winter-cup.pdf", "Регламент «Зимнего кубка»", cup)


def make_qr():
    import segno
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    qr = segno.make(QR_URL, error="m")
    qr_path = docs / "qr-u-12.png"
    qr.save(qr_path, scale=8, border=2, dark="#0F0E17", light="#FFFFFF")
    doc = pymupdf.open()
    page = doc.new_page(width=595, height=842)
    page.insert_font(fontname="arial", fontfile=str(FONT))
    page.insert_font(fontname="arialbd", fontfile=str(FONT_B))
    page.draw_rect(pymupdf.Rect(0, 0, 595, 120), color=(15 / 255, 14 / 255, 23 / 255), fill=(15 / 255, 14 / 255, 23 / 255))
    page.insert_text((40, 74), "RESPAWN", fontname="arialbd", fontsize=32, color=(1, 1, 1))
    page.insert_text((40, 180), "Будни до 14:00 −30 %", fontname="arialbd", fontsize=22, color=(123 / 255, 47 / 255, 242 / 255))
    page.insert_text((40, 230), "Стандарт 150 ₽/час. VIP 250 ₽/час.", fontname="arial", fontsize=14, color=(0.1, 0.1, 0.15))
    page.insert_text((40, 260), "ТЦ «Орбита», 3 этаж. +7 (900) 222-02-22", fontname="arial", fontsize=14, color=(0.1, 0.1, 0.15))
    page.insert_image(pymupdf.Rect(40, 300, 280, 540), filename=str(qr_path))
    page.insert_text((40, 580), "Сканируйте код: дневная скидка и цены.", fontname="arial", fontsize=13, color=(0.1, 0.1, 0.15))
    page.insert_text((40, 610), "Кампания respawn_nov_2026", fontname="arial", fontsize=11, color=(0.2, 0.2, 0.25))
    page.insert_text((40, 628), "tz-22-kompyuternyy-klub-respawn.vercel.app", fontname="arial", fontsize=11, color=(0.2, 0.2, 0.25))
    doc.save(docs / "afisha.pdf", deflate=True, garbage=4)
    doc.close()
    print("afisha.pdf", (docs / "afisha.pdf").stat().st_size)


if __name__ == "__main__":
    make_images()
    make_pdfs()
    make_qr()
    for name in ("arial-subset.ttf", "arialbd-subset.ttf"):
        path = ROOT / "files" / name
        if path.exists():
            path.unlink()
