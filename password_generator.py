from string import *
from tkinter import *
from random import randint, choice
import os


def generate_password():
    all_chars = ascii_letters + punctuation + digits
    password = "".join(choice(all_chars) for i in range(randint(10, 18)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    if os.path.exists(str(en.get()+".json")):
        with open(str(en.get()+'.json'), 'a+') as file:
            file.write('\n' + password_name.get() + " = " + password)
        file.close()
    else:
        with open(str(en.get()+'.json'), "w+") as file:
            file.write('\n' + password_name.get() + ' = ' + password)
        file.close()


win = Tk()
win.title("Générateur de mot de passe")
win.geometry("720x480")
win.iconbitmap("logo.ico")
win.config(background="#2cbade")
frame = Frame(win, bg='#2cbade')
can = Canvas(frame, bg='#2cbade', width=300, height=300, bd=0, highlightthickness=0)
image = PhotoImage(file='image_password.png').zoom(35).subsample(32)
can.create_image(150, 150, image=image)
can.grid(row=0, column=0, sticky=W)
right_frame = Frame(frame, bg='#2cbade')
Label(right_frame, text='Mot de passe', font=("Helvetica", 20), bg='#2cbade', fg='white').pack()
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#2cbade', fg='white')
password_name = Entry(right_frame, font=("Helvetica", 20), bg='#2cbade', fg='white')
en = Entry(right_frame,bg="#2cbade",fg="white",font=("Helvetica",20))
en.insert(0,"fichier")
password_entry.insert(0,"mot de passe généré")
password_name.insert(0,"nom de l'enseigne")
en.pack(fill=X)
password_name.pack()
password_entry.pack()
Button(right_frame, text="Générer", font=("Helvetica", 20), bg='#2cbade', fg='white', command=generate_password).pack(fill=X)
right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)
menu_bar = Menu(win)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Nouveau', command=generate_password)
file_menu.add_command(label="Quitter", command=win.quit)
menu_bar.add_cascade(label='Fichier', menu=file_menu)
win.config(menu=menu_bar)
win.mainloop()

