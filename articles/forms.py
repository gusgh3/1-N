from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        #fields = '__all__'
        #fields => 추가할 필드 이름 목록
        fields = ('content', )
        #-> content를 추가하고 보여주는 명령어
        #exclude => 제거할 필드 이름 목록
        #exclude = ('article', )
        #-> article을 제외하고 보여주는 명령어
