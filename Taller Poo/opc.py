from re import U
from usuario import Usuario,Admin
from abc import ABC,abstractmethod
class Opc_sistema(Usuario,Admin): 

    def __init__(self,ced,nom,tel,dir,email):
        self.clave = ced
        self.nombre = nom
        self.telefono = tel
        self.direccion = dir
        self.correo = email
    def mostrar_usuario(self):
        print(self.nombre,self.clave,self.telefono,self.correo)
class Mantenimiento(Usuario):
    def __init__(self,cla,nom,tel,dir,mail,sueldo,usu=True):
        super().__init__(cla,nom,tel,dir,mail,sueldo)
        self.__usu= "Mantenimiento" if usu  else "no es de mantenimiento"
    @property
    def usu(self):
        return self.__usu
    def mostrar_usuario(self):
        super().mostrar_usuario()
        print(self.usu) 
man = Mantenimiento("0926","cristhian","$400","Control","cs@gmail.com","$400",True)
man.mostrar_usuario()
class Opc_sistema(Usuario,Admin): 
    def __init__(self,ced,nom,tel,dir,email):
        self.cedula = ced
        self.nombre = nom
        self.telefono = tel
        self.direccion = dir
        self.correo = email
    def mostrar_usuario(self):
        print(self.nombre,self.cedula,self.telefono,self.correo)
class Control(Usuario):
    def __init__(self,ced,nom,tel,dir,mail,sueldo,usu=True):
        super().__init__(ced,nom,tel,dir,mail,sueldo)
        self.__usu= "Control" if usu  else "no es de control"
    @property
    def contrato(self):
        return self.__usu
    def mostrar_usuario(self):
        super().mostrar_usuario()
        print(self.contrato) 
con = Control("0006","joel","$400","Tecnico","js@gmail.com","$700",True)
con.mostrar_usuario()
class Planificacion(Usuario):
    def __init__(self,ced,nom,tel,dir,mail,sueldo,usu=True):
        super().__init__(ced,nom,tel,dir,mail,sueldo)
        self.__usu= "Planificacion" if usu  else "no es de planificacion"
    @property
    def contrato(self):
        return self.__usu
    def mostrar_usuario(self):
        super().mostrar_usuario()
        print(self.contrato) 
pla = Planificacion("1010","Enrique","","Registra","er@gmail.com","$900",True)
pla.mostrar_usuario()

