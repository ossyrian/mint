# Mint

The new old MapleStory auction house

## Stack

- **Frontend**: Svelte 5 + Vite + Tailwind CSS + Skeleton UI
- **Backend**: Django 5 + Django REST Framework + drf-spectacular
- **Database**: PostgreSQL
- **Package Management**: pnpm (frontend), uv (backend)

## Project Structure

```
mint/
├── apps/
│   ├── ui/          # Svelte frontend
│   └── backend/     # Django backend
│       ├── api/     # REST API app
│       └── frontend/# Frontend serving app
├── infra/           # Terraform infrastructure
└── docker-compose.yml
```

## Development Setup

### Using Docker Compose (Recommended)

1. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your settings (generate a secure SECRET_KEY!)
   ```

2. **Start all services**:
   ```bash
   docker compose up
   ```

   This will start:
   - PostgreSQL on port 5432
   - Django backend on port 8000 (serves both API and frontend)
   - Vite dev server on port 5173 (proxied through Django)

3. **Access the application**:
   - Application: http://localhost:8000/ (serves frontend via django-vite)
   - API: http://localhost:8000/api/v1/
   - API Docs: http://localhost:8000/api/v1/docs/
   - Admin: http://localhost:8000/admin/

   Note: The Vite dev server runs on port 5173 internally but is accessed through Django at port 8000 for same-host serving with HMR support.

4. **Stop all services**:
   ```bash
   docker compose down
   ```

5. **Rebuild containers** (after dependency changes):
   ```bash
   docker compose up --build
   ```

### Manual Setup

Note: Manual setup requires running both backend and frontend servers. The frontend will be accessible at http://localhost:8000/ via django-vite integration.

#### Backend

1. **Install dependencies**:
   ```bash
   cd apps/backend
   uv sync
   ```

2. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Start PostgreSQL** (if not using Docker):
   ```bash
   brew services start postgresql
   createdb mint
   ```

4. **Run migrations**:
   ```bash
   uv run python manage.py migrate
   ```

5. **Create superuser** (optional):
   ```bash
   uv run python manage.py createsuperuser
   ```

6. **Start server**:
   ```bash
   uv run python manage.py runserver
   ```

   The Django server will serve the frontend at http://localhost:8000/

#### Frontend

The frontend dev server must be running for HMR (hot module replacement) to work:

1. **Install dependencies**:
   ```bash
   cd apps/ui
   pnpm install
   ```

2. **Start dev server**:
   ```bash
   pnpm dev
   ```

## API Versioning

The API uses URL path versioning. All endpoints are versioned:

- `/api/v1/items/` - Item CRUD endpoints
- `/api/v1/schema/` - OpenAPI schema
- `/api/v1/docs/` - Swagger UI

To add a new version, create a new serializer in `apps/backend/api/serializers/` and update the version mapping.

## Environment Variables

### For Docker Compose (root .env)

```bash
# PostgreSQL
POSTGRES_DB=mint
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your-secure-password-here

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,backend
```

### For Manual Backend Setup (apps/backend/.env)

```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=mint
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

## Database

The application uses PostgreSQL. When using Docker Compose, the database is automatically created and configured.

For manual setup:
```bash
createdb mint
psql mint
```

## Contributing

This is a personal project, but suggestions are welcome!
