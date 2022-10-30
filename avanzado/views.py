from django.shortcuts import render, redirect
from avanzado.models import Mascota
from avanzado.forms import MascotaFormulario

#CLASES BASADAS EN VISTAS
from django.views.generic import ListView     #CLASE BASADA EN VISTA DE DJANGO
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()
    
    return render(request, 'avanzado/ver_mascotas.html', {'mascotas' : mascotas})


def crear_mascota(request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota = Mascota(
                nombre=datos['nombre'],
                tipo=datos['tipo'],
                edad=datos['edad'],
                fecha_nacimiento=datos['fecha_nacimiento'],                       
            )
            mascota.save()
            return redirect ('ver_mascotas')   
        else:
            return render(request, 'avanzado/crear_mascota.html', {'formulario' : formulario})  #te dice q el formulario es invalido por poner otro formato de fechca por eejmplo
                
    formulario = MascotaFormulario()

    return render(request, 'avanzado/crear_mascota.html', {'formulario' : formulario})


def editar_mascota(request, id):
    
    mascota = Mascota.objects.get(id = id)
     
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
                        
            mascota.nombre = datos['nombre']
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            mascota.save()
            
            return redirect ('ver_mascotas')   
        else:
            return render(request, 'avanzado/editar_mascota.html', {'formulario' : formulario})  #te dice q el formulario es invalido por poner otro formato de fechca por eejmplo
            
    formulario = MascotaFormulario(
        initial= {
                'nombre': mascota.nombre, 
                'tipo' : mascota.tipo, 
                'edad':mascota.edad, 
                'fecha de nacimiento' : mascota.fecha_nacimiento
              }
                                   )

    return render(request, 'avanzado/editar_mascota.html', {'formulario' : formulario, 'mascota' : mascota})
    
def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id = id)
    mascota.delete()
    return redirect ('ver_mascotas')


#VAMOS A USAR CLASES BASADAS EN VISTAS QUE BRINDA DJANGO, COMO PLANTILLAS, ESTAS SON:

#LISTAR
#CREAR
#EDITAR
#ELIMINAR
#VER

class ListaMascotas(ListView):          #La clases ListaMascotas hereda de ListView
    model = Mascota
    template_name =  'avanzado/ver_mascotas_cbv.html'                   #Nombre del template q va a usar esta clase
    

class CrearMascota(CreateView):
    model = Mascota
    success_url =   '/avanzado/mascotas/'                                   #Direccion a la cual accede cuando se crea una mascota correctamente 
    template_name =  'avanzado/crear_mascota_cbv.html'                    #Le decimos a que template ir
    fields =  ['nombre', 'tipo', 'edad', 'fecha_nacimiento']      #Datos del formulario q queremos q tenga
    
    
class EditarMascota(UpdateView):
    model = Mascota
    success_url =   '/avanzado/mascotas/'                                   #Direccion a la cual accede cuando se crea una mascota correctamente 
    template_name =  'avanzado/editar_mascota_cbv.html'                    #Le decimos a que template ir
    fields =  ['nombre', 'tipo', 'edad', 'fecha_nacimiento']      #Datos del formulario q queremos q tenga
    
class EliminarMascota(DeleteView):
    model = Mascota
    success_url =   '/avanzado/mascotas/'                                   #Direccion a la cual accede cuando se crea una mascota correctamente 
    template_name =  'avanzado/eliminar_mascota_cbv.html'                    #Le decimos a que template ir
          