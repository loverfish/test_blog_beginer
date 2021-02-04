from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, Comment


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/article_list.html'
    login_url = 'login'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body',]
    template_name = 'articles/article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'articles/article_delete.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body',]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'articles/comment_new.html'
    fields = ['article', 'comment',]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
