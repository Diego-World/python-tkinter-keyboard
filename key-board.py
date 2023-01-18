from tkinter import *
from tkinter.font import Font as font

# Definição da dimensão da tela
DEF_WIDTG = 1366
DEF_HEIGHT = 330

keyboard_frame = Tk()
keyboard_frame.title("Teclado Virtual Recicla Machine")
keyboard_frame.geometry(f"{DEF_WIDTG+10}x{DEF_HEIGHT+10}")

#TextBox de teste do teclado
textbox_frame = Tk()
textbox_frame.title("Textbox")
textbox_frame.geometry("300x50")
textbox = Entry(textbox_frame)
textbox.pack()

keyboard_frame.configure(bg='#1a1a1a')
# Sobreposição do teclado sobre itens na tela
keyboard_frame.attributes("-topmost", True)
keyboard_frame.resizable(False,False)

CONTRASTCLICK_COL = "#4169E1"
row1 = ["Esc", "'+/~", "1+/!", "2+/@", "3+/#", "4+/$", "5+/%", "6+/^", "7+/&", "8+/*", "9+/(", "0+/)", "-+/_", "=+/+", "Backspace"]
row2 = ["Tab", "q", "w", "e", "r", 't', 'y', 'u', 'i', 'o', 'p', '[+/{', "]+/}", "\\+/|", "Del"]
row3 = ["Caps", "a","s", "d", "f", "g", "h","j", "k", "l", ";+/:", "'+/""", "Enter"]
row4 = ["Shift", "z", "x", "c", "v", "b", "n", "m", ",+/<", ".+/>", "/+/?", "Up", "Shift R"]
row5 = [".com", "Ctrl", "Win", "Alt", " ", "Alt", "Ctrl", "Left", "Bottom", "Right", "menu"]

rows = [row1, row2, row3, row4, row5]

specials = ["Ctrl", "Alt", "Shift", "Shift R", "Win"]
nonLetterKey = specials + ["Esc", "Tab", "Del", "Backspace", "Caps", "Enter", "Up", "Left", "Bottom", "Right", "menu"]
allButtons = []

shiftSp = row1[1:14] + row2[11:14] + row3[10:12] + row4[8:11] +row5[0:0]

width15 = ["Backspace", "Tab"]
width20 = ["Caps", "Shift R"]
width25 = ["Enter", "Shift"]
width55 = [" "]

def on_enter(e):
    e.widget.configure(bg = "#ccc", fg="#000")
    if btnLabels[e.widget]:
        btnLabels[e.widget].configure(bg="#ccc", fg="#666")

def on_leave(e):
    e.widget.configure(bg = "#333", fg="#fff")
    if btnLabels[e.widget]:
        btnLabels[e.widget].configure(bg="#333", fg="#888")

#Printa no console

# def handleClick(event):
#         print(event.widget['text'])

shift_held = False

def handleClick(event):
    text = event.widget['text']
    if shift_held:
        if text in shiftSp:
            text = text.split("+/")[1]
    textbox.insert("end", text)

btnLabels = { }

Y = 2.5

for r in rows:
    X = 5

    for i in r:
        btnWidth = 0.06428*DEF_WIDTG
        btnHeight = 0.2*DEF_HEIGHT

        padx = round(btnWidth/9)
        pady = round(btnHeight/10)

        frame = Frame(keyboard_frame, highlightbackground="#1E1E1E", highlightthickness= 4)



        if i in shiftSp:
            anchor = "se"
            labelT = i.split("+/")
            label = Label(keyboard_frame,text = labelT[1], fg="#888", bg="#333", font=font(size = 11))
            label.place(x=X+padx, y=Y+pady)
            i = labelT[0]
        else:
            anchor = "nw"
            label = None

        btn = Button(frame, activebackground=CONTRASTCLICK_COL, text=i, bg="#333",fg="#fff", relief="flat", padx=padx, pady=pady,borderwidth=0,anchor=anchor, font=font(size=10))

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
        btn.bind("<ButtonRelease-1>",on_enter)
        btn.bind("<Enter>",on_enter)
        btn.bind("<Leave>",on_leave)
        btn.bind((""))

        btnLabels[btn] = label
        allButtons.append(btn)

    Y += btnHeight

# Fica escutando a aplicação até que seja fechada por algum Método ou evento.
keyboard_frame.mainloop()
