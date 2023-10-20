from django.shortcuts import render,redirect
from .models import investimentos
from .forms import investimentofrm
from django.contrib.auth.decorators import login_required




def so_investimento(request):
     dados ={
           'dados': investimentos.objects.all()
     }
     return render (request,'investimento.html',context=dados)


def detalhe(request,id_investimento):
    dados =   {
      'dados' : investimentos.objects.get(pk= id_investimento)
      }
    return render(request,'detalhe.html',dados) 
      

@login_required
def criar(request):
     if request.method == 'POST':
          investimento_form = investimentofrm(request.POST)
          if investimento_form.is_valid():
               investimento_form.save()
          return redirect('investimentos')
     else:
          investimento_form = investimentofrm()
          formulario = {
               'formulario':investimento_form
          }
          return render(request,'novo_investimento.html',formulario)
     

@login_required    # type: ignore
def editar(request,id_investimento):
   investimento =   investimentos.objects.get(pk=id_investimento)
   if request.method == 'GET':
          fomulario = investimentofrm(instance=investimento)
          return render(request, 'novo_investimento.html',{'formulario': fomulario})
   else:
     formulario =  investimentofrm(request.POST,instance=investimento)
     if formulario.is_valid():
          formulario.save()
          return redirect('investimentos')
     
     
@login_required     
def excluir(request,id_investimento):
     investimento = investimentos.objects.get(pk=id_investimento)
     if request.method == 'POST' :
          investimento.delete()
          return redirect('investimentos')
     return render(request,'exclusao.html',{'item': investimento})

      