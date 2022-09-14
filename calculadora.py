
from operaciones import *
from tkinter import *



root=Tk()

root.iconbitmap("ninfa.ico")

root.title("Calculadora")

miFrame=Frame(root,width=200,height=200)
miFrame.pack()

op=""
resultado=0
num1=0
num2=0
#------------pantalla----------------------------------------------------------------

numeroPantalla=StringVar()
numeroPantalla.set("0")
numerolabel=StringVar()
numerolabel.set("0")

labelpantalla=Label(miFrame,textvariable=numerolabel,width=32,font=100, justify="right").grid(row=0,column=0, columnspan=4,padx=10, pady=10)
pantalla=Entry(miFrame,textvariable=numeroPantalla,width=32)
pantalla.grid(row=1,column=0, columnspan=4,padx=10, pady=10)
pantalla.config(font=100, justify="right")

#------------------funciones--------------------------------------

def operacion(num):
    global op,num1
    coma=numeroPantalla.get()
    if coma[-1] == ".":
        
        numeroPantalla.set(numeroPantalla.get() + "0")
        numerolabel.set(numerolabel.get() + "0")
    if op == "":               # si no se ha pulsado operacion
        numerolabel.set(numerolabel.get()+str(num))
        num1=float(numeroPantalla.get())
        numeroPantalla.set("0")
        for key,fn in operaciones.items():
            if num == key:
                op = fn
                return op
    else:                      # si hay operacion pulsada sin numero
        if numeroPantalla.get() == "0":
            bo=numerolabel.get()
            numerolabel.set(bo.rstrip(bo[-1]))
            numerolabel.set(numerolabel.get()+num)
            

            op = num

        else:                  # otra operacion en orden
            igual(op)
            op = num
            for key,fn in operaciones.items():
                if num == key:
                    op = fn            
            
            
            numerolabel.set(numeroPantalla.get()+str(num))
            numeroPantalla.set("0")
            

def numero(num):

    if numeroPantalla.get() == "0" and op == "":
        numeroPantalla.set(num)
        numerolabel.set(num)
    elif numeroPantalla.get() == "0" and op != "":
        numeroPantalla.set(num)
        numerolabel.set(numerolabel.get() + num)
    else:
        numeroPantalla.set(numeroPantalla.get() + num)
        numerolabel.set(numerolabel.get() + num)

def igual(num):
    global op,num1,num2,resultado
    
    if op == "":
        numeroPantalla.set(numeroPantalla.get()) 
    elif op != "" and numeroPantalla.get() != "0": 
        num2=float(numeroPantalla.get())
        resultado=op(num1,num2)
        
        resultado = str(resultado)  
        
        coma=resultado.count('.')

        if resultado[-2] == "." and resultado[-1] == "0" and coma == 1: #evitar el ,0
            resultado = float(resultado)
            resultado = int(resultado)

               
        numeroPantalla.set(str(resultado))
        numerolabel.set(str(resultado))
        num1=float(numeroPantalla.get())
        resultado=float(numeroPantalla.get())
        op = ""
        

#----------------otras funciones-------------------------------------        

def otros(num):
    global op,num1,num2,resultado
    if num == "%":
        if num1 != 0 and op == multiplicacion and numeroPantalla.get() != "0":
            num2=float(numeroPantalla.get())
            resultado=ciento(num1,num2)
            numeroPantalla.set(str(resultado))
            numerolabel.set(str(resultado))
            op=""
            resultado=op(num1)

    elif num == "del":
        bo=numerolabel.get()
        
        signo=""
        for key,fn in operaciones.items():
            if op == fn:
                signo=key
        
        if bo[-1] == signo:
            op = ""
            numeroPantalla.set("0")
        numerolabel.set(bo.rstrip(bo[-1]))
        numeroPantalla.set(bo.rstrip(bo[-1]))
        if numerolabel.get() == "":
            numerolabel.set("0")
            numeroPantalla.set("0")
        

    elif num == ",":
        if numeroPantalla.get() == "0" and op == "":
            numeroPantalla.set("0.")
            numerolabel.set("0.")
        elif numeroPantalla.get() == "0" and op != "":
            numeroPantalla.set(".")
            numerolabel.set(numerolabel.get() + ".")
        else:
            numeroPantalla.set(numeroPantalla.get() + ".")
            numerolabel.set(numerolabel.get() + ".")


#-------------------diccionarios-------------------------------

simbolos = ["+","-","x","/","7","8","9","%","6","5","4","del","3","2","1","M","+/-","0",",","="]
funciones = {"+":operacion,"-":operacion,"x":operacion,"/":operacion,"7":numero,"8":numero,"9":numero,"%":otros,"6":numero,"5":numero,"4":numero,"del":otros,"3":numero,"2":numero,"1":numero,"M":otros,"+/-":otros,"0":numero,",":otros,"=":igual }
operaciones = {"+":suma,"-":resta,"x":multiplicacion,"/":division}

#---------------------teclado-------------------------------------
linea = 2
columna = 0
col=4
lin=7 # 5+2

#----------------construccion tabla-------------------

for btn in simbolos:

    if columna == col and lin >= col+3 : # 2-0 2-1 2-2 2-3 2-4 / 3-0 3-1 3-2 3-3 3-4/ ... 5-0 5-1 5-2 5-3 5-4/ col5 
        
        columna = 0 
        linea += 1
        if linea == col+3: # 
            col=col+1
            linea=2
            columna=col-1

    elif lin<col+3: # 2-5 3-5 4-5 5-5
        
        if linea==columna:
            lin += 1
        linea +=1
        columna = col-1
    
    columna +=1

#----------llamamiento de funciones de teclado---------------    

    for key,fn in funciones.items():
        if btn == key:
            funcion = fn 
            
    boton=Button(miFrame,text=btn,command=lambda n=btn, m=funcion :m(n),width=8,height=3)
    boton.grid(row=linea,column=columna, padx=3,pady=5)
    boton.config(font=100)


root=mainloop()