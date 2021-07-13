import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import*
from BasePaciente import*
from BaseProfesional import*
from BaseAlertas import*
from Profesional import*
from Alerta import*
from functools import partial
from ficha import*
from random import*
from datetime import date,datetime

root = tk.Tk()

#Fondo de pantalla
imagen0=tk.PhotoImage(file='fondo1.png')
background = Label(image = imagen0, text = "Imagen S.O de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#Se crea root
root.title('Hospital')
root.geometry('800x400')
root.iconphoto(False, tk.PhotoImage(file='hospitall.png'))
root.resizable(0,0)

# define el  grid layout
root.rowconfigure(0, weight=2)
root.columnconfigure(0, weight=1)

#Se crea Frame
frame=tk.Frame(root,highlightbackground="lightblue",highlightthickness=3)
frame.grid(row=0,column=0,ipadx=250,ipady=0,padx=0,pady=0)

# crear el treeview
tree = ttk.Treeview(frame,height=10,columns=("#0"))
tree.heading('#0', text='Centro Medico', anchor='w')
tree.column("#0",minwidth=200,width=800, stretch=NO)
estilo=ttk.Style(frame)
estilo.configure("Treeview.Heading", font=("Courier",10), foreground="blue")
estilo.configure("Treeview",rowheigh=700)

# adiciona opciones 

#inicializando
alerta=Alerta(1,"los sauces",1,"pendiente",22,16)
pte=Paciente(1,"vacio","h",123)
med=Profesional(1,"vacio","h",123,"esp")
fch=Ficha_Medica("","","",0,0)
lista_alerta=[]
lista_paciente=[]
profesional=[]
opc=[]



#Se agregan variables predefinidas
profesional.append(med1)
profesional.append(med2)
profesional.append(med3)
profesional.append(med4)
profesional.append(med5)

lista_paciente.append(pcte1)
lista_paciente.append(pcte2)
lista_paciente.append(pcte3)
lista_paciente.append(pcte4)
lista_paciente.append(pcte5)

lista_alerta.append(alt1)
lista_alerta.append(alt2)



lista_alerta[0].setPaciente(lista_paciente[0])
lista_alerta[0].paciente.ficha.setCondicion("Hipertenso")
lista_alerta[0].setProfesional(profesional[0])

lista_alerta[1].setPaciente(lista_paciente[1])
lista_alerta[1].paciente.ficha.setCondicion("Cancer")
lista_alerta[1].setProfesional(profesional[1])

imagen1 = tk.PhotoImage(file="alerta.png")
imagen2 = tk.PhotoImage(file="datos.png")
imagen3 = tk.PhotoImage(file="doctor.png")
imagen4 = tk.PhotoImage(file="hospitalizacion.png")
imagen5 = tk.PhotoImage(file="editar.png")
imagen6 = tk.PhotoImage(file="comprobado.png")
imagen7 = tk.PhotoImage(file="pendiente.png")
imagen8 = tk.PhotoImage(file="advertencia.png")
imagen9 = tk.PhotoImage(file="actualizar.png")
#Alertas
tree.insert('', tk.END, text='Alertas', iid=0, image=imagen1, open=False,values=0)
tree.insert('', tk.END, text='Pendientes', iid=1, image=imagen7, open=False,values=1)

tree.insert('', tk.END, text=lista_alerta[0], iid=2, open=False,values=2)
tree.insert('', tk.END, text=lista_alerta[0].paciente, iid=3, open=False,values=3)
tree.insert('', tk.END, text=lista_alerta[0].paciente.getFicha(), iid=4, open=False,values=4)
tree.insert('', tk.END, text=lista_alerta[0].getProfesional(), iid=5, open=False,values=5)
tree.insert('', tk.END, text='Despachar', iid=15, open=False,values=15)


tree.insert('', tk.END, text='Despachadas', iid=6, image=imagen6, open=False,values=6)

tree.insert('', tk.END, text=lista_alerta[1], iid=7, open=False,values=7)
tree.insert('', tk.END, text=lista_alerta[1].paciente, iid=8, open=False,values=8)
tree.insert('', tk.END, text=lista_alerta[1].paciente.getFicha(), iid=9, open=False,values=9)
tree.insert('', tk.END, text=lista_alerta[1].getProfesional(), iid=10, open=False,values=10)

#Datos
tree.insert('', tk.END, text='Datos', iid=11,image=imagen2, open=False,values=11)
tree.insert('', tk.END, text='Pacientes', iid=12, image=imagen4,open=False,values=12)
tree.insert('', tk.END, text='Medicos', iid=13,image=imagen3, open=False,values=13)
tree.insert('', tk.END, text='Emitir Alerta', iid=14, image=imagen8, open=False,values=14)
tree.insert('', tk.END, text='Añadir/Modificar/Eliminar',image=imagen5, iid=16, open=False)
tree.insert('', tk.END, text='Paciente', iid=17,image=imagen4, open=False)
tree.insert('', tk.END, text='Medico', iid=18, image=imagen3,open=False)
tree.insert('', tk.END, text='Actualizar', iid=19, image=imagen9,open=False)


tree.move(1, 0, 0)
tree.move(2, 1, 0)
tree.move(3, 2, 0)
tree.move(4, 3, 0)
tree.move(5, 2, 1)

tree.move(6, 0, 1)
tree.move(7, 6, 0)
tree.move(8, 7, 0)
tree.move(9, 8, 0)
tree.move(10, 7, 1)

tree.move(12,11,0)
tree.move(13,11,0)

tree.move(14,0,2)
tree.move(15,2,2)
tree.move(16,11,12)
tree.move(17,16,0)
tree.move(18,16,0)
""" insertarPaciente(codigo,pos_p,agr_p)

tree.selection """


#Crear Botones para interfaz
#label_paciente=Label(root, text="Pacientes",font=("Verdana",11),height=2,width=8, bg="White").place(x=50,y=220)
#boton_paciente=Button(root, text="IR",font=("Verdana",11),height=2,width=6, bg="#93C2ED").place(x=55,y=250)

#label_medico=Label(root, text="Medicos",font=("Verdana",11),height=2,width=8, bg="White").place(x=195,y=220)
#boton_medico=Button(root, text="IR",font=("Verdana",11),height=2,width=6, bg="#93C2ED").place(x=200,y=250)

global codigo,pos_p,agr_p,pos_al,pos_des,agr_m,pos_m,con_p_t,con_m_t,marcado
pos_p=0    #posicion paciente
pos_m=0    #posicion medico
pos_al=2   #posicion alerta
pos_des=1  #poscion alertas despachadas
pos_al_p=1 #posicion alerta paciente
pos_al_m=1 #posicion alerta medico
agr_p=0 # los pacientes agregados de la lista de paciente para trabajar con insertar paciente
agr_m=0 # los medicos agregados de la lista de medicos para trabajar con insertar paciente
codigo=20 #id de tree SUMAR UNO AL HACER INSERT
marcado=[] #marcado para eliminacion

con_p_t=[] #conecta el id del tree con el paciente que se guarda (codigo,i)
con_m_t=[] #conecta el id del tree con el medico que se guarda (codigo,i)
con_apt=[] #conecta el pac bajo alerta al tree
con_apt.append([3,0])
con_apt.append([8,1])

con_mpt=[] #conecta el med bajo alerta al tree
con_mpt.append([5,0])
con_mpt.append([10,1])
# Insertando la lista de pacientes el Menú Arbol
for i in range(agr_p,len(lista_paciente)):
    tree.insert('',tk.END,text=lista_paciente[i],iid=codigo,open=False,values=codigo)
    tree.move(codigo,12,pos_p)
    con_p_t.append([codigo,i])

    pos_p=pos_p+1
    codigo=codigo+1
    agr_p=agr_p+1
    

# Insertando la lista de médicos en el Menú Arbol
for i in range(agr_m,len(profesional)):
    tree.insert('',tk.END,text=profesional[i],iid=codigo,open=False,values=codigo)
    tree.move(codigo,13,pos_m)
    con_m_t.append([codigo,i])

    pos_m=pos_m+1
    codigo=codigo+1
    agr_m=agr_m+1

#variables medico
nombreM=StringVar()
apellidoM=StringVar()
numeroM=IntVar()
rutM=IntVar()
especialidad=StringVar()



#variables paciente
nombreP=StringVar()
apellidoP=StringVar()
numeroP=StringVar()
rutP=IntVar()

#variables ficha medica
condicionF=StringVar()
direccionF=StringVar()
observacionesF=StringVar()
latitudF=StringVar()
longitudF=StringVar()

patologiaF=StringVar()


imagenM=tk.PhotoImage(file='fondo1.png')
def paciente(nombreP,apellidoP,numeroP,rutP,direccionF,observacionesF,patologiaF,condicionF,latitudF,longitudF):
    #variables pacientes
    paciente = Toplevel()
    background = Label(paciente,image = imagenM, text = "Imagen S.O de fondo")
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    paciente.title("Ficha Medica")
    paciente.geometry("310x460")
    paciente.config(bg="#41576B")

    lbl_pac=Label(paciente,      text="Paciente",font=("Verdena",11))
    lbl_nombre=Label(paciente,   text="Nombre :")
    lbl_apellido=Label(paciente, text="Apellido :")
    lbl_numero=Label(paciente,   text="Numero :")
    lbl_rut=Label(paciente,      text="Rut :")

    entry_nombre=Entry(paciente,textvariable=nombreP)
    entry_apellido=Entry(paciente,textvariable=apellidoP)
    entry_numero=Entry(paciente,textvariable=numeroP)
    entry_rut=Entry(paciente,textvariable=rutP)

    #Campos PACIENTE
    lbl_pac.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    #Campos FICHA

    lbl_ficha=Label(paciente,      text="Ficha medica",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_direccion=Label(paciente, text="Direccion :",bg="#41576B",fg="white")
    lbl_observaciones=Label(paciente,   text="Observaciones :",bg="#41576B",fg="white")
    lbl_patologia=Label(paciente,  text="Patologia :",bg="#41576B",fg="white")
    lbl_condicion=Label(paciente,  text="Condición :",bg="#41576B",fg="white")
    lbl_latitud=Label(paciente,  text="Latitud :",bg="#41576B",fg="white")
    lbl_longitud=Label(paciente,  text="Longitud :",bg="#41576B",fg="white")

    entry_direccion=Entry(paciente,textvariable=direccionF)
    entry_observaciones=Entry(paciente,textvariable=observacionesF)
    entry_patologia=Entry(paciente,textvariable=patologiaF)
    entry_condicion=Entry(paciente,textvariable=condicionF)
    entry_latitud=Entry(paciente,textvariable=latitudF)
    entry_longitud=Entry(paciente,textvariable=longitudF)

    lbl_ficha.grid(row=6,column=1, padx=5, pady=5, sticky=W)

    lbl_direccion.grid(row=7,column=0, padx=5, pady=5, sticky=E)
    entry_direccion.grid(row=7,column=1, padx=5, pady=5,sticky=W)

    lbl_condicion.grid(row=8,column=0, padx=5, pady=5, sticky=E)
    entry_condicion.grid(row=8,column=1, padx=5, pady=5,sticky=W)

    lbl_observaciones.grid(row=9,column=0, padx=5, pady=5, sticky=E)
    entry_observaciones.grid(row=9,column=1, padx=5, pady=5,sticky=W)

    lbl_latitud.grid(row=10, column=0, padx=5, pady=5, sticky=E)
    entry_latitud.grid(row=10,column=1, padx=5, pady=5,sticky=W)

    lbl_longitud.grid(row=11, column=0, padx=5, pady=5, sticky=E)
    entry_longitud.grid(row=11,column=1, padx=5, pady=5,sticky=W)

    #BOTONES
    
    #Funciones para botones pacientes

    def guardarPaciente(Rut,Nombre,Apellido,Fono,Direccion,Patologia,Observacion,agrp,cod,posp):
        
        
        lista_paciente.append(Paciente(Rut.get(),Nombre.get(),Apellido.get(),Fono.get()))
        largo=len(lista_paciente)-1
        lista_paciente[largo].setFicha(Ficha_Medica(Patologia.get(),Observacion.get(),Direccion.get(),0,0))
        rutP=""
        posicion=len(lista_paciente)
        #ctualizarTablaPtes()
        insertarPaciente()
    
    

    def buscarPaciente(Rut):
        largo=len(lista_paciente)
        for i in range(largo):
            nv=lista_paciente[i].rut
            print(nv,Rut.get())
            if nv==Rut.get():
                nombreP.set(lista_paciente[i].nombre)
                apellidoP.set(lista_paciente[i].apellido)
                numeroP.set(lista_paciente[i].fono)
                direccionF.set(lista_paciente[i].ficha.direccion)
                observacionesF.set(lista_paciente[i].ficha.observaciones)
                patologiaF.set(lista_paciente[i].ficha.condicion)

    def editarPaciente(Rut,Nombre,Apellido,Fono,Direccion,Patologia,Observacion):
        largo=len(lista_paciente)
        for i in range(largo):
            nv=lista_paciente[i].rut
            print(nv,Rut.get())
            if nv==Rut.get():
                lista_paciente[i].setRut(Rut.get())
                lista_paciente[i].setNombre(Nombre.get())
                lista_paciente[i].setApellido(Apellido.get())
                lista_paciente[i].setFono(Fono.get())
                lista_paciente[i].setFicha(Ficha_Medica(Patologia.get(),Observacion.get(),Direccion.get(),0,0))
                #actualizarTablaPtes()
                act=i
                print(lista_paciente[i].rut,lista_paciente[i].nombre,lista_paciente[i].apellido,lista_paciente[i].fono,lista_paciente[i].ficha.direccion,lista_paciente[i].ficha.condicion,lista_paciente[i].ficha.observaciones)

    def eliminarPaciente(Rut):
        global con_apt,con_p_t,marcado
        z=0
        for i in lista_paciente:
            if i.rut==Rut.get():
                lista_paciente.remove(i)
                for x in con_apt:
                    if x[1]==z:
                        con_apt.remove(x)
                        for y in range(0,len(con_apt)):
                            if y>=x[1]:
                                con_apt[y][1]-=1
                for x in con_p_t:
                    if x[1]==z:
                        marcado.append(x[0])
                        con_p_t.remove(x)
                        for y in range(0,len(con_p_t)):
                            if y>=x[1]:
                                con_p_t[y][1]-=1

                #actualizarTablaPtes()
            z+=1

    btn_agregar=Button(paciente,text="Agregar",font=("Verdana",10),height=2,width=6, bg="#74C69D",command=partial(guardarPaciente,rutP,nombreP,apellidoP,numeroP,direccionF,patologiaF,observacionesF,agr_p,codigo,pos_p)).place(x=20,y=400)
    btn_editar=Button(paciente,text="Editar",font=("Verdana",10),height=2,width=6,command=partial(editarPaciente,rutP,nombreP,apellidoP,numeroP,direccionF,patologiaF,observacionesF)).place(x=90,y=400)
    btn_buscar=Button(paciente,text="Buscar",font=("Verdana",10),height=2,width=6,command=partial(buscarPaciente,rutP)).place(x=160,y=400)
    btn_eliminar=Button(paciente,text="Eliminar",font=("Verdana",10),height=2,width=6,bg="#9D0208",command=partial(eliminarPaciente,rutP)).place(x=230,y=400)

def medico(nombreM,apellidoM,numeroM,rutM,especialidad):

    medico = Toplevel()
    background = Label(medico,image = imagenM, text = "Imagen S.O de fondo")
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    medico.title("Agregar Medico")
    medico.geometry("310x400")
    medico.config(bg="Lightblue")


    lbl_med=Label(medico,          text="Medico",font=("Verdena",11))
    lbl_nombre=Label(medico,       text="Nombre :")
    lbl_apellido=Label(medico,     text="Apellido :")
    lbl_numero=Label(medico,       text="Numero :")
    lbl_rut=Label(medico,          text="Rut :")
    lbl_especialidad=Label(medico, text="Especialidad :",bg="white")

    entry_nombre=Entry(medico,textvariable=nombreM)
    entry_apellido=Entry(medico,textvariable=apellidoM)
    entry_numero=Entry(medico,textvariable=numeroM)
    entry_rut=Entry(medico,textvariable=rutM)
    entry_especialidad=Entry(medico,textvariable=especialidad)

    #Campos medico
    lbl_med.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    lbl_especialidad.grid(row=6,column=0, padx=5, pady=5, sticky=E)
    entry_especialidad.grid(row=6,column=1, padx=5, pady=5,sticky=W)

    #BOTONES

    btn_agregar=Button(medico,text="Agregar",font=("Verdana",10),height=2,width=6,bg="#74C69D",command=partial(agregarMedico,rutM,nombreM,apellidoM,numeroM,especialidad)).place(x=20,y=300)
    btn_editar=Button(medico,text="Editar",font=("Verdana",10),height=2,width=6,command=partial(editarMedico,rutM,nombreM,apellidoM,numeroM,especialidad)).place(x=90,y=300)
    btn_buscar=Button(medico,text="Buscar",font=("Verdana",10),height=2,width=6,command=partial(buscarMedico,rutM)).place(x=160,y=300)
    btn_eliminar=Button(medico,text="Eliminar",font=("Verdana",10),height=2,width=6,bg="#9D0208",command=partial(eliminarMedico,rutM)).place(x=230,y=300)

def infoPaciente(nombreP,apellidoP,numeroP,rutP,direccionF,observacionesF,condicionF,latitudF,longitudF):
    #variables pacientes
    infoPaciente = Toplevel()
    background = Label(infoPaciente,image = imagenM, text = "Imagen S.O de fondo")
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    infoPaciente.title("Ficha Medica")
    infoPaciente.geometry("350x400")
    infoPaciente.config(bg="#41576B")


    lbl_pac=Label(infoPaciente,      text="Paciente",font=("Verdena",11))
    lbl_nombre=Label(infoPaciente,   text="Nombre :")
    lbl_apellido=Label(infoPaciente, text="Apellido :")
    lbl_numero=Label(infoPaciente,   text="Numero :")
    lbl_rut=Label(infoPaciente,      text="Rut :")


    entry_nombre=Entry(infoPaciente,textvariable=nombreP)
    entry_apellido=Entry(infoPaciente,textvariable=apellidoP)
    entry_numero=Entry(infoPaciente,textvariable=numeroP)
    entry_rut=Entry(infoPaciente,textvariable=rutP)

    #Campos infoPACIENTE
    lbl_pac.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    #Campos FICHA

    lbl_ficha=Label(infoPaciente,      text="Ficha medica")
    lbl_direccion=Label(infoPaciente, text="Direccion :")
    lbl_observaciones=Label(infoPaciente,   text="Observaciones :")
    lbl_patologia=Label(infoPaciente,  text="Patologia :")
    lbl_condicion=Label(infoPaciente,  text="Condición :")
    lbl_latitud=Label(infoPaciente,  text="Latitud :")
    lbl_longitud=Label(infoPaciente,  text="Longitud :")

    entry_direccion=Entry(infoPaciente,textvariable=direccionF)
    entry_observaciones=Entry(infoPaciente,textvariable=observacionesF)
    entry_patologia=Entry(infoPaciente,textvariable=patologiaF)
    entry_condicion=Entry(infoPaciente,textvariable=condicionF)
    entry_latitud=Entry(infoPaciente,textvariable=latitudF)
    entry_longitud=Entry(infoPaciente,textvariable=longitudF)

    lbl_ficha.grid(row=6,column=1, padx=5, pady=5, sticky=W)

    lbl_direccion.grid(row=7,column=0, padx=5, pady=5, sticky=E)
    entry_direccion.grid(row=7,column=1, padx=5, pady=5,sticky=W)

    lbl_condicion.grid(row=8,column=0, padx=5, pady=5, sticky=E)
    entry_condicion.grid(row=8,column=1, padx=5, pady=5,sticky=W)

    lbl_observaciones.grid(row=9,column=0, padx=5, pady=5, sticky=E)
    entry_observaciones.grid(row=9,column=1, padx=5, pady=5,sticky=W)

    lbl_latitud.grid(row=10, column=0, padx=5, pady=5, sticky=E)
    entry_latitud.grid(row=10,column=1, padx=5, pady=5,sticky=W)

    lbl_longitud.grid(row=11, column=0, padx=5, pady=5, sticky=E)
    entry_longitud.grid(row=11,column=1, padx=5, pady=5,sticky=W)
    
def infoMedico(nombreM,apellidoM,numeroM,rutM,especialidad):
    
    medico = Toplevel()
    background = Label(medico,image = imagenM, text = "Imagen S.O de fondo")
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    medico.title("Agregar Medico")
    medico.geometry("310x250")
    medico.config(bg="#41576B")

    lbl_med=Label(medico,          text="Medico",font=("Verdena",11))
    lbl_nombre=Label(medico,       text="Nombre :")
    lbl_apellido=Label(medico,     text="Apellido :")
    lbl_numero=Label(medico,       text="Numero :")
    lbl_rut=Label(medico,          text="Rut :")
    lbl_especialidad=Label(medico, text="Especialidad :")

    entry_nombre=Entry(medico,textvariable=nombreM)
    entry_apellido=Entry(medico,textvariable=apellidoM)
    entry_numero=Entry(medico,textvariable=numeroM)
    entry_rut=Entry(medico,textvariable=rutM)
    entry_especialidad=Entry(medico,textvariable=especialidad)

    #Campos medico
    lbl_med.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    lbl_especialidad.grid(row=6,column=0, padx=5, pady=5, sticky=E)
    entry_especialidad.grid(row=6,column=1, padx=5, pady=5,sticky=W)


def agregarMedico(Rut,Nombre,Apellido,Numero,Especialidad):
    profesional.append(Profesional(Rut.get(),Nombre.get(),Apellido.get(),Numero.get(),Especialidad.get()))
    insertarMedico()

def buscarMedico(Rut):
    largo=len(profesional)
    for i in range(largo):
        nv=profesional[i].rut
        print(nv,Rut.get())
        if nv==Rut.get():
            nombreM.set(profesional[i].nombre)
            apellidoM.set(profesional[i].apellido)
            numeroM.set(profesional[i].fono)
            especialidad.set(profesional[i].especialidad)

def editarMedico(Rut,Nombre,Apellido,Fono,Especialidad):
    largo=len(profesional)
    for i in range(largo):
        nv=profesional[i].rut
        print(nv,Rut.get())
        if nv==Rut.get():
            profesional[i].setNombre(Nombre.get())
            profesional[i].setApellido(Apellido.get())
            profesional[i].setFono(Fono.get())
            profesional[i].setEspecialidad(Especialidad.get())

def eliminarMedico(Rut):
    global con_mpt,con_m_t,marcado
    z=0
    for i in profesional:
        if i.rut==Rut.get():
            profesional.remove(i)
            for x in con_mpt:
                if x[1]==z:
                    print(con_mpt)
                    con_mpt.remove(x)
                    for y in range(0,len(con_mpt)):
                        if y>=x[1]:
                            print(con_mpt)
                            con_mpt[y][1]-=1
                            print(con_mpt)
            for x in con_m_t:
                if x[1]==z:
                    marcado.append(x[0])
                    con_m_t.remove(x)
                    for y in range(0,len(con_m_t)):
                        if y>=x[1]:
                            con_m_t[y][1]-=1
            #actualizarTablaPtes()
        z+=1


def emitirAlerta():
    contador=0
    largo=len(lista_paciente)
    azar=69
    prioridad=randint(1,10)
    if largo>1:
        id=len(lista_alerta)+1
        azar=randint(0,largo-1)
        lista_alerta.append(Alerta(id,comunas[randint(0,30)],prioridad,"Pendiente",date.today(),datetime.now()))
        lg=len(lista_alerta)-1
        lista_alerta[lg].setPaciente(lista_paciente[azar])
        lista_alerta[lg].setProfesional(profesional[randint(0,len(profesional)-1)])
        insertarAlerta(azar,randint(0,len(profesional)-1))
    elif largo==1:
        lista_alerta.append(Alerta(1,comunas[randint(0,30)],prioridad,"Pendiente",date.today(),datetime.now()))
        lg=len(lista_alerta)-1
        lista_alerta[lg].setPaciente(lista_paciente[0])
        lista_alerta[lg].setProfesional(profesional[randint(0,len(profesional)-1)])
        insertarAlerta(azar,randint(0,len(profesional)-1))

def despacharAlerta():

    despacho = Toplevel()
    despacho.title("Despachar alerta")
    despacho.geometry("310x420")
    despacho.config(bg="#41576B")

    lbl_alerta=Label(despacho, text="Alerta", bg="#41576B",fg="white",font=("Verdena",13))
    lbl_prioridad=Label(despacho, text="Prioridad: ",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_paciente=Label(despacho,text="Paciente",bg="#41576B",fg="white",font=("Verdena",13))
    lbl_nombreP=Label(despacho, text="Nombre: ",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_apellidoP=Label(despacho, text="Apellido: ",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_rutP=Label(despacho, text="Rut: ",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_direccion=Label(despacho, text="Direccion: ",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_fonoP=Label(despacho, text="Fono: ",bg="#41576B",fg="white",font=("Verdena",11))


    lbl_med=Label(despacho,          text="Medico",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_nombreMed=Label(despacho,       text="Nombre :",bg="#41576B",fg="white")
    lbl_apellidoMed=Label(despacho,     text="Apellido :",bg="#41576B",fg="white")
    lbl_numeroMed=Label(despacho,       text="Numero :",bg="#41576B",fg="white")
    lbl_rut=Label(despacho,          text="Rut :",bg="#41576B",fg="white")
    lbl_especialidad=Label(despacho, text="Especialidad :",bg="#41576B",fg="white")

    entry_nombre=Entry(despacho,textvariable=nombreM)
    entry_apellido=Entry(despacho,textvariable=apellidoM)
    entry_numero=Entry(despacho,textvariable=numeroM)
    entry_rut=Entry(despacho,textvariable=rutM)
    entry_especialidad=Entry(despacho,textvariable=especialidad)

    #Campos despacho
    lbl_med.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombreMed.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellidoMed.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numeroMed.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    lbl_especialidad.grid(row=6,column=0, padx=5, pady=5, sticky=E)
    entry_especialidad.grid(row=6,column=1, padx=5, pady=5,sticky=W)

    #BOTONES

    btn_agregar=Button(despacho,text="Agregar",font=("Verdana",10),height=2,width=6,bg="#74C69D",command=partial(agregarMedico,rutM,nombreM,apellidoM,numeroM,especialidad)).place(x=20,y=300)
    btn_editar=Button(despacho,text="Editar",font=("Verdana",10),height=2,width=6,command=partial(editarMedico,rutM,nombreM,apellidoM,numeroM,especialidad)).place(x=90,y=300)
    btn_buscar=Button(despacho,text="Buscar",font=("Verdana",10),height=2,width=6,command=partial(buscarMedico,rutM)).place(x=160,y=300)
    btn_eliminar=Button(despacho,text="Eliminar",font=("Verdana",10),height=2,width=6,bg="#9D0208",command=partial(eliminarMedico,rutM)).place(x=230,y=300)


def insertarPaciente():
    global codigo
    global agr_p
    global pos_p
    global con_p_t
    for i in range(agr_p,len(lista_paciente)):
        tree.insert('',tk.END,text=lista_paciente[i],iid=codigo,open=False, values=codigo)
        tree.move(codigo,12,pos_p)

        con_p_t.append([codigo,i])

        codigo=codigo+1
        agr_p=agr_p+1
        pos_p=pos_p+1
        

def insertarMedico():
    global codigo
    global agr_m
    global pos_m
    for i in range(agr_m,len(profesional)):
        tree.insert('',tk.END,text=profesional[i],iid=codigo,open=False,values=codigo)
        tree.move(codigo,13,pos_m)

        con_m_t.append([codigo,i])

        codigo=codigo+1
        agr_m=agr_m+1
        pos_m=pos_m+1

def insertarAlerta(paci,medi):
    global codigo,pos_al,pos_des,con_apt,con_mpt
    if lista_alerta[pos_al].estado=="Pendiente":
        tree.insert('', tk.END, text=lista_alerta[pos_al], iid=codigo, open=False,values=codigo)
        tree.move(codigo, 1, pos_al)
        codigo+=1
        tree.insert('', tk.END, text=lista_alerta[pos_al].paciente, iid=codigo, open=False,values=codigo)
        tree.move(codigo, codigo-1, 0)

        con_apt.append([paci,codigo])

        codigo+=1
        tree.insert('', tk.END, text=lista_alerta[pos_al].paciente.getFicha(), iid=codigo, open=False,values=codigo)
        tree.move(codigo, codigo-1, 0)
        codigo+=1
        tree.insert('', tk.END, text=lista_alerta[pos_al].profesional, iid=codigo, open=False,values=codigo)
        tree.move(codigo, codigo-3, 1)
        
        con_mpt.append([medi,codigo])

        codigo+=1
        tree.insert('', tk.END, text='Despachar', iid=codigo, open=False,values=codigo)
        tree.move(codigo, codigo-4, 2)
        codigo+=1
        pos_al=pos_al+1
    #para Reciclar en nueva funcion
    """ if lista_alerta[pos_al].estado=="Despachada":
        tree.insert('', tk.END, text=lista_alerta[pos_al], iid=codigo, open=False)
        tree.move(codigo, 6, pos_des)
        codigo+=1
        tree.insert('', tk.END, text=lista_alerta[pos_al].paciente, iid=codigo, open=False)
        tree.move(codigo, codigo-1, 0)
        codigo+=1
        tree.insert('', tk.END, text=lista_alerta[pos_al].paciente.getFicha(), iid=codigo, open=False)
        tree.move(codigo, codigo-1, 0)
        codigo+=1
        tree.insert('', tk.END, text=lista_alerta[pos_al].profesional, iid=codigo, open=False)
        tree.move(codigo, codigo-3, 1)
        codigo+=1
        pos_des+=1
    pos_al=pos_al+1 """

#Funcion de opciones escogidas
def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        global con_p_t,marcado
        item = tree.item(selected_item)
        # list
        valor = item['values']
        nombreOpcion = item['text']
        imagen = item['image']
        abierto = item['open']

        auxRut=""
        auxNombre=""
        auxApellido=""
        auxNumero=""
        auxEspecialidad=""
        auxCondicion=""
        auxObservaciones=""
        auxDireccion=""
        auxLatitud=""
        auxLongitud=""



        # Mostrando datos de profesionales clickeados en Menu
        for i in range (0,len(profesional)):
            if nombreOpcion==str(profesional[i]):

                auxRut=profesional[i].getRut()
                auxNombre=profesional[i].getNombre()
                auxApellido=profesional[i].getApellido()
                auxEspecialidad=profesional[i].getEspecialidad()
                auxNumero=profesional[i].getFono()

                rutM.set(auxRut)
                nombreM.set(auxNombre)
                apellidoM.set(auxApellido)
                numeroM.set(auxNumero)
                especialidad.set(auxEspecialidad)
                infoMedico(nombreM,apellidoM,numeroM,rutM,especialidad)
                print(valor)
                return
        #al clickear un paciente en el Menú
        for i in range (0,len(lista_paciente)):
            if nombreOpcion==str(lista_paciente[i]):
                auxRut=lista_paciente[i].getRut()
                auxNombre=lista_paciente[i].getNombre()
                auxApellido=lista_paciente[i].getApellido()
                auxNumero=lista_paciente[i].getFono()
                auxCondicion=lista_paciente[i].ficha.getCondicion()
                auxObservaciones=lista_paciente[i].ficha.getObservaciones()
                auxDireccion=lista_paciente[i].ficha.getDireccion()
                auxLatitud=lista_paciente[i].ficha.getLatitud()
                auxLongitud=lista_paciente[i].ficha.getLongitud()

                rutP.set(auxRut)
                nombreP.set(auxNombre)
                apellidoP.set(auxApellido)
                numeroP.set(auxNumero)
                condicionF.set(auxCondicion)
                observacionesF.set(auxObservaciones)
                direccionF.set(auxDireccion)
                latitudF.set(auxLatitud)
                longitudF.set(auxLongitud)

                infoPaciente(nombreP,apellidoP,numeroP,rutP,direccionF,observacionesF,condicionF,longitudF,latitudF)
                print(valor)


        for i in range(0,codigo):
            cd="["+str(i)+"]"
            print(str(valor),cd)
            if cd==str(valor) and nombreOpcion=="Despachar":
                print(tree.parent(valor))
                tree.move(tree.parent(valor),6,pos_p)
                tree.delete(valor)
                infoMedico(nombreM,apellidoM,numeroM,rutM,especialidad) 
                return
                
        if nombreOpcion=="Actualizar":
            for i in con_p_t:
                if tree.item(i[0],option='text')!=str(lista_paciente[i[1]]):
                    tree.item(i[0],text=str(lista_paciente[i[1]])) 
            for i in con_m_t:
                if tree.item(i[0],option='text')!=str(profesional[i[1]]):
                    tree.item(i[0],text=str(profesional[i[1]]))
            for i in con_apt:
                if i[1]<len(lista_paciente):
                    if tree.item(i[0],option='text')!=str(lista_paciente[i[1]]):
                        tree.item(i[0],text=str(lista_paciente[i[1]]))
            for i in con_mpt:
                 if i[1]<len(profesional):
                    if tree.item(i[0],option='text')!=str(profesional[i[1]]):
                        tree.item(i[0],text=str(profesional[i[1]]))    
            for i in marcado:
                tree.delete(i)
            marcado=[]

        print(tree.item(2,option='text'))
        if nombreOpcion=="Emitir Alerta" :
            emitirAlerta()

        if nombreOpcion=="Medico" :
            medico(nombreM,apellidoM,numeroM,rutM,especialidad)

        if nombreOpcion=="Paciente" :
            paciente(nombreP,apellidoP,numeroP,rutP,direccionF,observacionesF,patologiaF,condicionF,latitudF,longitudF)

        
        #if nombreOpcion=="Pacientes" or  nombreOpcion=='sub opcion 21' : 

def actualizarPaciente(valor,lista_paciente):
    for i in range(0,codigo):
        cd="["+str(i)+"]"
        print(str(valor),cd)
        if cd==str(valor):
            tree.parent
            print(tree.parent(valor))
            tree.set(valor,value=lista_paciente)
            return

def eliminarMenuPac(codigo):
    tree.delete(codigo)

# control de la opcion escogida
tree.bind('<<TreeviewSelect>>', item_selected)
# ubica el arbol en la raiz 
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()