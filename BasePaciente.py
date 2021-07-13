from Paciente import Paciente
from ficha import*
from Persona import *
from tkinter import *

#Pacientes Base
pcte1= Paciente(19792702, "Felipe", "Soto",88183474)
pcte2= Paciente(24815545, "Roberto", "Mesias",65168161)
pcte3= Paciente(21891656, "Romina", "Aranguiz",64821235)
pcte4= Paciente(56452612, "Andre", "Saavedra",56157569)
pcte5= Paciente(92518365, "Alejandro", "Morales",79618156)

pcte1.setFicha(Ficha_Medica("Depresion","Ninguna","Presidente Riesco 6967","70,55","72,35"))
pcte2.setFicha(Ficha_Medica("Hipertiroidismo","Ninguna","Pasaje Presidente 685","71,65","71,35"))
pcte3.setFicha(Ficha_Medica("Hipertenso","Ninguna","Calle San Martín 870","70,56","72,35"))
pcte4.setFicha(Ficha_Medica("Diabético","insulina normal","Alensandri 147","70,76","72,95"))
pcte4.setFicha(Ficha_Medica("Cáncer","Ninguna","Porvenir 463","71,64","72,33"))
