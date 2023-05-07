from Email import Email
import csv
class Manipulador_email:
    def __init__(self):
        self.__lista=[]
    def carga(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Ejercicio 1\\emails.csv')as f:
            reader=csv.reader(f,delimiter=';')
            for fila in reader:
                if fila[0]!='' and fila[1]!='' and fila[2]!='':
                    id=fila[0]
                    d=fila[1]
                    td=fila[2]
                    c=fila[3]
                    a=Email(id,d,td,c)
                    self.__lista.append(a)
        f.close()
    def cont(self,dom):
        j=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getDominio() == dom:
                j+=1
        print(f'{j} cuentas tienen el dominio {dom}')