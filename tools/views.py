from django.shortcuts import render, get_object_or_404, reverse, HttpResponse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Tools, Rating

class ToolsList(generic.ListView):
    model = Tools
    queryset = Tools.objects.filter(status=1).order_by('-created_on')
    template_name = 'tools.html'
    paginate_by = 6

"""
def tools(request: HttpRequest) -> HttpResponse:
    Tools = Tools.objects.all()
    for tools in tools:
        rating = Rating.objects.filter(post=post, user=request.user).first()
        tools.user_rating = rating.rating if rating else 0
    return render(request, "tools.html", {"tools": tools})
"""
