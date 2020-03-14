from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
import os
import subprocess


# -----Window-----
def window():
    global win
    win = Tk()
    win.title("Hades")
    win.resizable(width=False, height=False)
    win.geometry("900x600")
    win.configure(background="grey13")
    win.iconbitmap("icon.ico")
    win.tk_setPalette("indianred")


window()


# App Version
def aver():
    global appver, aversion
    aversion = "Alpha v2.5"
    appver = Label(win, text=aversion, font="sans 11", highlightthickness=0, borderwidth=0, width=8, height=1,
                   bg="grey13", fg="indianred")
    appver.place(x=817, y=570)


aver()


# -----Welcome------
def console_welcome():
    print("---------------------------------------------")
    print("▓▓▓   ▓▓▓    ▓▓▓    ▓▓▓▓▓    ▓▓▓▓▓▓   ▓▓▓▓▓")
    print("▓▓▓   ▓▓▓  ▓▓   ▓▓  ▓▓   ▓▓  ▓▓      ▓▓")
    print("▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓   ▓▓  ▓▓▓▓▓▓   ▓▓▓▓ ")
    print("▓▓▓   ▓▓▓  ▓▓   ▓▓  ▓▓   ▓▓  ▓▓          ▓▓")
    print("▓▓▓   ▓▓▓  ▓▓   ▓▓  ▓▓▓▓▓    ▓▓▓▓▓▓  ▓▓▓▓▓ ")
    print("---------------------------------------------")
    print("                 " + aversion)
    print("---------------------------------------------")


console_welcome()


# -----Settings-----
def set():
    global setback, eye, hide_set
    hide_bar()
    news.place_forget()
    show_buttons()
    setback = Button(win, width="4", height="1", text="◄", font="sans 20", highlightthickness=0, borderwidth=0,
                     command=lambda: menu())
    setback.place(x=1, y=550)
    eye = Button(win, width=40, height=20, image=eyeimg, highlightthickness=0, borderwidth=0,command=lambda: colorblindness())
    eye.place(x=15, y=25)
    def hide_set():
        setback.place_forget()
        eye.place_forget()
        eye_pressed.place_forget()

    # --images
    colorblindnessimg = PhotoImage(file="UI/settings/colorblindness.png")
    switch_disabledimg = PhotoImage(file="UI/settings/switch disabled.png")
    systeminfo_deu = PhotoImage(file="UI/tiles/deuteracromia/SYSTEMINFO.png")
    services_deu = PhotoImage(file="UI/tiles/deuteracromia/SERVICES.png")
    keyboard_deu = PhotoImage(file="UI/tiles/deuteracromia/OSK.png")
    charmap_deu = PhotoImage(file="UI/tiles/deuteracromia/CHARMAP.png")
    opt_deu = PhotoImage(file="UI/tiles/deuteracromia/OPTF.png")
    main_deu = PhotoImage(file="UI/tiles/deuteracromia/MAIN.png")
    controlpanel_deu = PhotoImage(file="UI/tiles/deuteracromia/CONTROLPANEL.png")
    calculator_deu = PhotoImage(file="UI/tiles/deuteracromia/CALCULATOR.png")

    # -- Go back
    def menu():
        power_options()
        tilespressed.place(x=bbx, y=bby)
        eye_pressed.place_forget()
        colorblindbar.place_forget()
        switch_disabled.place_forget()
        setback.place_forget()
        eye.place_forget()
        tiles.place(x=bbx, y=bby)
        eraser.place(x=bbx, y=bby2)
        help.place(x=bbx, y=bby3)
        start.place(x=15, y=15)
        settings.place(x=21, y=550)

    def colorblindness():
        global setcolorblind, colorblindbar, switch_disabled, eye_pressed
        eye_pressed = Label(win, width=40, height=20, image=eye_pressedimg, highlightthickness=0, borderwidth=0)
        eye_pressed.place(x=15, y=25)
        setcolorblind = "active"
        colorblindbar = Label(win, width=200, height=600, highlightthickness=0, borderwidth=0, image=colorblindnessimg)
        colorblindbar.place(x=72, y=0)
        switch_disabled = Button(win, width=50, height=28, image=switch_disabledimg, borderwidth=0,
                                 highlightthickness=0, command=lambda: deuteranopia_mode())
        switch_disabled.place(x=220, y=355)

        def deuteranopia_mode():
            # --columna 1---
            systeminfo.config(bg="orchid4", image=systeminfo_deu)
            services.config(bg="grey", image=services_deu)
            # --columna 2--
            keyboard.config(bg="yellow3", image=keyboard_deu)
            # --columna 3--
            charmap.config(bg="hot pink", image=charmap_deu)
            opt.config(bg="orchid3", image=opt_deu)
            # --columna4--
            main.config(bg="Slateblue3", image=main_deu)
            controlpanel.config(bg="orchid3", image=controlpanel_deu)
            calculator.config(bg="yellow3", image=calculator_deu)

    colorblindness()


