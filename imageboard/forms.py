from django import forms
from django.forms import ModelForm
from .models import Post


class PostFormAdmin(ModelForm):
	class Meta:
		models = Post
		fields = ('title', 'date_posted', 'image_link', 'contents')
		labels = {
			'title': '',
			'date_posted': 'YYYY-MM-DD HH:MM:SS',
			'imagelink': 'image_link',
			'description': '',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}),
			'date_posted': forms.TextInput(attrs={'class':'form-control', 'placeholder':'date_posted'}),
			'image_link': forms.CharField(attrs={'class':'form-select', 'placeholder':'Imagelink'}),
			'contents': forms.Textarea(attrs={'class':'form-control', 'placeholder':'contents'}),
		}

# User Event Form
class PostForm(ModelForm):
	class Meta:
		models = Post
		fields = ('title', 'date_posted', 'image_link', 'contents')
		labels = {
			'title': '',
			'date_posted': 'YYYY-MM-DD HH:MM:SS',
			'imagelink': 'image_link',
			'description': '',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}),
			'date_posted': forms.TextInput(attrs={'class':'form-control', 'placeholder':'date_posted'}),
			'image_link': forms.CharField(attrs={'class':'form-select', 'placeholder':'Imagelink'}),
			'contents': forms.Textarea(attrs={'class':'form-control', 'placeholder':'contents'}),
		}

