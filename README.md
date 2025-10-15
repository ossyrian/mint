# Mint

A comprehensive MapleStory game database and community hub featuring game data browsing,
marketplace functionality, and guild registry.

## Overview

Mint is a full-stack web application built with Django that provides:

- **MintyDB**: Complete game database with items, mobs, NPCs, quests, skills, and world
  maps
- **MintyMogul**: Marketplace for trading items (coming soon)
- **MintyHQ**: Guild registry and management (coming soon)

The application uses server-side rendering with Django templates, enhanced with HTMX for
dynamic content and Alpine.js for interactive components.

## Tech Stack

**Frontend:**

- Django Templates
- HTMX (dynamic content loading)
- Alpine.js (interactive components)
- Tailwind CSS 4
- DaisyUI (component styling)
- Vite 7 (asset bundling with HMR)

**Backend:**

- Django 5
- Django REST Framework
- drf-spectacular (OpenAPI docs)
- PostgreSQL 17

**Package Managers:**

- `pnpm` (frontend assets)
- `uv` (Python dependencies)

## Quick Start

### Prerequisites

- Docker and Docker Compose (recommended)
- OR: Python 3.11+, Node.js 20+, PostgreSQL 17, pnpm, uv

### Using Docker Compose (Recommended)

1. **Clone and configure**:
   ```bash
   git clone <repository-url>
   cd mint
   cp .env.example .env
   # Edit .env and set secure passwords
   ```

2. **Start all services**:
   ```bash
   docker compose up
   ```

   This starts:
   - PostgreSQL on port 5432
   - Django backend on port 8000
   - Vite dev server on port 5173 (accessed by browser for HMR)

3. **Access the application**:
   - Application: http://localhost:8000/
   - API Docs: http://localhost:8000/api/v1/docs/
   - Django Admin: http://localhost:8000/admin/

4. **Stop services**:
   ```bash
   docker compose down
   ```

5. **Rebuild after changes**:
   ```bash
   docker compose up --build
   ```

### Manual Development Setup

#### Backend Setup

```bash
cd apps/mint

# Create .env file with database credentials
cp .env.example .env
# Edit .env with your PostgreSQL settings

# Install dependencies
uv sync

# Run migrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Start Django server
uv run python manage.py runserver
```

#### Frontend Assets Setup

```bash
cd apps/static-src

# Install dependencies
pnpm install

# Start Vite dev server (HMR for CSS/JS)
pnpm dev
```

Access the application at http://localhost:8000/ (Django serves the app, browser loads
assets from Vite for HMR)

## Architecture

### Vertical Slice Architecture

Mint uses vertical slice architecture where each domain is a self-contained Django app:

**Domain Apps (Complete Vertical Slices):**

- **`common/`** - Shared utilities (BaseModel with UUID lookups and soft delete)
- **`users/`** - User authentication and profiles
- **`minty_db/`** - Game database (primary focus)
- **`minty_mogul/`** - Marketplace (coming soon)
- **`minty_hq/`** - Guild registry (coming soon)

**Presentation Layer:**

- **`api/`** - REST API that imports models from all domain apps

Each domain app contains its own models, views, templates, URLs, and admin
configuration.

### Django + HTMX + Alpine.js

The application combines:

- **Server-side rendering** for SEO-friendly pages and Discord previews
- **HTMX** for partial page updates (search, pagination, filters)
- **Alpine.js** for reactive components (dropdowns, modals, tabs)
- **DaisyUI** for consistent component styling (card, btn, navbar, etc.)

### Django-Vite Integration

Vite bundles CSS and JS assets while Django serves the application:

- Vite dev server on port 5173 provides HMR
- Django on port 8000 serves the main application
- Browser loads assets directly from Vite for hot reloading
- Access everything through http://localhost:8000

## Project Structure

```
mint/
├── apps/
│   ├── mint/                        # Django project
│   │   ├── mint/                    # Project settings
│   │   │   ├── settings.py
│   │   │   └── urls.py
│   │   ├── common/                  # Shared utilities
│   │   │   └── models.py            # BaseModel (UUID, soft delete)
│   │   ├── users/                   # User management
│   │   ├── minty_db/                # Game database
│   │   │   ├── models/
│   │   │   │   ├── items.py
│   │   │   │   ├── mobs.py
│   │   │   │   ├── characters.py
│   │   │   │   ├── npcs.py
│   │   │   │   ├── quests.py
│   │   │   │   ├── world.py
│   │   │   │   └── crafting.py
│   │   │   ├── templates/minty_db/
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── admin.py
│   │   ├── minty_mogul/             # Marketplace
│   │   ├── minty_hq/                # Guild registry
│   │   ├── api/                     # REST API
│   │   │   ├── views/
│   │   │   ├── serializers/
│   │   │   └── urls.py
│   │   ├── templates/               # Base templates
│   │   ├── manage.py
│   │   └── pyproject.toml
│   └── static-src/                  # Frontend assets
│       ├── src/
│       │   ├── main.js              # HTMX + Alpine.js
│       │   └── main.css             # Tailwind + DaisyUI
│       ├── package.json
│       └── vite.config.ts
├── docker-compose.yml
├── .env.example
├── CLAUDE.md                        # Project instructions for Claude Code
└── README.md
```

