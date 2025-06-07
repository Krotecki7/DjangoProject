from django.urls import path, include
from blogs.apps import BlogsConfig
from .views import BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView, BlogDeleteView

appname = BlogsConfig.name

urlpatterns = [
    path("blogs/blogs_list/", BlogListView.as_view(), name="blogs_list"),
    path("blogs/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/detail/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete")
]
