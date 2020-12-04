from tkinter import * 
import backend 

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[8])
    
    
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
        
def search_command():
    list1.delete(0,END)
    for row in backend.search(barcode_text.get(),number_text.get(),brand_text.get(),color_text.get(),location_text.get(),price_text.get(),entry_text.get(),expire_text.get()):
        list1.insert(END,row)        

def add_command():
    backend.insert(barcode_text.get(),number_text.get(),brand_text.get(),color_text.get(),location_text.get(),price_text.get(),entry_text.get(),expire_text.get())
    list1.delete(0,END)
    list1.insert(END,(barcode_text.get(),number_text.get(),brand_text.get(),color_text.get(),location_text.get(),price_text.get(),entry_text.get(),expire_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])    
    
def update_command():
    backend.update(selected_tuple[0],barcode_text.get(),number_text.get(),brand_text.get(),color_text.get(),location_text.get(),price_text.get(),entry_text.get(),expire_text.get() )        
        
window = Tk()

window.wm_title("PaintStore")

#titulos del cuadro
 
l1=Label(window,text="bar code")
l1.grid(row=0, column=0)

l2=Label(window,text="Number")
l2.grid(row=0, column=2)

l3=Label(window,text="Brand")
l3.grid(row=0, column=4)

l4=Label(window,text="Color")
l4.grid(row=0, column=6)

l5=Label(window,text="Location")
l5.grid(row=1, column=0)

l6=Label(window,text="Price")
l6.grid(row=1, column=2)

l7=Label(window,text="Entry")
l7.grid(row=1, column=4)

l8=Label(window,text="Expire")
l8.grid(row=1, column=6)

#entradas del contenido

barcode_text=StringVar()
e1=Entry(window, textvariable=barcode_text)
e1.grid(row=0, column=1)

number_text=StringVar()
e2=Entry(window, textvariable=number_text)
e2.grid(row=0, column=3)

brand_text=StringVar()
e3=Entry(window, textvariable=brand_text)
e3.grid(row=0, column=5)

color_text=StringVar()
e4=Entry(window, textvariable=color_text)
e4.grid(row=0, column=7)

location_text=StringVar()
e5=Entry(window, textvariable=location_text)
e5.grid(row=1, column=1)

price_text=StringVar()
e6=Entry(window, textvariable=price_text)
e6.grid(row=1, column=3)

entry_text=StringVar()
e7=Entry(window, textvariable=entry_text)
e7.grid(row=1, column=5)

expire_text=StringVar()
e8=Entry(window, textvariable=expire_text)
e8.grid(row=1, column=7)

# recuardo donde va la leyenda de todos los datos ingresados

list1 = Listbox(window, height=30,width=50)
list1.grid(row=2,column=0, rowspan=6,columnspan=3) 

# barra 

sb1=Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=4)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#Botones

b1=Button(window, text="View All", width=12,command=view_command)
b1.grid(row=2, column=4) 

b2=Button(window, text="Search entry", width=12,command=search_command)
b2.grid(row=3, column=4) 

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=4) 

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=4) 

b5=Button(window, text="Delete", width=12,command=delete_command)
b5.grid(row=6, column=4) 

b6=Button(window, text="Close", width=12,command=window.destroy)
b6.grid(row=7, column=4)

 
window.mainloop() 