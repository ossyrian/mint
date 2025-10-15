# Django static file asset directory

This directory hosts everything needed to build and package frontend
JavaScript/CSS/assets/etc. to be served by Django. This packaging step is handled by
Vite. During development, we use `docker compose` to mount the Vite dev server, which
allows Django to route all appropriate requests to Vite. For production, we use Vite to
build static assets and package those assets with the production Docker container.
