from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse


def about(request):
    return HttpResponse('aobut page')


class HomePage(TemplateView):
    template_name = "home.html"

class AboutPage(TemplateView):
    template_name = "about.html"