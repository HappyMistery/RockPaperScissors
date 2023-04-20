#Imports
from tkinter import*
import time
import random

#================================================== W I N D O W ========================================================

#Window configuration
window = Tk()
window.geometry("650x650")
window.resizable(1,1)
window.title("Pedra, paper tisora")
window.config(bg = "seashell3")

#Title
Label(window, text ="Pedra, paper tisora", font ="arial 20 bold", bg ="seashell3").pack()

#Users choice
Label(window, text ="Escull-ne una:", font ="arial 15 bold", bg ="seashell3").place(x=270, y=140)

#Lifes
Label(window, text =  "Vides", font = 'arial 14 bold', bg ='seashell3').place(x=315, y=300)
Label(window, text =  "Usuari:", font = 'arial 11 bold', bg ='seashell3').place(x=266, y=325)
Label(window, text =  "Ordinador:", font = 'arial 11 bold', bg ='seashell3').place(x=240, y=345)

#=======================================================================================================================


#================================================== P R O G R A M ======================================================

#Global variables
global user_lifes
global comp_lifes
global pick
user_lifes = 3
comp_lifes = 3
pick = ""

#Computer pick
def computer_choice():
    comp_pick = random.randint(1, 3)
    if comp_pick == 1:
        comp_pick = "pedra"
    elif comp_pick == 2:
        comp_pick = "paper"
    else:
        comp_pick = "tisora"
    return comp_pick


#User pick
def pick_stone():
    global pick
    pick = "pedra"
    Label(window, text=f"Has escollit: {pick}", font="arial 13 bold", bg="seashell3").place(x=270, y=250)

def pick_paper():
    global pick
    pick = "paper"
    Label(window, text=f"Has escollit: {pick}", font="arial 13 bold", bg="seashell3").place(x=270, y=250)

def pick_scissor():
    global pick
    pick = "tisora"
    Label(window, text=f"Has escollit: {pick}", font="arial 13 bold", bg="seashell3").place(x=270, y=250)


#Result of the fight
result = StringVar()
def play():
    global user_lifes
    global comp_lifes
    global pick
    comp_pick = computer_choice()
    if pick == comp_pick:
        result.set(f"Empat, tant tú com l'ordinador heu escollit {pick}.")
    elif pick == "pedra" and comp_pick == "paper":
        user_lifes-=1
        if user_lifes == 0:
            Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
            result.set("Has perdut, ja no et queden vides.")
            Label(window, text="Què vols fer a continuació?:", font='arial 12 bold', bg='seashell3').place(x=400, y=570)
            Button(window, font ="arial 13 bold", text ="TORNAR A JUGAR", padx=5, bg="seashell4", command=restart).place(x=400,y=600)
        else:
            Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
            result.set("Has perdut 1 vida, l'ordinador ha escollit paper.")
    elif pick == "paper" and comp_pick == "tisora":
        user_lifes-=1
        if user_lifes == 0:
            Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
            result.set("Has perdut, ja no et queden vides.")
            Label(window, text="Què vols fer a continuació?:", font='arial 12 bold', bg='seashell3').place(x=400, y=570)
            Button(window, font ="arial 13 bold", text ="TORNAR A JUGAR", padx=5, bg="seashell4", command=restart).place(x=400,y=600)
        else:
            Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
            result.set("Has perdut 1 vida, l'ordinador ha escollit tisora.")
    elif pick == "tisora" and comp_pick == "pedra":
        user_lifes-=1
        if user_lifes == 0:
            Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
            result.set("Has perdut, ja no et queden vides.")
            Label(window, text="Què vols fer a continuació?:", font='arial 12 bold', bg='seashell3').place(x=400, y=570)
            Button(window, font ="arial 13 bold", text ="TORNAR A JUGAR", padx=5, bg="seashell4", command=restart).place(x=400,y=600)
        else:
            Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
            result.set("Has perdut 1 vida, l'ordinador ha escollit pedra.")
    elif pick == "pedra" and comp_pick == "tisora":
        comp_lifes-=1
        if comp_lifes == 0:
            Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
            result.set("Has guanyat, l'ordinador té 0 vides.")
            Label(window, text="Què vols fer a continuació?:", font='arial 12 bold', bg='seashell3').place(x=400, y=570)
            Button(window, font="arial 13 bold", text="TORNAR A JUGAR", padx=5, bg="seashell4", command=restart).place(x=400, y=600)
        else:
            Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
            result.set("L'ordinador ha perdut 1 vida, ha escollit tisora.")
    elif pick == "paper" and comp_pick == "pedra":
        comp_lifes-=1
        if comp_lifes == 0:
            Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
            result.set("Has guanyat, l'ordinador té 0 vides.")
            Label(window, text="Què vols fer a continuació?:", font='arial 12 bold', bg='seashell3').place(x=400, y=570)
            Button(window, font ="arial 13 bold", text ="TORNAR A JUGAR", padx=5, bg="seashell4", command=restart).place(x=400,y=600)
        else:
            Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
            result.set("L'ordinador ha perdut 1 vida, ha escollit pedra.")
    elif pick == "tisora" and comp_pick == "paper":
        comp_lifes -= 1
        if comp_lifes == 0:
            Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
            result.set("Has guanyat, l'ordinador té 0 vides.")
            Label(window, text="Què vols fer a continuació?:", font='arial 12 bold', bg='seashell3').place(x=400, y=570)
            Button(window, font ="arial 13 bold", text ="TORNAR A JUGAR", padx=5, bg="seashell4", command=restart).place(x=400,y=600)
        else:
            Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
            result.set("L'ordinador ha perdut 1 vida, ha escollit pedra.")
    else:
        result.set("Resposta invàlida. Escull-ne una: pedra, paper, tisora")