eyeimg = PhotoImage(file="UI/settings/eye.png")
eye_pressedimg = PhotoImage(file="UI/settings/eye_pressed.png")

newsimg = PhotoImage(file="UI/version/version.png")
news = Label(win, image=newsimg, highlightthickness=0, borderwidth=0, activebackground="indian red")

# -----Bar------
def bar():
    global bar, hide_bar, tiles, tilespressed, eraser, help, start, startpressed, settings, bbx, bby, bby2, bby3
    bar = Label(win, bg="black", highlightthickness=0, borderwidth=0, width=10, height=600)
    bar.pack(side="left")
    # -Buttons
    tiles = Button(win, width=30, height=29, highlightthickness=0, borderwidth=0, image=tilesimg,
                   activebackground="grey13", command=lambda: tiles_())
    tilespressed = Label(win, width=30, height=29, highlightthickness=0, borderwidth=0, image=tilespressedimg)
    eraser = Button(win, bg="firebrick3", width=30, height=26, highlightthickness=0, borderwidth=0, image=eraserimg,
                    activebackground="firebrick3",
                    command=lambda: os.system("cls"))
    help = Button(win, text="HELP", width=30, height=30, bg="firebrick3", highlightthickness=0, borderwidth=0,
                  image=helpimg,
                  activebackground="grey13",
                  command=lambda: os.system("help"))
    start = Button(win, text="HELP", width=40, height=61, highlightthickness=0, borderwidth=0, image=startimg,
                   bg="firebrick3", activebackground="indianred",
                   command=lambda: new())
    startpressed = Label(win, width=40, bg="black", height=61, highlightthickness=0, borderwidth=0,
                         image=startpressedimg)
    settings = Button(win, bg="firebrick3", width=30, height=30, highlightthickness=0, borderwidth=0, image=setimg,
                      activebackground="firebrick3", command=lambda: set())
    # -Position

    bbx = 21
    bby = 200
    bby2 = bby + 50
    bby3 = bby2 + 50

    tilespressed.place(x=bbx, y=bby)
    eraser.place(x=bbx, y=bby2)
    help.place(x=bbx, y=bby3)
    start.place(x=15, y=15)
    settings.place(x=21, y=550)

    # --Hide
    def hide_bar():
        bar.place_forget()
        tiles.place_forget()
        tilespressed.place_forget()
        eraser.place_forget()
        help.place_forget()
        start.place_forget()
        startpressed.place_forget()
        settings.place_forget()

    # ----News
    def new():
        startpressed.place(x=15, y=15)
        tilespressed.place_forget()
        tiles.place(x=bbx, y=bby)
        power_options_hide()
        news.place(x=71, y=0)
        hide_buttons()

    # -----Tiles Button
    def tiles_():
        startpressed.place_forget()
        tilespressed.place(x=bbx, y=bby)
        news.place_forget()
        show_buttons()
        power_options()

