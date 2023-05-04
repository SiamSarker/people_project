from django.urls import path
from .views import PersonListCreate, PersonRetrieveUpdateDestroy

urlpatterns = [
    path('person/', PersonListCreate.as_view(), name='person-list-create'),
    path('person/<int:pk>/', PersonRetrieveUpdateDestroy.as_view(), name='person-retrieve-update-destroy'),
]
