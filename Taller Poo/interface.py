from usuario import Usuario,Admin
#interface--> clase que define metodos sin implementar

class Seguridad(Usuario,Admin): 

    def __init__(self,ced,nom,contra,dir,email):
        self.clave = ced
        self.nombre = nom
        self.contra = contra
        self.direccion = dir
        self.correo = email
    def mostrar_usuario(self):
         print(f"Nombre del Usuario :{self.nombre}")
         print(f"Clave : {self.clave}")
         print(f"Contraseña : {self.contra}")
class Contraseña(Seguridad):
     def __init__(self,cla,contra,nom,dir,mail,usu=True):
         super().__init__(cla,contra,nom,dir,mail)
         self.__usu= "Contraseña correcta" if usu  else "Contraseña incorrecta"
     @property
     def usu(self):
         return self.__usu
     def mostrar_admin(self):
         super().mostrar_usuario()
         print(self.usu) 
contra = Contraseña("0926","Cristhian","*******","","",False)
contra.mostrar_admin()


class Seguridad(Usuario,Admin): 

    def __init__(self,ced,nom,contra,dir,email):
        self.clave = ced
        self.nombre = nom
        self.contra = contra
        self.direccion = dir
        self.correo = email
    def mostrar_usuario(self):
         print(f"Nombre del Admin :{self.nombre}")
         print(f"Clave : {self.clave}")
         print(f"Contraseña : {self.contra}")
class Contraseña(Seguridad):
     def __init__(self,cla,contra,nom,dir,mail,usu=True):
         super().__init__(cla,contra,nom,dir,mail)
         self.__usu= "Contraseña correcta" if usu  else "Contraseña incorrecta"
     @property
     def usu(self):
         return self.__usu
     def mostrar_admin(self):
         super().mostrar_usuario()
         print(self.usu) 
contra = Contraseña("3045","joel","***","","",True)
contra.mostrar_admin()
