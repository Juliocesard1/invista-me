from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForms



    


def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username') 
            messages.success(request,f'O usuario {usuario} foi criado com sucesso' )
            return redirect('login')
       

    else:
        formulario = UserRegisterForms()


    
    return  render  (request,'usuarios/registrar.html',{'formulario': formulario})  