from classwork.models import Comment, Post

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
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
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset().annotate(comm_cnt=Count('comment'))
        return qs.filter(is_active=True)


class UserPostListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'classwork/user_post_list.html'
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    success_url = reverse_lazy('user_post_list')
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Post
    fields = ['image', 'header', 'short_description', 'description', 'is_active']
    success_url = reverse_lazy('post_detail')

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        comm = Comment.objects.filter(post_id=context['post'], is_published=True)
        context['comm'] = comm
        return context


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


class CommentListView(ListView):
    model = Comment
    fields = ['post', 'username', 'text', 'is_published']
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        ps_id = self.request.GET.get('post')
        return qs.filter(post=ps_id, is_published=True)

    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        ps_name = self.request.GET.get('name')
        back = self.request.META.get('HTTP_REFERER')
        context['ps_name'] = ps_name
        context['back'] = back
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['username', 'text']
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        ps_name = self.request.GET.get('name')
        context['ps_name'] = ps_name
        return context

    def form_valid(self, form):
        comm = form.save(commit=False)
        comm.post_id = self.request.GET.get('post')
        comm.save()
        self.object = comm
        return HttpResponseRedirect(self.get_success_url())
