from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .form import preguntaForm

# Create your views here.
@login_required
def EntradasAlmacenGeneral(request):
	return render(request, "fcp/entrada.html",{})

@login_required
def EntradasComprasDirectas(request):
	if request.method == 'POST':
		form = preguntaForm(request.POST)
		if form.is_valid():
			print (form.cleaned_data['asunto'])
			print (form.cleaned_data['descripcion'])
			return redirect('prueba')
	else:
		form = preguntaForm()
	return render(request,'fcp/prueba.html', {'form': form})