
from pathlib import Path
from shutil import copy2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth

CV_DIR = Path(__file__).resolve().parent
PORTFOLIO_DIR = CV_DIR.parent
ASSET_DIR = CV_DIR / "assets"
CV_DIR.mkdir(exist_ok=True)
ASSET_DIR.mkdir(exist_ok=True)
source_portrait = PORTFOLIO_DIR / "assets" / "khant-hero-facial-reference-v6.png"
portrait_path = ASSET_DIR / "khant-current-portrait.png"
copy2(source_portrait, portrait_path)
pdf_path = CV_DIR / "Khant_Maung_CV.pdf"
W, H = A4
DARK = HexColor("#0B0D0C")
SURFACE = HexColor("#F4F3EE")
TEXT = HexColor("#182019")
MUTED = HexColor("#596159")
QUIET = HexColor("#747B72")
LINE = HexColor("#CDD3C9")
ACCENT = HexColor("#A7D93F")
ACCENT_DARK = HexColor("#4F7100")
WHITE = HexColor("#F7F9F4")
c = canvas.Canvas(str(pdf_path), pagesize=A4)
c.setTitle("Khant Maung - Full-Stack Developer CV")
c.setAuthor("Khant Maung")
c.setSubject("Full-stack developer CV")

def wrap(text, font, size, width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = word if not current else current + " " + word
        if stringWidth(trial, font, size) <= width:
            current = trial
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    return lines

def draw_wrapped(text, x, y, width, font="Helvetica", size=8.2, color=MUTED, leading=11):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y

def section_label(number, title, x, y, width):
    c.setFillColor(ACCENT_DARK)
    c.setFont("Courier-Bold", 7.2)
    c.drawString(x, y, f"{number} / {title.upper()}")
    c.setStrokeColor(LINE)
    c.setLineWidth(.6)
    c.line(x, y - 6, x + width, y - 6)
    return y - 21

def role(x, y, width, title, company, dates, bullets):
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 9.2)
    c.drawString(x, y, title)
    c.setFillColor(ACCENT_DARK)
    c.setFont("Courier-Bold", 6.4)
    c.drawRightString(x + width, y + .5, dates.upper())
    y -= 12
    c.setFillColor(QUIET)
    c.setFont("Helvetica-Bold", 7.4)
    c.drawString(x, y, company)
    y -= 11
    for bullet in bullets:
        c.setFillColor(ACCENT_DARK)
        c.circle(x + 2, y + 2.6, 1.15, stroke=0, fill=1)
        y = draw_wrapped(bullet, x + 9, y, width - 9, size=7.25, color=MUTED, leading=9.4)
        y -= 2.5
    return y - 4

def sidebar_item(label, lines, x, y, width):
    c.setFillColor(QUIET)
    c.setFont("Courier-Bold", 6.1)
    c.drawString(x, y, label.upper())
    y -= 10
    for line in lines:
        y = draw_wrapped(line, x, y, width, font="Helvetica", size=7.25, color=TEXT, leading=9.1)
    return y - 8

c.setFillColor(DARK)
c.rect(0, H - 186, W, 186, stroke=0, fill=1)
c.setFillColor(ACCENT)
c.rect(36, H - 45, 28, 3, stroke=0, fill=1)
c.setFont("Courier-Bold", 7.4)
c.drawString(36, H - 64, "FULL-STACK DEVELOPER")
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 29)
c.drawString(36, H - 99, "Khant Maung")
draw_wrapped("I build reliable web products from interface and API design through databases, testing, and production deployment.", 36, H - 120, 348, size=9.2, color=HexColor("#B7BEB4"), leading=12)
c.setFillColor(ACCENT)
c.setFont("Courier-Bold", 6.6)
c.drawString(36, H - 162, "REACT  /  NODE.JS  /  DJANGO  /  POSTGRESQL")
c.drawImage(ImageReader(str(portrait_path)), 427, H - 181, width=132, height=166, preserveAspectRatio=True, anchor="c", mask="auto")

ribbon_y = H - 218
c.setFillColor(SURFACE)
c.rect(0, ribbon_y, W, 32, stroke=0, fill=1)
contacts = [
    ("EMAIL", "khantmg262626@gmail.com", "mailto:khantmg262626@gmail.com", 36),
    ("PHONE", "+66 93 047 0721", "tel:+66930470721", 226),
    ("GITHUB", "github.com/Khant26", "https://github.com/Khant26", 374),
]
for label, value, url, x in contacts:
    c.setFillColor(QUIET)
    c.setFont("Courier-Bold", 5.7)
    c.drawString(x, ribbon_y + 19, label)
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 7.1)
    c.drawString(x, ribbon_y + 8, value)
    c.linkURL(url, (x, ribbon_y + 5, x + stringWidth(value, "Helvetica-Bold", 7.1), ribbon_y + 17), relative=0)

left_x, left_w = 36, 352
side_x, side_w = 418, 141
top_y = ribbon_y - 22
c.setStrokeColor(LINE)
c.setLineWidth(.6)
c.line(402, 48, 402, top_y + 6)

