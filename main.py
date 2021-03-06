from functions import *
from tkinter import *
from PIL import Image, ImageTk
import pyautogui, colorsys, sys, math, threading, os, time, pyperclip
from pynput import keyboard, mouse
from subprocess import Popen





width = 550
height = 250
configs = [
    ["files.png", ""],
    ["camera.png", ["start", "microsoft.windows.camera:"]],
    ["steam.png", ""],
    ["vsc.png", ""],
      ["cmd.png", ""],
      [".png", ""],
      [".png", ""],
      [".png", ""],

]

class :
    def __init__(self, x, y, img, ):
        self.x   = x
        self.y   = y
        self.img = img
        self. = 

root = Tk()
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "#000000")
root.attributes('-topmost', True)
centerX, centerY = width / 2, height / 2
mouseX, mouseY = pyautogui.position()
offsetX, offsetY = mouseX - centerX, mouseY - centerY
screenWidth, screenHeight = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f'{width}x{height}+{int(offsetX)}+{int(offsetY)}')
c = Canvas(root, bg = "#000000", width = width, height = height, bd = -2)

icons, RI = [], []
currentSelection = None
hideProgram = True
doUpdate = True

t = 0
for o in range(-1, 2):
    for i in range(-3, 4):
        if t < len(configs):
            cord = [centerX - 30 + i * 75, centerY - 30 + o * 75, centerX + 30 + i * 75, centerY + 30 + o * 75]
            cc = (cord[0], cord[1], f"icons/{configs[t][0]}", configs[t][1])
            RI.append(Image.open(cc.img))
            iWidth, iHeight = RI[-1].size
            r = iHeight / iWidth
            RI[-1] = [
                ImageTk.PhotoImage(RI[-1].resize((40, int(40 * r)), Image.ANTIALIAS)), 
                ImageTk.PhotoImage(RI[-1].resize((47, int(47 * r)), Image.ANTIALIAS))
            ]
            normalSize = RI[-1][0]
            bigSize = RI[-1][1]
            icons.append([c.create_oval(cord), cord, c.create_image(cc.x + 30, cc.y + 30, image = normalSize), normalSize, bigSize, configs[t][1], cc])
        t += 1   
c.pack()

alternate = False
invertCase = False
evaluate = False

def doEval():
	global evaluate
	evaluate = True

def invertCase():
	global invertCase
	invertCase = True

def altC():
    global doUpdate, hideProgram
    doUpdate = True
    hideProgram = not hideProgram

def escape():
    global doUpdate, hideProgram
    if not hideProgram:
        doUpdate = True
        hideProgram = True

def on_click(x, y, button, pressed):
    global hideProgram, doUpdate
    if pressed == True:
        can = False
        if button == mouse.Button.left:
            alternate = False
            can = True
        if button == mouse.Button.right:
            alternate = True
            can = True
        if can and currentSelection != None:
            command = icons[currentSelection][-1].
            if type(command ) == str:
                Popen([icons[currentSelection][-1].], shell = True)
            else:
                Popen(command, shell = True)
            if not alternate:
                doUpdate = True
                hideProgram = True
        if currentSelection == None:
            escape()


def keyDetect():
    with keyboard.GlobalHotKeys({
            '<esc>'  : escape,
            '<alt>+d': invertCase,
            '<alt>+s': doEval,
            '<alt>+c': altC}) as h:
        h.join()

def mouseDetect():
    with mouse.Listener(on_click = on_click) as listener:
        listener.join()

t1 = threading.Thread(target = mouseDetect)
t2 = threading.Thread(target = keyDetect)
t1.start()
t2.start()

tX = 0
tVX = 0

def hide():
    root.withdraw()
    root.update()
    #print("HIDE")

def show():
    global mouseX, mouseY, offsetX, offsetY
    mouseX, mouseY = pyautogui.position()
    offsetX, offsetY = mouseX - centerX, mouseY - centerY
    root.geometry(f'{width}x{height}+{int(offsetX)}+{int(offsetY)}')
    root.deiconify()

timer = 0
time1 = 0

while True:
    time1 = time.time()
    m = pyautogui.position()
    mouseX, mouseY = m[0] - offsetX, m[1] - offsetY
    currentSelection = None
    if hideProgram == False:
        itt = 0
        for ico in icons:
            i = ico[0]
            x1, y1, x2, y2 = c.coords(i)
            mx, my = mp(x1, y1, x2, y2)
            rainbow = hsb(map(dist(mouseX, mouseY, mx, my), 0, 1500, 0, 255), 255, 255)
            c.itemconfig(i, fill = rainbow, width = 0)
            d = dist(mouseX, mouseY, mx, my)
            if d <= 30:
                c.coords(i, expand(ico[1],  5))
                c.itemconfig(ico[2], image = ico[4])
                currentSelection = itt
            elif d >= 35:
                c.coords(i, ico[1])
                c.itemconfig(ico[2], image = ico[3])
            itt += 1

    root.update()
    if doUpdate:
        if hideProgram:
            if tVX != -0.125:
                tVX = -0.125
                timer = 0
                time1 = time.time()
        else:
            if tVX != 0.125:
                tVX = 0.125
                timer = 0
                time1 = time.time()
                show()
        tX = constrain(tX + tVX, 0, 1)
        timer += 1
        if tX == 1:
            time1 = time.time()
            doUpdate = False
        if tX == 0:
            time1 = time.time()
            doUpdate = False
            hide()
        root.attributes("-alpha", tX)
            
    if invertCase:
        try:
            pyperclip.copy(root.clipboard_get().swapcase())
        except:
            pass
        invertCase = False
    if evaluate:
        try:
            pyperclip.copy(eval(root.clipboard_get()))
        except:
            pass
        evaluate = False
    dur = 0.0166666667
    if dur > 0:
        time.sleep(dur)
	
	
	## Code by ganer  
