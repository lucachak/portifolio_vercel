from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

PROJECTS = [
    {
        "featured": True,
        "icon": "💰",
        "title": _("FinGen"),
        "description": _(
            "Most people manage money reactively — they notice problems after they happen. "
            "FinGen changes that. Upload a bank statement PDF and the system parses your real "
            "transaction history, feeds it to an AI financial advisor, and returns concrete "
            "recommendations: where you're bleeding money, how your cash flow compares month-over-month, "
            "and where to invest based on current market data scraped live. "
            "Built with Spring Boot on the backend, Thymeleaf + HTMX on the front, "
            "and a Three.js animated currency visualization on the landing page."
        ),
        "tags": [
            "Java",
            "Spring Boot",
            "HTMX",
            "Thymeleaf",
            "Three.js",
            "OpenRouter AI",
            "PDF parsing",
            "Spring Security",
        ],
        "github_url": "https://github.com/lucachak/fingen",  # ← update with real repo
        "live_url": "https://fingen-app.onrender.com",
        "accent": "accent1",
        "terminal_lines": [
            {"type": "comment", "text": _("// AI financial advisor")},
            {"type": "cmd", "text": _("POST /api/chat/analyze"), "rest": ""},
            {"type": "out", "text": _("→ Parsing statement...")},
            {"type": "out", "text": _("→ Monthly spend: R$ 3.240")},
            {"type": "out", "text": _("→ Savings rate: 18.4%")},
            {"type": "out", "text": _("→ Recommendation ready ✓")},
            {"type": "cursor"},
        ],
    },
    {
        "featured": False,
        "icon": "🔍",
        "title": _("Dirb-like — Web Directory Scanner"),
        "description": _(
            "A brute-force web directory scanner built entirely in pure Python — "
            "no external libraries, no requests, no shortcuts. "
            "HTTP and HTTPS handlers written from scratch against the RFC spec. "
            "The point wasn't to reinvent the wheel; it was to understand exactly "
            "what tools like DIRB are doing under the hood before trusting them blindly. "
            "Concurrent scanning, configurable wordlists, and clean output formatting."
        ),
        "tags": [
            "Python",
            "Pure stdlib",
            "HTTP/HTTPS",
            "Security tooling",
            "Networking",
        ],
        "github_url": "https://github.com/lucachak/Dirb-like",
        "live_url": None,
        "accent": "accent2",
    },
    {
        "featured": False,
        "icon": "📬",
        "title": _("CV-Spammer — Automated Job Application Bot"),
        "description": _(
            "Job hunting at scale is a numbers game. CV-Spammer is a web scraper and automation tool "
            "that searches job boards, filters listings by role and location, and fires off "
            "tailored application emails — automatically. "
            "Built to solve a real problem (sending hundreds of applications manually is brutal), "
            "and as a practical exercise in scraping, browser automation, and SMTP handling."
        ),
        "tags": ["Python", "Web scraping", "Automation", "SMTP", "BeautifulSoup"],
        "github_url": "https://github.com/lucachak/CV-Spammer",
        "live_url": None,
        "accent": "accent3",
    },
    {
        "featured": True,  # second featured — or set False if you want only one
        "icon": "🔧",
        "title": _("CambioMatic — ERP for Auto Shops"),
        "description": _(
            "Small auto repair shops run on paper, WhatsApp messages, and memory. "
            "CambioMatic replaces that with a full ERP: service orders from open to invoiced, "
            "inventory tracking, customer records, and billing — all in one place. "
            "Built for non-technical operators who need something that just works, "
            "without training or IT support. Currently live and in use."
        ),
        "tags": ["Java", "Spring MVC", "PostgreSQL", "Thymeleaf", "ERP"],
        "github_url": "https://github.com/lucachak/cambiomatic",  # ← update with real repo
        "live_url": "https://cambiomatic.onrender.com/login",
        "accent": "accent4",
        "terminal_lines": [],
    },
    {
        "featured": False,
        "icon": "🚀",
        "title": _("Django SaaS Boilerplate"),
        "description": _(
            "Starting a SaaS from scratch means solving the same problems every time: "
            "auth, subscriptions, async tasks, database. This boilerplate eliminates that. "
            "Stripe subscription billing, OAuth2 via Google and GitHub, Celery for background jobs, "
            "and Postgres on Neon — production-ready architecture with proper separation of concerns. "
            "Designed to be the foundation you actually want to build on."
        ),
        "tags": [
            "Python",
            "Django",
            "Stripe",
            "OAuth2",
            "PostgreSQL",
            "Neon DB",
            "Tailwind",
            "HTMX",
        ],
        "github_url": "https://github.com/lucachak/django-saas-boilerplate",  # ← update with real repo
        "live_url": None,
        "accent": "accent5",
    },
    {
        "featured": False,
        "icon": "🛡️",
        "title": _("Security Research & Offensive Tooling"),
        "description": _(
            "A collection of self-directed security research done alongside formal ethical hacking "
            "coursework at university. Areas covered: network-layer attack analysis "
            "(understanding how DoS/DDoS traffic behaves at the protocol level, studied in isolated lab environments); "
            "Android security research (APK structure, static analysis, and payload behavior "
            "in sandboxed VMs); physical access testing with a Raspberry Pi Pico flashed as a "
            "USB HID device (Rubber Ducky-style keystroke injection); and web recon automation. "
            "All conducted in controlled environments — VMs, local labs, or with explicit permission. "
            "The goal: understand how attacks work before trying to defend against them."
        ),
        "tags": [
            "Python",
            "Android / APK analysis",
            "USB HID",
            "Network protocols",
            "Linux",
            "VMs",
            "CTF",
            "Ethical Hacking (coursework)",
        ],
        "github_url": "https://github.com/lucachak",
        "live_url": None,
        "accent": "accent2",
    },
    {
        "featured": False,
        "icon": "📦",
        "title": _("CourierIQ — Logistics Microservices"),
        "description": _(
            "Real-time package tracking system designed for throughput. "
            "Microservices architecture with FastAPI, event streams via Redis, "
            "live WebSocket dashboards, and dynamic ETA recalculation as shipments move. "
            "Built to explore async patterns, clean architecture, and production-grade "
            "error handling under concurrent load."
        ),
        "tags": [
            "FastAPI",
            "Redis",
            "WebSocket",
            "Async Python",
            "Microservices",
            "Docker",
        ],
        "github_url": "https://github.com/lucachak/CourierIQ",
        "live_url": None,
        "accent": "accent6",
    },
]


