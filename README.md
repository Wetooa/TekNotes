<div align="center">
  <img src="static/images/TekNotes-Logo.svg" alt="TekNotes Logo" height="80" />

  <h1>TekNotes</h1>
  <p><strong>A Community-Driven Note-Sharing Platform</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Django-5.1.1-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/WebSockets-Channels-FF6B35?style=flat-square" alt="Django Channels" />
    <img src="https://img.shields.io/badge/Redis-7-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
    <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License" />
  </p>

  <p>
    <a href="https://docs.google.com/document/d/1URJTpm3Hlx0y7B3-uTi-na-PMkL6C_RROTKfRzmD46E/edit">📄 Requirements</a> ·
    <a href="https://docs.google.com/spreadsheets/d/1Qv9dornM_tmBx_DIsR6O0nfzdDsjAocptcZI_6YKM88/edit?gid=0#gid=0">📅 Gantt Chart</a> ·
    <a href="https://drive.google.com/file/d/1Bi56yTs5twpEBNrrCoPJ5UbGa4qi9qPO/view">🗄️ ERD</a> ·
    <a href="https://www.figma.com/design/7dlTzt0s6K7ueXBsQ9X7Vf/TekNotes?node-id=0-1&node-type=canvas&t=lIU4MJopDo3t4F11-0">🎨 Figma</a>
  </p>
</div>

---

## About

**TekNotes** is a web-based platform designed to enhance collaboration and resource-sharing among students. Users can share, access, and collaborate on notes, study materials, and other academic resources — fostering a supportive learning environment that enriches the overall academic experience.

> Built for **CSIT327 Information Management 2**

### Authors

| Name | Role |
|---|---|
| Christian Gelo Cadavos | Developer |
| Simon Lyster Escaño | Developer |
| Adrian Sajulga | Developer |

---

## Features

- 📝 **Note sharing** — create, publish, and browse community notes
- 💬 **Real-time chat** — WebSocket-powered direct messaging between users
- 🔔 **Notifications** — stay updated on activity relevant to you
- 🔍 **Advanced search** — find notes and users quickly
- 🏷️ **Tags & courses** — organize content by subject
- 🔐 **OAuth login** — sign in with Google or Microsoft via django-allauth

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.1.1, Daphne (ASGI) |
| Real-time | Django Channels 4, Redis 7 |
| Database | PostgreSQL 16 (prod), SQLite (dev) |
| Frontend | Django Templates, Tailwind CSS, jQuery |
| Auth | django-allauth (Google, Microsoft) |
| Editor | CKEditor 5 |
| Storage | SFTP (prod), local media (dev) |
| Container | Docker Compose |

---

## Getting Started

### Option 1 — Docker (recommended)

1. Copy the example environment file and fill in your values:

   ```bash
   cp .env.example .env
   ```

2. Start all services:

   ```bash
   docker compose up -d
   ```

   The app will be available at `http://localhost:8000`. Migrations and static file collection run automatically on startup.

---

### Option 2 — Local Development

**Prerequisites:** Python 3.12+, a running Redis instance (for WebSocket support)

1. Create and activate a virtual environment:

   ```bash
   # Linux / macOS
   python3 -m venv venv && source venv/bin/activate

   # Windows
   python -m venv venv && .\venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy and configure environment variables:

   ```bash
   cp .env.example .env
   # Edit .env — at minimum set DJANGO_SECRET_KEY
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The app will be available at `http://localhost:8000`.

---

## Environment Variables

See [`.env.example`](.env.example) for the full list. Key variables:

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for dev, `False` for prod |
| `ALLOWED_HOSTS` | Space-separated list of allowed hostnames |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins for HTTPS |
| `DB_*` | PostgreSQL connection settings |
| `REDIS_URL` | Redis URL (e.g. `redis://redis:6379`) |
| `SFTP_*` | SFTP credentials for production media storage |
| `GOOGLE_CLIENT_ID/SECRET` | Google OAuth credentials |

---

## Contributing

### Branch Naming

| Type | Format |
|---|---|
| Feature | `feature/<feature-name>` |
| Bug fix | `fix/<issue-description>` |
| Hotfix | `hotfix/<issue-description>` |
| Docs | `docs/<update-description>` |

Please keep branch names descriptive and follow this structure to maintain consistency.

---

## License

This project is open-source and available under the [MIT License](LICENSE).
