from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView

from .forms import BlogForm
from .models import Blogs, Category


class HomeBlogs(ListView):
    model = Blogs
    template_name = "cool/blogs_list.html"
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context

    def get_queryset(self):
        return Blogs.objects.filter(is_published=True).select_related("category")


class BlogsByCategory(ListView):
    model = Blogs
    template_name = "cool/home_blogs_list.html"
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs["category_id"])
        return context

    def get_queryset(self):
        return Blogs.objects.filter(
            category_id=self.kwargs["category_id"], is_published=True
        ).select_related("category")


class ViewBlogs(DetailView):
    model = Blogs
    context_object_name = "blogs_item"


class CreateBlog(CreateView):
    form_class = BlogForm
    template_name = "cool/add_blog.html"


def get_category(request, category_id):
    blogs = Blogs.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, "cool/category.html", {"blogs": blogs, "category": category})
