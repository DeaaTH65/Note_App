from django.urls import path
from notes import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('create_note/', views.create_note, name='create_note'),  
]
