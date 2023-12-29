from django.shortcuts import render
from .models import Tools


def about_me(request, *args, **kwargs):
    """
    Renders the About page
    """
    tools = Tools.objects.all().first()

    return render(
        request,
        "tools.html",
        {
            "tools": tools
        },
    )

