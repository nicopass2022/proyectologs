
import os
path = "c:\script"
os.chdir(path) 

  
for file in os.listdir(): 
    
        archivo = open(path + '/' + file, 'r')

            #archivo = open(file_path,'r')
        lectura= archivo.read()
        #return HttpResponse("----------------------"+ lectura)
        
        archivo.close()






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
            fecha= texto[2:15]
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
        #lista_final.pop(0)
    #print("aca1" + lista_final[0][0])

    ###convertir la liusta en un diccionario
    #key_list = ['fecha', 'empresa']
    #value_list = ['Johnny', '27']

        #dict_from_list = {}
        #lista=[]
    #for key in key_list:    
    #for value in value_list:
        print ("aca")
        print(lista_final[1][3])
        if "BACKUP DATABASE successfully processed" in lista_final[1][3]:
            print ("Hola")
        else:
            print("revisar")
        #for valor in range(len(lista_final)):   
        #dict_from_list[key] = value
            #print ("aca2")
        #print(valor)
        #print(lista_final[valor])
        #dict_from_list[key] = lista_final[valor][1]
        #dict_from_list["fecha"] = fecha
        #dict_from_list["empresa"] = lista_final[valor][1]
            #dict_from_list.update({"fecha":fecha,"empresa":lista_final[valor][1]})
            #lista.append(dict_from_list)
            #print(dict_from_list)

            #####Guardo los datos en el modelo
            #fecha=request.POST["curso"]
#
            #return HttpResponse("se agrego backup:   "   + fecha + lectura)
    #return HttpResponse("se agrego backup:   "   )
        #value_list.remove(value)
        #break

    # print(lista)