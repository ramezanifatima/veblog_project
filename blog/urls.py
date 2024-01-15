from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('details/<slug:slug>', views.blog_details.as_view(), name='dtails'),
    path('list', views.blog_list.as_view(), name='list'),
    path('category/<int:pk>', views.list_cstegory, name='list_category'),
    path('sidbar', views.sidbar, name='sidbar'),
    # path('serch', views.serch, name='serch'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like')
]