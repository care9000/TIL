from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content.',
                'rows': 10,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article  
        fields = ('title', 'content', )
        # widgets = {
        #     'title': forms.TextInput(
        #     attrs={
        #         'class': 'my-title',
        #         'placeholder': 'Enter the title!',
        #         }
        #     )
        # }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

# 사진에 대한 정보, 그 사진을 설명해주는 또 다른 데이터 Meta data
# ArticleForm을 설명해주는 메타 데이터

# class ArticleForm(forms.Form):
#     # title = forms.CharField(max_length=20)
#     # content = forms.CharField(widget=forms.Textarea)
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title!',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content!',
#                 'rows': 10,
#                 'cols': 50,
#             }
#         )
#     )