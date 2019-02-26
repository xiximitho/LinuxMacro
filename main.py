#Lib to create de macro
import pyautogui as macro



from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread
#Lib to set intervals 
import time




class Thread_Primaria(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()
        
    

    def BtnStart_Pressed_Thread():
        Tecla = dlg.cbox_Keys.currentText()
        Intervalo = float(dlg.edit_Interval.text())
        print(Tecla)
        print(Intervalo)
        if (Tecla == "LEFT MOUSE BUTTON"):
            posX,PosY = macro.position(x=None,y = None)
            a = True
            while(a == True):
                macro.click(button = 'left')
                time.sleep(Intervalo)
                if (dlg.btn_Stop.text() == "Stop."):
                    a = False
            print("ABC_ES")
        if (Tecla == "RIGHT MOUSE BUTTON"):
            posX,PosY = macro.position(x=None,y = None)
            macro.click(x = posX,y = PosY,clicks = 12,interval = Intervalo,button = 'right') 
            print("ABC_DI")

    def run(self):
        self.BtnStart_Pressed_Thread()
        self.myThread = Thread_Primaria()
        self.myThread.start()
        
    




##pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

   # posX,posY = macro.position(x=None,y = None)
   # print(posX,posY)

    #pyautogui.click(clicks=20,interval=0.05,button='left')  # click the mouse

    ## FUNCOES DOS BOTOES DA UI

def BtnConfirmar_Pressed():
    dlg.btn_Confirmar.setText("ABC")
    Tecla = dlg.cbox_Keys.currentText()
    Intervalo = float(dlg.edit_Interval.text())
    return Tecla,Intervalo


def BtnStop_Pressed():
    dlg.btn_Stop.setText("Stop.")


def BtnStop_Pressed():
    dlg.btn_Stop.setText("Stop.")
    

app = QtWidgets.QApplication([])
dlg = uic.loadUi("QT5_window.ui")

dlg.btn_Confirmar.clicked.connect(BtnConfirmar_Pressed)
dlg.btn_Start.clicked.connect(Thread_Primaria.BtnStart_Pressed_Thread)
dlg.btn_Stop.clicked.connect(BtnStop_Pressed)

dlg.show()
app.exec()
















"""['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']"""