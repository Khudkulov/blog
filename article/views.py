
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Tag, Comment
from .form import CommentForm
from django.contrib import messages


def list_articles_view(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    articles = Article.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles_2 = Article.objects.order_by('-id')[3:]
    if cat:
        articles = articles.filter(category__name__exact=cat)

    if tag:
        articles = articles.filter(tags__name__exact=tag)

    q = request.GET.get('q')
    if q:
        q_condition = Q(name__icontains=q)
        articles = Article.objects.filter(q_condition,).order_by('-id')

    query = request.GET.get('search_author')
    if query:
        query_condition = Q(author__name__icontains=query)
        articles = Article.objects.filter(query_condition,).order_by('-id')

    context = {
        'object_list': articles,
        'categories': categories,
        'tags': tags,
        'articles_2': articles_2,
        'cat': cat,
        'tag': tag
    }
    return render(request, 'article/archive.html', context)


def detail_articles_view(request, slug):
    pid = request.GET.get('pid')

    articles = Article.objects.order_by('id')
    articles_2 = Article.objects.order_by('-id')[3:]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            if pid:
                print(pid)
                obj.parent = Comment.objects.get(id=pid)
            obj.article = article
            obj.save()
            messages.success(request, 'You have successfully commentary')
            return redirect('article:detail_articles', slug=slug)
    add = []
    for i in articles:
        add.append(i)
    article_id = add.index(article)
    if article_id == 0:
        pre_article = False
    else:
        pre_article = add[article_id-1]
    if article_id == len(add)-1:
        next_article = False
    else:
        next_article = add[article_id+1]
    context = {
        'categories': categories,
        'tags': tags,
        'articles_2': articles_2,
        'article': article,
        'comments': comments,
        'form': form,
        'pre_article': pre_article,
        'next_article': next_article,
    }
    return render(request, 'article/single-blog.html', context)


