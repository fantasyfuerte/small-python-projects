nombre_del_archivo= input("Nombre del archivo:  ") + ".txt"
contenido = input("\nAhora escribe el contenido:\n\n\n")

append = input("\n\n\nSi el archivo ya existe quieres sobreescribirlo o añadir la informacion??\n1-Sobreescribirlo\n2-Añadir la información al final\n(Por defecto se agregará la informacion nueva al final)\n\n\n")

if ((append == "1" )| (append == "sobreescribirlo") | (append == "sobrescribirlo")):
    with open(nombre_del_archivo,"w",encoding="utf-8") as file:
        file.write(contenido)
    
else:
    with open(nombre_del_archivo,"a",encoding="utf-8") as file:
        file.write(contenido)
        
finish = input("\nSe ha terminado la operación correctamente\n")
    


    