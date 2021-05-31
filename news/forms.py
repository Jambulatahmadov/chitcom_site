from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News Name'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News Anons'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Created Date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'News Text'
            }),
        }
