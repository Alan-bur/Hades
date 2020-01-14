from tkinter import *
import os


# Ventana
win = Tk()
win.title("Hades")
win.resizable(width=False, height=False)
win.geometry("900x600")
win.configure(background="Black")
win.iconbitmap("UI/windowicon.ico")


# App fondo
fondoimg = PhotoImage(file="UI/w.png")
fondoshow = Label(win, text="", image=fondoimg)
fondoshow.pack()

# Welcome
print("-----------------------------------------------")
print("Hello " + os.getlogin() + "!!,Welcome to Hades")
print("")
print("Thanks for trying my program! c:")
print("-Alan Burcet")
print("")
print("v1.0")
print("-----------------------------------------------")


#************Botones**************

# SystemInfo
systeminfoimg = PhotoImage(file="UI/systeminfo.png")
systeminfo = Button(win, text="SYSTEMINFO", image=systeminfoimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("systeminfo"))
systeminfo.place(x=35, y=150)

# REGEDIT
regimg = PhotoImage(file="UI/regedit.png")
regedit = Button(win, text="REGEDIT", image=regimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("regedit"))
regedit.place(x=35, y=461)

# MSCONFIG
msconfigimg = PhotoImage(file="UI/msconfig.png")
msconfig = Button(win, text="MSCONFIG", image=msconfigimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("msconfig"))
msconfig.place(x=35, y=253)

# SERVICES
servicesimg = PhotoImage(file="UI/services.png")
services = Button(win, text="services", width=150, height=67, highlightthickness= 0, borderwidth=0, image=servicesimg, command= lambda: os.system("services.msc"))
services.place(x=35, y=357)

# Administrador de tareas
adminimg = PhotoImage(file="UI/taskmgr.png")
admin = Button(win, text="TASKMGR", width=150, height=67, highlightthickness= 0, borderwidth=0, image=adminimg, command= lambda: os.system("taskmgr"))
admin.place(x=205, y=150)

# Administrador de Dispositivos
admindispimg = PhotoImage(file="UI/devmgmt.png")
admindisp = Button(win, text="DEVMGMT.MSC", image=admindispimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("DEVMGMT.MSC"))
admindisp.place(x=205, y=253)

# KEYBOARD
kimg = PhotoImage(file="UI/osk.png")
keyboard = Button(win, text="OSK", width=150, height=67, highlightthickness= 0, borderwidth=0, image= kimg, command= lambda: os.system("osk"))
keyboard.place(x=205, y=357)

# EXPLORER
explorerimg = PhotoImage(file="UI/explorer.png")
explorer = Button(win, text="EXPLORER", image=explorerimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("explorer"))
explorer.place(x=205, y=461)

# Snipping Tool
snippingimg = PhotoImage(file="UI/snippingtool.png")
snipping = Button(win, text="snippingtool", image=snippingimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("snippingtool"))
snipping.place(x=375, y=150)

# DRIVERQUERY
driverimg = PhotoImage(file="UI/driverquery.png")
driver = Button(win, text="driverquery", width=150, height=67, highlightthickness= 0, borderwidth=0, image= driverimg, command= lambda: os.system("driverquery"))
driver.place(x=375, y=357)

# APPDATA
appdataimg = PhotoImage(file="UI/APPDATA.png")
appdata = Button(win, text="APPDATA", image=appdataimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("start C:/Users/" + os.getlogin() + "/AppData"))
appdata.place(x=375, y=461)

# DISK MANAGEMENT
diskimg = PhotoImage(file="UI/diskmgmt.png")
disk = Button(win, text="diskmgmt", image=diskimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("diskmgmt.msc"))
disk.place(x=545, y=150)

# IPCONFIG
ipconfigimg = PhotoImage(file="UI/ipconfig.png")
ipconfig = Button(win, text="ipconfig", image=ipconfigimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("ipconfig /all"))
ipconfig.place(x=375, y=253)

# CHARMAP
charmapimg = PhotoImage(file="UI/charmap.png")
charmap = Button(win, text="Charmap", image=charmapimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("charmap"))
charmap.place(x=545, y=253)

# Optional Features
optimg = PhotoImage(file="UI/optionalfeatures.png")
opt = Button(win, text="OPT", width=150, height=67, highlightthickness= 0, borderwidth=0, image= optimg, command= lambda: os.system("optionalfeatures"))
opt.place(x=545, y=357)

# MAIN
mainimg = PhotoImage(file="UI/main.png")
main = Button(win, text="main", width=150, height=67, highlightthickness= 0, borderwidth=0, image= mainimg, command= lambda: os.system("main.cpl"))
main.place(x=545, y=461)

# CONTROL PANEL
controlimg = PhotoImage(file="UI/control panel.png")
controlpanel = Button(win, text="Control Panel", image=controlimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("control panel"))
controlpanel.place(x=714, y=150)

# NOTEPAD
notepadimg = PhotoImage(file="UI/notepad.png")
notepad = Button(win, text="NOTEPAD", image=notepadimg, width=150, height=67,borderwidth=0, highlightthickness= 0, command= lambda: os.system("notepad"))
notepad.place(x=714, y=253)

# HELP
helpimg = PhotoImage(file="UI/help.png")
help = Button(win, text="HELP", width=150, height=67, highlightthickness= 0, borderwidth=0, image= helpimg, command= lambda: os.system("help"))
help.place(x=714, y=357)

# CLR
clsimg = PhotoImage(file="UI/cls.png")
cls = Button(win, text="clr", width=150, height=67, highlightthickness= 0, borderwidth=0, image= clsimg, command= lambda: os.system("cls"))
cls.place(x=714, y=461)

#*****Botones de arriba****

# RESTART
restimg = PhotoImage(file="UI/restart.png")
restart = Button(win, text="RESTART", image=restimg, width=43, height=45,borderwidth=0, highlightthickness= 0, command= lambda: os.system("shutdown /r"))
restart.place(x=855, y=35)

#shutdown
shutimg = PhotoImage(file="UI/shutdown.png")
shut = Button(win, text="SHUTDOWN", image=shutimg, width=43, height=45,borderwidth=0, highlightthickness= 0, command= lambda: os.system("shutdown /s"))
shut.place(x=800, y=35)

# sleep
sleepimg = PhotoImage(file="UI/sleep.png")
sleep = Button(win, text="SLEEP", image=sleepimg, width=43, height=45, borderwidth=0, highlightthickness=0,command=lambda: os.system("shutdown /l"))
sleep.place(x=745, y=35)

win.mainloop()
