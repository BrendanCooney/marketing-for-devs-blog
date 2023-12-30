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


#def about_me(request, *args, **kwargs):
#    """
#    Renders the About page
#    """
#    tools = Tools.objects.all().first()

#    return render(
#        request,
#        "tools.html",
#        {
#            "tools": tools
#        },
#    )

