from django import forms

class preguntaForm(forms.Form):
	asunto = forms.CharField(max_length=100, required=True)
	descripcion = forms.CharField(max_length=100, required=True)