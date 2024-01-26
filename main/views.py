from django.shortcuts import render, redirect
from .form import ContactForm
from article.models import Article, Category, Tag
from django.contrib import messages


def home_view(request):
    articles = Article.objects.all()

    add = []
    for article in articles:
        comment_piece = article.comments.count()
        add.append(comment_piece)
        add.sort()
        add.reverse()
        print(add)
    max_articles = []
    for i in add[:3]:
        for article in articles:
            if article.comments.count() == i:
                max_articles.append(article)
    articles = max_articles
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles_2 = Article.objects.order_by('-id')[3:]
    import random
    article_random = Article.objects.order_by('id')[random.randint(0, len(Article.objects.order_by('id'))-1)]

    context = {
        'object_list': articles,
        'categories': categories,
        'articles_2': articles_2,
        'tags': tags,
        'article_random': article_random
    }
    return render(request, 'main/index.html', context)


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context)
