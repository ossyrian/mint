from django.shortcuts import render


def index(request):
    """Serve the frontend with Vite integration."""
    return render(request, 'index.html')
