from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.article.models import Article 
from .forms import ArticleForm  # , CommentArticleForm


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

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            'articles/create.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(
            request,
            'articles/create.html',
            {'form': form}
        )

# class CommentArticleView(View):
#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm()
#         return render(
#             request,
#             'comment.html',
#             {'form': form}
#         )
# 
#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST)
#         if form.is_valid()
#             comment = Comment(
#                 name = form.cleanded_data['content']
#             )
#             comment.save()
