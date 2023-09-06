from .models import Notes
from django import forms
class NotesFrom(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {
            'text': "Your Text Here"
        }