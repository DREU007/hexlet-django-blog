from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())


def about(request):
    return render(request, 'about.html')
