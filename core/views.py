from django.shortcuts import render
from django.views import generic
from .models import Posts

class HomeView(generic.TemplateView):
    template_name = 'home.html'
    model = Posts

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["props"] = Posts.objects.all()
        return context
        
# Create your views here.admin/core/posts/