# -Images
helpimg = PhotoImage(file="UI/bar/HELP.png")
eraserimg = PhotoImage(file="UI/bar/eraser.png")
tilesimg = PhotoImage(file="UI/bar/tiles.png")
tilespressedimg = PhotoImage(file="UI/bar/tiles_pressed.png")
startimg = PhotoImage(file="UI/bar/start.png")
startpressedimg = PhotoImage(file="UI/bar/startpressed.png")
setimg = PhotoImage(file="UI/bar/settings.png")
# -----Tile Buttons------#

# -Size
width = 165
height = 43

# -Images
systeminfoimg = PhotoImage(file="UI/tiles/SYSTEMINFO.png")
msconfigimg = PhotoImage(file="UI/tiles/msconfig.png")
servicesimg = PhotoImage(file="UI/tiles/SERVICES.png")
regimg = PhotoImage(file="UI/tiles/regedit.png")
adminimg = PhotoImage(file="UI/tiles/taskmgr.png")
admindispimg = PhotoImage(file="UI/tiles/devmgmt.png")
kimg = PhotoImage(file="UI/tiles/osk.png")
explorerimg = PhotoImage(file="UI/tiles/explorer.png")
snippingimg = PhotoImage(file="UI/tiles/snippingtool.png")
ipconfigimg = PhotoImage(file="UI/tiles/ipconfig.png")
driverimg = PhotoImage(file="UI/tiles/driverquery.png")
appdataimg = PhotoImage(file="UI/tiles/APPDATA.png")
diskimg = PhotoImage(file="UI/tiles/diskmgmt.png")
charmapimg = PhotoImage(file="UI/tiles/charmap.png")
optimg = PhotoImage(file="UI/tiles/optionalfeatures.png")
mainimg = PhotoImage(file="UI/tiles/main.png")
controlimg = PhotoImage(file="UI/tiles/CONTROLPANEL.png")
notepadimg = PhotoImage(file="UI/tiles/notepad.png")
paintimg = PhotoImage(file="UI/tiles/MSPAINT.png")
calculatorimg = PhotoImage(file="UI/tiles/CALC.png")
# -Buttons

systeminfo = Button(win, text=" SYSTEMINFO   ", font="Helvetica", image=systeminfoimg, bg="Slateblue3",
                    activebackground="Slateblue4", activeforeground="white", fg="white", compound="left", width=width,
                    height=height, borderwidth=0, highlightthickness=0,
                    command=lambda: subprocess.Popen("systeminfo", shell=True))
msconfig = Button(win, text="  MSCONFIG      ", font="Helvetica", image=msconfigimg, bg="cornflower blue",
                  activebackground="royal blue", activeforeground="white", fg="white", compound="left", width=width,
                  height=height, borderwidth=0, highlightthickness=0,
                  command=lambda: subprocess.Popen("msconfig", shell=True))

services = Button(win, text="  SERVICES       ", font="Helvetica", image=servicesimg, bg="Cadet Blue3", fg="white",
                  activebackground="cyan4", activeforeground="white", compound="left", width=width, height=height,
                  borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("services.msc", shell=True))

regedit = Button(win, text="  REGEDIT          ", font="Helvetica", image=regimg, bg="skyblue1", fg="white",
                 activeforeground="white", activebackground="deepskyblue", compound="left", width=width, height=height,
                 borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("regedit", shell=True))

admin = Button(win, text="  TASKMGR       ", font="Helvetica", image=adminimg, bg="Palegreen3",
               activebackground="Palegreen4", activeforeground="white", fg="white", compound="left", width=width,
               height=height, borderwidth=0, highlightthickness=0,
               command=lambda: subprocess.Popen("taskmgr", shell=True))

admindisp = Button(win, text="  DEVMGMT         ", activebackground="green4", activeforeground="white",
                   font="Helvetica", image=admindispimg, bg="Palegreen4", fg="white", compound="left", width=width,
                   height=height, borderwidth=0, highlightthickness=0,
                   command=lambda: subprocess.Popen("DEVMGMT.MSC", shell=True))

