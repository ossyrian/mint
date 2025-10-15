# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Mint is a comprehensive MapleStory game database and community hub. The codebase uses a monorepo structure with Django for both the REST API and server-rendered web application.

**Stack:**
- Frontend: Django Templates + HTMX + Alpine.js + Tailwind CSS 4 + DaisyUI
- Backend: Django 5 + Django REST Framework + drf-spectacular
- Build Tools: Vite 7 (for CSS/JS bundling)
- Database: PostgreSQL 17
- Package Managers: pnpm (frontend assets), uv (backend)

## Key Development Commands

### Running the Full Stack

**Docker Compose (Recommended):**
```bash
# Start all services (postgres, mint backend, frontend assets)
docker compose up

# Rebuild after dependency changes
docker compose up --build

# Stop all services
docker compose down
```

**Manual Development:**
```bash
# Backend (from apps/mint/)
uv run python manage.py runserver

# Frontend assets (from apps/static-src/)
pnpm dev
```

### Backend Commands

```bash
# From apps/mint/

# Run migrations
uv run python manage.py migrate

# Create migrations
uv run python manage.py makemigrations

# Create superuser
uv run python manage.py createsuperuser

# Django shell
uv run python manage.py shell

# Add Python dependency
uv add <package>

# Sync dependencies from pyproject.toml
uv sync
```

### Frontend Asset Commands

```bash
# From apps/static-src/

# Start dev server (HMR for CSS/JS)
pnpm dev

# Build for production
pnpm build

# Preview production build
pnpm preview
```

## Architecture

### Django + HTMX + Alpine.js Architecture

The application uses server-side rendering with Django templates, enhanced with HTMX for dynamic content loading and Alpine.js for interactive components.

**Key Concepts:**
- **Server-Side Rendering**: Django generates full HTML pages
- **HTMX**: Enables partial page updates without full reloads (search, pagination, filters)
- **Alpine.js**: Provides reactive behavior for dropdowns, modals, tabs
- **DaisyUI (CSS-only)**: Tailwind plugin for consistent component styling
- **Django Templates**: All UI rendering happens server-side

### Django-Vite Integration

Vite bundles CSS and JS assets (Tailwind, DaisyUI, HTMX, Alpine.js). Django serves the main application while Vite provides HMR in development.

**Key Configuration:**
- `apps/mint/mint/settings.py` - DJANGO_VITE settings point to localhost:5173
- `apps/static-src/vite.config.ts` - Builds main.js (HTMX + Alpine) and main.css (Tailwind + DaisyUI)
- `apps/mint/templates/base.html` - Uses {% vite_asset 'src/main.js' %} template tag
- `apps/static-src/src/main.css` - Uses Tailwind v4 CSS syntax with @source directives
- Access everything at http://localhost:8000 (Vite dev server on 5173 is accessed by browser for HMR)

**Do NOT add CORS configuration** - the browser accesses both servers on localhost.

### API Versioning Pattern

The API uses URL path versioning (`/api/v1/`, `/api/v2/`, etc.):

1. **URLs are versioned**: `apps/mint/mint/urls.py` includes version in path (`/api/<str:version>/`)
2. **Views**: ViewSets in `apps/mint/api/views/` (game.py, users.py, guilds.py, mogul.py)
3. **Serializers**: Located in `apps/mint/api/serializers/` (v1.py, game_v1.py, base.py)
4. **Router**: `apps/mint/api/urls.py` uses DRF DefaultRouter to register viewsets

**To add a new API version:**
1. Create new serializers in `apps/mint/api/serializers/v2.py`
2. Add "v2" to ALLOWED_VERSIONS in settings.py
3. Update views to use version-aware serializer selection if needed

### Vertical Slice Architecture

Mint uses **Vertical Slice Architecture** where each domain app is a complete, self-contained feature:

**Domain Apps (Complete Vertical Slices):**
- **`common/`** - Shared utilities (BaseModel with soft delete, SoftDeleteManager)
- **`users/`** - User authentication and profiles (models, admin)
- **`minty_db/`** - Game database (models, views, templates, URLs, admin) - primary focus
- **`minty_mogul/`** - Marketplace (models, views, templates, URLs, admin) - coming soon
- **`minty_hq/`** - Guild registry (models, views, templates, URLs, admin) - coming soon

**Presentation Layer (No Models):**
- **`api/`** - REST API that imports models from all domain apps (views/, serializers/, urls.py)

Each domain app contains:
- `models/` or `models.py` - Database models (inherit from common.models.BaseModel)
- `views.py` - Django views (HTML rendering with HTMX)
- `templates/<app_name>/` - HTML templates
- `urls.py` - URL routing
- `admin.py` - Django admin configuration

**BaseModel (common/models.py):**
All models inherit from BaseModel which provides:
- `uuid` field (used as lookup key in REST APIs)
- `created_at`, `updated_at` timestamps
- Soft delete functionality (`deleted_at`, `delete()`, `hard_delete()`, `restore()`)
- SoftDeleteManager (filters out soft-deleted by default)

