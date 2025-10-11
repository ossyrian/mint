# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Mint is a whimsical recreation of BasilMarket (a MapleStory auction house) using modern web technologies. The codebase uses a monorepo structure with separate frontend and backend applications.

**Stack:**
- Frontend: Svelte 5 + Vite 7 + Tailwind CSS 4 + Skeleton UI
- Backend: Django 5 + Django REST Framework + drf-spectacular
- Database: PostgreSQL 17
- Package Managers: pnpm (frontend), uv (backend)

## Key Development Commands

### Running the Full Stack

**Docker Compose (Recommended):**
```bash
# Start all services (postgres, backend, frontend)
docker compose up

# Rebuild after dependency changes
docker compose up --build

# Stop all services
docker compose down
```

**Manual Development:**
```bash
# Backend (from apps/backend/)
uv run python manage.py runserver

# Frontend (from apps/ui/)
pnpm dev
```

### Backend Commands

```bash
# From apps/backend/

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

### Frontend Commands

```bash
# From apps/ui/

# Start dev server
pnpm dev

# Build for production
pnpm build

# Type check
pnpm check

# Preview production build
pnpm preview
```

## Architecture

### Django-Vite Integration

The backend serves the frontend through django-vite integration. In development, Django generates script tags pointing to the Vite dev server for HMR support while maintaining same-host serving through the Django server.

**Key Configuration:**
- `apps/backend/mint/settings.py` - DJANGO_VITE settings point to localhost:5173
- `apps/ui/vite.config.ts` - base set to `/static/` to match Django's STATIC_URL, origin set to http://localhost:8000
- `apps/backend/frontend/templates/index.html` - Uses {% vite_asset %} template tags
- Access everything at http://localhost:8000 (the Vite dev server on 5173 is accessed by the browser for assets)

**Do NOT add CORS configuration** - the browser accesses both servers on localhost.

### API Versioning Pattern

The API uses URL path versioning (`/api/v1/`, `/api/v2/`, etc.) with version-aware serializers:

1. **URLs are versioned**: `apps/backend/mint/urls.py` includes version in path
2. **Views are version-agnostic**: Views call `get_serializer_class()` which checks `request.version`
3. **Serializers are version-specific**: Located in `apps/backend/api/serializers/v1.py`, `v2.py`, etc.
4. **Serializer selector**: `apps/backend/api/serializers/__init__.py` maps versions to serializers

**To add a new API version:**
1. Create `apps/backend/api/serializers/v2.py` with new serializer
2. Update `get_item_serializer()` in `apps/backend/api/serializers/__init__.py`
3. Add "v2" to ALLOWED_VERSIONS in settings.py
4. Views automatically use correct serializer based on request version

### Django App Structure

- **`api/`** - REST API endpoints, models, serializers, viewsets
- **`frontend/`** - Serves the Svelte UI via django-vite integration

### Frontend Routing

Uses `svelte-spa-router` for client-side routing. Routes defined in `apps/ui/src/App.svelte`:
- `/` - Home page
- `/listings` - Browse items
- `/item/:id` - Item detail

All components wrapped in `Layout.svelte` which provides navigation.

## Environment Configuration

**Root `.env`** (for Docker Compose):
```bash
POSTGRES_DB=mint
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<secure-password>
SECRET_KEY=<django-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,backend
```

**Backend `.env`** (for manual setup):
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

Backend requires SECRET_KEY environment variable - will raise ValueError if missing.

## Access Points

When running via Docker Compose or manual setup:
- **Application**: http://localhost:8000/ (Django serves frontend via django-vite)
- **API**: http://localhost:8000/api/v1/
- **API Docs**: http://localhost:8000/api/v1/docs/
- **OpenAPI Schema**: http://localhost:8000/api/v1/schema/
- **Django Admin**: http://localhost:8000/admin/

Note: The Vite dev server runs on port 5173 but assets are loaded by the browser directly from localhost:5173 for HMR. You access the app through localhost:8000.

## Important Notes

- All secrets must be in `.env` files (never hardcoded)
- `.env` files are gitignored, `.env.example` is committed
- PostCSS config uses `@tailwindcss/postcss` for Tailwind CSS v4
- Frontend uses Skeleton UI component library
- Database uses PostgreSQL (never SQLite)
