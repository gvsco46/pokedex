from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from data import *

#### colors #### 
co0 = "#444466"  # black
co1 = "#feffff"  # white
co2 = "#6f9fbd"  # blue
co3 = "#38576b"  # 
co4 = "#403d3d"   # 
co5 = "#ef5350"   # red

# creating window
window = Tk()
window.title('Follow me on GitHub - gvsco46')
window.geometry('550x510')
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

#creating frame
frame_pokemon = Frame(window, width=550, height=250, relief='flat',)
frame_pokemon.grid(row=1, column=0)

def switch_pokemon(i):
    global image_pokemon, pok_image

    #switch bg of frame
    frame_pokemon['bg'] = pokemon[i]['type'][3]
    
    #type of pokemon
    pok_name['text'] = i
    pok_name['bg'] = pokemon[i]['type'][3] 
    pok_type['text'] = pokemon[i]['type'][1]
    pok_type['bg'] = pokemon[i]['type'][3] 
    pok_id['text'] = pokemon[i]['type'][0]
    pok_id['bg'] = pokemon[i]['type'][3] 

    image_pokemon = pokemon[i]['type'][2]
    # image pokemon
    image_pokemon = Image.open(image_pokemon)
    image_pokemon = image_pokemon.resize((210, 200))
    image_pokemon = ImageTk.PhotoImage(image_pokemon)

    pok_image = Label(frame_pokemon, image=image_pokemon, relief='flat', bg=pokemon[i]['type'][3] , fg=co1)
    pok_image.place(x=60, y=50)

    pok_type.lift()

    #pokemon status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_attack['text'] = pokemon[i]['status'][1]
    pok_def['text'] = pokemon[i]['status'][2]
    pok_speed['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    #pokemon skills
    pok_sk_1['text'] = pokemon[i]['skills'][0]
    pok_sk_2['text'] = pokemon[i]['skills'][1]

# name
pok_name = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_name.place(x=12, y=15)

# cat
pok_type = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=co1)
pok_type.place(x=12, y=50)

# ID
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=co1)
pok_id.place(x=12, y=75)

# Status
pok_status = Label(window, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# Health Points
pok_hp = Label(window, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

# Attack
pok_attack = Label(window, text='Attack: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_attack.place(x=15, y=385)

# Defense
pok_def = Label(window, text='Defense: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_def.place(x=15, y=410)

# Speed
pok_speed = Label(window, text='Speed: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_speed.place(x=15, y=435)

# Total
pok_total = Label(window, text='Total: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# Skills
pok_skills = Label(window, text='Skills', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_skills.place(x=195, y=310)

# Skill 1
pok_sk_1 = Label(window, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_sk_1.place(x=195, y=360)

# Skill 2
pok_sk_2 = Label(window, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_sk_2.place(x=195, y=385)

# Creating  buttons for pokemon

# image/button pikachu
image_pokemon_1 = Image.open('images/cabeca-pikachu.png')
image_pokemon_1 = image_pokemon_1.resize((40, 40))
image_pokemon_1 = ImageTk.PhotoImage(image_pokemon_1)

b_pok_1 = Button(window, command=lambda:switch_pokemon('Pikachu'), image=image_pokemon_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

# image/button bulbasaur
image_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
image_pokemon_2 = image_pokemon_2.resize((40, 40))
image_pokemon_2 = ImageTk.PhotoImage(image_pokemon_2)

b_pok_2 = Button(window, command=lambda:switch_pokemon('Bulbasaur'), image=image_pokemon_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)

# image/button charmander
image_pokemon_3 = Image.open('images/cabeca-charmander.png')
image_pokemon_3 = image_pokemon_3.resize((40, 40))
image_pokemon_3 = ImageTk.PhotoImage(image_pokemon_3)

b_pok_3 = Button(window, command=lambda:switch_pokemon('Charmander'), image=image_pokemon_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

# image\button gyarados
image_pokemon_4 = Image.open('images/cabeca-gyarados.png')
image_pokemon_4 = image_pokemon_4.resize((40, 40))
image_pokemon_4 = ImageTk.PhotoImage(image_pokemon_4)

b_pok_4 = Button(window, command=lambda:switch_pokemon('Gyarados'), image=image_pokemon_4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

# image/button gengar
image_pokemon_5 = Image.open('images/cabeca-gengar.png')
image_pokemon_5 = image_pokemon_5.resize((40, 40))
image_pokemon_5 = ImageTk.PhotoImage(image_pokemon_5)

b_pok_5 = Button(window, command=lambda:switch_pokemon('Gengar'), image=image_pokemon_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)

# image/button dragonite
image_pokemon_6 = Image.open('images/cabeca-dragonite.png')
image_pokemon_6 = image_pokemon_6.resize((40, 40))
image_pokemon_6 = ImageTk.PhotoImage(image_pokemon_6)

b_pok_6 = Button(window, command=lambda:switch_pokemon('Dragonite'), image=image_pokemon_6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)

import random
list_pokemon = ['Pikachu', 'Bulbasaur', 'Charmander', 'Gyarados', 'Gengar', 'Dragonite']

selected_pokemon = random.sample(list_pokemon, 1)
switch_pokemon(selected_pokemon[0])

window.mainloop()
