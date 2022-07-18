class Empresa:
    def __init__(self,nombre="Empresa XXX",tel="0985179979",dir="Milagro"):
        self.nom=nombre
        self.tel=tel
        self.dir=dir
if __name__ == "__main__":     
    emp= Empresa()
    print(f"Nombre de la Empresa : {emp.nom} ")
    print(f"Direccion de la Empresa : {emp.dir} ")
    print(f"Telefono de la Empresa : {emp.tel} ")
class Usuario:
    def __init__(self,clave,nom,tel,cargo,email,sueldo):
        self.clave = clave
        self.nombre = nom
        self.telefono = tel
        self.cargo = cargo
        self.correo = email
        self.suelo = sueldo
    def mostrar_usuario(self):
        print("Usuario: {}- {}- {}- {}- {}".format(self.clave,self.nombre,self.correo,self.cargo,self.suelo))
class Admin:
    def __init__(self,clave,nom,tel,cargo,email,sueldo):
        self.clave = clave
        self.nombre = nom
        self.telefono = tel
        self.cargo = cargo
        self.correo = email
        self.sueldo = sueldo
    def mostrar_admin1(self):
        print("Admin: {}- {}- {}- {}- {}".format(self.clave,self.nombre,self.correo,self.cargo,self.sueldo))
class Rol(Usuario):
    def __init__(self,ced,nom,tel,dir,email,sueldo,usu=True):
        super().__init__(ced,nom,tel,dir,email,sueldo)
        self.__usu= usu
    def mostrar_usuario(self):
        contra = "usuario" if self.__usu else "admin"
        super().mostrar_usuario()
        print("Rol => {}".format(contra))
class Rol_admin(Admin):
    def __init__(self,ced,nom,tel,dir,email,sueldo,adm=True):
        super().__init__(ced,nom,tel,dir,email,sueldo)
        self.__adm= adm
    def mostrar(self):
        contra = "Admin" if self.__adm else "usuario"
        super().mostrar_admin1()
        print("Rol=> {}".format(contra))
class Rol1(Admin):
    def __init__(self,ced,nom,tel,dir,cargo,email):
        super().__init__(ced,nom,tel,dir,cargo,email)
    def mostrar_admin(self):
        print("Admin: {}{}{}{}{}".format(self.cargo,self.cedula,self.nombre,self.correo,self.__adm,self.sueldo))      
class Rol2(Usuario):
    def __init__(self,ced,nom,tel,cargo,dir,email):
        super().__init__(ced,nom,tel,dir,cargo,email)
    def mostrar_usuario(self):
        print("Usuario: {}{}{}{}{}".format(self.cedula,self.cargo,self.nombre,self.correo,self.__usu,self.sueldo))
if __name__ == "__main__":
    usuario = Rol("0926","cristhian","$400","Tecnico","cs@gmail.com","$400",True)
    admin = Rol_admin("3045","joel","$600"," Controlador","js@gmail.com","$8000",True)
    usuario.mostrar_usuario()
    admin.mostrar_admin1()