keyboard = Button(win, text="  OSK                   ", font="Helvetica", image=kimg, bg="yellow green", fg="white",
                  activeforeground="white", activebackground="chartreuse4", compound="left", width=width, height=height,
                  borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("osk", shell=True))

explorer = Button(win, text="  EXPLORER     ", font="Helvetica", image=explorerimg, bg="khaki3", fg="white",
                  activeforeground="white", activebackground="khaki4", compound="left", width=width, height=height,
                  borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("explorer", shell=True))

snipping = Button(win, text="  SNIPPING TOOL  ", font="Helvetica 10 ", image=snippingimg, bg="chocolate3",
                  fg="white", activeforeground="white", activebackground="tan4", compound="left", width=width,
                  height=height, borderwidth=0, highlightthickness=0,
                  command=lambda: subprocess.Popen("snippingtool", shell=True))
ipconfig = Button(win, text="  IPCONFIG         ", font="Helvetica", image=ipconfigimg, bg="tan2", fg="white",
                  activeforeground="white", activebackground="sienna4", compound="left", width=width, height=height,
                  borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("ipconfig /all", shell=True))
driver = Button(win, text="  DRIVERQUERY   ", font="Helvetica 10", image=driverimg, bg="darkorange3", fg="white",
                activeforeground="white", activebackground="sienna4", compound="left", width=width, height=height,
                borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("driverquery", shell=True))
appdata = Button(win, text="  APPDATA       ", font="Helvetica", image=appdataimg, bg="indianred3", fg="white",
                 activeforeground="white", activebackground="indianred4", compound="left", width=width, height=height,
                 borderwidth=0, highlightthickness=0,
                 command=lambda: subprocess.Popen("start C:/Users/" + os.getlogin() + "/AppData", shell=True))

disk = Button(win, text="  DISKMGMT       ", font="Helvetica", image=diskimg, bg="orchid1", fg="white",
              activeforeground="white", activebackground="orchid4", compound="left", width=width, height=height,
              borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("diskmgmt.msc", shell=True))
charmap = Button(win, text="  CHARMAP       ", font="Helvetica", image=charmapimg, bg="medium orchid", fg="white",
                 activeforeground="white", activebackground="orchid3", compound="left", width=width, height=height,
                 borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("charmap", shell=True))
opt = Button(win, text="  OPTF                 ", font="Helvetica", image=optimg, bg="slateblue1", fg="white",
             activeforeground="white", activebackground="dark slate blue", compound="left", width=width, height=height,
             borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("optionalfeatures", shell=True))
main = Button(win, text="  MAIN                  ", font="Helvetica", image=mainimg, bg="medium blue", fg="white",
              activeforeground="white", activebackground="navy", compound="left", width=width, height=height,
              borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("main.cpl", shell=True))
controlpanel = Button(win, text=" CONTROL PANEL  ", font="Helvetica 10", image=controlimg, bg="royal blue", fg="white",
                      activeforeground="white", activebackground="royalblue4", compound="left", width=width,
                      height=height,
                      borderwidth=0, highlightthickness=0,
                      command=lambda: subprocess.Popen("control panel", shell=True))
notepad = Button(win, text="  NOTEPAD        ", font="Helvetica", image=notepadimg, bg="steelblue2", fg="white",
                 activeforeground="white", activebackground="steel blue", compound="left", width=width, height=height,
                 borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("notepad", shell=True))
paint = Button(win, text="  PAINT               ", font="Helvetica", image=paintimg, bg="deep sky blue2", fg="white",
               activeforeground="white", activebackground="turquoise3", compound="left", width=width, height=height,
               borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("mspaint", shell=True))
