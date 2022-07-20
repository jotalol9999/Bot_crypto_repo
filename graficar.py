import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import *
from data import currencies
import data


def actualizar_datos():
    exec("data")


lista_monedas = []
# Creando función
print("Grafico realizado correctamente")
def funcion_graficar(moneda):    
    
    path = "./Monedas/%s-data.csv" % (moneda)
    
    df = pd.read_csv(path, sep=",")
    
    df.plot('Fecha','Precio')
    limit_down = min(df['Precio']*0.8)
    limit_up =max(df['Precio']*1.2)
    lista_monedas.append(moneda)
    
    plt.ylim(limit_down,limit_up)
    plt.show()

#print(currencies)
#Interfaz

Ventana = Tk()
Ventana.geometry("500x500")
Ventana.title("Mi interfaz")

L1 =Label(Ventana,text="Ingresa la moneda")
L1.place(x = 10, y = 15)
E1 =Entry(Ventana)
E1.place(x = 10,y =35)





billetera = []

f1 =open("./Monedas/currencies.csv","r")
df_monedas = pd.read_csv("./Monedas/currencies.csv", sep=",")
for item in df_monedas["0"]:
    billetera.append(item)

#print(df_monedas['0'])
#print(billetera)


lista =Listbox(Ventana)
for item in billetera:
    lista.insert(-1,item)

lista.place(x = 10,y= 100)


#mostrar el grafico de la moneda ingresada
def obtener_graficar ():
    moneda = E1.get()
    funcion_graficar(moneda)

B1 = Button(Ventana,text="Aceptar",command=obtener_graficar)
B1.place(x=150,y=33)

B2 = Button(Ventana,text="Actualizar",command=actualizar_datos)
B2.place(x=300,y= 100)

#mostrar la interfaz
Ventana.mainloop()

print('El programa se ha ejecutado correctamente')