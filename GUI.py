#GUI.py code:
from tkinter import *
from tkinter import messagebox
from Functions import Mosque
from connection import MosqueDB
mosque_manager=Mosque()
db = MosqueDB()

top = Tk()
top.title("Mosques Manangement System")
top.geometry('1000x450')
top.configure(bg="lightgray")

l1=Label(top,text='ID: ')
l1.grid(row=1,column=1)

l2=Label(top,text='Type: ')
l2.grid(row=2,column=1)

l3=Label(top,text='Coordinates: ')
l3.grid(row=3,column=1)

l4=Label(top,text='Name: ')
l4.grid(row=1,column=3)

l5=Label(top,text='Address: ')
l5.grid(row=2,column=3)

l6=Label(top,text='Imam Name: ')
l6.grid(row=3,column=3)

E1=Entry(top)
E1.grid(row=1,column=2)

E2=Entry(top)
E2.grid(row=3,column=2)

E3=Entry(top)
E3.grid(row=1,column=4)

E4=Entry(top)
E4.grid(row=2,column=4)

E5=Entry(top)
E5.grid(row=3,column=4)


def add_entery():
    ID=E1.get()
    Type=value_inside.get()
    Coordinates=E2.get()
    Name=E3.get()
    Address=E4.get()
    Imam=E5.get()
    mosque_manager.Add_Entery(db,ID,Name,Type,Address,Coordinates,Imam)

def delete_entry():
    ID=E1.get()
    mosque_manager.Del_Entrey(db,ID)
    

def search_entry():
    Name=E3.get()
    mosque_manager.Search(db,Name)    

def display_all():
    mosque_manager.Display_all(db) 

def update():
    Name=E3.get()
    new_Imam=E5.get()

    if not Name or not new_Imam:
        messagebox.showwarning('Update','Please enter both Mosque Name and new Imam Name')
        return
    new_data={'Imam':new_Imam}
   
    mosque_manager.Update_Entery(db,Name,new_data) 
    
def clear_fields():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
      

l0=Label(top,text=" ")
l0.grid(row=4,column=0)

b1=Button(top, text="Display All",command=display_all,width=15 ,height=1)
b1.grid(row=5,column=2 ,padx=5,pady=5)

b2=Button(top, text="Search by Name",command=search_entry,width=15 ,height=1)
b2.grid(row=5,column=3,padx=5,pady=5)

b3=Button(top, text="Add Entry",command=add_entery,width=15 ,height=1)
b3.grid(row=6,column=2,padx=5,pady=5)

b4=Button(top, text="Delete Enrty",command=delete_entry,width=15 ,height=1)
b4.grid(row=6,column=3,padx=5,pady=5)

b5=Button(top, text="Update Entry",command=update,width=15 ,height=1)
b5.grid(row=5,column=4,padx=5,pady=5)

b6 = Button(top, text="Display on Map", width=15, height=1, command=lambda: mosque_manager.Display_on_Map(db, E3.get()))
b6.grid(row=6,column=4,padx=5,pady=5)

b7 = Button(top, text="Clear Fields", width=15, height=1, command=clear_fields)
b7.grid(row=7,column=2,padx=5,pady=5)

mosques=["Mosque", "Grand Mosque"]
value_inside = StringVar(top)
value_inside.set("_________________")

o1= OptionMenu(top ,value_inside, *mosques)
o1.grid(row=2,column=2)

right_frame = Frame(top)
right_frame.grid(row=0, column=6, rowspan=14, padx=14, pady=14, sticky="nsew")

display_records = Listbox(right_frame, width=83, height=27)
display_records.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(right_frame, orient=VERTICAL, command=display_records.yview)
scrollbar.pack(side=RIGHT, fill=Y)
display_records.config(yscrollcommand=scrollbar.set)

mosque_manager.display_box=display_records




top.mainloop()
