from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('add-author',views.addAuthor,name='add_autor'),
    path('add-blog',views.addBlog,name='add_blog')
]
