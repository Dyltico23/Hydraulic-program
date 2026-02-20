from tabulate import tabulate
import numpy as np
import math 
from scipy.interpolate import interp1d
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import os

def resource_path(relative_path):
    """Obtiene la ruta absoluta del recurso en el ejecutable."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

SistemaSI = [[0,9.81,1000,1.75E-3,1.75E-6],[5,9.81,1000,1.52E-3,1.52E-6],[10,9.81,1000,1.30E-3,1.30E-6],[15,9.81,1000,1.15E-3,1.15E-6],[20,9.79,998,1.02E-3,1.02E-6],[25,9.78,997,8.91E-4,8.94E-7],[30,9.77,996,8E-4,8.03E-7],[35,9.75,994,7.18E-4,7.22E-7],[40,9.73,992,6.51E-4,6.56E-7],[45,9.71,990,5.94E-4,6E-7],[50,9.69,988,5.41E-4,5.48E-7],[55,9.67,986,4.98E-4,5.05E-7],[60,9.65,984,4.60E-4,6.67E-7],[65,9.62,981,4.31E-4,4.39E-7],[70,9.59,978,4.02E-4,4.11E-7],[75,9.56,975,3.73E-4,3.83E-7],[80,9.53,971,3.50E-4,3.60E-7],[85,9.50,968,3.30E-4,3.41E-7],[90,9.47,965,3.11E-4,3.22E-7],[95,9.44,962,2.92E-4,3.04E-7],[100,9.40,958,2.82E-4,2.94E-7]]

SistemaSB = [[32,62.4,1.94,3.66E-5,1.89E-5],[40,62.4,1.94,3.23E-5,1.67E-5],[50,62.4,1.94,2.72E-5,1.40E-5],[60,62.4,1.94,2.35E-5,1.21E-5],[70,62.3,1.94,2.04E-5,1.05E-5],[80,62.2,1.93,1.77E-5,9.15E-6],[90,62.1,1.93,1.60E-5,8.29E-6],[100,62.0,1.93,1.42E-5,7.37E-6],[110,61.9,1.92,1.26E-5,6.55E-6],[120,61.7,1.92,1.14E-5,5.94E-6],[130,61.5,1.91,1.05E-5,5.49E-6],[140,61.4,1.91,9.60E-6,5.03E-6],[150,61.2,1.90,8.90E-6,4.68E-6],[160,61.0,1.90,8.30E-6,4.38E-6],[170,60.8,1.89,7.70E-6,4.07E-6],[180,60.6,1.88,7.23E-6,3.84E-6],[190,60.4,1.88,6.80E-6,3.63E-6],[200,60.1,1.87,6.25E-6,3.35E-6],[212,59.8,1.86,5.89E-6,3.17E-6]]

descarga = [[12,45,4.45,1.35,40,1,1.315,33.4,0.133,3.38,1.049,26.6,0.000394,3.660E-5],[25,95,5.36,1.63,40,1.25,1.660,42.2,0.140,3.56,1.380,35.1,0.01039,9.653E-4],[35,130,5.51,1.68,40,1.5,1.90,48.3,0.145,3.68,1.610,40.9,0.01414,1.314E-3],[50,190,7.88,2.40,40,1.5,1.90,48.3,0.145,3.68,1.610,40.9,0.01414,1.314E-3],[75,285,7.16,2.18,40,2,2.375,60.3,0.154,3.91,2.067,52.5,0.02333,2.168E-3],[125,475,8.37,2.55,40,2.5,2.875,73,0.203,5.16,2.469,62.7,0.03326,3.090E-3],[175,660,7.59,2.31,40,3,3.5,88.9,0.216,5.49,3.068,77.9,0.05132,4.768E-3],[250,950,6.30,1.92,40,4,4.5,114.3,0.237,6.02,4.026,102.3,0.08840,8.213E-3],[500,1890,8.01,2.44,40,5,5.563,141.3,0.258,6.55,5.047,128.2,0.1390,1.291E-2],[1000,3800,11.10,3.38,40,6,6.625,168.3,0.280,7.11,6.065,154.1,0.2006,1.864E-2],[1250,4730,8.02,2.44,40,8,8.625,219.1,0.322,8.18,7.981,202.7,0.3472,3.226E-2],[1750,6625,11.22,3.42,40,8,8.625,219.1,0.322,8.18,7.981,202.7,0.3472,3.226E-2],[2500,9450,10.16,3.10,40,10,10.750,273.1,0.365,9.27,10.020,254.5,0.5479,5.090E-2],[3500,13250,10.03,3.06,40,12,12.750,323.9,0.406,10.31,11.938,303.2,0.7771,7.219E-2]]

succion = [[12,45,1.89,0.57,40,1.5,1.90,48.3,0.145,3.68,1.610,40.9,0.01414,1.314E-3],[25,95,2.39,0.73,40,2,2.375,60.3,0.154,3.91,2.067,52.5,0.02333,2.168E-3],[35,130,2.34,0.71,40,2.5,2.875,73,0.203,5.16,2.469,62.7,0.03326,3.090E-3],[50,190,2.17,0.66,40,3,3.5,88.9,0.216,5.49,3.068,77.9,0.05132,4.768E-3],[75,285,2.43,0.74,40,3.5,4,101.6,0.226,5.74,3.548,90.1,0.06868,6.381E-3],[125,475,0.96,3.15,40,4,4.5,114.3,0.237,6.02,4.026,102.3,0.08840,8.213E-3],[175,660,2.80,0.85,40,5,5.563,141.3,0.258,6.55,5.047,128.2,0.1390,1.291E-2],[250,950,2.78,0.85,40,6,6.625,168.3,0.280,7.11,6.065,154.1,0.2006,1.864E-2],[500,1890,3.21,0.98,40,8,8.625,219.1,0.322,8.18,7.981,202.7,0.3472,3.226E-2],[1000,3800,4.06,1.24,40,10,10.750,273.1,0.365,9.27,10.020,254.5,0.5479,5.090E-2],[1250,4730,3.58,1.09,40,12,12.750,323.9,0.406,10.31,11.938,303.2,0.7771,7.219E-2],[1750,6625,4.15,1.26,40,14,14,355.6,0.437,11.10,13.126,333.4,0.9396,8.729E-2],[2500,9450,4.54,1.38,40,16,16,406.4,0.5,12.70,15,381,1.227,0.1140],[3500,13250,5.02,1.53,40,18,18,457.2,0.562,14.27,16.876,428.7,1.553,0.1443]]

tuberiaced40 = [[0.125,0.0224,6.8E-3,0.000394,3.660E-5],[0.25,0.303,9.2E-3,0.000723,6.717E-5],[0.375,0.0411,12.5E-3,0.00133,1.236E-4],[0.5,0.0518,15.8E-3,0.00211,1.960E-4],[0.75,0.0687,20.9E-3,0.00370,3.437E-4],[1,0.0874,26.6E-3,0.006,5.574E-4],[1.25,0.1150,35.1E-3,0.01039,9.653E-4],[1.5,0.1342,40.9E-3,0.01414,1.314E-3],[2,0.1723,52.5E-3,0.02333,2.168E-3],[2.5,0.2058,62.7E-3,3.03326,3.090E-3],[3,0.2557,77.9E-3,0.05132,4.768E-3],[3.5,0.2957,90.1E-3,0.06868,6.381E-3],[4,0.3355,102.3E-3,0.08840,8.213E-3],[5,0.4206,128.2E-3,0.139,1.291E-2],[6,0.5054,154.1E-3,0.2006,1.864E-2],[8,0.6651,202.7E-3,0.3472,3.226E-2],[10,0.8350,254.5E-3,0.5479,5.090E-2],[12,0.9948,303.2E-3,0.7771,7.219E-2],[14,1.094,333.4E-3,0.9396,8.729E-2],[16,1.250,381E-3,1.227,0.1140],[18,1.406,428.7E-3,1.553,0.1443],[20,1.568,477.9E-3,1.931,0.1794],[24,1.886,574.7E-3,2.792,0.2594]]

temperatura = 0
sistema = 23

def Boton1():
    global sistema
    sistema = 1

def Boton2():
    global sistema
    sistema = 2
        
def Boton7():
    global sistema
    sistema = 1
    lbl10 = Label(seleccion, text="(L/min)", bg="white")
    lbl10.place(x=320, y=60, width=60, height=30)
        
def Boton8():
    global sistema
    sistema = 2
    lbl10 = Label(seleccion, text="(gal/min)", bg="white")
    lbl10.place(x=320, y=60, width=60, height=30)
        
def Boton3():
    raiz.pack_forget()
    menu.pack(fill="both", expand=True)
    x = (Ventana.winfo_screenwidth() // 2) - (650 // 2)
    y = (Ventana.winfo_screenheight() // 2) - (250 // 2)
    Ventana.geometry(f"{650}x{250}+{x}+{y}")
    
def Boton4():
    menu.pack_forget()
    raiz.pack(fill="both", expand=True)
    
def Boton5():
    menu.pack_forget()
    seleccion.pack(fill="both", expand=True)
    x = (Ventana.winfo_screenwidth() // 2) - (1100 // 2)
    y = (Ventana.winfo_screenheight() // 2) - (350 // 2)
    Ventana.geometry(f"{1100}x{350}+{x}+{y}")
    
def Boton6():
    seleccion.pack_forget()
    menu.pack(fill="both", expand=True)
    x = (Ventana.winfo_screenwidth() // 2) - (650 // 2)
    y = (Ventana.winfo_screenheight() // 2) - (250 // 2)
    Ventana.geometry(f"{650}x{250}+{x}+{y}")
    
def Boton13():
    menu.pack_forget()
    perdidas.pack(fill="both", expand=True)
    x = (Ventana.winfo_screenwidth() // 2) - (1500 // 2)
    y = (Ventana.winfo_screenheight() // 2) - (850 // 2)
    Ventana.geometry(f"{1500}x{850}+{x}+{y}")

def Boton14():
    perdidas.pack_forget()
    menu.pack(fill="both", expand=True)
    x = (Ventana.winfo_screenwidth() // 2) - (650 // 2)
    y = (Ventana.winfo_screenheight() // 2) - (250 // 2)
    Ventana.geometry(f"{650}x{250}+{x}+{y}")
    
def BotonDN(boton,D,FTS):
    global boton_activo, Diam, Ft
    Diam = D
    Ft = FTS
    if boton_activo is not None:
        boton_activo.config(bg="lightyellow")
    boton.config(bg="yellow")
    boton_activo = boton
    
def BotonMaterial(btn,SisI,SisB):
    global boton_act, SistemaInter, SistemaBrit
    SistemaInter = SisI
    SistemaBrit = SisB
    if boton_act is not None:
        boton_act.config(bg="lightyellow")
    btn.config(bg="yellow")
    boton_act = btn
    
def perdidaSistema(btn,sis):
    global Boton_Press
    global Perdida_Sis
    global lbl37, lbl38, lbl39, lbl40, lbl42, lbl43, lbl44
    Perdida_Sis = sis
    #para la Variable "Perdida_Sis" 1 es Internacional y 2 es Británico.
    if Boton_Press is not None:
        Boton_Press.config(bg="lightyellow")
    btn.config(bg="yellow")
    Boton_Press = btn
    global lbl40
    if Perdida_Sis == 1:
        lbl37.place(x=225, y=60, width=40, height=20)
        lbl38.place(x=225, y=85, width=25, height=20)
        lbl39.place(x=225, y=110, width=20, height=20)
        lbl42.place_forget()
        lbl43.place_forget()
        lbl44.place_forget()
        
    elif Perdida_Sis == 2:
        lbl42.place(x=225, y=60, width=40, height=20)
        lbl43.place(x=225, y=85, width=25, height=20)
        lbl44.place(x=225, y=110, width=20, height=20)
        lbl37.place_forget()
        lbl38.place_forget()
        lbl39.place_forget()
            
    
def otrofluido(valor):
    #1 es agua, 2 es "otro".
    global txt6, txt7, lbl15, lbl16, btn15, btn16, valorfluido, lbl40, lbl41
    valorfluido = valor
    if valor == 2:
        btn16.config(bg = "cyan")
        btn15.config(bg = "lightseagreen")
        lbl15.place(x=27, y=160, width=110, height=20)
        txt6.place(x=155, y=160, width=100, height=20)
        lbl16.place(x=27, y=185, width=130, height=20)
        txt7.place(x=155, y=185, width=100, height=20)
        if Perdida_Sis == 1:
            lbl40.place(x=255, y=185, width=45, height=20)
            lbl41.place_forget()
        elif Perdida_Sis == 2:
            lbl41.place(x=255, y=185, width=45, height=20)
            lbl40.place_forget()
    elif valor == 1:
        btn15.config(bg = "cyan")
        btn16.config(bg = "lightseagreen")
        lbl15.place_forget()
        txt6.place_forget()
        lbl16.place_forget()
        txt7.place_forget()
        lbl40.place_forget()
        lbl41.place_forget()
    
    
#print(tabulate(SistemaSI, headers=["Temperatura \n °C","Peso específico \n KN/m3", "Densidad \n kg/m3","Viscosidad dinámica \n Pa*s", "Viscosidad cinemática \n m2/s"], tablefmt="orgtbl", ))

#print(tabulate(SistemaSB, headers=["Temperatura \n °F","Peso específico \n lb/ft3", "Densidad \n slugs/ft3","Viscosidad dinámica \n (lb*s)/ft2", "Viscosidad cinemática \n ft2/s"], tablefmt="orgtbl", ))
def FunEnter():
    temperatura = float(txt1.get())
    
    if sistema == 1:
        count = 0
        while count == 0:
            if temperatura < 0 or temperatura > 100:
                messagebox.showinfo("Temperatura inválida!","Rango de temperatura debe ser: 0°C - 100°C")
                count = 1
            else:
                count = 1
            

        for i in range(len(SistemaSI)):
            if temperatura == SistemaSI[i][0]:
                
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(raiz, columns = ("Col1","Col2","Col3","Col4"))
                tv.column("#0", width=80)
                tv.column("Col1", width=90, anchor=CENTER)
                tv.column("Col2", width=100, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.heading("#0", text = "Temperatura \n       °C", anchor=CENTER)
                tv.heading("Col1", text = "Peso específico \n      KN/m3", anchor=CENTER)
                tv.heading("Col2", text = "Densidad \n    kg/m3", anchor=CENTER)
                tv.heading("Col3", text = "Viscosidad dinámica \n             Pa*s", anchor=CENTER)
                tv.heading("Col4", text = "Viscosidad cinemática \n              m2/s", anchor=CENTER)
                tv.insert("", END, text = SistemaSI[i][0], values = (SistemaSI[i][1],SistemaSI[i][2],SistemaSI[i][3],SistemaSI[i][4]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=70, y=100)
                tv.configure(height=1)
                raiz.grid_rowconfigure(0, weight=1)
                raiz.grid_columnconfigure(0, weight=1)

        timer = 0
        aumento_temp = 5
        while timer < 20:
            timermax = timer + 1
            if temperatura > (-5 + aumento_temp) and temperatura < (0 + aumento_temp):
                Tmin_max = [SistemaSI[timer][0],SistemaSI[timermax][0]]
                resultado = [temperatura]

                for s in range(4):
                    Stotal = s+1
                    min_max = [SistemaSI[timer][Stotal],SistemaSI[timermax][Stotal]]
                    interp_func = interp1d(Tmin_max,min_max, kind="linear")
                    interpolacion = interp_func(temperatura)
                    resultado.append(interpolacion)
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(raiz, columns = ("Col1","Col2","Col3","Col4"))
                tv.column("#0", width=80)
                tv.column("Col1", width=90, anchor=CENTER)
                tv.column("Col2", width=100, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.heading("#0", text = "Temperatura \n       °C", anchor=CENTER)
                tv.heading("Col1", text = "Peso específico \n      KN/m3", anchor=CENTER)
                tv.heading("Col2", text = "Densidad \n    kg/m3", anchor=CENTER)
                tv.heading("Col3", text = "Viscosidad dinámica \n             Pa*s", anchor=CENTER)
                tv.heading("Col4", text = "Viscosidad cinemática \n              m2/s", anchor=CENTER)
                tv.insert("", END, text = resultado[0], values = (resultado[1],resultado[2],resultado[3],resultado[4]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=70, y=100)
                tv.configure(height=1)
                raiz.grid_rowconfigure(0, weight=1)
                raiz.grid_columnconfigure(0, weight=1)
            timer = timer + 1
            aumento_temp = aumento_temp + 5
                
                
                        
    elif sistema == 2:
        count = 0
        while count == 0:
            if temperatura < 32 or temperatura > 212:
                messagebox.showinfo("Temperatura inválida!","Rango de temperatura debe ser: 32°F - 212°F")
                count = 1
            else:
                count = 1
            
        for i in range(len(SistemaSB)):
            if temperatura == SistemaSB[i][0]:

                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(raiz, columns = ("Col1","Col2","Col3","Col4"))
                tv.column("#0", width=80)
                tv.column("Col1", width=90, anchor=CENTER)
                tv.column("Col2", width=100, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.heading("#0", text = "Temperatura \n       °F", anchor=CENTER)
                tv.heading("Col1", text = "Peso específico \n      lb/ft3", anchor=CENTER)
                tv.heading("Col2", text = "Densidad \n    slugs/ft3", anchor=CENTER)
                tv.heading("Col3", text = "Viscosidad dinámica \n             (lb*s)/ft2", anchor=CENTER)
                tv.heading("Col4", text = "Viscosidad cinemática \n              ft2/s", anchor=CENTER)
                tv.insert("", END, text = SistemaSB[i][0], values = (SistemaSB[i][1],SistemaSB[i][2],SistemaSB[i][3],SistemaSB[i][4]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=70, y=100)
                tv.configure(height=1)
                raiz.grid_rowconfigure(0, weight=1)
                raiz.grid_columnconfigure(0, weight=1)
                
        #Caso en el que la temperatura tiene valores intermedios entre 32 y 40 °F
        if temperatura > 32 and temperatura < 40:
            Tmin_max = [SistemaSB[0][0],SistemaSB[1][0]]
            resultado = [temperatura]

            for s in range(4):
                Stotal = s+1
                min_max = [SistemaSB[0][Stotal],SistemaSB[1][Stotal]]
                interp_func = interp1d(Tmin_max,min_max, kind="linear")
                interpolacion = interp_func(temperatura)
                resultado.append(interpolacion)

            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(raiz, columns = ("Col1","Col2","Col3","Col4"))
            tv.column("#0", width=80)
            tv.column("Col1", width=90, anchor=CENTER)
            tv.column("Col2", width=100, anchor=CENTER)
            tv.column("Col3", width=130, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.heading("#0", text = "Temperatura \n       °F", anchor=CENTER)
            tv.heading("Col1", text = "Peso específico \n      lb/ft3", anchor=CENTER)
            tv.heading("Col2", text = "Densidad \n    slugs/ft3", anchor=CENTER)
            tv.heading("Col3", text = "Viscosidad dinámica \n             (lb*s)/ft2", anchor=CENTER)
            tv.heading("Col4", text = "Viscosidad cinemática \n              ft2/s", anchor=CENTER)
            tv.insert("", END, text = resultado[0], values = (resultado[1],resultado[2],resultado[3],resultado[4]))
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=70, y=100)
            tv.configure(height=1)
            raiz.grid_rowconfigure(0, weight=1)
            raiz.grid_columnconfigure(0, weight=1)
    
    
    
    
        #Caso en el que la temperatura tiene valores intermedios entre 200 y 212 °F      
        if temperatura > 200 and temperatura < 212:
            Tmin_max = [SistemaSB[17][0],SistemaSB[18][0]]
            resultado = [temperatura]

            for s in range(4):
                Stotal = s+1
                min_max = [SistemaSB[17][Stotal],SistemaSB[18][Stotal]]
                interp_func = interp1d(Tmin_max,min_max, kind="linear")
                interpolacion = interp_func(temperatura)
                resultado.append(interpolacion)
                
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(raiz, columns = ("Col1","Col2","Col3","Col4"))
            tv.column("#0", width=80)
            tv.column("Col1", width=90, anchor=CENTER)
            tv.column("Col2", width=100, anchor=CENTER)
            tv.column("Col3", width=130, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.heading("#0", text = "Temperatura \n       °F", anchor=CENTER)
            tv.heading("Col1", text = "Peso específico \n      lb/ft3", anchor=CENTER)
            tv.heading("Col2", text = "Densidad \n    slugs/ft3", anchor=CENTER)
            tv.heading("Col3", text = "Viscosidad dinámica \n             (lb*s)/ft2", anchor=CENTER)
            tv.heading("Col4", text = "Viscosidad cinemática \n              ft2/s", anchor=CENTER)
            tv.insert("", END, text = resultado[0], values = (resultado[1],resultado[2],resultado[3],resultado[4]))
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=70, y=100)
            tv.configure(height=1)
            raiz.grid_rowconfigure(0, weight=1)
            raiz.grid_columnconfigure(0, weight=1)

        
        #Todos los demás casos de opciones de temperatura. (En intervalos de 10)
        timer = 1
        aumento_temp = 10
        while timer < 17:
            timermax = timer + 1
        
            if temperatura > (30 + aumento_temp) and temperatura < (40 + aumento_temp):
                Tmin_max = [SistemaSB[timer][0],SistemaSB[timermax][0]]
                resultado = [temperatura]

                for s in range(4):
                    Stotal = s+1
                    min_max = [SistemaSB[timer][Stotal],SistemaSB[timermax][Stotal]]
                    interp_func = interp1d(Tmin_max,min_max, kind="linear")
                    interpolacion = interp_func(temperatura)
                    resultado.append(interpolacion)
                    
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(raiz, columns = ("Col1","Col2","Col3","Col4"))
                tv.column("#0", width=80)
                tv.column("Col1", width=90, anchor=CENTER)
                tv.column("Col2", width=100, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.heading("#0", text = "Temperatura \n       °F", anchor=CENTER)
                tv.heading("Col1", text = "Peso específico \n      lb/ft3", anchor=CENTER)
                tv.heading("Col2", text = "Densidad \n    slugs/ft3", anchor=CENTER)
                tv.heading("Col3", text = "Viscosidad dinámica \n             (lb*s)/ft2", anchor=CENTER)
                tv.heading("Col4", text = "Viscosidad cinemática \n              ft2/s", anchor=CENTER)
                tv.insert("", END, text = resultado[0], values = (resultado[1],resultado[2],resultado[3],resultado[4]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=70, y=100)
                tv.configure(height=1)
                raiz.grid_rowconfigure(0, weight=1)
                raiz.grid_columnconfigure(0, weight=1)
            timer = timer + 1
            aumento_temp = aumento_temp + 10
            
def selectuberia():
    caudal = float(txt2.get())
    lbl17 = Label(seleccion, text="Tubería de succión", font=("Arial", 10, "bold"))
    lbl17.place(x=5, y=90, width=150, height=30)
    lbl17 = Label(seleccion, text="Tubería de descarga", font=("Arial", 10, "bold"))
    lbl17.place(x=7, y=205, width=150, height=30)
    
    #Caso de Sistema internacional.
    if sistema == 1:

        count = 0
        while count == 0:
            if caudal < 45 or caudal > 13250:
                messagebox.showinfo("Caudal fuera del rango.","Por favor seleccione un caudal \n dentro del rango: 45 L/min - 13 250 L/min")
                count = 1
            else:
                count = 1
            
#Tubería de succion - valor exácto - Sistema Internacional 
        for i in range(len(succion)):
            if caudal == succion[i][1]:
                
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
                tv.column("#0", width=130)
                tv.column("Col1", width=130, anchor=CENTER)
                tv.column("Col2", width=130, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=130, anchor=CENTER)                
                tv.column("Col7", width=130, anchor=CENTER)                
                
                tv.heading("#0", text = "Caudal", anchor=CENTER)
                tv.heading("Col1", text = "Velocidad", anchor=CENTER)
                tv.heading("Col2", text = "Calibre", anchor=CENTER)
                tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
                tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
                tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
                tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
                tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=120)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)
                
                #Formato de Sub-Tabla de contenidos.
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
                tv.column("#0", width=65, anchor=CENTER)
                tv.column("Col1", width=65, anchor=CENTER)
                tv.column("Col2", width=65, anchor=CENTER)
                tv.column("Col3", width=65, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=65, anchor=CENTER)                
                tv.column("Col7", width=65, anchor=CENTER)                
                tv.column("Col8", width=65, anchor=CENTER)
                tv.column("Col9", width=65, anchor=CENTER)
                tv.column("Col10", width=65, anchor=CENTER)
                tv.column("Col11", width=65, anchor=CENTER)
                tv.column("Col12", width=65, anchor=CENTER)
                tv.column("Col13", width=65, anchor=CENTER)                

                
                tv.heading("#0", text = "gal/min", anchor=CENTER)
                tv.heading("Col1", text = "L/min", anchor=CENTER)
                tv.heading("Col2", text = "ft/s", anchor=CENTER)
                tv.heading("Col3", text = "m/s", anchor=CENTER)
                tv.heading("Col4", text = "(céd)", anchor=CENTER)
                tv.heading("Col5", text = "in", anchor=CENTER)
                tv.heading("Col6", text = "in", anchor=CENTER)
                tv.heading("Col7", text = "mm", anchor=CENTER)
                tv.heading("Col8", text = "in", anchor=CENTER)
                tv.heading("Col9", text = "mm", anchor=CENTER)
                tv.heading("Col10", text = "in", anchor=CENTER)
                tv.heading("Col11", text = "mm", anchor=CENTER)
                tv.heading("Col12", text = "ft^2", anchor=CENTER)
                tv.heading("Col13", text = "m^2", anchor=CENTER)
                
                tv.insert("", END, text = succion[i][0], values = (succion[i][1],succion[i][2],succion[i][3],succion[i][4],succion[i][5],succion[i][6],succion[i][7],succion[i][8],succion[i][9],succion[i][10],succion[i][11],succion[i][12],succion[i][13]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=148)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)

#Tubería de descarga - valor exácto - Sistema Internacional    
        for i in range(len(descarga)):
            if caudal == descarga[i][1]:
                
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
                tv.column("#0", width=130)
                tv.column("Col1", width=130, anchor=CENTER)
                tv.column("Col2", width=130, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=130, anchor=CENTER)                
                tv.column("Col7", width=130, anchor=CENTER)                
                
                tv.heading("#0", text = "Caudal", anchor=CENTER)
                tv.heading("Col1", text = "Velocidad", anchor=CENTER)
                tv.heading("Col2", text = "Calibre", anchor=CENTER)
                tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
                tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
                tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
                tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
                tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=235)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)
                
                #Formato de Sub-Tabla de contenidos.
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
                tv.column("#0", width=65, anchor=CENTER)
                tv.column("Col1", width=65, anchor=CENTER)
                tv.column("Col2", width=65, anchor=CENTER)
                tv.column("Col3", width=65, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=65, anchor=CENTER)                
                tv.column("Col7", width=65, anchor=CENTER)                
                tv.column("Col8", width=65, anchor=CENTER)
                tv.column("Col9", width=65, anchor=CENTER)
                tv.column("Col10", width=65, anchor=CENTER)
                tv.column("Col11", width=65, anchor=CENTER)
                tv.column("Col12", width=65, anchor=CENTER)
                tv.column("Col13", width=65, anchor=CENTER)                

                
                tv.heading("#0", text = "gal/min", anchor=CENTER)
                tv.heading("Col1", text = "L/min", anchor=CENTER)
                tv.heading("Col2", text = "ft/s", anchor=CENTER)
                tv.heading("Col3", text = "m/s", anchor=CENTER)
                tv.heading("Col4", text = "(céd)", anchor=CENTER)
                tv.heading("Col5", text = "in", anchor=CENTER)
                tv.heading("Col6", text = "in", anchor=CENTER)
                tv.heading("Col7", text = "mm", anchor=CENTER)
                tv.heading("Col8", text = "in", anchor=CENTER)
                tv.heading("Col9", text = "mm", anchor=CENTER)
                tv.heading("Col10", text = "in", anchor=CENTER)
                tv.heading("Col11", text = "mm", anchor=CENTER)
                tv.heading("Col12", text = "ft^2", anchor=CENTER)
                tv.heading("Col13", text = "m^2", anchor=CENTER)
                
                tv.insert("", END, text = descarga[i][0], values = (descarga[i][1],descarga[i][2],descarga[i][3],descarga[i][4],descarga[i][5],descarga[i][6],descarga[i][7],descarga[i][8],descarga[i][9],descarga[i][10],descarga[i][11],descarga[i][12],descarga[i][13]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=263)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)


#tubería de succión y descarga en caso de interpolación - Sistema internacional
        if caudal > 45 and caudal < 95:
            Qmin_max = [succion[0][1],succion[1][1]]
            Qmin_max_desc = [descarga[0][1],descarga[1][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[1]
            ref_max_desc = descarga[1]
            
            for s in range(5):
                min_max = [succion[0][s],succion[1][s]]
                min_max_desc = [descarga[0][s],descarga[1][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
                
        elif caudal > 95 and caudal < 130:
            Qmin_max = [succion[1][1],succion[2][1]]
            Qmin_max_desc = [descarga[1][1],descarga[2][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[2]
            ref_max_desc = descarga[2]
            
            for s in range(5):
                min_max = [succion[1][s],succion[2][s]]
                min_max_desc = [descarga[1][s],descarga[2][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 130 and caudal < 190:
            Qmin_max = [succion[2][1],succion[3][1]]
            Qmin_max_desc = [descarga[2][1],descarga[3][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[3]
            ref_max_desc = descarga[3]
            
            for s in range(5):
                min_max = [succion[2][s],succion[3][s]]
                min_max_desc = [descarga[2][s],descarga[3][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
        
        elif caudal > 190 and caudal < 285:
            Qmin_max = [succion[3][1],succion[4][1]]
            Qmin_max_desc = [descarga[3][1],descarga[4][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[4]
            ref_max_desc = descarga[4]
            
            for s in range(5):
                min_max = [succion[3][s],succion[4][s]]
                min_max_desc = [descarga[3][s],descarga[4][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 285 and caudal < 475:
            Qmin_max = [succion[4][1],succion[5][1]]
            Qmin_max_desc = [descarga[4][1],descarga[5][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[5]
            ref_max_desc = descarga[5]
            
            for s in range(5):
                min_max = [succion[4][s],succion[5][s]]
                min_max_desc = [descarga[4][s],descarga[5][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 475 and caudal < 660:
            Qmin_max = [succion[5][1],succion[6][1]]
            Qmin_max_desc = [descarga[5][1],descarga[6][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[6]
            ref_max_desc = descarga[6]
            
            for s in range(5):
                min_max = [succion[5][s],succion[6][s]]
                min_max_desc = [descarga[5][s],descarga[6][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 660 and caudal < 950:
            Qmin_max = [succion[6][1],succion[7][1]]
            Qmin_max_desc = [descarga[6][1],descarga[7][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[7]
            ref_max_desc = descarga[7]
            
            for s in range(5):
                min_max = [succion[6][s],succion[7][s]]
                min_max_desc = [descarga[6][s],descarga[7][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 950 and caudal < 1890:
            Qmin_max = [succion[7][1],succion[8][1]]
            Qmin_max_desc = [descarga[7][1],descarga[8][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[8]
            ref_max_desc = descarga[8]
            
            for s in range(5):
                min_max = [succion[7][s],succion[8][s]]
                min_max_desc = [descarga[7][s],descarga[8][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 1890 and caudal < 3800:
            Qmin_max = [succion[8][1],succion[9][1]]
            Qmin_max_desc = [descarga[8][1],descarga[9][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[9]
            ref_max_desc = descarga[9]
            
            for s in range(5):
                min_max = [succion[8][s],succion[9][s]]
                min_max_desc = [descarga[8][s],descarga[9][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 3800 and caudal < 4730:
            Qmin_max = [succion[9][1],succion[10][1]]
            Qmin_max_desc = [descarga[9][1],descarga[10][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[10]
            ref_max_desc = descarga[10]
            
            for s in range(5):
                min_max = [succion[9][s],succion[10][s]]
                min_max_desc = [descarga[9][s],descarga[10][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 4730 and caudal < 6625:
            Qmin_max = [succion[10][1],succion[11][1]]
            Qmin_max_desc = [descarga[10][1],descarga[11][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[11]
            ref_max_desc = descarga[11]
            
            for s in range(5):
                min_max = [succion[10][s],succion[11][s]]
                min_max_desc = [descarga[10][s],descarga[11][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 6625 and caudal < 9450:
            Qmin_max = [succion[11][1],succion[12][1]]
            Qmin_max_desc = [descarga[11][1],descarga[12][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[12]
            ref_max_desc = descarga[12]
            
            for s in range(5):
                min_max = [succion[11][s],succion[12][s]]
                min_max_desc = [descarga[11][s],descarga[12][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 9450 and caudal < 13250:
            Qmin_max = [succion[12][1],succion[13][1]]
            Qmin_max_desc = [descarga[12][1],descarga[13][1]]
            resultado = []
            resultado_desc = []
            ref_max = succion[13]
            ref_max_desc = descarga[13]
            
            for s in range(5):
                min_max = [succion[12][s],succion[13][s]]
                min_max_desc = [descarga[12][s],descarga[13][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        
        if caudal != 45 and caudal != 95 and caudal != 130 and caudal != 190 and caudal != 285 and caudal != 475 and caudal != 660 and caudal != 950 and caudal != 1890 and caudal != 3800 and caudal != 4730 and caudal != 6625 and caudal != 9450 and caudal != 13250:
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
            tv.column("#0", width=130)
            tv.column("Col1", width=130, anchor=CENTER)
            tv.column("Col2", width=130, anchor=CENTER)
            tv.column("Col3", width=130, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=130, anchor=CENTER)                
            tv.column("Col7", width=130, anchor=CENTER)                
                
            tv.heading("#0", text = "Caudal", anchor=CENTER)
            tv.heading("Col1", text = "Velocidad", anchor=CENTER)
            tv.heading("Col2", text = "Calibre", anchor=CENTER)
            tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
            tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
            tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
            tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
            tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=120)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
                
            #Formato de Sub-Tabla de contenidos.
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
            tv.column("#0", width=65, anchor=CENTER)
            tv.column("Col1", width=65, anchor=CENTER)
            tv.column("Col2", width=65, anchor=CENTER)
            tv.column("Col3", width=65, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=65, anchor=CENTER)                
            tv.column("Col7", width=65, anchor=CENTER)                
            tv.column("Col8", width=65, anchor=CENTER)
            tv.column("Col9", width=65, anchor=CENTER)
            tv.column("Col10", width=65, anchor=CENTER)
            tv.column("Col11", width=65, anchor=CENTER)
            tv.column("Col12", width=65, anchor=CENTER)
            tv.column("Col13", width=65, anchor=CENTER)                

                
            tv.heading("#0", text = "gal/min", anchor=CENTER)
            tv.heading("Col1", text = "L/min", anchor=CENTER)
            tv.heading("Col2", text = "ft/s", anchor=CENTER)
            tv.heading("Col3", text = "m/s", anchor=CENTER)
            tv.heading("Col4", text = "(céd)", anchor=CENTER)
            tv.heading("Col5", text = "in", anchor=CENTER)
            tv.heading("Col6", text = "in", anchor=CENTER)
            tv.heading("Col7", text = "mm", anchor=CENTER)
            tv.heading("Col8", text = "in", anchor=CENTER)
            tv.heading("Col9", text = "mm", anchor=CENTER)
            tv.heading("Col10", text = "in", anchor=CENTER)
            tv.heading("Col11", text = "mm", anchor=CENTER)
            tv.heading("Col12", text = "ft^2", anchor=CENTER)
            tv.heading("Col13", text = "m^2", anchor=CENTER)
                
            tv.insert("", END, text = resultado[0], values = (resultado[1],resultado[2],resultado[3],resultado[4],ref_max[5],ref_max[6],ref_max[7],ref_max[8],ref_max[9],ref_max[10],ref_max[11],ref_max[12],ref_max[13]))
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=148)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
            
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
            tv.column("#0", width=130)
            tv.column("Col1", width=130, anchor=CENTER)
            tv.column("Col2", width=130, anchor=CENTER)
            tv.column("Col3", width=130, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=130, anchor=CENTER)                
            tv.column("Col7", width=130, anchor=CENTER)                
                
            tv.heading("#0", text = "Caudal", anchor=CENTER)
            tv.heading("Col1", text = "Velocidad", anchor=CENTER)
            tv.heading("Col2", text = "Calibre", anchor=CENTER)
            tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
            tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
            tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
            tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
            tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=235)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
                
            #Formato de Sub-Tabla de contenidos.
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
            tv.column("#0", width=65, anchor=CENTER)
            tv.column("Col1", width=65, anchor=CENTER)
            tv.column("Col2", width=65, anchor=CENTER)
            tv.column("Col3", width=65, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=65, anchor=CENTER)                
            tv.column("Col7", width=65, anchor=CENTER)                
            tv.column("Col8", width=65, anchor=CENTER)
            tv.column("Col9", width=65, anchor=CENTER)
            tv.column("Col10", width=65, anchor=CENTER)
            tv.column("Col11", width=65, anchor=CENTER)
            tv.column("Col12", width=65, anchor=CENTER)
            tv.column("Col13", width=65, anchor=CENTER)                

                
            tv.heading("#0", text = "gal/min", anchor=CENTER)
            tv.heading("Col1", text = "L/min", anchor=CENTER)
            tv.heading("Col2", text = "ft/s", anchor=CENTER)
            tv.heading("Col3", text = "m/s", anchor=CENTER)
            tv.heading("Col4", text = "(céd)", anchor=CENTER)
            tv.heading("Col5", text = "in", anchor=CENTER)
            tv.heading("Col6", text = "in", anchor=CENTER)
            tv.heading("Col7", text = "mm", anchor=CENTER)
            tv.heading("Col8", text = "in", anchor=CENTER)
            tv.heading("Col9", text = "mm", anchor=CENTER)
            tv.heading("Col10", text = "in", anchor=CENTER)
            tv.heading("Col11", text = "mm", anchor=CENTER)
            tv.heading("Col12", text = "ft^2", anchor=CENTER)
            tv.heading("Col13", text = "m^2", anchor=CENTER)
                
            tv.insert("", END, text = resultado_desc[0], values = (resultado_desc[1],resultado_desc[2],resultado_desc[3],resultado_desc[4],ref_max_desc[5],ref_max_desc[6],ref_max_desc[7],ref_max_desc[8],ref_max_desc[9],ref_max_desc[10],ref_max_desc[11],ref_max_desc[12],ref_max_desc[13]))
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=263)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
            
    #Caso de sistema inglés             
    elif sistema == 2:
        count = 0
        while count == 0:
            if caudal < 12 or caudal > 3500:
                messagebox.showinfo("Caudal fuera del rango.","Por favor seleccione un caudal \n dentro del rango: 12 gal/min - 3 500 gal/min")
                count = 1
            else:
                count = 1
                
#Tubería de succion - valor exácto - Sistema Ingles 
        for i in range(len(succion)):
            if caudal == succion[i][0]:
                
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
                tv.column("#0", width=130)
                tv.column("Col1", width=130, anchor=CENTER)
                tv.column("Col2", width=130, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=130, anchor=CENTER)                
                tv.column("Col7", width=130, anchor=CENTER)                
                
                tv.heading("#0", text = "Caudal", anchor=CENTER)
                tv.heading("Col1", text = "Velocidad", anchor=CENTER)
                tv.heading("Col2", text = "Calibre", anchor=CENTER)
                tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
                tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
                tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
                tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
                tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=120)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)
                
                #Formato de Sub-Tabla de contenidos.
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
                tv.column("#0", width=65, anchor=CENTER)
                tv.column("Col1", width=65, anchor=CENTER)
                tv.column("Col2", width=65, anchor=CENTER)
                tv.column("Col3", width=65, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=65, anchor=CENTER)                
                tv.column("Col7", width=65, anchor=CENTER)                
                tv.column("Col8", width=65, anchor=CENTER)
                tv.column("Col9", width=65, anchor=CENTER)
                tv.column("Col10", width=65, anchor=CENTER)
                tv.column("Col11", width=65, anchor=CENTER)
                tv.column("Col12", width=65, anchor=CENTER)
                tv.column("Col13", width=65, anchor=CENTER)                

                
                tv.heading("#0", text = "gal/min", anchor=CENTER)
                tv.heading("Col1", text = "L/min", anchor=CENTER)
                tv.heading("Col2", text = "ft/s", anchor=CENTER)
                tv.heading("Col3", text = "m/s", anchor=CENTER)
                tv.heading("Col4", text = "(céd)", anchor=CENTER)
                tv.heading("Col5", text = "in", anchor=CENTER)
                tv.heading("Col6", text = "in", anchor=CENTER)
                tv.heading("Col7", text = "mm", anchor=CENTER)
                tv.heading("Col8", text = "in", anchor=CENTER)
                tv.heading("Col9", text = "mm", anchor=CENTER)
                tv.heading("Col10", text = "in", anchor=CENTER)
                tv.heading("Col11", text = "mm", anchor=CENTER)
                tv.heading("Col12", text = "ft^2", anchor=CENTER)
                tv.heading("Col13", text = "m^2", anchor=CENTER)
                
                tv.insert("", END, text = succion[i][0], values = (succion[i][1],succion[i][2],succion[i][3],succion[i][4],succion[i][5],succion[i][6],succion[i][7],succion[i][8],succion[i][9],succion[i][10],succion[i][11],succion[i][12],succion[i][13]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=148)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)

#Tubería de descarga - valor exácto - Sistema Ingles    
        for i in range(len(descarga)):
            if caudal == descarga[i][0]:
                
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
                tv.column("#0", width=130)
                tv.column("Col1", width=130, anchor=CENTER)
                tv.column("Col2", width=130, anchor=CENTER)
                tv.column("Col3", width=130, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=130, anchor=CENTER)                
                tv.column("Col7", width=130, anchor=CENTER)                
                
                tv.heading("#0", text = "Caudal", anchor=CENTER)
                tv.heading("Col1", text = "Velocidad", anchor=CENTER)
                tv.heading("Col2", text = "Calibre", anchor=CENTER)
                tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
                tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
                tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
                tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
                tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=235)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)
                
                #Formato de Sub-Tabla de contenidos.
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
                style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
                style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
                tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
                tv.column("#0", width=65, anchor=CENTER)
                tv.column("Col1", width=65, anchor=CENTER)
                tv.column("Col2", width=65, anchor=CENTER)
                tv.column("Col3", width=65, anchor=CENTER)
                tv.column("Col4", width=130, anchor=CENTER)
                tv.column("Col5", width=130, anchor=CENTER)                
                tv.column("Col6", width=65, anchor=CENTER)                
                tv.column("Col7", width=65, anchor=CENTER)                
                tv.column("Col8", width=65, anchor=CENTER)
                tv.column("Col9", width=65, anchor=CENTER)
                tv.column("Col10", width=65, anchor=CENTER)
                tv.column("Col11", width=65, anchor=CENTER)
                tv.column("Col12", width=65, anchor=CENTER)
                tv.column("Col13", width=65, anchor=CENTER)                

                
                tv.heading("#0", text = "gal/min", anchor=CENTER)
                tv.heading("Col1", text = "L/min", anchor=CENTER)
                tv.heading("Col2", text = "ft/s", anchor=CENTER)
                tv.heading("Col3", text = "m/s", anchor=CENTER)
                tv.heading("Col4", text = "(céd)", anchor=CENTER)
                tv.heading("Col5", text = "in", anchor=CENTER)
                tv.heading("Col6", text = "in", anchor=CENTER)
                tv.heading("Col7", text = "mm", anchor=CENTER)
                tv.heading("Col8", text = "in", anchor=CENTER)
                tv.heading("Col9", text = "mm", anchor=CENTER)
                tv.heading("Col10", text = "in", anchor=CENTER)
                tv.heading("Col11", text = "mm", anchor=CENTER)
                tv.heading("Col12", text = "ft^2", anchor=CENTER)
                tv.heading("Col13", text = "m^2", anchor=CENTER)
                
                tv.insert("", END, text = descarga[i][0], values = (descarga[i][1],descarga[i][2],descarga[i][3],descarga[i][4],descarga[i][5],descarga[i][6],descarga[i][7],descarga[i][8],descarga[i][9],descarga[i][10],descarga[i][11],descarga[i][12],descarga[i][13]))
                tv.pack(expand=True, fill=BOTH)
                tv.place(x=30, y=263)
                tv.configure(height=1)
                seleccion.grid_rowconfigure(0, weight=1)
                seleccion.grid_columnconfigure(0, weight=1)
                
                
                
                
                
        #Sistema Inglés - caso no exacto - succión y descarga
        if caudal > 12 and caudal < 25:
            Qmin_max = [succion[0][0],succion[1][0]]
            Qmin_max_desc = [descarga[0][0],descarga[1][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[1]
            ref_max_desc = descarga[1]
            
            for s in range(5):
                min_max = [succion[0][s],succion[1][s]]
                min_max_desc = [descarga[0][s],descarga[1][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 25 and caudal < 35:
            Qmin_max = [succion[1][0],succion[2][0]]
            Qmin_max_desc = [descarga[1][0],descarga[2][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[2]
            ref_max_desc = descarga[2]
            
            for s in range(5):
                min_max = [succion[1][s],succion[2][s]]
                min_max_desc = [descarga[1][s],descarga[2][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 35 and caudal < 50:
            Qmin_max = [succion[2][0],succion[3][0]]
            Qmin_max_desc = [descarga[2][0],descarga[3][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[3]
            ref_max_desc = descarga[3]
            
            for s in range(5):
                min_max = [succion[2][s],succion[3][s]]
                min_max_desc = [descarga[2][s],descarga[3][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
        
        elif caudal > 50 and caudal < 75:
            Qmin_max = [succion[3][0],succion[4][0]]
            Qmin_max_desc = [descarga[3][0],descarga[4][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[4]
            ref_max_desc = descarga[4]
            
            for s in range(5):
                min_max = [succion[3][s],succion[4][s]]
                min_max_desc = [descarga[3][s],descarga[4][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 75 and caudal < 125:
            Qmin_max = [succion[4][0],succion[5][0]]
            Qmin_max_desc = [descarga[4][0],descarga[5][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[5]
            ref_max_desc = descarga[5]
            
            for s in range(5):
                min_max = [succion[4][s],succion[5][s]]
                min_max_desc = [descarga[4][s],descarga[5][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 125 and caudal < 175:
            Qmin_max = [succion[5][0],succion[6][0]]
            Qmin_max_desc = [descarga[5][0],descarga[6][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[6]
            ref_max_desc = descarga[6]
            
            for s in range(5):
                min_max = [succion[5][s],succion[6][s]]
                min_max_desc = [descarga[5][s],descarga[6][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 175 and caudal < 250:
            Qmin_max = [succion[6][0],succion[7][0]]
            Qmin_max_desc = [descarga[6][0],descarga[7][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[7]
            ref_max_desc = descarga[7]
            
            for s in range(5):
                min_max = [succion[6][s],succion[7][s]]
                min_max_desc = [descarga[6][s],descarga[7][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 250 and caudal < 500:
            Qmin_max = [succion[7][0],succion[8][0]]
            Qmin_max_desc = [descarga[7][0],descarga[8][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[8]
            ref_max_desc = descarga[8]
            
            for s in range(5):
                min_max = [succion[7][s],succion[8][s]]
                min_max_desc = [descarga[7][s],descarga[8][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 500 and caudal < 1000:
            Qmin_max = [succion[8][0],succion[9][0]]
            Qmin_max_desc = [descarga[8][0],descarga[9][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[9]
            ref_max_desc = descarga[9]
            
            for s in range(5):
                min_max = [succion[8][s],succion[9][s]]
                min_max_desc = [descarga[8][s],descarga[9][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 1000 and caudal < 1250:
            Qmin_max = [succion[9][0],succion[10][0]]
            Qmin_max_desc = [descarga[9][0],descarga[10][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[10]
            ref_max_desc = descarga[10]
            
            for s in range(5):
                min_max = [succion[9][s],succion[10][s]]
                min_max_desc = [descarga[9][s],descarga[10][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 1250 and caudal < 1750:
            Qmin_max = [succion[10][0],succion[11][0]]
            Qmin_max_desc = [descarga[10][0],descarga[11][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[11]
            ref_max_desc = descarga[11]
            
            for s in range(5):
                min_max = [succion[10][s],succion[11][s]]
                min_max_desc = [descarga[10][s],descarga[11][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 1750 and caudal < 2500:
            Qmin_max = [succion[11][0],succion[12][0]]
            Qmin_max_desc = [descarga[11][0],descarga[12][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[12]
            ref_max_desc = descarga[12]
            
            for s in range(5):
                min_max = [succion[11][s],succion[12][s]]
                min_max_desc = [descarga[11][s],descarga[12][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
                
        elif caudal > 2500 and caudal < 3500:
            Qmin_max = [succion[12][0],succion[13][0]]
            Qmin_max_desc = [descarga[12][0],descarga[13][0]]
            resultado = []
            resultado_desc = []
            ref_max = succion[13]
            ref_max_desc = descarga[13]
            
            for s in range(5):
                min_max = [succion[12][s],succion[13][s]]
                min_max_desc = [descarga[12][s],descarga[13][s]]
                interp_func = interp1d(Qmin_max,min_max, kind="linear")
                interpolacion = interp_func(caudal)
                resultado.append(interpolacion)
                
                interp_func_desc = interp1d(Qmin_max_desc,min_max_desc, kind="linear")
                interpolacion_desc = interp_func_desc(caudal)
                resultado_desc.append(interpolacion_desc)
    
        if caudal != 12 and caudal != 25 and caudal != 35 and caudal != 50 and caudal != 75 and caudal != 125 and caudal != 175 and caudal != 250 and caudal != 500 and caudal != 1000 and caudal != 1250 and caudal != 1750 and caudal != 2500 and caudal != 3500:
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
            tv.column("#0", width=130)
            tv.column("Col1", width=130, anchor=CENTER)
            tv.column("Col2", width=130, anchor=CENTER)
            tv.column("Col3", width=130, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=130, anchor=CENTER)                
            tv.column("Col7", width=130, anchor=CENTER)                
                
            tv.heading("#0", text = "Caudal", anchor=CENTER)
            tv.heading("Col1", text = "Velocidad", anchor=CENTER)
            tv.heading("Col2", text = "Calibre", anchor=CENTER)
            tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
            tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
            tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
            tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
            tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=120)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
                
            #Formato de Sub-Tabla de contenidos.
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
            tv.column("#0", width=65, anchor=CENTER)
            tv.column("Col1", width=65, anchor=CENTER)
            tv.column("Col2", width=65, anchor=CENTER)
            tv.column("Col3", width=65, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=65, anchor=CENTER)                
            tv.column("Col7", width=65, anchor=CENTER)                
            tv.column("Col8", width=65, anchor=CENTER)
            tv.column("Col9", width=65, anchor=CENTER)
            tv.column("Col10", width=65, anchor=CENTER)
            tv.column("Col11", width=65, anchor=CENTER)
            tv.column("Col12", width=65, anchor=CENTER)
            tv.column("Col13", width=65, anchor=CENTER)                

                
            tv.heading("#0", text = "gal/min", anchor=CENTER)
            tv.heading("Col1", text = "L/min", anchor=CENTER)
            tv.heading("Col2", text = "ft/s", anchor=CENTER)
            tv.heading("Col3", text = "m/s", anchor=CENTER)
            tv.heading("Col4", text = "(céd)", anchor=CENTER)
            tv.heading("Col5", text = "in", anchor=CENTER)
            tv.heading("Col6", text = "in", anchor=CENTER)
            tv.heading("Col7", text = "mm", anchor=CENTER)
            tv.heading("Col8", text = "in", anchor=CENTER)
            tv.heading("Col9", text = "mm", anchor=CENTER)
            tv.heading("Col10", text = "in", anchor=CENTER)
            tv.heading("Col11", text = "mm", anchor=CENTER)
            tv.heading("Col12", text = "ft^2", anchor=CENTER)
            tv.heading("Col13", text = "m^2", anchor=CENTER)
                
            tv.insert("", END, text = resultado[0], values = (resultado[1],resultado[2],resultado[3],resultado[4],ref_max[5],ref_max[6],ref_max[7],ref_max[8],ref_max[9],ref_max[10],ref_max[11],ref_max[12],ref_max[13]))
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=148)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
            
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
            tv.column("#0", width=130)
            tv.column("Col1", width=130, anchor=CENTER)
            tv.column("Col2", width=130, anchor=CENTER)
            tv.column("Col3", width=130, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=130, anchor=CENTER)                
            tv.column("Col7", width=130, anchor=CENTER)                
                
            tv.heading("#0", text = "Caudal", anchor=CENTER)
            tv.heading("Col1", text = "Velocidad", anchor=CENTER)
            tv.heading("Col2", text = "Calibre", anchor=CENTER)
            tv.heading("Col3", text = "Tamaño Nominal", anchor=CENTER)
            tv.heading("Col4", text = "Diámetro ext", anchor=CENTER)
            tv.heading("Col5", text = "Espesor pared", anchor=CENTER)
            tv.heading("Col6", text = "Diámetro int", anchor=CENTER)
            tv.heading("Col7", text = "Area de flujo", anchor=CENTER)
                
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=235)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
                
            #Formato de Sub-Tabla de contenidos.
            style = ttk.Style()
            style.theme_use("clam")
            style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
            style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
            style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
            tv = ttk.Treeview(seleccion, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9","Col10","Col11","Col12","Col13"))
            tv.column("#0", width=65, anchor=CENTER)
            tv.column("Col1", width=65, anchor=CENTER)
            tv.column("Col2", width=65, anchor=CENTER)
            tv.column("Col3", width=65, anchor=CENTER)
            tv.column("Col4", width=130, anchor=CENTER)
            tv.column("Col5", width=130, anchor=CENTER)                
            tv.column("Col6", width=65, anchor=CENTER)                
            tv.column("Col7", width=65, anchor=CENTER)                
            tv.column("Col8", width=65, anchor=CENTER)
            tv.column("Col9", width=65, anchor=CENTER)
            tv.column("Col10", width=65, anchor=CENTER)
            tv.column("Col11", width=65, anchor=CENTER)
            tv.column("Col12", width=65, anchor=CENTER)
            tv.column("Col13", width=65, anchor=CENTER)                

                
            tv.heading("#0", text = "gal/min", anchor=CENTER)
            tv.heading("Col1", text = "L/min", anchor=CENTER)
            tv.heading("Col2", text = "ft/s", anchor=CENTER)
            tv.heading("Col3", text = "m/s", anchor=CENTER)
            tv.heading("Col4", text = "(céd)", anchor=CENTER)
            tv.heading("Col5", text = "in", anchor=CENTER)
            tv.heading("Col6", text = "in", anchor=CENTER)
            tv.heading("Col7", text = "mm", anchor=CENTER)
            tv.heading("Col8", text = "in", anchor=CENTER)
            tv.heading("Col9", text = "mm", anchor=CENTER)
            tv.heading("Col10", text = "in", anchor=CENTER)
            tv.heading("Col11", text = "mm", anchor=CENTER)
            tv.heading("Col12", text = "ft^2", anchor=CENTER)
            tv.heading("Col13", text = "m^2", anchor=CENTER)
                
            tv.insert("", END, text = resultado_desc[0], values = (resultado_desc[1],resultado_desc[2],resultado_desc[3],resultado_desc[4],ref_max_desc[5],ref_max_desc[6],ref_max_desc[7],ref_max_desc[8],ref_max_desc[9],ref_max_desc[10],ref_max_desc[11],ref_max_desc[12],ref_max_desc[13]))
            tv.pack(expand=True, fill=BOTH)
            tv.place(x=30, y=263)
            tv.configure(height=1)
            seleccion.grid_rowconfigure(0, weight=1)
            seleccion.grid_columnconfigure(0, weight=1)
    

def perdidasTub():
    global txt5, txt3, txt4, Perdida_Sis, Ft
        
    if Perdida_Sis == "":
        messagebox.showinfo("Sistema de medida!","Debe seleccionar un sistema de medida.")
        
    if Perdida_Sis == 1:
        if txt4.get().strip() == "" or float(txt4.get()) < 0 or float(txt4.get()) > 100:
            messagebox.showinfo("Temperatura inválida!","Rango de temperatura debe ser: 0°C - 100°C")

        if txt3.get().strip() == "":
            messagebox.showinfo("No ha seleccionado un Caudal","Por favor, ingrese el caudal de flujo en L/min")

        if txt5.get().strip() == "":
            messagebox.showinfo("No ha seleccionado Longitud","Por favor, ingrese la longitud total de la tubería en metros")

        if Diam == "":
            messagebox.showinfo("Selección de Tubería","Por favor, Seleccione un diámetro nominal de tuberia")
        
        if SistemaInter == "":
            messagebox.showinfo("Selección de material","Por favor, Seleccione un material de tubería")
        
    
        #Encontrar el diámetro interno.
        D_int = 1
        for i in range(len(tuberiaced40)):
            if Diam == tuberiaced40[i][0]:
                D_int = tuberiaced40[i][2]
        #Encontrar la longitud.
        L = float(txt5.get())
        #Encontrar V float(txt3.get())
        V = (float(txt3.get())/60000)/((3.141592/4)*(D_int**2))
        #encontrar viscocidad cinemática.
        visc = 0
        if valorfluido == 1:
            for s in range(len(SistemaSI)):
                if float(txt4.get()) == SistemaSI[s][0]:
                    visc = SistemaSI[s][4]
            timer = 0
            aumento_temper = 5
            while timer < 20:
                timermax = timer + 1
                if float(txt4.get()) > (-5 + aumento_temper) and float(txt4.get()) < (0 + aumento_temper):
                    Tminmax = [SistemaSI[timer][0],SistemaSI[timermax][0]]
                    Viscmin_Viscmax = [SistemaSI[timer][4],SistemaSI[timermax][4]]
                    interp_func = interp1d(Tminmax,Viscmin_Viscmax, kind="linear")
                    visc = interp_func(float(txt4.get()))
                timer = timer + 1
                aumento_temper = aumento_temper + 5
            
        elif valorfluido == 2:
            visc = float(txt7.get())
        #Cálculo de Reynols.
        Re = (D_int*V)/visc
        #Cálculo de D/e
        e = SistemaInter
        De = D_int/e
        # Encontrar el coeficiente de fricción F.
        if Re <= 4000:
            F=64/Re
        elif Re > 4000:
            F = 0.25/((math.log10(((1)/(3.7*De))+(5.74)/(Re**0.9))))**2
        #Calcular la pérdida por longitud.
        Lh = F*(L/D_int)*((V**2)/(2*9.81))
        #ACCESORIOS
        #Modificación de Ft = F para flujo laminar.
        if Re <= 4000:
            Ft = F
        #Acá vamos a calcular la longitud equivalente.
        if Diam <= 8 and Diam >= 2:
            LeVm = 45
        elif Diam <= 14 and Diam >= 10:
            LeVm = 35
        elif Diam <= 24 and Diam >= 16:
            LeVm = 25
        Le_D = 340*float(txt8.get())+150*float(txt9.get())+8*float(txt10.get())+100*float(txt11.get())+150*float(txt12.get())+LeVm*float(txt13.get())+420*float(txt14.get())+75*float(txt15.get())+30*float(txt16.get())+20*float(txt17.get())+50*float(txt18.get())+16*float(txt19.get())+26*float(txt20.get())+50*float(txt21.get())+20*float(txt22.get())+60*float(txt23.get())
        #Perdida por accesorios
        Lacc = Ft*Le_D*((V**2)/(2*9.81))
        Ltotal = Lh + Lacc

        #Gráfica para los resultados generales.
        lbl45 = Label(perdidas, text = "Resultados generales", font=("Ubuntu", 16, "bold"), bg="white")
        lbl45.place(x=300, y=175, width=300, height=25)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
        style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
        tv = ttk.Treeview(perdidas, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9"))
        tv.column("#0", width=80)
        tv.column("Col1", width=100, anchor=CENTER)
        tv.column("Col2", width=100, anchor=CENTER)
        tv.column("Col3", width=100, anchor=CENTER)
        tv.column("Col4", width=100, anchor=CENTER)
        tv.column("Col5", width=100, anchor=CENTER)
        tv.column("Col6", width=100, anchor=CENTER)
        tv.column("Col7", width=130, anchor=CENTER)
        tv.column("Col8", width=130, anchor=CENTER)
        tv.column("Col9", width=130, anchor=CENTER)         
        
        tv.heading("#0", text = "  Caudal \n    m3/s", anchor=CENTER)
        tv.heading("Col1", text = "Area Transversal \n          m2", anchor=CENTER)
        tv.heading("Col2", text = "Longitud Tubería \n             m", anchor=CENTER)
        tv.heading("Col3", text = "Diam int Tubería \n             m", anchor=CENTER)
        tv.heading("Col4", text = "Factor Fricción \n              F", anchor=CENTER)
        tv.heading("Col5", text = "Long. Equivalente \n          (Le/D)", anchor=CENTER)
        tv.heading("Col6", text = "Reynolds \n      Re", anchor=CENTER)
        tv.heading("Col7", text = "Pérdida por Longitud \n               m", anchor=CENTER)
        tv.heading("Col8", text = "Pérdida por Accesorios \n                m", anchor=CENTER)        
        tv.heading("Col9", text = "Pérdida Total \n            m", anchor=CENTER)         
        
        tv.insert("", END, text = (round(float(txt3.get())/60000,4)), values = (round((3.141592/4)*(D_int**2),4),L,D_int,round(F,4),Le_D,round(Re,4),round(Lh,4),round(Lacc,4),round(Ltotal,4)))
        tv.pack(expand=True, fill=BOTH)
        tv.place(x=300, y=210)
        tv.configure(height=1)
        perdidas.grid_rowconfigure(0, weight=1)
        perdidas.grid_columnconfigure(0, weight=1)

        #Tabla de pérdidas por accesorio
        lbl46 = Label(perdidas, text = "Perdidas por cada accesorio", font=("Ubuntu", 16, "bold"), bg="white")
        lbl46.place(x=300, y=300, width=300, height=20)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
        style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
        tv = ttk.Treeview(perdidas, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
        tv.column("#0", width=130)
        tv.column("Col1", width=140, anchor=CENTER)
        tv.column("Col2", width=140, anchor=CENTER)
        tv.column("Col3", width=140, anchor=CENTER)
        tv.column("Col4", width=140, anchor=CENTER)
        tv.column("Col5", width=140, anchor=CENTER)
        tv.column("Col6", width=140, anchor=CENTER)
        tv.column("Col7", width=140, anchor=CENTER)     
        
        tv.heading("#0", text = "Válv.globo", anchor=CENTER)
        tv.heading("Col1", text = "Válv.angulo", anchor=CENTER)
        tv.heading("Col2", text = "Válv.Compuerta abierta", anchor=CENTER)
        tv.heading("Col3", text = "Válv.Reten.Oscilante", anchor=CENTER)
        tv.heading("Col4", text = "Válv.Reten.Bola", anchor=CENTER)
        tv.heading("Col5", text = "Válv.Marip.Abierta", anchor=CENTER)
        tv.heading("Col6", text = "Válv. Pie Disc. Vást", anchor=CENTER)
        tv.heading("Col7", text = "Válv. Pie Disc. Bisag", anchor=CENTER)      
        
        tv.insert("", END, text = (round(340*float(txt8.get())*Ft*((V**2)/(2*9.81)),4)), values = (round(150*float(txt9.get())*Ft*((V**2)/(2*9.81)),4),     round(8*float(txt10.get())*Ft*((V**2)/(2*9.81)),4),      round(100*float(txt11.get())*Ft*((V**2)/(2*9.81)),4),      round(150*float(txt12.get())*Ft*((V**2)/(2*9.81)),4),     round(LeVm*float(txt13.get())*Ft*((V**2)/(2*9.81)),4),     round(420*float(txt14.get())*Ft*((V**2)/(2*9.81)),4),     round(75*float(txt15.get())*Ft*((V**2)/(2*9.81)),4),     round(30*float(txt16.get())*Ft*((V**2)/(2*9.81)),4)))
        #Le_D = 340*float(txt8.get())    +   150*float(txt9.get())   +   8*float(txt10.get())    +   100*float(txt11.get())  +   150*float(txt12.get())  +   LeVm*float(txt13.get())  +   420*float(txt14.get())  +   75*float(txt15.get())  +   30*float(txt16.get())   +   20*float(txt17.get())   +   50*float(txt18.get())   +   16*float(txt19.get())   +   26*float(txt20.get())   +  50*float(txt21.get())    +   20*float(txt22.get())   +   60*float(txt23.get())
        tv.pack(expand=True, fill=BOTH)
        tv.place(x=300, y=325)
        tv.configure(height=1)
        perdidas.grid_rowconfigure(0, weight=1)
        perdidas.grid_columnconfigure(0, weight=1)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
        style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
        tv = ttk.Treeview(perdidas, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
        tv.column("#0", width=130)
        tv.column("Col1", width=140, anchor=CENTER)
        tv.column("Col2", width=140, anchor=CENTER)
        tv.column("Col3", width=140, anchor=CENTER)
        tv.column("Col4", width=140, anchor=CENTER)
        tv.column("Col5", width=140, anchor=CENTER)
        tv.column("Col6", width=140, anchor=CENTER)
        tv.column("Col7", width=140, anchor=CENTER)     
        
        tv.heading("#0", text = "Codo estánd 90°", anchor=CENTER)
        tv.heading("Col1", text = "Codo 90° radio largo", anchor=CENTER)
        tv.heading("Col2", text = "Codo 90° para calle", anchor=CENTER)
        tv.heading("Col3", text = "Codo estándar 45°", anchor=CENTER)
        tv.heading("Col4", text = "Codo 45° para calle", anchor=CENTER)
        tv.heading("Col5", text = "Doblez Retorno Cerrado", anchor=CENTER)
        tv.heading("Col6", text = "T estándar Flujo Princ", anchor=CENTER)
        tv.heading("Col7", text = "T estándar Flujo Ramific", anchor=CENTER)      
        
        tv.insert("", END, text = (round(30*float(txt16.get())*Ft*((V**2)/(2*9.81)),4)), values = (round(20*float(txt17.get())*Ft*((V**2)/(2*9.81)),4),     round(50*float(txt18.get())*Ft*((V**2)/(2*9.81)),4),      round(16*float(txt19.get())*Ft*((V**2)/(2*9.81)),4),      round(26*float(txt20.get())*Ft*((V**2)/(2*9.81)),4),     round(50*float(txt21.get())*Ft*((V**2)/(2*9.81)),4),     round(20*float(txt22.get())*Ft*((V**2)/(2*9.81)),4),     round(60*float(txt23.get())*Ft*((V**2)/(2*9.81)),4)))
        tv.pack(expand=True, fill=BOTH)
        tv.place(x=300, y=375)
        tv.configure(height=1)
        perdidas.grid_rowconfigure(0, weight=1)
        perdidas.grid_columnconfigure(0, weight=1)
    
    elif Perdida_Sis == 2:
        if txt4.get().strip() == "" or float(txt4.get()) < 32 or float(txt4.get()) > 212:
            messagebox.showinfo("Temperatura inválida!","Rango de temperatura debe ser: 32°F - 212°F")

        if txt3.get().strip() == "":
            messagebox.showinfo("No ha seleccionado un Caudal","Por favor, ingrese el caudal de flujo en gal/min")

        if txt5.get().strip() == "":
            messagebox.showinfo("No ha seleccionado Longitud","Por favor, ingrese la longitud total de la tubería en pies")

        if Diam == "":
            messagebox.showinfo("Selección de Tubería","Por favor, Seleccione un diámetro nominal de tuberia")
        
        if SistemaInter == "":
            messagebox.showinfo("Selección de material","Por favor, Seleccione un material de tubería")    

        #Encontrar el diámetro interno.
        D_int = 1
        for i in range(len(tuberiaced40)):
            if Diam == tuberiaced40[i][0]:
                D_int = tuberiaced40[i][1]
        #Encontrar la longitud.
        L = float(txt5.get())
        #Encontrar V float(txt3.get())
        V = (float(txt3.get())/448.8312)/((3.141592/4)*(D_int**2))
        #encontrar viscocidad cinemática.
        visc = 0
        if valorfluido == 1:
            for s in range(len(SistemaSB)):
                if float(txt4.get()) == SistemaSB[s][0]:
                    visc = SistemaSB[s][4]
            timer = 1
            aumento_temper = 10
            while timer < 17:
                timermax = timer + 1
                if float(txt4.get()) > (30 + aumento_temper) and float(txt4.get()) < (40 + aumento_temper):
                    Tminmax = [SistemaSB[timer][0],SistemaSB[timermax][0]]
                    Viscmin_Viscmax = [SistemaSB[timer][4],SistemaSB[timermax][4]]
                    interp_func = interp1d(Tminmax,Viscmin_Viscmax, kind="linear")
                    visc = interp_func(float(txt4.get()))
                timer = timer + 1
                aumento_temper = aumento_temper + 10
                
            if float(txt4.get()) > 32 and float(txt4.get()) < 40:
                Tminmax = [SistemaSB[0][0],SistemaSB[1][0]]
                Viscmin_Viscmax = [SistemaSB[0][4],SistemaSB[1][4]]
                interp_func = interp1d(Tminmax,Viscmin_Viscmax, kind="linear")
                visc = interp_func(float(txt4.get()))
                
            elif float(txt4.get()) > 200 and float(txt4.get()) < 212:
                Tminmax = [SistemaSB[17][0],SistemaSB[18][0]]
                Viscmin_Viscmax = [SistemaSB[17][4],SistemaSB[18][4]]
                interp_func = interp1d(Tminmax,Viscmin_Viscmax, kind="linear")
                visc = interp_func(float(txt4.get()))
                
        elif valorfluido == 2:
            visc = float(txt7.get())
        #Cálculo de Reynols.
        Re = (D_int*V)/visc
        #Cálculo de D/e
        e = SistemaBrit
        De = D_int/e
        # Encontrar el coeficiente de fricción F.
        if Re <= 4000:
            F=64/Re
        elif Re > 4000:
            F = 0.25/((math.log10(((1)/(3.7*De))+(5.74)/(Re**0.9))))**2
        #Calcular la pérdida por longitud.
        Lh = F*(L/D_int)*((V**2)/(2*32.2))
        #ACCESORIOS
        #Modificación de Ft = F para flujo laminar.
        if Re <= 4000:
            Ft = F
        #Acá vamos a calcular la longitud equivalente.
        if Diam <= 8 and Diam >= 2:
            LeVm = 45
        elif Diam <= 14 and Diam >= 10:
            LeVm = 35
        elif Diam <= 24 and Diam >= 16:
            LeVm = 25
        Le_D = 340*float(txt8.get())+150*float(txt9.get())+8*float(txt10.get())+100*float(txt11.get())+150*float(txt12.get())+LeVm*float(txt13.get())+420*float(txt14.get())+75*float(txt15.get())+30*float(txt16.get())+20*float(txt17.get())+50*float(txt18.get())+16*float(txt19.get())+26*float(txt20.get())+50*float(txt21.get())+20*float(txt22.get())+60*float(txt23.get())
        #Perdida por accesorios
        Lacc = Ft*Le_D*((V**2)/(2*32.2))
        Ltotal = Lh + Lacc

        #Gráfica para los resultados generales.
        lbl45 = Label(perdidas, text = "Resultados generales", font=("Ubuntu", 16, "bold"), bg="white")
        lbl45.place(x=300, y=175, width=300, height=20)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
        style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
        tv = ttk.Treeview(perdidas, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9"))
        tv.column("#0", width=80)
        tv.column("Col1", width=100, anchor=CENTER)
        tv.column("Col2", width=100, anchor=CENTER)
        tv.column("Col3", width=100, anchor=CENTER)
        tv.column("Col4", width=100, anchor=CENTER)
        tv.column("Col5", width=100, anchor=CENTER)
        tv.column("Col6", width=100, anchor=CENTER)
        tv.column("Col7", width=130, anchor=CENTER)
        tv.column("Col8", width=130, anchor=CENTER)
        tv.column("Col9", width=130, anchor=CENTER)         
        
        tv.heading("#0", text = "  Caudal \n    Ft3/s", anchor=CENTER)
        tv.heading("Col1", text = "Area Transversal \n           Ft2", anchor=CENTER)
        tv.heading("Col2", text = "Longitud Tubería \n             Ft", anchor=CENTER)
        tv.heading("Col3", text = "Diam int Tubería \n             Ft", anchor=CENTER)
        tv.heading("Col4", text = "Factor Fricción \n            F", anchor=CENTER)
        tv.heading("Col5", text = "Long. Equivalente \n         (Le/D)", anchor=CENTER)
        tv.heading("Col6", text = "Reynolds \n      Re", anchor=CENTER)
        tv.heading("Col7", text = "Pérdida por Longitud \n                 Ft", anchor=CENTER)
        tv.heading("Col8", text = "Pérdida por Accesorios \n               Ft", anchor=CENTER)        
        tv.heading("Col9", text = "Pérdida Total \n         Ft", anchor=CENTER)         
        
        tv.insert("", END, text = (round(float(txt3.get())/448.8312,4)), values = (round((3.141592/4)*(D_int**2),4),L,D_int,round(F,4),Le_D,round(Re,4),round(Lh,4),round(Lacc,4),round(Ltotal,4)))
        tv.pack(expand=True, fill=BOTH)
        tv.place(x=300, y=210)
        tv.configure(height=1)
        perdidas.grid_rowconfigure(0, weight=1)
        perdidas.grid_columnconfigure(0, weight=1)

        #Tabla de pérdidas por accesorio
        lbl46 = Label(perdidas, text = "Perdidas por cada accesorio", font=("Ubuntu", 16, "bold"), bg="white")
        lbl46.place(x=300, y=300, width=300, height=20)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
        style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
        tv = ttk.Treeview(perdidas, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
        tv.column("#0", width=130)
        tv.column("Col1", width=140, anchor=CENTER)
        tv.column("Col2", width=140, anchor=CENTER)
        tv.column("Col3", width=140, anchor=CENTER)
        tv.column("Col4", width=140, anchor=CENTER)
        tv.column("Col5", width=140, anchor=CENTER)
        tv.column("Col6", width=140, anchor=CENTER)
        tv.column("Col7", width=140, anchor=CENTER)     
        
        tv.heading("#0", text = "Válv.globo", anchor=CENTER)
        tv.heading("Col1", text = "Válv.angulo", anchor=CENTER)
        tv.heading("Col2", text = "Válv.Compuerta abierta", anchor=CENTER)
        tv.heading("Col3", text = "Válv.Reten.Oscilante", anchor=CENTER)
        tv.heading("Col4", text = "Válv.Reten.Bola", anchor=CENTER)
        tv.heading("Col5", text = "Válv.Marip.Abierta", anchor=CENTER)
        tv.heading("Col6", text = "Válv. Pie Disc. Vást", anchor=CENTER)
        tv.heading("Col7", text = "Válv. Pie Disc. Bisag", anchor=CENTER)      
        
        tv.insert("", END, text = (round(340*float(txt8.get())*Ft*((V**2)/(2*32.2)),4)), values = (round(150*float(txt9.get())*Ft*((V**2)/(2*32.2)),4),     round(8*float(txt10.get())*Ft*((V**2)/(2*32.2)),4),      round(100*float(txt11.get())*Ft*((V**2)/(2*32.2)),4),      round(150*float(txt12.get())*Ft*((V**2)/(2*32.2)),4),     round(LeVm*float(txt13.get())*Ft*((V**2)/(2*32.2)),4),     round(420*float(txt14.get())*Ft*((V**2)/(2*32.2)),4),     round(75*float(txt15.get())*Ft*((V**2)/(2*32.2)),4),     round(30*float(txt16.get())*Ft*((V**2)/(2*32.2)),4)))
        #Le_D = 340*float(txt8.get())    +   150*float(txt9.get())   +   8*float(txt10.get())    +   100*float(txt11.get())  +   150*float(txt12.get())  +   LeVm*float(txt13.get())  +   420*float(txt14.get())  +   75*float(txt15.get())  +   30*float(txt16.get())   +   20*float(txt17.get())   +   50*float(txt18.get())   +   16*float(txt19.get())   +   26*float(txt20.get())   +  50*float(txt21.get())    +   20*float(txt22.get())   +   60*float(txt23.get())
        tv.pack(expand=True, fill=BOTH)
        tv.place(x=300, y=325)
        tv.configure(height=1)
        perdidas.grid_rowconfigure(0, weight=1)
        perdidas.grid_columnconfigure(0, weight=1)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", rowheight=30, background="#d9d9d9", relief="raised") 
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", bordercolor="black", borderwidth=1)
        style.map("Treeview", background=[("selected", "#ececec")], bordercolor=[("focus", "#000000")])
        tv = ttk.Treeview(perdidas, columns = ("Col1","Col2","Col3","Col4","Col5","Col6","Col7"))
        tv.column("#0", width=130)
        tv.column("Col1", width=140, anchor=CENTER)
        tv.column("Col2", width=140, anchor=CENTER)
        tv.column("Col3", width=140, anchor=CENTER)
        tv.column("Col4", width=140, anchor=CENTER)
        tv.column("Col5", width=140, anchor=CENTER)
        tv.column("Col6", width=140, anchor=CENTER)
        tv.column("Col7", width=140, anchor=CENTER)     
        
        tv.heading("#0", text = "Codo estánd 90°", anchor=CENTER)
        tv.heading("Col1", text = "Codo 90° radio largo", anchor=CENTER)
        tv.heading("Col2", text = "Codo 90° para calle", anchor=CENTER)
        tv.heading("Col3", text = "Codo estándar 45°", anchor=CENTER)
        tv.heading("Col4", text = "Codo 45° para calle", anchor=CENTER)
        tv.heading("Col5", text = "Doblez Retorno Cerrado", anchor=CENTER)
        tv.heading("Col6", text = "T estándar Flujo Princ", anchor=CENTER)
        tv.heading("Col7", text = "T estándar Flujo Ramific", anchor=CENTER)      
        
        tv.insert("", END, text = (round(30*float(txt16.get())*Ft*((V**2)/(2*32.2)),4)), values = (round(20*float(txt17.get())*Ft*((V**2)/(2*32.2)),4),     round(50*float(txt18.get())*Ft*((V**2)/(2*32.2)),4),      round(16*float(txt19.get())*Ft*((V**2)/(2*32.2)),4),      round(26*float(txt20.get())*Ft*((V**2)/(2*32.2)),4),     round(50*float(txt21.get())*Ft*((V**2)/(2*32.2)),4),     round(20*float(txt22.get())*Ft*((V**2)/(2*32.2)),4),     round(60*float(txt23.get())*Ft*((V**2)/(2*32.2)),4)))
        tv.pack(expand=True, fill=BOTH)
        tv.place(x=300, y=375)
        tv.configure(height=1)
        perdidas.grid_rowconfigure(0, weight=1)
        perdidas.grid_columnconfigure(0, weight=1)

#CODIGO MAIN

#Creación de la ventana general de todo el programa.
Ventana = Tk()
Ventana.title("Herramienta hidráulica.")
Ventana.resizable(False,False)
x = (Ventana.winfo_screenwidth() // 2) - (650 // 2)
y = (Ventana.winfo_screenheight() // 2) - (250 // 2)
Ventana.geometry(f"{650}x{250}+{x}+{y}")
Ventana.iconbitmap(resource_path("assets/LogoUCR.ico"))
imagen_fondo = PhotoImage(file=resource_path("assets/fondo.png"))
imagen_fondo2 = PhotoImage(file=resource_path("assets/Fondo2.png"))
imagen_fondo3 = PhotoImage(file=resource_path("assets/fondo3.png"))

#Se crea el Frame de menu, este frame corresponde a la ventana del menu principal.
menu = Frame(Ventana)
menu.pack(fill="both", expand=True)

#Se crea el Frame de raiz, este frame corresponde a la ventana de las propiedades del agua.
raiz = Frame(Ventana)
raiz.pack(fill="both", expand=True)
raiz.pack_forget()

#Se le aplica un fondo al frame de raiz.
fondo = Label(raiz, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)
fondo.lower()

#Se crea el Frame de seleccion, este frame corresponde a la ventana de selección de tubería.
seleccion = Frame(Ventana)
seleccion.pack(fill="both", expand=True)
seleccion.pack_forget()

#Se le aplica un fondo al frame de raiz.
fondo2 = Label(seleccion, image=imagen_fondo2)
fondo2.place(x=0, y=0, relwidth=1, relheight=1)
fondo2.lower()

#Se crea el Frame de perdidas, este frame corresponde a la ventana de pérdidas en la tubería.
perdidas = Frame(Ventana)
perdidas.pack(fill="both", expand=True)
perdidas.pack_forget()

#Se le aplica un fondo al frame de raiz.
fondo2 = Label(perdidas, image=imagen_fondo3)
fondo2.place(x=0, y=0, relwidth=1, relheight=1)
fondo2.lower()

#CONFIGURACIÓN DEL MENU PRINCIPAL------------------------------------------------------------------------------------

lbl4 = Label(menu, text="Bienvenido, seleccione una opción:", font=("Arial", 16, "bold"))
lbl4.place(x=140, y=20, width=400, height=30)

lbl5 = Label(menu, text="Ver las principales propiedades del agua a diferentes temperaturas para SI y SB.")
lbl5.place(x=127, y=80, width=600, height=30)

lbl6 = Label(menu, text="Seleccionar la tubería para el sistema de succión y descarga de una bomba.     ")
lbl6.place(x=125, y=130, width=600, height=30)

lbl13 = Label(menu, text="Calcular las pérdidas hidráulicas en la tubería y accesorios.")
lbl13.place(x=74, y=180, width=600, height=30)

btn4 = Button(menu, text= "Propiedades del Agua", bg="green", command= Boton4)
btn4.place(x=10, y=80, width=200, height=30)

btn5 = Button(menu, text= "Selección de tubería", bg="green", command= Boton5)
btn5.place(x=10, y=130, width=200, height=30)

btn13 = Button(menu, text= "Perdidas en Tubería", bg="green", command= Boton13)
btn13.place(x=10, y=180, width=200, height=30)

# FIN CONFIGURACIÓN DEL MENU PRINCIPAL-------------------------------------------------------------------------------

#CONFIGURACIÓN DE PROPIEDADES DEL AGUA-------------------------------------------------------------------------------
lbl1 = Label(raiz, text="Ingrese la temperatura: ", bg="white")
lbl1.place(x=20, y=60, width=150, height=30)
txt1 = Entry(raiz, bg="pink")
txt1.place(x=220, y=60, width=100, height=30)
btn0 = Button(raiz, text= "Calcular", bg="green", command = FunEnter)
btn0.place(x=330, y=60, width=150, height=30)

lbl2 = Label(raiz, text="Seleccione el sistema de medida: ", bg="white")
lbl2.place(x=30, y=20, width=180, height=30)

lbl3 = Label(raiz, text="ó", bg="white")
lbl3.place(x=300, y=20, width=180, height=30)

btn1 = Button(raiz, text= "Sistema Internacional", bg="turquoise", command= Boton1)
btn1.place(x=220, y=20, width=150, height=30)

btn2 = Button(raiz, text= "Sistema Inglés", bg="turquoise", command= Boton2)
btn2.place(x=410, y=20, width=150, height=30)
    
btn3 = Button(raiz, text= "⬅ Volver", bg="turquoise", command= Boton3)
btn3.place(x=0, y=0, width=100, height=20)


#FIN CONFIGURACIÓN DE PROPIEDADES DEL AGUA--------------------------------------------------------------------------

#CONFIGURACIÓN DE SELECCION DE TUBERIA-------------------------------------------------------------------------------
lbl7 = Label(seleccion, text="Ingrese el caudal: ", bg="white")
lbl7.place(x=40, y=60, width=150, height=30)
txt2 = Entry(seleccion, bg="pink")
txt2.place(x=220, y=60, width=100, height=30)
btn6 = Button(seleccion, text= "Calcular", bg="green", command = selectuberia)
btn6.place(x=410, y=60, width=150, height=30)

lbl8 = Label(seleccion, text="Seleccione el sistema de medida: ", bg="white")
lbl8.place(x=30, y=20, width=180, height=30)

lbl9 = Label(seleccion, text="ó", bg="white")
lbl9.place(x=300, y=20, width=180, height=30)

btn7 = Button(seleccion, text= "Sistema Internacional", bg="yellow", command= Boton7)
btn7.place(x=220, y=20, width=150, height=30)

btn8 = Button(seleccion, text= "Sistema Inglés", bg="yellow", command= Boton8)
btn8.place(x=410, y=20, width=150, height=30)
    
btn9 = Button(seleccion, text= "⬅ Volver", bg="turquoise", command= Boton6)
btn9.place(x=0, y=0, width=100, height=20)


#FIN CONFIGURACIÓN DE SELECCION DE TUBERIA--------------------------------------------------------------------------

#CONFIGURACIÓN DE PERDIDAS EN LA TUBERIA-------------------------------------------------------------------------------
global Perdida_Sis, SistemaInter, Ft
Perdida_Sis=""
Diam=""
SistemaInter = ""
SistemaBrit = ""
lbl11 = Label(perdidas, text="Caudal: ",font=("Arial", 10, "bold"), bg="white")
lbl11.place(x=15, y=60, width=70, height=20)
txt3 = Entry(perdidas, bg="pink")
txt3.place(x=125, y=60, width=100, height=20)

lbl12 = Label(perdidas, text="Temperatura: ",font=("Arial", 10, "bold"),  bg="white")
lbl12.place(x=20, y=85, width=95, height=20)
txt4 = Entry(perdidas, bg="pink")
txt4.place(x=125, y=85, width=100, height=20)

lbl13 = Label(perdidas, text="Longitud: ", font=("Arial", 10, "bold"), bg="white")
lbl13.place(x=16, y=110, width=80, height=20)

txt5 = Entry(perdidas, bg="pink")
txt5.place(x=125, y=110, width=100, height=20)

lbl15 = Label(perdidas, text="Nombre del fluido: ", bg="white")
txt6 = Entry(perdidas, bg="lightblue")
lbl16 = Label(perdidas, text="Viscosidad cinemática: ", bg="white")
txt7 = Entry(perdidas, bg="lightblue")

lbl14 = Label(perdidas, text="Fluido:                    ó",font=("Arial", 10, "bold"),  bg="white")
lbl14.place(x=-17, y=135, width=215, height=20)
btn15 = Button(perdidas, text= "Agua", bg="lightseagreen", command = lambda: otrofluido(1))
btn15.place(x=75, y=135, width=70, height=20)
btn16 = Button(perdidas, text= "Otro", bg="lightseagreen", command = lambda: otrofluido(2))
btn16.place(x=160, y=135, width=70, height=20)
lbl40 = Label(perdidas, text="(m^2/s)", bg="white")
lbl41 = Label(perdidas, text="(ft^2/s)", bg="white")
#Selección de diámetro nominal.

lbl17 = Label(perdidas, text="Diámetro Nominal (in - céd 40): ",font=("Arial", 10, "bold"),  bg="white")
lbl17.place(x=40, y=210, width=205, height=20)

boton_activo = None

btn17 = Button(perdidas, text= "1/8", bg="lightyellow", command = lambda: BotonDN(btn17,0.125,0.032))
btn17.place(x=30, y=235, width=35, height=20)
btn18 = Button(perdidas, text= "1/4", bg="lightyellow", command = lambda: BotonDN(btn18,0.25,0.030))
btn18.place(x=70, y=235, width=35, height=20)
btn19 = Button(perdidas, text= "3/8", bg="lightyellow", command = lambda: BotonDN(btn19,0.375,0.028))
btn19.place(x=110, y=235, width=35, height=20)
btn20 = Button(perdidas, text= "1/2", bg="lightyellow", command = lambda: BotonDN(btn20,0.5,0.026))
btn20.place(x=150, y=235, width=35, height=20)
btn21 = Button(perdidas, text= "3/4", bg="lightyellow", command = lambda: BotonDN(btn21,0.75,0.024))
btn21.place(x=190, y=235, width=35, height=20)
btn22 = Button(perdidas, text= "1", bg="lightyellow", command = lambda: BotonDN(btn22,1,0.022))
btn22.place(x=230, y=235, width=35, height=20)
btn23 = Button(perdidas, text= "1 1/4", bg="lightyellow", command = lambda: BotonDN(btn23,1.25,0.021))
btn23.place(x=30, y=260, width=35, height=20)
btn24 = Button(perdidas, text= "1 1/2", bg="lightyellow", command = lambda: BotonDN(btn24,1.5,0.020))
btn24.place(x=70, y=260, width=35, height=20)
btn25 = Button(perdidas, text= "2", bg="lightyellow", command = lambda: BotonDN(btn25,2,0.019))
btn25.place(x=110, y=260, width=35, height=20)
btn26 = Button(perdidas, text= "2 1/2", bg="lightyellow", command = lambda: BotonDN(btn26,2.5,0.018))
btn26.place(x=150, y=260, width=35, height=20)
btn27 = Button(perdidas, text= "3", bg="lightyellow", command = lambda: BotonDN(btn27,3,0.017))
btn27.place(x=190, y=260, width=35, height=20)
btn28 = Button(perdidas, text= "3 1/2", bg="lightyellow", command = lambda: BotonDN(btn28,3.5,0.017))
btn28.place(x=230, y=260, width=35, height=20)
btn29 = Button(perdidas, text= "4", bg="lightyellow", command = lambda: BotonDN(btn29,4,0.016))
btn29.place(x=30, y=285, width=35, height=20)
btn30 = Button(perdidas, text= "5", bg="lightyellow", command = lambda: BotonDN(btn30,5,0.015))
btn30.place(x=70, y=285, width=35, height=20)
btn31 = Button(perdidas, text= "6", bg="lightyellow", command = lambda: BotonDN(btn31,6,0.015))
btn31.place(x=110, y=285, width=35, height=20)
btn32 = Button(perdidas, text= "8", bg="lightyellow", command = lambda: BotonDN(btn32,8,0.014))
btn32.place(x=150, y=285, width=35, height=20)
btn33 = Button(perdidas, text= "10", bg="lightyellow", command = lambda: BotonDN(btn33,10,0.013))
btn33.place(x=190, y=285, width=35, height=20)
btn34 = Button(perdidas, text= "12", bg="lightyellow", command = lambda: BotonDN(btn34,12,0.013))
btn34.place(x=230, y=285, width=35, height=20)
btn35 = Button(perdidas, text= "14", bg="lightyellow", command = lambda: BotonDN(btn35,14,0.013))
btn35.place(x=30, y=310, width=35, height=20)
btn36 = Button(perdidas, text= "16", bg="lightyellow", command = lambda: BotonDN(btn36,16,0.012))
btn36.place(x=70, y=310, width=35, height=20)
btn37 = Button(perdidas, text= "18", bg="lightyellow", command = lambda: BotonDN(btn37,18,0.012))
btn37.place(x=110, y=310, width=35, height=20)
btn38 = Button(perdidas, text= "20", bg="lightyellow", command = lambda: BotonDN(btn38,20,0.012))
btn38.place(x=150, y=310, width=35, height=20)
btn39 = Button(perdidas, text= "24", bg="lightyellow", command = lambda: BotonDN(btn39,24,0.011))
btn39.place(x=190, y=310, width=35, height=20)

lbl18 = Label(perdidas, text="Accesorios: ", font=("Arial", 10, "bold"), bg="white")
lbl18.place(x=34, y=340, width=100, height=20)

lbl19 = Label(perdidas, text="                   Tipo                    |      cantidad    ", bg="skyblue")
lbl19.place(x=34, y=365, width=225, height=20)

#Selección de accesorios

lbl20 = Label(perdidas, text= "Válv.Globo",relief="solid", bd=1)
lbl20.place(x=34, y=385, width=145, height=20)
lbl21 = Label(perdidas, text= "Válv.ángulo",relief="solid", bd=1)
lbl21.place(x=34, y=405, width=145, height=20)
lbl22 = Label(perdidas, text= "Válv.Compuerta Abierta",relief="solid", bd=1)
lbl22.place(x=34, y=425, width=145, height=20)
lbl23 = Label(perdidas, text= "Válv.Reten.Oscilante",relief="solid", bd=1)
lbl23.place(x=34, y=445, width=145, height=20)
lbl24 = Label(perdidas, text= "Válv.Reten.Bola",relief="solid", bd=1)
lbl24.place(x=34, y=465, width=145, height=20)
lbl25 = Label(perdidas, text= "Válv.Marip.Abierta",relief="solid", bd=1)
lbl25.place(x=34, y=485, width=145, height=20)
lbl26 = Label(perdidas, text= "Válv.Pie Disc.Vást",relief="solid", bd=1)
lbl26.place(x=34, y=505, width=145, height=20)
lbl27 = Label(perdidas, text= "Válv.Pie Disc.Bisag",relief="solid", bd=1)
lbl27.place(x=34, y=525, width=145, height=20)
lbl28 = Label(perdidas, text= "Codo estánd 90°",relief="solid", bd=1)
lbl28.place(x=34, y=545, width=145, height=20)
lbl29 = Label(perdidas, text= "Codo 90° radio Largo",relief="solid", bd=1)
lbl29.place(x=34, y=565, width=145, height=20)
lbl30 = Label(perdidas, text= "Codo 90° para calle",relief="solid", bd=1)
lbl30.place(x=34, y=585, width=145, height=20)
lbl31 = Label(perdidas, text= "Codo estándar 45°",relief="solid", bd=1)
lbl31.place(x=34, y=605, width=145, height=20)
lbl32 = Label(perdidas, text= "Codo 45° para calle",relief="solid", bd=1)
lbl32.place(x=34, y=625, width=145, height=20)
lbl33 = Label(perdidas, text= "Doblez Retorno cerrado",relief="solid", bd=1)
lbl33.place(x=34, y=645, width=145, height=20)
lbl34 = Label(perdidas, text= "T estádar Flujo Princip",relief="solid", bd=1)
lbl34.place(x=34, y=665, width=145, height=20)
lbl35 = Label(perdidas, text= "T estádar Flujo Ramific",relief="solid", bd=1)
lbl35.place(x=34, y=685, width=145, height=20)

txt8 = Entry(perdidas, justify="center", bg="lightcyan2")
txt8.place(x=180, y=385, width=80, height=20)
txt8.insert(0, "0")
txt9 = Entry(perdidas, justify="center", bg="lightcyan2")
txt9.place(x=180, y=405, width=80, height=20)
txt9.insert(0, "0")
txt10 = Entry(perdidas, justify="center", bg="lightcyan2")
txt10.place(x=180, y=425, width=80, height=20)
txt10.insert(0, "0")
txt11 = Entry(perdidas, justify="center", bg="lightcyan2")
txt11.place(x=180, y=445, width=80, height=20)
txt11.insert(0, "0")
txt12 = Entry(perdidas, justify="center", bg="lightcyan2")
txt12.place(x=180, y=465, width=80, height=20)
txt12.insert(0, "0")
txt13 = Entry(perdidas, justify="center", bg="lightcyan2")
txt13.place(x=180, y=485, width=80, height=20)
txt13.insert(0, "0")
txt14 = Entry(perdidas, justify="center", bg="lightcyan2")
txt14.place(x=180, y=505, width=80, height=20)
txt14.insert(0, "0")
txt15 = Entry(perdidas, justify="center", bg="lightcyan2")
txt15.place(x=180, y=525, width=80, height=20)
txt15.insert(0, "0")
txt16 = Entry(perdidas, justify="center", bg="lightcyan2")
txt16.place(x=180, y=545, width=80, height=20)
txt16.insert(0, "0")
txt17 = Entry(perdidas, justify="center", bg="lightcyan2")
txt17.place(x=180, y=565, width=80, height=20)
txt17.insert(0, "0")
txt18 = Entry(perdidas, justify="center", bg="lightcyan2")
txt18.place(x=180, y=585, width=80, height=20)
txt18.insert(0, "0")
txt19 = Entry(perdidas, justify="center", bg="lightcyan2")
txt19.place(x=180, y=605, width=80, height=20)
txt19.insert(0, "0")
txt20 = Entry(perdidas, justify="center", bg="lightcyan2")
txt20.place(x=180, y=625, width=80, height=20)
txt20.insert(0, "0")
txt21 = Entry(perdidas, justify="center", bg="lightcyan2")
txt21.place(x=180, y=645, width=80, height=20)
txt21.insert(0, "0")
txt22 = Entry(perdidas, justify="center", bg="lightcyan2")
txt22.place(x=180, y=665, width=80, height=20)
txt22.insert(0, "0")
txt23 = Entry(perdidas, justify="center", bg="lightcyan2")
txt23.place(x=180, y=685, width=80, height=20)
txt23.insert(0, "0")


#Selección de material.

lbl36 = Label(perdidas, font=("Arial", 10, "bold"), text= "Selección de Material:", bg="white")
lbl36.place(x=290, y=60, width=140, height=20)

boton_act = None

btn40 = Button(perdidas, text= "Vidrio", bg="lightyellow", command = lambda: BotonMaterial(btn40,5E-8,1.64E-7))
btn40.place(x=290, y=85, width=120, height=20)
btn41 = Button(perdidas, text= "Plástico", bg="lightyellow", command = lambda: BotonMaterial(btn41,3E-7,1E-6))
btn41.place(x=415, y=85, width=120, height=20)
btn42 = Button(perdidas, text= "Tubo estirado", bg="lightyellow", command = lambda: BotonMaterial(btn42,1.5E-6,5E-6))
btn42.place(x=540, y=85, width=120, height=20)
btn43 = Button(perdidas, text= "Acero comercial", bg="lightyellow", command = lambda: BotonMaterial(btn43,4.6E-5,1.5E-4))
btn43.place(x=290, y=110, width=120, height=20)
btn44 = Button(perdidas, text= "hierro Galvanizado", bg="lightyellow", command = lambda: BotonMaterial(btn44,1.5E-4,5E-4))
btn44.place(x=415, y=110, width=120, height=20)
btn45 = Button(perdidas, text= "Hierro dúc.Revest", bg="lightyellow", command = lambda: BotonMaterial(btn45,1.2E-4,4E-4))
btn45.place(x=540, y=110, width=120, height=20)
btn46 = Button(perdidas, text= "Hierro Dúc.No Revest", bg="lightyellow", command = lambda: BotonMaterial(btn46,2.4E-4,8E-4))
btn46.place(x=290, y=135, width=120, height=20)
btn47 = Button(perdidas, text= "Concreto", bg="lightyellow", command = lambda: BotonMaterial(btn47,1.2E-4,4E-4))
btn47.place(x=415, y=135, width=120, height=20)
btn48 = Button(perdidas, text= "Acero remachado", bg="lightyellow", command = lambda: BotonMaterial(btn48,1.8E-3,6E-3))
btn48.place(x=540, y=135, width=120, height=20)




#Demás botones.

Boton_Press = None

btn10 = Button(perdidas, text= "Calcular",font=("Arial", 12, "bold"), bg="green", command = lambda: perdidasTub())
btn10.place(x=30, y=710, width=230, height=50)

lbl12 = Label(perdidas, text="Seleccione el sistema de medida: ",font=("Arial", 9, "bold"),  bg="white")
lbl12.place(x=18, y=20, width=200, height=30)

lbl13 = Label(perdidas, text="ó",font=("Arial", 10, "bold"), bg="white")
lbl13.place(x=300, y=20, width=180, height=30)

btn11 = Button(perdidas, text= "Sistema Internacional", bg="lightyellow", command= lambda: perdidaSistema(btn11,1))
btn11.place(x=220, y=20, width=150, height=25)

btn12 = Button(perdidas, text= "Sistema Inglés", bg="lightyellow", command= lambda: perdidaSistema(btn12,2))
btn12.place(x=410, y=20, width=150, height=25)

lbl37 = Label(perdidas, text="(L/min)",bg="white")
lbl38 = Label(perdidas, text="(°C)",bg="white")
lbl39 = Label(perdidas, text="(m)",bg="white")
lbl40 = Label(perdidas, text="(m^2/s)",bg="white")
lbl42 = Label(perdidas, text="(gal/min)",bg="white")
lbl43 = Label(perdidas, text="(°F)",bg="white")
lbl44 = Label(perdidas, text="(ft)",bg="white")


    
btn14 = Button(perdidas, text= "⬅ Volver", bg="turquoise", command= Boton14)
btn14.place(x=0, y=0, width=100, height=20)


#FIN CONFIGURACIÓN DE PERDIDAS EN LA TUBERIA--------------------------------------------------------------------------
Ventana.mainloop()