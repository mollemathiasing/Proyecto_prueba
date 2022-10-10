from re import template
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader   #para generar template
import random
from home.models import Persona
from django.shortcuts import render   #herramienta de Django para generar los render

def hola (request):
    return HttpResponse("Hola a")

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
    # cargar_archivo = open(r'C:\Users\Mathias\Documents\Python - Coderhouse\Proyecto-clases\home\templates\tu_template.html', 'r')  #llamamos el archivo al cual le queremos hacer un template
    # template = Template(cargar_archivo.read())                                                                             #con esto generamos un template del archivo q teniamos enn html
    # cargar_archivo.close()                                                                             #cerramos el archivo
    # contexto = Context({'persona': nombre})                                                                                #creamos un contexto, tiene la inforkación q le queremos pasar al templateS
    # template_renderizado= template.render(contexto)                                                                       #puesta en marcha, dibujamos el template 
    
    #forma simplificada:
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

def crear_persona(request, nombre, apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad= random.randrange(1,99), fecha_nacimiento=datetime.now())
    persona.save()
    
    # template = loader.get_template('crear_persona.html')    
    # template_renderizado = template.render({'persona': persona})
    # return HttpResponse('')
    
    # Reemplazo todo lo anterior por lo siguiente:
    
    return render(request, 'home/crear_persona.html', {'persona': persona})   

def ver_personas(request):
    
    #le paso a la base de datos todfos los objetos de personas
    
    persona = Persona.objects.all()
    
    # template = loader.get_template('ver_persona.html')    
    # template_renderizado = template.render({'personas': persona})
    # return HttpResponse(template_renderizado)
    
    # Reemplazo todo lo anterior por lo siguiente:
    
    return render(request, 'home/ver_persona.html', {'personas': persona})

def index(request):
    
    return render(request, 'home/index.html')