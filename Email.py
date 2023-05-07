class Email:
    def __init__(self,id='',d='',td='',c='a'):
        self.__idCuenta = id 
        self.__dominio = d
        self.__tipoDominio = td
        self.__contraseña = c
    def returnEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}{self.__tipoDominio}"
    def getDominio(self):
        return self.__dominio
    def crearcuenta(self,dirc):
        email=dirc.split('@')
        self.__idCuenta=email[0]
        dom=email[1].split('.')
        self.__dominio=dom[0]
        self.__tipoDominio=dom[1]
    def modcontraseña(self):
       corr=False
       while corr==False:
            vieja=input('\nIngrese anterior contrseña: ')
            if vieja== self.__contraseña:
                self.__contraseña= input('\nIngrese nueva contraseña: ')
                corr=True
