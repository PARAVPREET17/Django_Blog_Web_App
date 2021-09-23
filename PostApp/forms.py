# from django_summernote.widgets import  SummernoteInplaceWidget,SummernoteWidget #widgets
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField #fields
from django import forms
from .models import Post,Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=SummernoteWidget())
    # content = SummernoteTextField()
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 30}))
    is_published = forms.BooleanField(label="Publish")
    class Meta:
      model=Post
      fields=('title','category','content','image','is_published')
      # widgets={
      #   'content':forms.ChoiceField()
      # }

class CommentForm(forms.ModelForm): 
 
  class Meta:
    model = Comment
    fields=('name','email','body')     