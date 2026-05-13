from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


TICKER_ITEMS = [
    "Python", "Django", "Java", "Spring Boot", "HTMX",
    "PostgreSQL", "Tailwind CSS", "Stripe API", "REST APIs",
    "Three.js", "Linux", "Neovim", "Git",
]

CORE_SKILLS = [
    "Python", "Java", "Django", "Spring Boot",
    "PostgreSQL", "HTMX", "Tailwind CSS", "Stripe",
    "OAuth2", "Neon DB", "REST APIs",
]

EXTRA_SKILLS = [
    "Three.js", "Thymeleaf", "C#", "C",
    "Pandas", "Streamlit", "Power BI", "Linux", "Git", "Neovim",
]

LANGUAGES = [
    {"flag": "🇧🇷", "name": _("Portuguese"), "level": _("Native")},
    {"flag": "🇬🇧", "name": _("English"),    "level": _("Fluent")},
    {"flag": "🇭🇺", "name": _("Hungarian"),  "level": _("Intermediate")},
    {"flag": "🇷🇺", "name": _("Russian"),    "level": _("Basic")},
]

PROJECTS = [
    {
        "featured": True,
        "accent": "accent1",
        "icon": "💰",
        "title": "FinGen",
        "description": _(
            "Personal and household finance management web app powered by AI. "
            "Connects to OpenRouter's API to give intelligent advice based on "
            "your actual financial data. Upload bank statements as PDF and let "
            "the system analyze patterns, flag risks, and suggest optimizations. "
            "Built with a full Spring Boot backend and Thymeleaf frontend with "
            "an animated Three.js coin visualization on the landing page."
        ),
        "tags": [
            "Java", "Spring Boot", "HTMX", "Thymeleaf",
            "Three.js", "OpenRouter AI", "PDF parsing", "Spring Security",
        ],
        "github_url": "https://github.com/lucachak",
        "live_url_fingen":"https://fingen-app.onrender.com" ,
        "terminal_lines": [
            {"type": "comment", "text": _("// AI financial advisor")},
            {"type": "cmd",     "text": "POST", "rest": "/api/chat/analyze"},
            {"type": "empty"},
            {"type": "out",     "text": _("→ Analyzing your finances...")},
            {"type": "out",     "text": _("→ Monthly burn: R$ 3,240")},
            {"type": "out",     "text": _("→ Savings rate: 18.4%")},
            {"type": "out",     "text": _("→ Recommendation ready ✓")},
            {"type": "empty"},
            {"type": "cursor"},
        ],
    },
    {
        "featured": False,
        "accent": "accent2",
        "icon": "🚀",
        "title": "Django SaaS Platform",
        "description": _(
            "Full-featured SaaS boilerplate with subscription billing via Stripe, "
            "Google/GitHub OAuth2 login, async tasks, and a Postgres database "
            "hosted on Neon. Production-ready architecture with proper separation "
            "of concerns and environment configuration."
        ),
        "tags": ["Python", "Django", "Stripe", "OAuth2", "PostgreSQL", "Neon DB", "Tailwind", "HTMX"],
        "github_url": "https://github.com/lucachak",
    },
    {
        "featured": False,
        "accent": "accent3",
        "icon": "🔍",
        "title": "Web Directory Scanner",
        "description": _(
            "A DIRB-like web directory brute-force scanner written in pure Python — "
            "zero external libraries. HTTP/HTTPS handlers implemented from scratch "
            "following RFC specifications. A deliberate exercise in understanding "
            "the fundamentals before reaching for abstractions."
        ),
        "tags": ["Python", "Pure stdlib", "HTTP/HTTPS", "Security tooling", "Networking"],
        "github_url": "https://github.com/lucachak",
    },
    {
        "featured": True,
        "accent": "accent4",
        "icon": "🔧",
        "title": _("Mechanic & HVAC ERP"),
        "description": _(
            "Business management system for mechanic shops and HVAC service "
            "companies. Handles service orders, inventory, client records, "
            "and invoicing. Designed for small business operators who need "
            "something that just works."
        ),
        "tags": ["Java", "Spring MVC", "ERP", "PostgreSQL", "Thymeleaf"],
        "github_url": "https://github.com/lucachak",
        "live_url_erp":"https://cambiomatic.onrender.com/",
    },
    {
        "featured": False,
        "accent": "accent5",
        "icon": "🏦",
        "title": _("Banking System in Pure Python"),
        "description": _(
            "A banking simulation that explores Python's advanced internals — "
            "metaclasses, __slots__, and descriptor protocols used to enforce "
            "business rules at the class level. More about deep language "
            "understanding than practical finance."
        ),
        "tags": ["Python", "Metaclasses", "__slots__", "OOP patterns"],
        "github_url": "https://github.com/lucachak",
    },
]


def home(request):
    return render(request, "core/index.html", {
        "ticker_items": TICKER_ITEMS,
    })


def about(request):
    return render(request, "core/about.html", {
        "core_skills": CORE_SKILLS,
        "extra_skills": EXTRA_SKILLS,
        "languages": LANGUAGES,
    })


def projects(request):
    return render(request, "core/projects.html", {
        "projects": PROJECTS,
    })


def contact(request):
    return render(request, "core/contact.html", {})