#Restart the game
def restart():
    global user_lifes
    global comp_lifes
    global pick
    user_lifes = 3
    comp_lifes = 3
    pick = ""
    Label(window, text= "", font="arial 13 bold", bg="seashell3", width = 50).place(x=270, y=250)
    Label(window, font='arial 12 bold', text = "", bg='antiquewhite2', width=50, ).place(x=75, y=500)
    Label(window, text=user_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=325)
    Label(window, text=comp_lifes, font='arial 12 bold', bg='seashell3').place(x=330, y=345)
    Label(window, text="", font='arial 12 bold', bg='seashell3', width = 50).place(x=400, y=570)
    Label(window, text="", font='arial 12 bold', bg='seashell3', width = 17).place(x=397, y=599)
    Label(window, text="", font='arial 12 bold', bg='seashell3', width=17).place(x=397, y=622)


#Exit the program
def Exit():
    window.destroy()

#=======================================================================================================================



#================================================== W I N D O W ========================================================

Label(window, text = user_lifes, font = 'arial 12 bold', bg ='seashell3').place(x=330, y=325)
Label(window, text = comp_lifes, font = 'arial 12 bold', bg ='seashell3').place(x=330, y=345)

#Buttons
Label(window, font = 'arial 12 bold', textvariable = result , bg ='antiquewhite2',width = 50,).place(x=75, y=500)
Button(window, font = 'arial 13 bold', text = 'JUGAR'  ,padx =5,bg ='seashell4' ,command = play).place(x=300,y=380)
Button(window, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=575,y=600)
Button(window, font = 'arial 13 bold', text = "PEDRA", padx =5,bg ='seashell4' ,command = pick_stone).place(x=200, y=200)
Button(window, font = 'arial 13 bold', text = "PAPER", padx =5,bg ='seashell4' ,command = pick_paper).place(x=300, y=200)
Button(window, font = 'arial 13 bold', text = "TISORA", padx =5,bg ='seashell4' ,command = pick_scissor).place(x=400, y=200)

#=======================================================================================================================


window.mainloop()