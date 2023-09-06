from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('addnote', views.addNote.as_view() , name='addNote'),
   path('allnotes', views.NotesList.as_view() , name='allNotes'),
   path('notes/<int:pk>', views.note, name = 'single.note'),
   path('notes/update/<int:pk>', views.updateNote.as_view(), name = 'update.note'),
   path('notes/delete/<int:pk>', views.deleteNote.as_view(), name = 'delete.note')




]