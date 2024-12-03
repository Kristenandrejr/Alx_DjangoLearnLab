from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from taggit.forms import TagWidget  # Import TagWidget

# Form for User Registration
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for Blog Post Creation and Updating
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Add tags to the form

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=TagWidget())  # Add TagWidget()

# Comment Form for Creating and Updating Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Enter your comment here...', 'rows': 4}),
        }
