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

