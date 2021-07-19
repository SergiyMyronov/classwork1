from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.PostCreateView.as_view(), name='post_form'),
    path('post/edit/<int:pk>', views.PostUpdateView.as_view(), name='post_form'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view()),
    path('login/', views.login, name='login'),
]
