from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('userpost/', views.UserPostListView.as_view(), name='user_post_list'),
    path('userpost/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('userpost/new', views.PostCreateView.as_view(), name='post_new'),
    path('userpost/edit/<int:pk>', views.PostUpdateView.as_view(), name='post_form'),
    path('userpost/delete/<int:pk>', views.PostDeleteView.as_view()),
    path('login/', views.login, name='login'),
]
