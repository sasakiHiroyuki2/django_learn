from django.urls import path

from . import views
app_name = 'thread'

urlpatterns = [
    path('create_topic/', views.TocicCreateViewBySession.as_view(), name='create_topic'),
    path('<int:pk>/', views.TopicAndCommentView.as_view(), name='topic'),
    path('category/<str:url_code>/', views.show_catgegory, name='category'),
]
