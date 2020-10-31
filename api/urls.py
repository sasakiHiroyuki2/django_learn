from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('v1/vote/', views.CreateVoteView.as_view(), name='create_vote'),
]
