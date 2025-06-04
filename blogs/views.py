from django.views.generic import ListView, DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'text', 'image',]
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.filter(is_valid=True)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'text', 'image', ]
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")

    def get_success_url(self):
        return reverse("blogs/blog_detail", args=self.kwargs.get("pk"))


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = 'blog'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blog_list")
