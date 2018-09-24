from django.shortcuts import render, HttpResponse
from .models import UserModel
from .forms import UserForm


def index(request):
    user_form = UserForm(request.POST)
    template_name = 'index.html'
    if user_form.is_valid():
        print(user_form.cleaned_data)
        user_form.save(commit = True)
        return HttpResponse('success')
    return render(request,template_name, {'form': user_form})

        
        