TICKER_ITEMS = [
    "Python",
    "Django",
    "Java",
    "Spring Boot",
    "HTMX",
    "PostgreSQL",
    "Tailwind CSS",
    "REST APIs",
    "Linux",
    "Neovim",
    "Git",
    "Pentesting",
    "CTF",
    "Web Recon",
    "USB HID",
    "Network Protocols",
    "Microservices",
    "Docker",
    "Redis",
    "FastAPI",
]


# ─────────────────────────────────────────────
#  ABOUT — skills blocks
# ─────────────────────────────────────────────

CORE_SKILLS = [
    "Python",
    "Django",
    "Java",
    "Spring Boot",
    "PostgreSQL",
    "HTMX",
    "Tailwind CSS",
    "REST APIs",
    "Docker",
]

EXTRA_SKILLS = [
    "FastAPI",
    "Redis",
    "Celery",
    "Stripe API",
    "Three.js",
    "Thymeleaf",
    "Spring Security",
    "Neon DB",
]

LANGUAGES = [
    {"flag": "🇧🇷", "name": "Portuguese", "level": "Native"},
    {"flag": "🇺🇸", "name": "English", "level": "Fluent"},
    {"flag": "🇭🇺", "name": "Hungarian", "level": "Conversational"},
    {"flag": "🇪🇸", "name": "Spanish", "level": "Intermediate"},
]


def home(request):
    return render(
        request,
        "core/index.html",
        {
            "ticker_items": TICKER_ITEMS,
        },
    )


def about(request):
    return render(
        request,
        "core/about.html",
        {
            "core_skills": CORE_SKILLS,
            "extra_skills": EXTRA_SKILLS,
            "languages": LANGUAGES,
        },
    )


def projects(request):
    return render(
        request,
        "core/projects.html",
        {
            "projects": PROJECTS,
        },
    )


def contact(request):
    return render(request, "core/contact.html", {})

