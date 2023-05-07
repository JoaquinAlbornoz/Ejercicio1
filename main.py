from Email import Email
from man_email import Manipulador_email
def test():
    p1=Email()
    p2=Email()
    p3=Email()
    c1='informatica.fcefn@gmail.com'
    c2='wicc2023@unsj-cuim.edu'
    c3='juanLiendro1957@yahoo.com'
    p1.crearcuenta(c1)
    p2.crearcuenta(c2)
    p3.crearcuenta(c3)
    print(p1.returnEmail())
    print(p2.returnEmail())
    print(p3.returnEmail())
if __name__== '__main__':
    test()
    correo=Email()
    nombre=input('\nIngrese nombre:')
    c=input('\n Ingrese corrreo:')
    correo.crearcuenta(c)
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre,c))
    correo.modcontraseña() 
    m= Manipulador_email()
    m.carga()
    dom=input('Ingrese dominio a buscar:')
    m.cont(dom)


    
