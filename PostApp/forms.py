# from django_summernote.widgets import  SummernoteInplaceWidget,SummernoteWidget #widgets
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField #fields
from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=SummernoteWidget())
    # content = SummernoteTextField()
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 30}))
    class Meta:
      model=Post
      fields=('title','category','content')
      # widgets={
      #   'content':forms.ChoiceField()
      # }
      