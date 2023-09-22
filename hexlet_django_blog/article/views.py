from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.article.models import Article # , Comment


class IndexView(View):
    template_name = 'articles/index.html'
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            self.template_name,
            context={'articles': articles}
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/article.html',
            context={'article': article}
        )


# class ArticleCommentsView(View):
#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(
#             Comment,
#             id=kwargs['id'],
#             article__id=kwargs['article_id']
#         )
#         return render(...)
