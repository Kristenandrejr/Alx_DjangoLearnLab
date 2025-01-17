from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, label='Book Title')
    author = forms.CharField(max_length=100, label='Author')
    publication_year = forms.IntegerField(label='Publication Year')

    # Optional: Custom validation
    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year < 1900 or year > 2100:
            raise forms.ValidationError("Publication year must be between 1900 and 2100.")
        return year
