from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template import loader
from datetime import datetime
# from contextlib import ExitStack
import os 

import re
from .models import Articulos, backup
# from .models import Curso, Familia, Profesor
# from AppCoder.models import Profesor

# Create your views here.

# def curso(request,nombre,camada):
#     micurso=Curso(nombre=nombre,camada=camada)
#     micurso.save()
#     #return HttpResponse(f"se genero curso {micurso.nombre} y la camada {micurso.camada}")
#     return render(request, "appcoder/cursos.html", {"nombre": nombre, "camada":camada})

# def profesor(request,nombre,apellido, email,profesion):
#     profe=Profesor(nombre=nombre,apellido=apellido,email=email, profesion=profesion)
#     profe.save()
#     return HttpResponse(f"se agrego el profesor {profe.nombre} , {profe.apellido}")

# def recuperar_profesor(request):
#     profe=Profesor.objects.all()
 
#     #contexto= Context({"p":profe})
#     return render(request,"template2.html",{"profe":profe})


# def recuperar_curso(request):
#     curso=Curso.objects.all()
 
#     #contexto= Context({"p":profe})
#     return render(request,"template_cursos.html",{"curso":curso})
    
# def probandotemplate(request):

#     listaNotas =[1,4,8,10,20] 
#     mihtml= open(r"C:\Users\usuario\Documents\proyecto_coder\ProyectoPrueba\ProyectoPrueba\templates\template1.html")
#     plantilla = Template(mihtml.read())
#     mihtml.close()
#     contexto= Context({"notas":listaNotas})
#     return HttpResponse(plantilla.render(contexto))

def profesores(request):
    return render(request,"appcoder/profesores.html")
    #return HttpResponse("vista de profesores")

# def estudiantes(request):
#     return render(request,"AppCoder/estudiantes.html")

# def entregables(request):
#     return render(request,"appcoder/entregables.html")

def inicio(request):
    #return render(request,"appcoder/inicio.html")
    return render(request,"AppCoder/padre.html")
 
# #agregar familiares
# def agregafamiliar(request,nombre,apellido, dni,fecha_nacimiento):
#     familiar=Familia(nombre=nombre,apellido=apellido,dni=dni,fecha_nacimiento=fecha_nacimiento)
#     familiar.save()
#     return HttpResponse(f"se agrego el familiar {familiar.nombre} , {familiar.apellido}")


# #agregar articulos
def agregaarticulos(request):

        codigo=request.POST["codigo"]
        descripcion=request.POST["descripcion"]
        stock=request.POST["stock"]
        articulo=Articulos(Codigo=codigo, descripcion=descripcion,stock=stock)
        articulo.save()
        #return HttpResponse(f"se genero curso {articulo.Codigo} y la camada {articulo.descripcion}")
        return render(request, "AppCoder/cursos.html", {"codigo": codigo, "descripcion":descripcion})

    # articulo=Articulos(codigo=codigo,descripcion=descripcion,stock=stock)
    # articulo.save()
    # return HttpResponse(f"se agrego el articulo {articulo.codigo} , {articulo.descipcion}")

def recuperar_articulos(request):
    articulos=Articulos.objects.all()
 
    #contexto= Context({"p":profe})
    return render(request,"AppCoder/recuperar_articulos.html",{"familia":articulos})




def pedidoformulario(request):






    if request.method=="POST":
        nombre=request.POST["curso"]
        camada=request.POST["camada"]
        micurso=Curso(nombre=nombre,camada=camada)
        micurso.save()
        #return HttpResponse(f"se genero curso {micurso.nombre} y la camada {micurso.camada}")
        return render(request, "appcoder/cursos.html", {"nombre": nombre, "camada":camada})
        
        
        # curso= Curso , 
        # curso.save()
        # return render (request, "AppCoder/inicio.html")
    return render(request, "AppCoder/pedidoformulario.html")


    #------------------------funcion agregar texto a la base--------
def bkp(request): 
    path = "c:\script"
    os.chdir(path) 

  
    for file in os.listdir(): 
    
        archivo = open(path + '/' + file, 'r')

            #archivo = open(file_path,'r')
        lectura= archivo.read()
        #return HttpResponse("----------------------"+ lectura)
        







    # #abro multiples txt

    
  
  
    # path = "c:\script"
    # os.chdir(path) 
  
  
  
    # def read_text_file(file_path): 
    #     with open(file_path, 'r') as f: 
    #         print(f.read()) 
  
  
#     for file in os.listdir(): 
    
#         if file.endswith(".log"): 
#             #file_path = f"{path}\{file}"
#             #file_path = "{path}\{file}"
#         #return HttpResponse("se agrego backup:   " + file_path)
        
#             #read_text_file(file_path) 
# ##################anterior a funcion
#     # with ExitStack as stack:
#     #     files = [stack.enter_context(open("C:\\script\\*.log",'r')) for fname in filenames]
#     # # Do something with "files"   

#             archivo = open(path + '/' + file, 'r')

#             #archivo = open(file_path,'r')
#             lectura= archivo.read()
# # print(archivo.readable())
# print (lectura)
# fecha= lectura[3:15]
# print (fecha)


# try:
#     found= re.search(fecha(.+?)successfully, string)
#     print(found)
# except:
#     print("An exception occurred")


#--------------------busca un texto en un string
# patterns=(fecha, "successfully")

# text=lectura
# for pattern in patterns:
#     print("buscando '%s' y '%s'"% (pattern,text), end="")
#     if re.search(pattern,text):
#         print("encontrado")
#     else:
#         print("no coincidencia")

    #usa ---Resultado para agregar elemenso a la lista
        separador="---Resultado---"
        string_list=lectura.split(separador)
    #print(string_list[1])
    #print(type(string_list))
    #--- de cada elemento de la lista, saco la fecha
        #return HttpResponse("----------------------"+ string_list)
        lista_final=[]
        for x in range(len(string_list)):
            texto=string_list[x]
            fecha= texto[2:21]
            separador1="-"
            lista_datos=texto.split(separador1)
            lista_final.append(lista_datos)
            #return HttpResponse("----------------------"+ fecha)
        # empresa=lista_datos[1]
        # print (empresa)

            # print (lista_datos)
        # separador1="-"
        # lista_datos=texto.split(separador1)

        # empresa=lista_datos[1]
        # print (empresa)
            #print("aca" + lista_final[0][0])
        lista_final.pop(0)
    #print("aca1" + lista_final[0][0])

    ###convertir la liusta en un diccionario
    #key_list = ['fecha', 'empresa']
    #value_list = ['Johnny', '27']

        #dict_from_list = {}
        #lista=[]
    #for key in key_list:    
    #for value in value_list:
       
        for valor in range(len(lista_final)):   
            if "BACKUP DATABASE successfully processed" in lista_final[valor][3]:
                resultado="satisfactorio"
            else:
                resultado="revisar"

            emp=lista_final[valor][1]
            ruta=lista_final[valor][2]
            estado=resultado
            if backup.objects.filter(empresa=emp):
                backup.objects.filter(empresa=emp).update(fecha=fecha, ruta=ruta, estado=estado)
            
                
            else:
                # mibkp=backup.objects.filter(empresa=emp)

                mibkp=backup(fecha=fecha, empresa=emp,ruta=ruta, estado=estado)
            
                mibkp.save()

            #return HttpResponse(f"se agrego el articulo  {emp} ")
    backups=backup.objects.all()
    return render(request, "AppCoder/backup.html",{"backups":backups,'time':datetime.now()})
