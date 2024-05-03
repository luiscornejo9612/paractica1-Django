from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UsuariForm
from . import models


def teachers(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    # teachers = [
    #             {"id": 1, "nom":"Oriol", "Cognom":"Roca", "edat":34, "Rol":"teachers","curs":"DAW2"},
    #             {"id": 2, "nom":"Juan", "Cognom":"perez", "edat":30, "Rol":"teachers", "curs":"DAM"},
    #             {"id": 3, "nom":"Juanma", "Cognom":"sanchez", "edat":40, "Rol":"teachers", "curs":"DAW"}
    #            ]
    teachers = list(models.Usuari.objects.filter(rol_id=1))
    return render(request,'teachers.html', {"dataTeachers": teachers})

def students(request):
    # students = [
    #             {"id": 1, "nom":"Luis", "Cognom":"antonio", "edat":27, "Rol":"students", "curs":"DAM"},
    #             {"id": 2, "nom":"Pablo", "Cognom":"perez", "edat":20, "Rol":"students","curs":"DAW2"},
    #             {"id": 3, "nom":"Jose", "Cognom":"Marañon", "edat":24, "Rol":"students","curs":"DAW"}
    #            ]
    students = list(models.Usuari.objects.filter(rol_id=2))
    return render(request,'students.html', {"dataStudents": students})


def infoAlumnat(request, student_id):
    try:
        # Suponiendo que student_id es el parámetro que recibe el ID del estudiante desde la URL
        id_DB = student_id
        student = models.Usuari.objects.get(id=id_DB)
        nom = student.nom

        # Si se encuentra el estudiante con el ID proporcionado, renderiza la plantilla con los datos del estudiante
        return render(request, 'infoAlumnat.html', {"student_info": student})
    except models.Usuari.DoesNotExist:
        # Si no se encuentra ningún estudiante con el ID proporcionado, puedes mostrar un mensaje de error o redirigir a otra página.
        return render(request, 'error.html', {"message": "El estudiante no existe"})

def user_form(request):
    form = UsuariForm()
 
    if request.method == 'POST':
        form = UsuariForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        
    context = {'form':form}
    return render(request, 'form.html', context)



def update_user(request, pk):
    person = models.Usuari.objects.get(id = pk)
    form = UsuariForm(instance=person)

    if request.method == 'POST':
        form = UsuariForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        
    context = {'form':form}
    return render(request, 'form.html', context)




def delete_user (request, pk):
    person = models.Usuari.objects.get(id = pk)

    if request.method == 'POST':
        person.delete()
        return redirect('teachers')
    
    context = {'object':person}
    return render(request, 'delete_object.html', context)
   