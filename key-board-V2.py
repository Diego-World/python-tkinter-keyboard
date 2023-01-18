from tkinter import *
from tkinter.font import Font as font

# Definição da dimensão da tela
DEF_WIDTG = 1366
DEF_HEIGHT = 330

keyboard_frame = Tk()
keyboard_frame.title("Teclado Virtual Recicla Machine V2")
keyboard_frame.geometry(f"{DEF_WIDTG + 10}x{DEF_HEIGHT + 10}")

#TextBox de teste do teclado
textbox_frame = Tk()
textbox_frame.title("Textbox")
textbox_frame.geometry("300x50")
textbox = Entry(textbox_frame)
textbox.pack()

keyboard_frame.configure(bg='#1a1a1a')
# Sobreposição do teclado sobre itens na tela
keyboard_frame.attributes("-topmost", True)
keyboard_frame.resizable(False, False)

CONTRASTCLICK_COL = "#4169E1"
row1 = ["q+/1", "w+/2", "e+/3", "r+/4", 't+/5', 'y+/6', 'u+/7', 'i+/8', 'o+/9', 'p+/0', "Backspace"]
row2 = ["Caps","a", "s", "d", "f", "g", "h", "j", "k", "l", "Enter"]
row3 = ["Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "?"]
row4 = ["Simbolos", "@", " ", ".com", "<=", "=>"]

rows = [row1, row2, row3, row4]

shiftSp = row1[0:10]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "'", ",", ".", "/", "`", "~"]
specials = ["Caps","Shift", "Simbolos", "Backspace","Enter","<=","=>"," "] + symbols
nonLetterKey = specials
allButtons = []

width15 = ["Caps"]
width20 = ["<=","=>","Enter"]
width25 = [ "Shift","Backspace"]
width55 = [" "]


def on_enter(e):
    e.widget.configure(bg="#ccc", fg="#000")
    if btnLabels[e.widget]:
        btnLabels[e.widget].configure(bg="#ccc", fg="#666")


def on_leave(e):
    e.widget.configure(bg="#333", fg="#fff")
    if btnLabels[e.widget]:
        btnLabels[e.widget].configure(bg="#333", fg="#888")

index = 0
symbols_mode = False
letter_to_symbol = {"q": "!", "w": "@", "e": "#", "r": "$", "t": "%", "y": "^", "u": "&", "i": "*", "o": "(", "p": ")","a": "-", "s": "_", "d": "+", "f": "=", "g": "[", "h": "]", "j": "{", "k": "}", "l": ";", "'": ":", "z": ",", "x": ".", "c": "/", "v": "`", "b": "~","m":"'","n":":"}
letter_to_number = {"q": "1", "w": "2", "e": "3", "r": "4", "t": "5", "y": "6", "u": "7", "i": "8", "o": "9", "p": "0"}

switched_buttons = []
caps_mode = False
shift_mode = False

def handleClick(event):
    global symbols_mode, caps_mode, shift_mode
    text = event.widget['text']
    if text == "Backspace":
        textbox.delete(len(textbox.get()) - 1)
    elif text == "<=":
        textbox.icursor(textbox.index(INSERT) - 1)
    elif text == "=>":
        textbox.icursor(textbox.index(INSERT) + 1)
    elif text == "Enter":
        print("Enter pressed")
    elif text == "Shift":
        shift_mode = not shift_mode
        for i, button in enumerate(row1[0:10]):
            letter, number = button.split("+/")
            if shift_mode:
                allButtons[i].config(text=number)
            else:
                allButtons[i].config(text=letter)
    elif text == "Caps":
        caps_mode = not caps_mode
        for button in allButtons:
            if button['text'].isalpha() and button['text'] not in specials and button['text'] != "Caps":
                if caps_mode:
                    button.config(text=button['text'].upper())
                else:
                    button.config(text=button['text'].lower())
    elif text == "Simbolos":
        symbols_mode = not symbols_mode
        if symbols_mode:
            for button in allButtons:
                if button['text'] not in nonLetterKey:
                    switched_buttons.append(button)
                    button['text'] = letter_to_symbol.get(button['text'], button['text'])
        else:
            for button in switched_buttons:
                button['text'] = next((letter for letter, symbol in letter_to_symbol.items() if symbol == button['text']), button['text'])
            switched_buttons.clear()
    else:
        textbox.insert("end", text)


#ACOMPANHA O BLOCO DE CÒDIGO ACIMA
def symbol_on_release(event, btn):
    global index
    index = 0

btnLabels = {}

Y = 2.5

for r in rows:
    X = 4
    for i in r:
        btnWidth = 0.0798 * DEF_WIDTG
        btnHeight = 0.25 * DEF_HEIGHT

        padx = round(btnWidth / 9)
        pady = round(btnHeight / 10)

        frame = Frame(keyboard_frame, highlightbackground="#1E1E1E", highlightthickness=4)

        if i in shiftSp:
            anchor = "se"
            labelT = i.split("+/")
            label = Label(keyboard_frame, text=labelT[1], fg="#888", bg="#333", font=font(size=11))
            label.place(x=X + padx, y=Y + pady)
            i = labelT[0]
        else:
            anchor = "nw"
            label = None

        btn = Button(frame, activebackground=CONTRASTCLICK_COL, text=i, bg="#333", fg="#fff", relief="flat", padx=padx,
                     pady=pady, borderwidth=0, anchor=anchor, font=font(size=15))

        if i in width15:
            btnWidth *= 1.5
        if i in width20:
            btnWidth *= 2
        elif i in width25:
            btnWidth *= 2.5
        elif i in width55:
            btnWidth *= 5.5

        btn.place(x=0, y=0, width=btnWidth, height=btnHeight)
        frame.place(x=X, y=Y, width=btnWidth, height=btnHeight)

        X += btnWidth

        btn.bind("<Button-1>", handleClick)
        btn.bind("<ButtonRelease-1>", on_enter)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)



        btnLabels[btn] = label
        allButtons.append(btn)

    Y += btnHeight

# Fica escutando a aplicação até que seja fechada por algum Método ou evento.
keyboard_frame.mainloop()
