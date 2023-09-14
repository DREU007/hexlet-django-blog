from django.shortcuts import render
from django.views import View
# from django.http import HttpResponse


class Index(View):
    template_name = 'articles/index.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def article(self, request, tags, article_id):
        body = f"Article number: {article_id}. Tag: {tags}"
        return render(request, self.template_name, context={'body': body})
    
