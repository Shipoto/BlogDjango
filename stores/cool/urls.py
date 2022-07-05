from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeBlogs.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', BlogsByCategory.as_view(), name='category'),
    # path('blogs/<int:blogs_id>/', view_blogs, name='view_blogs'),
    path('blogs/<int:pk>/', ViewBlogs.as_view(), name='view_blogs'),
    # path('blogs/add-blog>/', add_blog, name='add_blog'),
    path('blogs/add-blog>/', CreateBlog.as_view(), name='add_blog'),
]