## Development Commands

### Backend Commands (from `apps/mint/`)

```bash
# Run Django server
uv run python manage.py runserver

# Database migrations
uv run python manage.py makemigrations
uv run python manage.py migrate

# Create superuser
uv run python manage.py createsuperuser

# Django shell
uv run python manage.py shell

# Add Python dependency
uv add <package>

# Sync dependencies from pyproject.toml
uv sync
```

### Frontend Asset Commands (from `apps/static-src/`)

```bash
# Development mode (HMR)
pnpm dev

# Production build
pnpm build

# Preview production build
pnpm preview
```

### Docker Compose Commands

```bash
# Start all services
docker compose up

# Rebuild after dependency changes
docker compose up --build

# Stop all services
docker compose down

# View logs
docker compose logs -f mint
```

## REST API

### API Endpoints

The REST API uses versioned URLs (`/api/v1/`) with full OpenAPI documentation:

**Game Database (MintyDB):**

- `/api/v1/db/items/` - Items
- `/api/v1/db/mobs/` - Monsters
- `/api/v1/db/classes/` - Character classes
- `/api/v1/db/jobs/` - Job advancements
- `/api/v1/db/skills/` - Skills
- `/api/v1/db/npcs/` - NPCs
- `/api/v1/db/quests/` - Quests
- `/api/v1/db/continents/` - World continents
- `/api/v1/db/regions/` - World regions
- `/api/v1/db/maps/` - Maps
- `/api/v1/db/recipes/` - Crafting recipes

**Other Features:**

- `/api/v1/users/` - User management
- `/api/v1/mogul/items/` - Marketplace items
- `/api/v1/guilds/` - Guild registry

### API Documentation

- **Swagger UI**: http://localhost:8000/api/v1/docs/
- **OpenAPI Schema**: http://localhost:8000/api/v1/schema/

All API endpoints use UUIDs for lookups instead of integer IDs for improved security.

## Access Points

When running the application:

- **Main Application**: http://localhost:8000/
- **MintyDB**: http://localhost:8000/db/
- **API Documentation**: http://localhost:8000/api/v1/docs/
- **OpenAPI Schema**: http://localhost:8000/api/v1/schema/
- **Django Admin**: http://localhost:8000/admin/

## Key Features

- **SEO-Friendly**: Server-side rendering with Open Graph tags for Discord previews
- **Dynamic Content**: HTMX-powered search, pagination, and filtering without page
  reloads
- **Interactive UI**: Alpine.js for dropdowns, modals, and tabs
- **Secure APIs**: UUID-based endpoints instead of sequential integer IDs
- **Soft Delete**: All models support soft delete with restore functionality
- **Versioned API**: URL path versioning with OpenAPI documentation
- **Modern CSS**: Tailwind CSS 4 with DaisyUI component library
- **Hot Reloading**: Vite provides instant CSS/JS updates during development

## Environment Configuration

### For Docker Compose (root `.env`)

```bash
# PostgreSQL
POSTGRES_DB=mint
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<secure-password>

# Django
SECRET_KEY=<django-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,mint
```

### For Manual Backend Setup (`apps/mint/.env`)

```bash
SECRET_KEY=<django-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=mint
DB_USER=postgres
DB_PASSWORD=<password>
DB_HOST=localhost
DB_PORT=5432
```

**Important:**

- Never commit `.env` files
- Use `.env.example` as a template
- SECRET_KEY is required (Django will raise ValueError if missing)

## Database

The application uses PostgreSQL 17. Key features:

- **BaseModel**: All models inherit from `common.models.BaseModel` which provides:
  - UUID primary keys (used in API lookups)
  - Automatic timestamps (`created_at`, `updated_at`)
  - Soft delete functionality (`deleted_at`, `delete()`, `restore()`, `hard_delete()`)
  - `SoftDeleteManager` that filters out deleted records by default

## Contributing

This is a personal project, but suggestions are welcome!

### Development Guidelines

1. Create a new branch for your feature
2. Follow vertical slice architecture (keep domain logic within apps)
3. Use HTMX for dynamic content, Alpine.js for interactive components
4. Inherit from `common.models.BaseModel` for all models
5. Add API endpoints to `api/` app, not domain apps
6. Use DaisyUI classes for consistent styling
7. Write meaningful commit messages

## License

[Add license information]
