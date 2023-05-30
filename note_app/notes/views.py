from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('notes_list')
    return render(request, 'create_note.html')


# Define other view functions for editing and deleting notes

