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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tool_list = context['object_list']
        ratings = [tool.average_rating() for tool in tool_list]
        context['ratings'] = ratings
        return context

def tools_detail(request, slug, *args, **kwargs):
    """
    A function-based view to view the detail of a post.
    Largely the same as the class-based, but we don't have
    different methods for GET and POST. Because it's not a
    class, all of the extra "self" stuff is removed too.

    Functionally, it's the same, but it is a bit clearer
    what's going on. To differentiate between request methods,
    we use request.method == "GET" or request.method == "POST"
    """

    queryset = Tools.objects.filter(status=1)
    tools = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "tools_detail.html",
        {
            "tools": tools,
            "rating": rating,
        },
    )