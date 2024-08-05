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

from django.core.paginator import Paginator
def get_index_page(request):
    # Get Page ID from URL
    page = request.GET.get("page")
    if page:
        page = int(page)
    else:
        page = 1

    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 3)
    """
    Paginator is a class in Django that facilitates pagination of a dataset.
    Args:
        1st Parm (QuerySet or list): The collection of items you want to paginate.
        2nd Parm (int): The number of items to display on each page.
    """
    number_of_pages = paginator.num_pages       # Get how many pages are there
    page_article_list = paginator.page(page)    # Get the content in current page
    top5_article_list = Article.objects.order_by('-published_date')[:10]    # Get the top 10 newest articles
                                                                            # order_by(ATTRIBUTE)

    if page_article_list.has_next():            # if there is next page
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():        # if there is previous page
        previous_page = page - 1
    else:
        previous_page = page
    
    return render(request, "index.html", {"article_list": page_article_list,
                                          "number_of_pages": range(1, number_of_pages+1),
                                          'current_page': page,
                                          'previous_page': previous_page,
                                          'next_page': next_page,
                                          'top5_article_list': top5_article_list,
                                          })

# Get information for an Article in the blog
def get_detail_page(request, article_id):
    # article = Article.objects.get(pk=article_id)
    all_articles = Article.objects.all()
    current_article = None
    previous_article = None
    previous_article_index = 0
    next_article = None
    next_article_index = 0

    # enumerate： automatically provides an index alongside each element of the iterable pass in
    for index, article in enumerate(all_articles):
        if index == 0:
            previous_article_index = 0
            next_article_index = index + 1
        elif index == len(all_articles) - 1:
            next_article_index = 0
            previous_article_index = index - 1
        else:
            previous_article_index = index - 1
            next_article_index = index + 1

        if article.article_id == article_id:
            current_article = article
            previous_article = all_articles[previous_article_index]
            next_article = all_articles[next_article_index]
            break

    return render(request, "article.html", {"current_article": current_article,
                                            "previous_article": previous_article,
                                            "next_article": next_article,
                                            })