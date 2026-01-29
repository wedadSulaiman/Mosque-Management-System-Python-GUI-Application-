#Functions.py code:
from difflib import get_close_matches
import difflib
import folium
import sqlite3
import webbrowser
from tkinter import messagebox

class Mosque:

    def __init__(self):
    
        self.display_box=None

    def Add_Entery(self, db, ID, Name, Type, Address, Coordinates, Imam):
      if not ID or not Name or not Type or not Address or not Coordinates or not Imam:
        messagebox.showwarning('Add Entery', 'Please fill all fields')
        return

      if not ID.isdigit():
        messagebox.showerror('ID', 'Please enter numbers only for ID')
        return

      if len(ID) > 4:
        messagebox.showerror('ID', 'ID must be 4 digits or less')
        return

     
      if db.exists(ID):
        messagebox.showerror('ID', 'This ID already exists')
        return
          
      db.insert(ID, Name, Type, Address, Coordinates, Imam)   
      messagebox.showinfo('Add Entery', 'Mosque added successfully')


    
    def Del_Entrey(self, db, ID):
        db.cursor.execute("DELETE FROM Mosque WHERE ID=?", (ID,))
        db.connection.commit()
        if db.cursor.rowcount > 0:
            messagebox.showinfo('Delete', 'Mosque deleted successfully')
            self.Display_all(db)
        else:
            messagebox.showerror('Delete', 'Mosque not found')

    
    def Update_Entery(self, db, Name, new_data):
        db.cursor.execute("UPDATE Mosque SET Imam_Name=? WHERE Name=?", (new_data['Imam'], Name))
        db.connection.commit()
        if db.cursor.rowcount > 0:
            messagebox.showinfo('Update Enter', 'Imam_Name Updated successfully')
            self.Display_all(db)
        else:
            messagebox.showerror('Update Entery', 'Mosque not found')

    
    def Search(self, db, Name):
        if self.display_box:
            self.display_box.delete(0, 'end')

        db.cursor.execute("SELECT * FROM Mosque WHERE Name=?", (Name,))
        results = db.cursor.fetchall()

        if results:
            for mosque in results:
                if self.display_box:
                    self.display_box.insert('end', f"ID: {mosque[0]}")
                    self.display_box.insert('end', f"Name: {mosque[1]}")
                    self.display_box.insert('end', f"Type: {mosque[2]}")
                    self.display_box.insert('end', f"Address: {mosque[3]}")
                    self.display_box.insert('end', f"Coordinates: {mosque[4]}")
                    self.display_box.insert('end', f"Imam: {mosque[5]}")
                    self.display_box.insert('end', "-" * 90)
                else:
                    print(mosque)
            return
        db.cursor.execute("SELECT Name FROM Mosque")
        all_names=[row[0] for row in db.cursor.fetchall()]

        close_match= difflib.get_close_matches(Name,all_names,n=1,cutoff=0.5)

       

        if not close_match:
            messagebox.showerror('Search','Mosque not found')
            return
        
        corrected_name=close_match[0]
        messagebox.showinfo("Corrected Name",f"DO you mean: {corrected_name}")

        db.cursor.execute("SELECT * FROM Mosque WHERE Name=?", (corrected_name,))
        results=db.cursor.fetchall()

        for mosque in results:
             if self.display_box:
                    self.display_box.insert('end', f"ID: {mosque[0]}")
                    self.display_box.insert('end', f"Name: {mosque[1]}")
                    self.display_box.insert('end', f"Type: {mosque[2]}")
                    self.display_box.insert('end', f"Address: {mosque[3]}")
                    self.display_box.insert('end', f"Coordinates: {mosque[4]}")
                    self.display_box.insert('end', f"Imam: {mosque[5]}")
                    self.display_box.insert('end', "-" * 90)
             else:
                 print(mosque)
          

                 
    
    def Display_all(self, db):
        if self.display_box:
            self.display_box.delete(0, 'end')

        db.cursor.execute("SELECT * FROM Mosque")
        mosques = db.cursor.fetchall()

        if not mosques:
            if self.display_box:
                self.display_box.insert('end', "No Mosque to display yet")
            else:
                print("No Mosque to display yet")
        else:
            for mosque in mosques:
                if self.display_box:
                    self.display_box.insert('end', f"ID: {mosque[0]}")
                    self.display_box.insert('end', f"Name: {mosque[1]}")
                    self.display_box.insert('end', f"Type: {mosque[2]}")
                    self.display_box.insert('end', f"Address: {mosque[3]}")
                    self.display_box.insert('end', f"Coordinates: {mosque[4]}")
                    self.display_box.insert('end', f"Imam: {mosque[5]}")
                    self.display_box.insert('end', "-" * 90)
                else:
                    print(mosque)
                    
    def Display_on_Map(self, db, Name):
        # جلب الإحداثيات من قاعدة البيانات
        db.cursor.execute("SELECT Name, Coordinates FROM Mosque WHERE Name=?", (Name,))
        result = db.cursor.fetchone()

        if result:
            mosque_name, coords = result
            try:
                latitude, longitude = map(float, coords.split(","))
            except ValueError:
                messagebox.showerror("Coordinates Error, please enter the coordinates in this format: number,number\nExample: 26.1234,44.1234")

        #     # إنشاء خريطة وتحديد موقع المسجد عليها
            mosque_map = folium.Map(location=[latitude, longitude], zoom_start=16)
            folium.Marker([latitude, longitude], popup=mosque_name).add_to(mosque_map)

        #     # حفظ الخريطة وفتحها في المتصفح
            map_file = "mosque_map.html"
            mosque_map.save(map_file)
            webbrowser.open(map_file)
        else:
            messagebox.showerror('Map', 'Mosque not found')
