from django import forms
from .models import Feedback


class AddFeedback(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Не выбрана'

    class Meta:
        model = Feedback
        fields = ['title', 'content',  'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field'}),
            'content': forms.Textarea(attrs={'class': 'text'}),
            'category': forms.Select(attrs={'class': 'cat-select'}),
        }
