from django import forms

from .models import News

class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "user", "content", "image", "draft", "publish"]