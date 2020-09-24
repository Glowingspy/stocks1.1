#importing modules
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import csv
#base window
root = Tk()
root.title('Stock Manager')
root.geometry('600x600')
#class to manage the amount of instances(materials)
class Sorter:
    
    noe_of_materials = 0
    
    def __init__(self, title, entry):
        self.title = title
        self.entry = entry
        Sorter.noe_of_materials += 1
    def get_title(self):
        return self.title
    def get_entry(self):
        return self.entry

countertitle = []
counterentery = []
titles = []
allval = []
def passage_maker():
    
    enter = Entry(root)
    for number in range(no_of_materials):
        x = Sorter(f'Part{number + 1}', enter)
        countertitle.append(x.title)
        counterentery.append(x.entry)
        allval.append(x)  
    
    
    
    x=20
    for value in countertitle:
        x += 1
        value = Label(root,text=f'{value}')
        titles.append(value)
        value.grid(row=x, column=19)
    
    
    y=20
    valsk_raw = []
    for val in counterentery:
        y += 1
        val = Entry(root)
        valsk_raw.append(val)
        val.grid(row=y,column=20)
    
    z = 20
    valsv_raw = []
    for values in countertitle:
        z += 1
        values = Entry(root)
        valsv_raw.append(values)
        values.grid(row=z, column=21)

    saved = False
    def saver():
        
        global saved
       # saving.config(state=DISABLED)
        dictionary_items = str(f'{cordict.items()}\n')
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return 

        f.write(f'{fullname}: ')
        #replacing the defaluts with a more readable format
        dictionary_items = dictionary_items.replace('),','\n')
        dictionary_items = dictionary_items.replace('([(','')
        dictionary_items = dictionary_items.replace(',','-------')
        dictionary_items = dictionary_items.replace(')])','')
        dictionary_items = dictionary_items.replace('(','')
        dictionary_items = dictionary_items.replace('dict_items','\n')
        #
        f.write(dictionary_items)
        
        
        
        saved = True
    
    def exit():
        #global saved
        resposne = messagebox.askquestion('Exit','Are you sure you want to exit?')
        print(resposne)
        if resposne == 'yes':
            if saved == True:
                sys.exit()
            elif saved == False:
                areusure = messagebox.askokcancel('Are you sure', 'Do you want to save the current file?')

                if areusure == True:
                    saver()
                    sys.exit()
                if areusure == False:
                    sys.exit()

    def new():        
        for i in valsv_raw:
            i.destroy()
        valsv_raw.clear()
        for c in valsk_raw:
            c.destroy()
        valsk_raw.clear()
        for z in titles:
            z.destroy()
        titles.clear()
        countertitle.clear()
        counterentery.clear()

        saving.destroy()
        exiter.destroy()
        newer.destroy()
        spami.destroy()
        separator.destroy()
        excel_saving.destroy()


        stocksfunc()

    def ex():
        
        
        f = filedialog.asksaveasfile(mode='w', defaultextension='.csv')
        print(f)
        
        if f is None:
            return 

        with open(r'f.csv', 'w')as a_file:


            writer = csv.writer(a_file, delimiter=';')
            for key, value in cordict.items():
                writer.writerow([key, value])




           # fieldnames = ['Parts', 'Stocks']
            
            #writer = csv.writer(csvfile, fieldnames,delimiter=';')
            
            #writer.writeheader()
           # writer.writerow(cordict)

    def endder():
        global saving, exiter,newer,separator,excel_saving
        saving = Button(root, text='Save As Text', command=saver)
        exiter = Button(root, text='Exit', command=exit)
        newer = Button(root, text='New list',command=new)
        separator = Label(root,text='')
        excel_saving = Button(root, text='Save as Excel',command=ex) 

        saving.grid(row=x+10,column=20)   
        exiter.grid(row=x+10, column=21)
        newer.grid(row=x+10, column=22)
        separator.grid(row=x+15,column=20)
        excel_saving.grid(row=x+20,column=20)

    valskey = []
    valsval = []
    cordict = {}
    def takeparts():
    
        for i in valsk_raw:
            i.config(state=DISABLED)
            x = i.get()
            valskey.append(x)
        
       

        for f in valsv_raw:
            f.config(state=DISABLED)
            y = f.get()
            valsval.append(y)

        spami.config(state=DISABLED)

        print(valskey)
        print(valsk_raw)
        print()
        print(valsval)
        print(valsv_raw)
        #i just ziped it
        for key, value in zip(valskey, valsval):
            cordict[key] = value
        
        
        
        print(cordict)
        endder()





    spami = Button(root, text='Submit', command=takeparts)
    spami.grid(row=x+1,column=20)
    

def stocksfunc():
    global matin, matsub
    matno = Label(root, text='How many materials do you have?(Write in numerical form)')
    matin = Entry(root)
    matsub = Button(root, text='Submit', command=mattake)
    matno.grid(row=20,column=20)
    matin.grid(row=20,column=21)
    matsub.grid(row=20,column=22)



def mattake():             
    global no_of_materials
    no_of_materials = matin.get()
    print(no_of_materials)
    try:
        no_of_materials = int(no_of_materials)
        matin.config(state=DISABLED)
        matsub.config(state=DISABLED)
        passage_maker()    
    except ValueError:
        print('Invalid. Type in integer')
        error = Label(root, text='That is invalid, Type an integer')
        error.grid(row=2,column=2)
        error.grid_forget()
        stocksfunc()
    
    
    









#definitions

#last name definitions
last_name = Label(root, text='Last Name: ',font=('ariel',15))
last_name_e = Entry(root)

def getfirst():
    global firstname
    firstname = first_name_e.get()
    try:
        firstname1 = firstname[0].upper()
        firstname2 = firstname[1:].lower()
        firstname = firstname1+firstname2
        print(firstname)
    except IndexError:
        pass
    
    first_name_s.config(state=DISABLED)
    first_name_e.config(state=DISABLED)

    last_name.grid(row=21,column=21)
    last_name_e.grid(row=21,column=22)
    last_name_s.grid(row=21,column=23)

def getlast():
    global lastname, fullname
    lastname = last_name_e.get()
    try:
        lastname1 = lastname[0].upper()
        lastname2 = lastname[1:].lower()
        lastname = lastname1+lastname2
        print(lastname)
    except IndexError:
        pass
    last_name_s.config(state=DISABLED)
    last_name_e.config(state=DISABLED)
    fullname = '{} {}'.format(firstname,lastname)
    print(fullname)
    #
    first_name.destroy()
    first_name_e.destroy()
    first_name_s.destroy()
    last_name.destroy()
    last_name_e.destroy()
    last_name_s.destroy()
    #take to the part where it asks about the stocks
    stocksfunc()


#first name entry
first_name = Label(root,text='First Name: ',font=('ariel',15))
first_name_e = Entry(root, borderwidth=5)
first_name_s = Button(root, text='Submit',command=getfirst)
#last name entry
last_name_s = Button(root, text='Submit',command=getlast)

#display choices


first_name.grid(row=20,column=21)
first_name_e.grid(row=20,column=22)
first_name_s.grid(row=20,column=23)







root.mainloop()