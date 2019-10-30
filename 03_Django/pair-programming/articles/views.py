from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def index(request):
    # articles = ArticlesForm(request.POST)
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            article_form.save()
            # return render(request, 'articles/index.html')
            return redirect('/articles')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
        }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    # comments = Comment.objects.filter(article_id=article_pk)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def article_update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            # article.title = request.POST.get('title')
            # article.content = request.POST.get('content')
            # article.save()
        return redirect('articles:detail', article_pk)
    else:
        context = {
            'article': article,
            }
    return render(request, 'articles/update.html', context)

def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

def comment_create(request, article_pk):
    content = request.POST.get('content')
    comment = Comment(content=content, article_id=article_pk)
    comment.save()
    return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)