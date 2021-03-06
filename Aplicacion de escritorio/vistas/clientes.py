from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from controladores.logicaClientes import logicaClientes
class clientes:
    def __init__(self,ventana):
        self.ventana=ventana
        self.client=logicaClientes()
        self.ventana.title("Clientes")
        self.ventana.geometry("825x555")
        self.ventana.config(bg="slategrey")
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap("imagenes/cliente.ico")
        self.frame=LabelFrame(self.ventana, text="Clientes", font=('Times', 10,BOLD),padx=20,pady=20)
        self.frame.config(labelanchor=N,width=500)
        self.frame.grid(row=0,column=0,columnspan=3)
        Label(self.frame,text="Por favor escribir el nombre de el cliente para buscarlo",font=('Times', 10)).grid(row=0,columnspan=2,pady=5,sticky=W+E)
        Button(self.frame,text="Buscar",font=('Times', 10,BOLD), command=lambda: self.client.buscarCliente(self.arbol,self.entrada1.get())).grid(row=1,column=0)
        self.entrada1=Entry(self.frame,width=50)
        self.entrada1.grid(row=1,column=1)
        Button(self.frame,text="Añadir un cliente", font=('Times', 10,BOLD),command=self.añadircliente).grid(row=2,columnspan=2,pady=5,sticky=W+E)
        Button(self.frame,text="Eliminar un cliente", font=('Times', 10,BOLD), command=lambda: self.client.eliminarCliente(self.arbol, self.arbol.item(self.arbol.selection())['text'])).grid(row=3,columnspan=2,pady=5,sticky=W+E)
        Button(self.frame,text="Editar un cliente", font=('Times', 10,BOLD),command=self.editarcliente).grid(row=4,columnspan=2,pady=5,sticky=W+E)
        Button(self.frame,text="Refrescar", font=('Times', 10,BOLD), command=lambda: self.client.llenarClientes(self.arbol)).grid(row=5,columnspan=2,pady=5,sticky=W+E)
        Button(self.frame,text="Exportar clientes a una lista excel", font=('Times', 10,BOLD), command=self.pantallita3).grid(row=6,columnspan=2,pady=5,sticky=W+E)
        #lambda: self.client.exportarClientes("SELECT * FROM clientes", self.arbol)
        self.arbol=ttk.Treeview(self.ventana,columns=('#1','#2','#3'))
        self.arbol.grid(row=5,column=0,columnspan=2,padx=2)
        self.arbol.heading("#0",text="ID",anchor = CENTER)
        self.arbol.heading("#1",text="No.Factura",anchor = CENTER)
        self.arbol.heading("#2",text="Nombre",anchor = CENTER)
        self.arbol.heading("#3",text="Telefono",anchor=CENTER)
        scroll=Scrollbar(self.ventana,command=self.arbol.yview)
        scroll.grid(row=5,column=2,sticky="nsew")
        self.client.llenarClientes(self.arbol)
        Button(self.ventana,text="Salir de la vista clientes", font=('Times', 10,BOLD),command=self.ventana.destroy).grid(row=9,column=0,columnspan=2,sticky=W+E)
        self.ventana.mainloop()


    def pantallita3(self):
      #Vista para poner nombre a listas
      self.pantallita3=Toplevel(self.ventana)
      self.pantallita3.geometry("300x200")
      self.pantallita3.title("Titulo de listas")
      self.pantallita3.config(bg="slategrey")
      self.pantallita3.resizable(0,0)
      self.pantallita3.iconbitmap("imagenes/escritura.ico")
      Label(self.pantallita3, text= "Por favor escribir un titulo", font=('Times', 10), bg="slategrey",fg="gray1").pack()
      Label(self.pantallita3, text= "para la lista", font=('Times', 10), bg="slategrey",fg="gray1").pack()
      Label(self.pantallita3, text= " ", bg="slategrey").pack()
      tablaClientes=Entry(self.pantallita3, width=40)
      tablaClientes.pack()
      Label(self.pantallita3, text= " ", bg="slategrey").pack()
      Button(self.pantallita3, text="Confirmar", font=('Times', 10), fg="gray1", command=lambda: self.client.exportarClientes("SELECT * FROM clientes", self.arbol,tablaClientes.get())).pack()
      Label(self.pantallita3, text= " ", bg="slategrey").pack()
      Button(self.pantallita3, text="Cancelar", font=('Times', 10), fg="gray1", command=self.pantallita3.destroy).pack()

    def añadircliente(self):
      #Vista de la ventana añadir entrada
      self.añadircliente=Toplevel(self.ventana)
      self.añadircliente.geometry("400x355")
      self.añadircliente.title("Añadir Cliente")
      self.añadircliente.config(bg="slategrey")
      self.añadircliente.resizable(0,0)
      self.añadircliente.iconbitmap("imagenes/cliente.ico")
      Label(self.añadircliente ,text="", bg = "slateGray").pack()
      Label(self.añadircliente ,text="Por favor llenar las siguientes casillas para",font=('Times',10,), fg="black", bg = "slateGray").pack()
      Label(self.añadircliente ,text="añadir un nuevo cliente", font=('Times',10,), fg="black", bg = "slateGray").pack()
      Label(self.añadircliente ,text="", bg = "slateGray").pack()
      Label(self.añadircliente ,text="No.Factura", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
      Nofa_entry = Entry(self.añadircliente, width = "40")
      Nofa_entry.pack()
      Label(self.añadircliente ,text="", bg = "slateGray").pack()
      Label(self.añadircliente ,text="Nombre", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
      Nombre_entry = Entry(self.añadircliente, width = "40")
      Nombre_entry.pack()
      Label(self.añadircliente ,text="", bg = "slateGray").pack()
      Label(self.añadircliente ,text="Telefono", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
      Telefono_entry = Entry(self.añadircliente, width = "40")
      Telefono_entry.pack()
      Label(self.añadircliente ,text="", bg = "slateGray").pack()
      Button(self.añadircliente,text="Confirmar",font=('Times',10,),command=lambda: self.client.añadirCliente(Nofa_entry.get(), Nombre_entry.get(), Telefono_entry.get(),self.arbol), fg="black",width = "12", height = "1", bg = "LightSkyBlue3").pack()
      Label(self.añadircliente,text="", bg="slateGray" ).pack()
      Button(self.añadircliente,text="Salir",font=('Times', 10,), fg="black",width = "12", height = "1", bg = "LightSkyBlue3", command=self.añadircliente.destroy).pack()

    def editarcliente(self):
      oldId=self.arbol.item(self.arbol.selection())['text']
      if(oldId):
        #Vista de la ventana editar entrada
        self.editarcliente=Toplevel(self.ventana)
        self.editarcliente.geometry("400x415")
        self.editarcliente.title("Editar un cliente")
        self.editarcliente.config(bg="slategrey")
        self.editarcliente.resizable(0,0)
        self.editarcliente.iconbitmap("imagenes/cliente.ico")
        nombre=StringVar(self.editarcliente)
        factura=IntVar(self.editarcliente)
        telefono=StringVar(self.editarcliente)
        factura.set(self.arbol.item(self.arbol.selection())['values'][0])
        nombre.set(self.arbol.item(self.arbol.selection())['values'][1])
        telefono.set(self.arbol.item(self.arbol.selection())['values'][2])
        Label(self.editarcliente ,text="", bg = "slateGray").pack()
        Label(self.editarcliente ,text="Por favor llenar las siguientes casillas para",font=('Times',10,), fg="black", bg = "slateGray").pack()
        Label(self.editarcliente ,text="editar un cliente", font=('Times',10,), fg="black", bg = "slateGray").pack()
        Label(self.editarcliente ,text="", bg = "slateGray").pack()
        Label(self.editarcliente ,text="No.Factura", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
        Nof_entry = Entry(self.editarcliente, width = "40",textvariable=factura)
        Nof_entry.pack()
        Label(self.editarcliente ,text="", bg = "slateGray").pack()
        Label(self.editarcliente ,text="Nombre", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
        Name_entry = Entry(self.editarcliente, width = "40", textvariable=nombre)
        Name_entry.pack()
        Label(self.editarcliente ,text="", bg = "slateGray").pack()
        Label(self.editarcliente ,text="Telefono", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
        Telef_entry = Entry(self.editarcliente, width = "40", textvariable=telefono)
        Telef_entry.pack()
        Label(self.editarcliente ,text="", bg = "slateGray").pack()
        Button(self.editarcliente,text="Confirmar",font=('Times',10,),command= lambda: self.client.editarCliente(oldId,Nof_entry.get(),Name_entry.get(),Telef_entry.get(),self.arbol), fg="black",width = "12", height = "1", bg = "LightSkyBlue3").pack()
        Label(self.editarcliente,text="", bg="slateGray" ).pack()
        Button(self.editarcliente,text="Salir",font=('Times', 10,), fg="black",width = "12", height = "1", bg = "LightSkyBlue3", command=self.editarcliente.destroy).pack()
      else:
        messagebox.showerror(message="Por favor elija un cliente a editar", title="Mensaje del sistema")
        return