calculator = Button(win, text=" CALCULATOR ", font="Helvetica", image=calculatorimg, bg="pale green", fg="white",
                    activeforeground="white", activebackground="seagreen3", compound="left", width=width, height=height,
                    borderwidth=0, highlightthickness=0, command=lambda: subprocess.Popen("calc", shell=True))


# -----Show/Hide/Edit Buttons-----#
def show_buttons():
    # ** valores en x**
    columna1 = 100
    columna2 = columna1 + 195
    columna3 = columna2 + 195
    columna4 = columna3 + 195
    # **valores en y**
    fila1 = 140
    fila2 = fila1 + 70
    fila3 = fila2 + 70
    fila4 = fila3 + 70
    fila5 = fila4 + 70
    # --columna 1--
    systeminfo.place(x=columna1, y=fila1)
    msconfig.place(x=columna1, y=fila2)
    services.place(x=columna1, y=fila3)
    regedit.place(x=columna1, y=fila4)
    admin.place(x=columna1, y=fila5)
    # --columna 2--
    admindisp.place(x=columna2, y=fila1)
    keyboard.place(x=columna2, y=fila2)
    explorer.place(x=columna2, y=fila3)
    snipping.place(x=columna2, y=fila4)
    ipconfig.place(x=columna2, y=fila5)
    # --columna 3--
    driver.place(x=columna3, y=fila1)
    appdata.place(x=columna3, y=fila2)
    disk.place(x=columna3, y=fila3)
    charmap.place(x=columna3, y=fila4)
    opt.place(x=columna3, y=fila5)
    # --columna4--
    main.place(x=columna4, y=fila1)
    controlpanel.place(x=columna4, y=fila2)
    notepad.place(x=columna4, y=fila3)
    paint.place(x=columna4, y=fila4)
    calculator.place(x=columna4, y=fila5)


def hide_buttons():
    # --columna 1--
    systeminfo.place_forget()
    msconfig.place_forget()
    services.place_forget()
    regedit.place_forget()
    admin.place_forget()
    # --columna 2--
    admindisp.place_forget()
    keyboard.place_forget()
    explorer.place_forget()
    snipping.place_forget()
    ipconfig.place_forget()
    # --columna 3--
    driver.place_forget()
    appdata.place_forget()
    disk.place_forget()
    charmap.place_forget()
    opt.place_forget()
    # --columna4--
    main.place_forget()
    controlpanel.place_forget()
    notepad.place_forget()
    paint.place_forget()
    calculator.place_forget()


