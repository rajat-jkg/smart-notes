from django.db.models.query import QuerySet
from django.shortcuts import redirect
from typing import Any
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NotesFrom, MailerForm
from django.contrib.auth.decorators import login_required
from .emails import mailTo
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


#notes related views here
class addNote(CreateView):
    model = Notes
    success_url = '/allnotes'
    template_name = 'notes/add-notes.html'
    form_class = NotesFrom

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get(self, request: HttpRequest, *args: str, **kwargs: Any):
        if not (self.request.user.is_authenticated):
            return redirect('login')    
        return super().get(request, *args, **kwargs)
    
@login_required
def note(request,pk):
    note = Notes.objects.get(pk = pk)
    return render(request, 'notes/single-note.html', {'note':note})


class NotesList(LoginRequiredMixin,ListView):
    template_name = 'notes/all-notes.html'
    model = Notes
    context_object_name = 'notes'
    login_url = '/account/login'

    def get_queryset(self) -> QuerySet[Any]:
        return self.request.user.notes.all()


class updateNote(LoginRequiredMixin,UpdateView):
    template_name = 'notes/add-notes.html'
    model = Notes
    success_url= '/allnotes'
    form_class = NotesFrom
    login_url = '/account/login'

class deleteNote(LoginRequiredMixin,DeleteView):
    template_name = 'notes/delete.html'
    model= Notes
    success_url = '/allnotes'
    login_url = '/account/login'


def sendMail(request, pk):
    note = Notes.objects.get(pk = pk)
    title = note.title
    text = note.text
    if request.method=='POST':
        filled_form = MailerForm(request.POST)
        if filled_form.is_valid():
            toEmail = filled_form.cleaned_data['email']
            if mailTo(toEmail,title,text):
                return redirect('/mail-success')
            else:
                return redirect('/mail-failed')
    else:
        form = MailerForm
        return render(request, 'mails/sendmail.html',{'title': title, 'text':text, 'form': form})
    
def mailsuccess(request):
    return render(request, 'mails/success.html',{})

def mailfailure(request):
    return render(request, 'mails/failure.html',{})