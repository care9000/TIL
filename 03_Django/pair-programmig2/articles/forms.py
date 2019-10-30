from .models import Article,Comment
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]