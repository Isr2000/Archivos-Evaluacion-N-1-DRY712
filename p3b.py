#PARTE 3 DE APARTADO B 
acl = input(str("Introduzcael numero de ACL:"))
if int(acl)>= 1 and int (acl)<= 99:
    print ("ACL Estandard")
elif int(acl)>= 100 and int (acl)<= 199:
    print ("ACL Extendida")
else:
    print("El numero ingresado no pertenece a ACL ESTANDARD y tampoco a Extendida")