### App Structure Example

```
apps/mint/minty_db/
├── models/                          # Game data models
│   ├── __init__.py
│   ├── base.py                      # Shared model utilities
│   ├── items.py                     # Item, ItemDrop
│   ├── mobs.py                      # Mob, MobSpawn
│   ├── characters.py                # MapleClass, Job, Skill
│   ├── npcs.py                      # NPC, NPCLocation, NPCShopItem
│   ├── quests.py                    # Quest, QuestReward
│   ├── world.py                     # Continent, Region, Map
│   └── crafting.py                  # CraftingRecipe, CraftingIngredient
├── templates/minty_db/              # Domain-specific templates
│   ├── landing.html                 # MintyDB landing page
│   ├── items/
│   │   ├── list.html               # Items list with HTMX search
│   │   └── detail.html             # Item detail page
│   └── ...                          # Other resource templates
├── views.py                         # HTML views (ListView, DetailView)
├── urls.py                          # URL patterns
└── admin.py                         # Django admin configuration
```

### Frontend Assets Structure

```
apps/static-src/
├── src/
│   ├── main.js                      # HTMX + Alpine.js imports
│   └── main.css                     # Tailwind v4 + DaisyUI (@source directives)
├── dist/                            # Build output (gitignored, Django reads from here)
├── package.json
└── vite.config.ts
```

### Routing

Routing is handled by Django URL patterns in `apps/mint/mint/urls.py` which includes domain app URLs:

**Root URLs:**
- `/` - Home page (game database focus)
- `/db/` - MintyDB (game database) - includes to `minty_db.urls`
- `/mogul/` - MintyMogul (marketplace) - includes to `minty_mogul.urls`
- `/guilds/` - MintyHQ (guild registry) - includes to `minty_hq.urls`
- `/api/v1/` - REST API (includes to `api.urls`)
- `/admin/` - Django admin

**MintyDB URLs** (`minty_db/urls.py`):
- `/db/` - Landing page
- `/db/items/` - Items list
- `/db/items/<uuid>/` - Item detail
- `/db/mobs/`, `/db/classes/`, `/db/jobs/`, `/db/skills/` - Other resources
- `/db/npcs/`, `/db/quests/`, `/db/maps/` - More resources

**API URLs** (`api/urls.py`):
Uses DRF DefaultRouter with these patterns:
- `/api/v1/users/` - User management
- `/api/v1/mogul/items/` - Marketplace items
- `/api/v1/guilds/` - Guild registry
- `/api/v1/db/classes/`, `/api/v1/db/jobs/`, `/api/v1/db/skills/` - Game data
- `/api/v1/db/items/`, `/api/v1/db/mobs/`, `/api/v1/db/npcs/` - More game data
- `/api/v1/db/continents/`, `/api/v1/db/regions/`, `/api/v1/db/maps/` - World data
- `/api/v1/db/quests/`, `/api/v1/db/recipes/` - Quest and crafting data

All API viewsets use `lookup_field = "uuid"` for detail views.

## Environment Configuration

**Root `.env`** (for Docker Compose):
```bash
POSTGRES_DB=mint
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<secure-password>
SECRET_KEY=<django-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,mint
```

**Backend `.env`** (for manual setup in `apps/mint/.env`):
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

**IMPORTANT:** Backend requires SECRET_KEY environment variable - will raise ValueError if missing.

## Access Points

When running via Docker Compose or manual setup:
- **Application**: http://localhost:8000/ (Django serves HTML + HTMX/Alpine)
- **API**: http://localhost:8000/api/v1/
- **API Docs**: http://localhost:8000/api/v1/docs/ (Swagger UI via drf-spectacular)
- **OpenAPI Schema**: http://localhost:8000/api/v1/schema/
- **Django Admin**: http://localhost:8000/admin/

Note: The Vite dev server runs on port 5173 but assets are loaded by the browser directly from localhost:5173 for HMR. You access the app through localhost:8000.

## Important Notes

- All secrets must be in `.env` files (never hardcoded)
- `.env` files are gitignored, `.env.example` should be committed
- Tailwind v4 uses new CSS syntax with `@import 'tailwindcss'` and `@source` directives
- DaisyUI is used via `@plugin 'daisyui'` in main.css
- Database uses PostgreSQL (never SQLite)
- HTMX handles dynamic content updates (search, pagination, filters)
- Alpine.js handles interactive components (dropdowns, modals, tabs)
- Focus is on game database (MintyDB) - MintyMogul and MintyHQ are coming soon
- Django templates use DaisyUI classes: `.card`, `.btn`, `.navbar`, `.footer`, etc.
- SEO-friendly with server-side rendering and Open Graph tags for Discord previews
- All models inherit from `common.models.BaseModel` for UUID lookups and soft delete
- API uses UUIDs instead of integer IDs (see `api/serializers/base.py`)
- API viewsets tagged with "MintyDB", "MintyMogul", "MintyHQ", or "Users" for drf-spectacular docs
