from re import template
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader   #para generar template
import random
from home.models import Persona
from django.shortcuts import render, redirect   #herramienta de Django para generar los render
from home.forms import BusquedaPersonaFormulario, PersonaFormulario

def hola (request):
    return HttpResponse('<h1> Holaaa</h1> ')
def fecha (request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f"La fecha y hora actual es {fecha_y_hora}")

def fecha_nacimiento (request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'La fecha aproximada een q nacio persona es {fecha}')

def mi_template (request):
    cargar_archivo = open(r'C:\Users\Mathias\Documents\Python - Coderhouse\Proyecto-clases\home\templates\mi_template.html', 'r')  #llamamos el archivo al cual le queremos hacer un template
    template = Template(cargar_archivo.read())                                                                             #con esto generamos un template del archivo q teniamos enn html
    cargar_archivo.close()                                                                                                 #cerramos el archivo
    contexto = Context()                                                                                                   #creamos un contexto
    template_renderizado = template.render(contexto)                                                                       #puesta en marcha, dibujamos el template 
    return HttpResponse(template_renderizado)                                                                              #pasamos el template al http response

def tu_template (request, nombre):
   
    template = loader.get_template('home/tu_template.html')    #La direccion de la carpeta no la puse completa porq la asigne en el archivo settings en DIR
    template_renderizado = template.render({'persona': nombre})
    
    return HttpResponse(template_renderizado)   

def prueba_template (request):
    
    mi_contexto = {'rango' : list(range(1,11)),
                   'valor_aleatorio': random.randrange(1,11),
                   }
    
    
    template = loader.get_template('home/prueba_template.html')    #La direccion de la carpeta no la puse completa porq la asigne en el archivo settings en DIR
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado) 

def crear_persona(request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data  #atributo de los formualrios q una vez validados te da la info limpia q vamos a poder usar
               
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento = data['fecha_nacimiento'] 
            if not fecha_nacimiento:                     #si viene una fecha la uso, sino usa el datetime.now
                fecha_nacimiento = datetime.now()
                
                                  
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
            persona.save()
        
            return redirect ('ver_personas')   #si se guarda el ususario correctamente va a ver personas
    
    formulario = PersonaFormulario()
            
    return render(request, 'home/crear_persona.html', {'formulario': formulario})   

def ver_personas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()
    
    formulario = BusquedaPersonaFormulario()
    
    return render(request, 'home/ver_persona.html', {'personas': personas, 'formulario' : formulario})

def index(request):
    
    return render(request, 'home/index.html')

def eliminar_persona(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect ('ver_personas')
