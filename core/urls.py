from django.contrib import admin
from django.urls import path
import core.views
from .views import ContatoView, CreatePostView

app_name = 'core'

urlpatterns = [
    path('', core.views.index, name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('post/', CreatePostView.as_view(), name='criar-post')
]
