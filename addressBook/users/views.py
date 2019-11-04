from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Osoba, Email, Telefon
from .forms import UserRegisterForm
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):

    query = request.GET.get('q')
    posts = []
    for user in Osoba.objects.all():
        temp_dict = dict()
        temp_dict['imie'] = user.imie
        temp_dict['nazwisko'] = user.nazwisko
        temp_dict['id'] = user._get_pk_val()
        temp_dict['emails'] = [email.email for email in Email.objects.filter(osoba=user)]
        temp_dict['phones'] = [telefon.telefon for telefon in Telefon.objects.filter(osoba=user)]
        posts.append(temp_dict)

    if query:
        query = str(query).lower()
        posts = [data for data in posts if
                 query in data['imie'].lower().split() or
                 query in data['nazwisko'].lower().split() or
                 query in data['emails'] or
                 query in data['phones']
                 ]

    context = {
        'posts': posts,

    }
    return render(request, 'users/home.html', context)

class UsersListView(ListView):
    model = Osoba
    template_name = 'users/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class UserDetailView(DetailView):
    model = Osoba

class UserUpdateView(UpdateView):
    model = Osoba
    fields = ['imie', 'nazwisko']

class UserDeleteView(DeleteView):
    model = Osoba
    success_url = '/'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('imie')
            messages.success(request, f'Account created for {username}!')
            return redirect('users-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class CreateEmailView(CreateView):
    model = Email
    fields = ['email']
    template_name = 'users/profile.html'

    def form_valid(self, form):
        form.instance.osoba = Osoba.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class CreatePhoneView(CreateView):
    model = Telefon
    fields = ['telefon']
    template_name = 'users/profile.html'

    def form_valid(self, form):
        form.instance.osoba = Osoba.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)



