from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Blogs, Category
from .forms import BlogForm


class HomeBlogs(ListView):
    model = Blogs
    template_name = 'cool/blogs_list.html'
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Blogs.objects.filter(is_published=True).select_related('category')


class BlogsByCategory(ListView):
    model = Blogs
    template_name = 'cool/home_blogs_list.html'
    context_object_name = 'blogs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Blogs.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewBlogs(DetailView):
    model = Blogs
    context_object_name = 'blogs_item'
    # template_name = 'cool/home_detail.html'
    # pk_url_kwarg = 'blogs_id'


class CreateBlog(CreateView):
    form_class = BlogForm
    template_name = 'cool/add_blog.html'


# def index(request):
#     blogs = Blogs.objects.all()
#     context = {
#         'blogs': blogs,
#         'title': 'Содержание блогов',
#     }
#     return render(request, 'cool/index.html', context)

def get_category(request, category_id):
    blogs = Blogs.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'cool/category.html', {'blogs': blogs, 'category': category})

# def view_blogs(request, blogs_id):
#     blogs_item = get_object_or_404(Blogs, pk=blogs_id)
#     return render(request, 'cool/view_blogs.html', {'blogs_item': blogs_item})

# def add_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             # blogs = Blogs.objects.create(**form.cleaned_data)
#             blogs = form.save()
#             return redirect(blogs)
#     else:
#         form = BlogForm()
#     return render(request, 'cool/add_blog.html', {'form': form})