from ctypes import cast
from multiprocessing import AuthenticationError, context
from re import template
from turtle import pos
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .utils import *
from .models import *



class PosterHome(DataMixin, ListView):
    model = Poster
    template_name = 'poster/index.html'
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

        # context['menu'] = menu
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0

    def get_queryset(self):
        return Poster.objects.filter(is_published=True)

# def index(request): #HttpRequest
#     posts = Poster.objects.all()

#     context = {
#         'posts': posts,
#         'menu' : menu,
#         'title': 'aFISHA',
#         'afisha': 'Киноафиша',
#         'cat_selected': 0,
#     }

#     return render(request, 'poster/index.html', context=context)



def about(request): #HttpRequest
    # contact_list = Poster.objects.all()
    # paginator = Paginator(contact_list, 6)

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'poster/about.html', { 'menu': menu, 'title' : 'aFISHA about'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'poster/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Добавить фильм")
        return dict(list(context.items()) + list(c_def.items()))




# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try: 
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, "Error adding post")
#     else:
#         form = AddPostForm()
#     return render(request, 'poster/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавьте фильм', 'afisha': 'Киноафиша'})



class ContactFormView(DataMixin,FormView):
    form_class = ContactForm
    template_name = 'poster/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')





# def contact(request):
#     return HttpResponse("Обратная связь")



# def login(request):
#     return HttpResponse("Авторизация")



class ShowPost(DataMixin, DetailView):
    model = Poster
    template_name = 'poster/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        return dict(list(context.items()) + list(c_def.items()))

    


# def show_post(request, post_id):
#     post = get_object_or_404(Poster, pk=post_id)

#     context = {
#             'post': post,
#             'menu': menu,
#             'title': post.title,
#             'cat_selected': post.cat_id,
#     }
    
#     return render(request, 'poster/post.html', context=context)





    # return HttpResponse(f"Отображение статьи с id = {post_id}")


class PosterCategory(DataMixin, ListView):
    model = Poster
    template_name = 'poster/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(pk =self.kwargs['cat_id'])
        c_def = self.get_user_context(title = 'Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        # context['menu'] = menu
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # context['afisha'] = 'Киноафиша'
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Poster.objects.filter(cat__id=self.kwargs['cat_id'], is_published=True).select_related('cat')
    


# def show_category(request, cat_id):
#     posts = Poster.objects.filter(cat_id=cat_id)

#     if len(posts) == 0:
#         raise Http404()

    
#     context = {
#         'posts': posts,
#         'menu' : menu,
#         'title': 'Отображение по рубрикам',
#         'afisha': 'Киноафиша',
#         'cat_selected': cat_id,
#     }

#     return render(request, 'poster/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Увы, такой страницы не сущетсвует :(</h1>')


# def categories(request, catid):
#     if(request.POST):
#         print(request.POST)

#     return HttpResponse (f"<h1>Статьи по категориям</h1><p>{catid}</p>")

# def archive(request, year):
#     if int(year) > 2022:
#         return redirect('home', permanent=True)
#     return HttpResponse (f"<h1>Архив по годам</h1><p>{year}</p>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'poster/register.html'
    success_url = reverse_lazy ('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'poster/login.html'
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')