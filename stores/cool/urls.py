from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeBlogs.as_view(), name="home"),
    path("category/<int:category_id>/", BlogsByCategory.as_view(), name="category"),
    path("blogs/<int:pk>/", ViewBlogs.as_view(), name="view_blogs"),
    path("blogs/add-blog>/", CreateBlog.as_view(), name="add_blog"),
]
