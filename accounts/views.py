from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from menu.models import Cupcake
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout


@login_required
def user_profile(request):
    my_cakes = Cupcake.objects.filter(writer=request.user)
    context = {'cakes':my_cakes}
    return render(request,"registration/profile.html",context)

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/profile')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print(new_user.username)
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                my_cakes = Cupcake.objects.filter(writer=user)
                context = {'cakes':my_cakes}
                request.user = user
                return render(request,"registration/profile.html",context)
            else:
                return HttpResponseRedirect('/accounts/profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
