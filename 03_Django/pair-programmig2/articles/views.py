from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        return redirect('articles:index')
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        print(form)
    return render(request, 'articles/new.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    commentform = CommentForm()
    context = {
        'article': article,
        'commentform': commentform,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)    
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        form.save()
        return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def comment_create(request, article_pk):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()

    return redirect('articles:detail', article_pk)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
    
    

    
