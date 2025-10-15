from django.shortcuts import render


def landing(request):
    """MintyHQ landing page."""
    return render(request, "minty_hq/landing.html")
