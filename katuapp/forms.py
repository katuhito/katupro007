# from pyexpat import model
# from socket import fromshare
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content')
