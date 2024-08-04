from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

from .models import Article
def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    abstract = article.abstract
    content = article.content
    article_id = article.article_id
    published_date = article.published_date
    return_str = "title:%s, abstract:%s, content:%s, article_id:%s, published_date:%s" % (title, abstract, content, article_id, published_date)
    return HttpResponse(return_str)