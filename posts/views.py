"""Posts Views"""

from django.contrib.auth.mixins import LoginRequiredMixin
# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm
# Models
from posts.models import Post


# from django.http import HttpResponse


# LoginRequired into Views
class CreatePostView_buy(LoginRequiredMixin, CreateView):
    """Create New Post View de Compra"""
    template_name = 'posts/new-buy.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


class CreatePostView_sell(LoginRequiredMixin, CreateView):
    """Create New Post View de Venta"""
    template_name = 'posts/new-sell.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context


class PostFeedView(ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Detail view posts"""
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'
