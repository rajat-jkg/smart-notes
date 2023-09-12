from .models import Notes
from django import forms

class MailerForm(forms.Form):
    email = forms.EmailField()
    class Meta:
        fields = ('email',)
        labels = {
            'email': 'Enter your email'
        }
class NotesFrom(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {
            'text': "Your Text Here"
        }