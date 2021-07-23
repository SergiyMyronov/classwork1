from classwork.models import Post

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def index(request):
    return HttpResponse("Hello, world. You're at the classwork index.")


def login(request):
    return HttpResponse("Log in through the admin panel")


class PostListView(ListView):
    model = Post
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_active=True)


class UserPostListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'classwork/user_post_list.html'
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    success_url = reverse_lazy('user_post_list')
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Post
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    success_url = reverse_lazy('post_detail')


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Post
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    success_url = reverse_lazy('user_post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        self.object = post
        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Post
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    success_url = reverse_lazy('user_post_list')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Post
    success_url = reverse_lazy('user_post_list')