y = section_label("01", "Experience", left_x, top_y, left_w)
y = role(left_x, y, left_w, "Freelance Full-Stack Developer", "Independent Projects", "2024 - Present", [
    "Delivered airline booking, event ticketing, company operations, and content-management products across the full development lifecycle.",
    "Built authentication, REST APIs, dashboards, database workflows, validation, and deployment architecture for real product use."
])
y = role(left_x, y, left_w, "Full-Stack Developer", "Civil Master Solution", "Sep 2025 - Feb 2026", [
    "Developed a React and Django administration platform with role-based access, reusable UI components, and publishing workflows.",
    "Integrated production APIs and supported deployments on Vercel and Render with maintainable frontend and backend structure."
])
y = role(left_x, y, left_w, "Test Automation Engineer", "Brillar Company", "Apr 2025 - Aug 2025", [
    "Created Tosca automated test cases and executed functional and regression coverage for critical user journeys.",
    "Reported defects clearly and collaborated with developers to strengthen release quality and repeatable QA workflows."
])
y = section_label("02", "Selected Projects", left_x, y - 1, left_w)
projects = [
    ("Airline Booking Platform", "React / Node.js / PostgreSQL", "Dynamic search, protected sessions, pricing, bookings, history, JWT, and reverse-proxy deployment."),
    ("Enterprise Management System", "React / Node.js / PostgreSQL", "Employee operations, performance tracking, reporting, meetings, events, and role-based administration."),
    ("Event Booking and Ticketing", "React / Node.js / MongoDB", "Event discovery, listing creation, user roles, ticket booking, validation, APIs, and management dashboards."),
    ("Content Management System", "React / Django / REST", "Role-based publishing, administration workflows, reusable content tools, and production deployment.")
]
for name, stack, detail in projects:
    c.setFillColor(TEXT)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(left_x, y, name)
    c.setFillColor(ACCENT_DARK)
    c.setFont("Courier-Bold", 5.8)
    c.drawRightString(left_x + left_w, y + .2, stack.upper())
    y -= 10
    y = draw_wrapped(detail, left_x, y, left_w, size=6.85, color=MUTED, leading=8.6)
    y -= 5

y = section_label("03", "Engineering Practice", left_x, y - 2, left_w)
for practice in [
    "Translate product requirements into clear frontend, API, and data responsibilities.",
    "Prioritize secure authentication, role-based access, validation, and reliable error handling.",
    "Build reusable components and maintainable services for efficient iteration.",
    "Test critical workflows and prepare applications for dependable production deployment."
]:
    c.setFillColor(ACCENT_DARK)
    c.circle(left_x + 2, y + 2.5, 1.1, stroke=0, fill=1)
    y = draw_wrapped(practice, left_x + 9, y, left_w - 9, size=7.05, color=MUTED, leading=9.1)
    y -= 2

sy = section_label("04", "Profile", side_x, top_y, side_w)
sy = draw_wrapped("Full-stack developer with one year of practical experience building, testing, and deploying web applications.", side_x, sy, side_w, size=7.4, color=MUTED, leading=9.4)
sy -= 8
sy = sidebar_item("Education", ["B.Sc. Information and Communication Technology", "Rangsit University", "2023 - Jan 2026"], side_x, sy, side_w)
sy = sidebar_item("Location", ["Prachathipat, Thanyaburi District", "Pathum Thani 12130, Thailand"], side_x, sy, side_w)
sy = section_label("05", "Core Skills", side_x, sy - 2, side_w)
sy = sidebar_item("Frontend", ["React.js, JavaScript, Tailwind CSS, HTML, CSS"], side_x, sy, side_w)
sy = sidebar_item("Backend", ["Node.js, Express.js, Django, Python"], side_x, sy, side_w)
sy = sidebar_item("Data and APIs", ["PostgreSQL, MongoDB, REST APIs, JWT"], side_x, sy, side_w)
sy = sidebar_item("Delivery and QA", ["Git, GitHub, Nginx, Vercel, Render, Tosca"], side_x, sy, side_w)
sy = section_label("06", "Strengths", side_x, sy - 2, side_w)
sy = draw_wrapped("Problem solving / Communication / Ownership / Time management / Critical thinking", side_x, sy, side_w, size=7.15, color=TEXT, leading=9.2)
sy = section_label("07", "Links", side_x, sy - 8, side_w)
for label, value, url in [
    ("Portfolio", "khantmaung.com", "https://khantmaung.com/"),
    ("LinkedIn", "View profile", "https://www.linkedin.com/in/khant-mg-899330280/")
]:
    c.setFillColor(QUIET)
    c.setFont("Courier-Bold", 5.8)
    c.drawString(side_x, sy, label.upper())
    sy -= 10
    c.setFillColor(ACCENT_DARK)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(side_x, sy, value)
    c.linkURL(url, (side_x, sy - 2, side_x + stringWidth(value, "Helvetica-Bold", 7.2), sy + 8), relative=0)
    sy -= 15

sy -= 3
c.setFillColor(SURFACE)
c.roundRect(side_x, sy - 52, side_w, 52, 2, stroke=0, fill=1)
c.setFillColor(ACCENT_DARK)
c.setFont("Courier-Bold", 6.1)
c.drawString(side_x + 9, sy - 14, "OPEN TO OPPORTUNITIES")
draw_wrapped("Full-time development roles, freelance product work, and collaborative web projects.", side_x + 9, sy - 28, side_w - 18, size=6.8, color=MUTED, leading=8.5)

c.setStrokeColor(LINE)
c.line(36, 39, W - 36, 39)
c.setFillColor(QUIET)
c.setFont("Courier", 5.8)
c.drawString(36, 25, "KHANT MAUNG / FULL-STACK DEVELOPER")
c.drawRightString(W - 36, 25, "PORTFOLIO CV / 2026")
c.save()

(CV_DIR / "README.md").write_text("""# Khant Maung CV

This folder contains the complete CV package:

- Khant_Maung_CV.pdf - final one-page CV used by the portfolio
- create_cv.py - editable ReportLab source
- assets/khant-current-portrait.png - current portfolio portrait used in the CV

Run python create_cv.py from this folder to regenerate the PDF.
""", encoding="utf-8")
print(pdf_path)
