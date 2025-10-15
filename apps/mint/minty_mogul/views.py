from django.shortcuts import render


def landing(request):
    """MintyMogul landing page."""
    return render(request, "minty_mogul/landing.html")
