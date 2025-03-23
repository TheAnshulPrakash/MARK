from PIL import Image,ImageTk
import ctypes


class Mark_icon():

    def __init__(self,parent):
        app_id = "MARK.mark"  
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        self.icon=Image.open("src/icons/MARK.png")
        self.icon=ImageTk.PhotoImage(self.icon)
        parent.iconphoto(True,self.icon)