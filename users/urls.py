from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.user_account, name="account"),
    path('edit-account/', views.edit_account, name="edit-account"),

    path('create-skill/', views.create_skill, name="create-skill"),
    path('update-skill/<str:pk>/', views.update_skill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.delete_skill, name="delete-skill"),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('send-message/<str:pk>/', views.createMessage, name="create-message"),

]
