from django.urls import path
from .views import (
    UsersListView,
    UserDetailView,
    # PostCreateView,
    UserUpdateView,
    UserDeleteView,
    CreateEmailView,
    CreatePhoneView,

)
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('register/', views.register, name='register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('post/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('update/<int:pk>/email/', CreateEmailView.as_view(), name='email'),
    path('update/<int:pk>/phone/', CreatePhoneView.as_view(), name='phone'),

]