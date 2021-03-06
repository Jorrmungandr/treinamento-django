from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse  
from django.urls import reverse_lazy
from templated_email import send_templated_mail


def index(request):
    return render(request, 'core/index.html', {'posts':Post.objects.all()})

class ContatoView(generic.TemplateView):
    template_name = 'core/contato.html'
    def post (self,request, *args, **kwargs):
        print('teste')
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        assunto=request.POST.get('assunto')
        mensagem=request.POST.get('mensagem')
        send_templated_mail(
        template_name='email',
        from_email= email,
        recipient_list=['edgarmarques123321@gmail.com'],
        context={
            'nome':nome,
            'email':email,
            'telefone':telefone,
            'assunto':assunto,
            'mensagem':mensagem
        },)
        print('teste2')
        return HttpResponseRedirect(reverse_lazy("core:contato"))

class CreatePostView(generic.CreateView):
    template_name = 'core/create-post.html'
    model = Post
    form_class = PostForm

    #   
    #   O teu erro tava nessa função:
    #   Tu tava chamando get_sucess_url e é get_success_url
    #
    # def get_sucess_url(self):
    #     return reverse_lazy('core:index')

    def get_success_url(self):
        return reverse_lazy('core:index')

    
    def get_initial(self):
        return {'author': self.request.user}
        
# Create your views here.admin/core/posts/