# ----Login
def login():
    loginbackground = Label(win, image=loginbackgroundimg, highlightthickness=0, borderwidth=0)
    loginbackground.place(x=0, y=0)
    bar()
    set()
    keyboard_access = Button(win, width=50, height=47, image=keyboard_accimg, highlightthickness=0, borderwidth=0,
                             activebackground="black", command=lambda: subprocess.Popen("osk", shell=True))
    keyboard_access.place(x=11, y=100)

    # --Name
    def whats_name():
        global nameframe, nameinput
        nameframe = Label(win, image=nameframeimg, width=400, height=125, highlightthickness=0, borderwidth=0)
        nameframe.place(x=270, y=205)
        nameinput = Entry(win, width=10, font="Helvetica 19", highlightthickness=0, borderwidth=0, bg="grey40")
        nameinput.place(x=445, y=274)
        next = Button(win, width=30, height=28, bg="firebrick3", image=nextimg, fg="black", highlightthickness=0,
                      borderwidth=0, command=lambda: verify_name())
        next.place(x=587, y=275)

        def verify_name():
            name = nameinput.get()
            if name == "":
                messagebox.askokcancel(message="Oh.. You forgot to put your name.")
            elif name.isdigit():
                messagebox.askokcancel(message="A name cant have numbers or special characters.")
            else:
                next.place_forget()
                favcolor_function()

    whats_name()

    # --Favorite Color
    def favcolor_function():
        global pick_color
        hide_set()
        startpressed.place(x=15, y=15)
        favcolorframe = Label(win, image=favcolorframeimg, width=350, height=289, highlightthickness=0, borderwidth=0)
        favcolorframe.place(x=300, y=150)
        finishb = Button(win, width=30, height=28, bg="firebrick3", image=nextimg, fg="black", highlightthickness=0,
                         borderwidth=0, command=lambda: finish(),state="disabled")
        finishb.place(x=615, y=407)
        # Sample Colors
        yellow = Button(win, width=6, height=3, bg="yellow3", highlightthickness=0, borderwidth=0,
                        activebackground="yellow", command=lambda: yellow_color())
        blue = Button(win, width=6, height=3, bg="light sky blue", highlightthickness=0, borderwidth=0,
                      activebackground="blue", command=lambda: blue_color())
        green = Button(win, width=6, height=3, bg="sea green", highlightthickness=0, borderwidth=0,
                       activebackground="green", command=lambda: green_color())
        red = Button(win, width=6, height=3, bg="indian red", highlightthickness=0, borderwidth=0,
                     activebackground="red", command=lambda: red_color())
        barcolorb = Button(win, width=15, height=2, bg="Black", text="Custom Color", font="helvetica 12", fg="white",
                           highlightthickness=0, borderwidth=0, activebackground="grey25", command=lambda: pick_color())

        def yellow_color():
            finishb.config(state="active")
            bar.config(bg="yellow3")
            tiles.config(bg="yellow3")
            tilespressed.config(bg="yellow3")
            eraser.config(bg="yellow3", activebackground="yellow3")
            help.config(bg="yellow3", activebackground="yellow3")
            start.config(bg="yellow3", activebackground="yellow3")
            startpressed.config(bg="yellow3")
            settings.config(bg="yellow3", activebackground="yellow3")
            #--
            eye_pressed.config(bg="yellow3", activebackground="yellow3")
            eye.config(bg="yellow3", activebackground="yellow3")

        def blue_color():
            finishb.config(state="active")
            bar.config(bg="light sky blue")
            tiles.config(bg="light sky blue")
            tilespressed.config(bg="light sky blue")
            eraser.config(bg="light sky blue", activebackground="light sky blue")
            help.config(bg="light sky blue", activebackground="light sky blue")
            start.config(bg="light sky blue", activebackground="light sky blue")
            startpressed.config(bg="light sky blue")
            settings.config(bg="light sky blue", activebackground="light sky blue")
            #--
            eye_pressed.config(bg="light sky blue", activebackground="light sky blue")
            eye.config(bg="light sky blue", activebackground="light sky blue")

        def red_color():
            finishb.config(state="active")
            bar.config(bg="indian red")
            tiles.config(bg="indian red")
            tilespressed.config(bg="indian red")
            eraser.config(bg="indian red", activebackground="indian red")
            help.config(bg="indian red", activebackground="indian red")
            start.config(bg="indian red", activebackground="indian red")
            startpressed.config(bg="indian red")
            settings.config(bg="indian red", activebackground="indian red")
            #--
            eye_pressed.config(bg="indian red", activebackground="indian red")
            eye.config(bg="indian red", activebackground="indian red")

        def green_color():
            finishb.config(state="active")
            bar.config(bg="sea green")
            tiles.config(bg="sea green")
            tilespressed.config(bg="sea green")
            eraser.config(bg="sea green", activebackground="sea green")
            help.config(bg="sea green", activebackground="sea green")
            start.config(bg="sea green", activebackground="sea green")
            startpressed.config(bg="sea green")
            settings.config(bg="sea green", activebackground="sea green")
            #--
            eye_pressed.config(bg="sea green", activebackground="sea green")
            eye.config(bg="sea green", activebackground="sea green")

        # ----Custom Color
        def pick_color():
            finishb.config(state="active")
            eye_pressed.place_forget()
            eye.place_forget()
            global color, here
            here = "barcolor"
            color = colorchooser.askcolor()
            bar.config(bg=color[1])
            tiles.config(bg=color[1], activebackground=color[1])
            tilespressed.config(bg=color[1])
            eraser.config(bg=color[1], activebackground=color[1])
            help.config(bg=color[1], activebackground=color[1])
            start.config(bg=color[1], activebackground=color[1])
            startpressed.config(bg=color[1])
            settings.config(bg=color[1], activebackground=color[1])
            setback.config(bg=color[1], activebackground=color[1])
            eye.config(bg=color[1], activebackground=color[1])
            eye_pressed.config(bg=color[1], activebackground=color[1])
            finishb.place(x=615, y=407)

        # ---place
        colorx = 347
        colorx2 = colorx + 70
        colorx3 = colorx2 + 70
        colorx4 = colorx3 + 70
        yellow.place(x=colorx, y=244)
        blue.place(x=colorx2, y=244)
        red.place(x=colorx3, y=244)
        green.place(x=colorx4, y=244)
        barcolorb.place(x=409, y=330)
        # --
        setback.place_forget()
        colorblindbar.place_forget()
        switch_disabled.place_forget()
        nameframe.place_forget()

        # ---Finish Login
        def finish():
            show_buttons()
            power_options()
            hide_login()
            # -Position

            bbx = 21
            bby = 200
            bby2 = bby + 50
            bby3 = bby2 + 50

            tilespressed.place(x=bbx, y=bby)
            eraser.place(x=bbx, y=bby2)
            help.place(x=bbx, y=bby3)
            start.place(x=15, y=15)
            settings.place(x=21, y=550)
            finishb.place_forget()
            barcolorb.place_forget()

        def hide_login():
            startpressed.place_forget()
            keyboard_access.place_forget()
            favcolorframe.place_forget()
            loginbackground.place_forget()
            nameinput.place_forget()
            yellow.place_forget()
            red.place_forget()
            blue.place_forget()
            green.place_forget()

    start.place_forget()
    eye_pressed.place_forget()
    eye.place_forget()
    setback.place_forget()
    colorblindbar.place_forget()
    switch_disabled.place_forget()
    startpressed.place(x=15, y=15)
    settings.place_forget()
    tilespressed.place_forget()
    eraser.place_forget()
    help.place_forget()


