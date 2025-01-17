from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class ArticleList(ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'article_list.html'
    context_object_name = "articles"

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = "article"

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    





