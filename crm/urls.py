from django.urls import path
from . import views

urlpatterns = [
    path('leads/', views.ItemListCreateView.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', views.ItemRetrieveUpdateDestroyView.as_view(), name='lead-retrieve-update-destroy'),
    path('login/', views.login, name='api-login'),

]