nextimg = PhotoImage(file="UI/login/next.png")
favcolorframeimg = PhotoImage(file="UI/login/favcolorframe.png")
nameframeimg = PhotoImage(file="UI/login/whatsname.png")
keyboard_accimg = PhotoImage(file="UI/bar/keyboard_access.png")
loginbackgroundimg = PhotoImage(file="UI/login/login.png")
login()


# ----Power Buttons----#
def power_options():
    global restart, shut, sleep,power_options_hide
    # ----Size----#
    width2 = 25
    height2 = 25
    # ------Buttons---------#
    restart = Button(win, activebackground="grey10", text="RESTART", image=restimg, width=width2, height=height2,
                     borderwidth=0, highlightthickness=0, command=lambda: os.system("shutdown /r"))
    shut = Button(win, activebackground="grey10", text="SHUTDOWN", image=shutimg, width=width2, height=height2,
                  borderwidth=0, highlightthickness=0, command=lambda: os.system("shutdown /s"))

    sleep = Button(win, activebackground="grey10", text="SLEEP", image=sleepimg, width=width2, height=height2,
                   borderwidth=0, highlightthickness=0, command=lambda: os.system("shutdown /l"))

    # ------Coordenates-----#
    space = 745
    space2 = space + 40
    space3 = space2 + 40
    # --
    sleep.place(x=space, y=35)
    shut.place(x=space2, y=35)
    restart.place(x=space3, y=35)
    #-Hide
    def power_options_hide():
        sleep.place_forget()
        shut.place_forget()
        restart.place_forget()

sleepimg = PhotoImage(file="UI/sleep.png")
shutimg = PhotoImage(file="UI/shutdown.png")
restimg = PhotoImage(file="UI/restart.png")

# End Window
win.mainloop()
