from django import forms
  
class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 30)
    apellido = forms.CharField(max_length= 30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required = False)
    
class BusquedaPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 30, required=False)