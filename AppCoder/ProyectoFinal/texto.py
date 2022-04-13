
import os
# from contextlib import ExitStack
# with ExitStack as stack:
#     files = [stack.enter_context(open(fname)) for fname in filenames]
#     # Do something with "files"
# # with open("C:\\script\\backup.txt") as temp_f:
# #     datafile = temp_f.readlines()
# #     for line in datafile:
# #         if 'Abaco' in line:
# #             print("ok") # The string is found
# #     #return False  # The string does not exist in the file
# # with open(r"C:\\script\\backup.txt",'r') as fp:
    
# #     fp.seek(0.10)

# #     print (fp.read())
# # string= open("C:\\script\\backup.txt",'r')
# # fecha= string[0:10]
# # print (fecha)

# # from ast import Try
# # import re
# # import string


# # archivo = open("C:\\script\\backup.log",'r')
# # lectura= archivo.read()
# # # print(archivo.readable())
# # # print (lectura)
# # # fecha= lectura[3:15]
# # # print (fecha)


# # # try:
# # #     found= re.search(fecha(.+?)successfully, string)
# # #     print(found)
# # # except:
# # #     print("An exception occurred")


# # #--------------------busca un texto en un string
# # # patterns=(fecha, "successfully")

# # # text=lectura
# # # for pattern in patterns:
# # #     print("buscando '%s' y '%s'"% (pattern,text), end="")
# # #     if re.search(pattern,text):
# # #         print("encontrado")
# # #     else:
# # #         print("no coincidencia")

# # #usa ---Resultado para agregar elemenso a la lista
# # separador="---Resultado---"
# # string_list=lectura.split(separador)
# # #print(string_list[1])
# # #print(type(string_list))
# # #--- de cada elemento de la lista, saco la fecha
# # lista_final=[]
# # for x in range(len(string_list)):
# #     texto=string_list[x]
# #     fecha= texto[2:15]
# #     separador1="-"
# #     lista_datos=texto.split(separador1)
# #     lista_final.append(lista_datos)
# #     # empresa=lista_datos[1]
# #     # print (empresa)

# #     # print (lista_datos)
# # # separador1="-"
# # # lista_datos=texto.split(separador1)

# # # empresa=lista_datos[1]
# # # print (empresa)
# # print("aca" + lista_final[0][0])
# # lista_final.pop(0)
# # #print("aca1" + lista_final[0][0])

# # ###convertir la liusta en un diccionario
# # #key_list = ['fecha', 'empresa']
# # #value_list = ['Johnny', '27']

# # dict_from_list = {}
# # lista=[]
# # #for key in key_list:    
# #   #for value in value_list:
 
# # for valor in range(len(lista_final)):   
# #     #dict_from_list[key] = value
# #     print ("aca2")
# #     #print(valor)
# #     #print(lista_final[valor])
# #     #dict_from_list[key] = lista_final[valor][1]
# #     #dict_from_list["fecha"] = fecha
# #     #dict_from_list["empresa"] = lista_final[valor][1]
# #     dict_from_list.update({"fecha":fecha,"empresa":lista_final[valor][1]})
# #     lista.append(dict_from_list)
# #     print(dict_from_list)
    
    
# #     #value_list.remove(value)
# #     #break

# # print(lista)

# def bkp(request):    
#     archivo = open("C:\\script\\backup.log",'r')
#     lectura= archivo.read()



# # try:
# #     found= re.search(fecha(.+?)successfully, string)
# #     print(found)
# # except:
# #     print("An exception occurred")


# #--------------------busca un texto en un string
# # patterns=(fecha, "successfully")

# # text=lectura
# # for pattern in patterns:
# #     print("buscando '%s' y '%s'"% (pattern,text), end="")
# #     if re.search(pattern,text):
# #         print("encontrado")
# #     else:
# #         print("no coincidencia")

# #usa ---Resultado para agregar elemenso a la lista
#     separador="---Resultado---"
#     string_list=lectura.split(separador)
# #print(string_list[1])
# #print(type(string_list))
# #--- de cada elemento de la lista, saco la fecha
#     lista_final=[]
#     for x in range(len(string_list)):
#         texto=string_list[x]
#         fecha= texto[2:15]
#         separador1="-"
#         lista_datos=texto.split(separador1)
#         lista_final.append(lista_datos)
#     # empresa=lista_datos[1]
#     # print (empresa)

#     # print (lista_datos)
# # separador1="-"
# # lista_datos=texto.split(separador1)

# # empresa=lista_datos[1]
# # print (empresa)
#     #print("aca" + lista_final[0][0])
#     lista_final.pop(0)
# #print("aca1" + lista_final[0][0])

# ###convertir la liusta en un diccionario
# #key_list = ['fecha', 'empresa']
# #value_list = ['Johnny', '27']

#     #dict_from_list = {}
#     #lista=[]
# #for key in key_list:    
#   #for value in value_list:
 
#     for valor in range(len(lista_final)):   
#     #dict_from_list[key] = value
#         #print ("aca2")
#     #print(valor)
#     #print(lista_final[valor])
#     #dict_from_list[key] = lista_final[valor][1]
#     #dict_from_list["fecha"] = fecha
#     #dict_from_list["empresa"] = lista_final[valor][1]
#         #dict_from_list.update({"fecha":fecha,"empresa":lista_final[valor][1]})
#         #lista.append(dict_from_list)
#         #print(dict_from_list)

#         #####Guardo los datos en el modelo
#         #fecha=request.POST["curso"]
       
# #         emp=lista_final[valor][1]
# #         #mibkp=backup(fecha="fecha",empresa=emp)
        
# #         #mibkp.save()
# #         return HttpResponse("se agrego backup")
# #         print(emp)
    
# #     #value_list.remove(value)
# #     #break

#    # print(lista)
# path = "c:\script"
# os.chdir(path) 

  
# for file in os.listdir(): 
    
#     archivo = open(path + '/' + file, 'r')

#             #archivo = open(file_path,'r')
#     lectura= archivo.read()
#     print (lectura)