from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def teachers(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    teachers = [{"id": 1, 
                 "nom":"Oriol", 
                 "Cognom":"Roca", 
                 "edat":34, 
                 "Rol":"teachers",
                 "curs":"DAW2"
                },
                {"id": 2, 
                 "nom":"Juan", 
                 "Cognom":"perez", 
                 "edat":30, 
                 "Rol":"teachers",
                 "curs":"DAM"
                },
                {"id": 3, 
                 "nom":"Juanma", 
                 "Cognom":"sanchez", 
                 "edat":40, 
                 "Rol":"teachers",
                 "curs":"DAW"
                 }
                 ]
    
    return render(request,'teachers.html', {"dataTeachers": teachers})

def students(request):
    students = [{"id": 1, 
                 "nom":"Luis", 
                 "Cognom":"antonio", 
                 "edat":27, 
                 "Rol":"students",
                 "curs":"DAM"
                },
                {"id": 2, 
                 "nom":"Pablo", 
                 "Cognom":"perez", 
                 "edat":20, 
                 "Rol":"students",
                 "curs":"DAW2"
                },
                {"id": 3, 
                 "nom":"Jose", 
                 "Cognom":"Marañon", 
                 "edat":24, 
                 "Rol":"students",
                 "curs":"DAW"
                 }
                 ]
    
    return render(request,'students.html', {"dataStudents": students})

def infoAlumnat(request, student_id):
    # Suponiendo que student_id es el parámetro que recibe el ID del estudiante desde la URL
    students = [
        {"id": 1, "nom": "Luis", "Cognom": "Antonio", "edat": 27, "Rol": "student", "curs": "DAM"},
        {"id": 2, "nom": "Pablo", "Cognom": "Perez", "edat": 20, "Rol": "student", "curs": "DAW2"},
        {"id": 3, "nom": "Jose", "Cognom": "Marañon", "edat": 24, "Rol": "student", "curs": "DAW"}
    ]
    
    # Filtrar la lista de estudiantes para obtener solo el estudiante con el ID proporcionado
    student_info = None
    for student in students:
        if student["id"] == student_id:
            student_info = student
            break

    # Si se encuentra el estudiante con el ID proporcionado, renderiza la plantilla con los datos del estudiante
    return render(request, 'infoAlumnat.html', {"student_info": student_info})