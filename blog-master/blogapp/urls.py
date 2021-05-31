from django.urls import path
from .views import IndexView , BlogView , PostView , CommentView , CategoryView , TagView
urlpatterns =[
    path('' , IndexView.as_view() , name='home'), 
    path('blog/' , BlogView.as_view() , name="blog"), 
    path('post/<str:slug>/' , PostView.as_view() , name='post-detail'), 
    path('comment/<str:slug>' , CommentView.as_view() , name='comment'), 
    path('category/<str:category>' , CategoryView.as_view() , name='category'), 
    path('tags/<str:tage>' , TagView.as_view() , name='tag-view')
]