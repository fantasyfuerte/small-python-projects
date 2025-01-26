fileName= input("File name (without extension):\n")
content = input("\nContent:\n\n\n")

append = input("\n\n\nWant to append or overwrite the file?\n1-Append\n2-Overwrite\n3-Cancel\n")

if ((append == "1" )| (append == "sobreescribirlo") | (append == "sobrescribirlo")):
    with open(fileName,"w",encoding="utf-8") as file:
        file.write(content)
    
else:
    with open(fileName,"a",encoding="utf-8") as file:
        file.write(content)
        
finish = input("\nProcess finished successfully.\n")
    


    