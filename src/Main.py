import customtkinter as ctk

from Buttons import button_widget
from Display import DialogBox
from WhisperAI import WhisperTTS

import threading
import time

from Data_sharing import whisper_data

import serial.tools.list_ports

import os
import sys



from Icon import Mark_icon
from SerialComm import SerialCommunication
from robot import Commands

from PIL import Image
from data_json import ConfigJSON



def ui():

    global window

    

    current_theme=ConfigJSON.get_value("system.theme")
    current_mode=ConfigJSON.get_value("system.mode")
    ctk.set_appearance_mode(current_mode)
    
    print(current_theme)
    ctk.set_default_color_theme(f"src/themes/{current_theme}.json")
    window = ctk.CTk()
    window.title("M.A.R.K.")
    Mark_icon(window)
    window.geometry("900x550")
    window.minsize(900,530)

    frame=ctk.CTkFrame(window, width=900, height=600)
    frame.pack(fill="both", padx=10, pady=10,expand=True)
    frame.pack_propagate(False)
    
    frame_left = ctk.CTkFrame(frame, height=220, corner_radius=10)
    frame_left.pack_propagate(False)
    frame_left.pack(side="top", padx=15, pady=15, anchor="w",fill="x")

    frame_desktop = ctk.CTkFrame(frame_left,width=350)
    frame_desktop.pack(side="right",fill="x",padx=10,pady=10)
    frame_desktop.pack_propagate(False)
    

    
    
    
    frame_whisper = ctk.CTkFrame(frame)
    frame_whisper.pack(side="left", padx=15, pady=15, anchor="s",fill="both",expand=True)
    frame_whisper.pack_propagate(False)
    DialogBox.output_box(frame_whisper)
    
    frame_Serial = ctk.CTkFrame(frame)
    frame_Serial.pack(side="right", padx=15, pady=15, anchor="s",fill="both",expand=True)
    frame_Serial.pack_propagate(False)
    DialogBox.Serial_Box(frame_Serial)

    var = ctk.BooleanVar()
    
    def WhisperThread():
        TTS = WhisperTTS()
        TTS.listen_and_transcribe(Whisper_On)
    
    def updateDialog():
        while Whisper_On:
            value = whisper_data.get()
            if value == "Listening\n":
                DialogBox.clear_text()
            
            print(f"Output {value}")
            DialogBox.text_whisper(value)
            Commands().classify(value)

            time.sleep(0.8)
    
    def to_start_whisper():
        global Whisper_On, t1, t2
        if var.get():
            Whisper_On = True
            t2 = threading.Thread(target=updateDialog, daemon=True)
            t1 = threading.Thread(target=WhisperThread, daemon=True)
            t1.start()
            t2.start()
        else:
            Whisper_On = False
            DialogBox.clear_text()
    
    checkbox_a = ctk.CTkCheckBox(frame_whisper, text="Voice Commands", checkbox_width=20, checkbox_height=20, variable=var, command=to_start_whisper)
    checkbox_a.pack(side="top", anchor="n", pady=5)
    
    ports = [port.device for port in serial.tools.list_ports.comports()]
    ports.insert(0, "Select One")

    state={"0":"Select One"}

    
    def comm_port_select(clicked):
        
        print(clicked)
        
        if state["0"] != clicked and clicked !="Select One":
            global comm
            ConfigJSON.update_value("system.port",clicked)
            comm=SerialCommunication(port=clicked,baudrate=115200)
            comm.connect()
            print("yes")
        elif clicked == "Select One":
            comm.disconnect()

            
        state["0"]=clicked
        
            
        

    
    
    comm_port = ctk.CTkComboBox(frame_Serial, values=ports, command=comm_port_select)
    comm_port.pack(side="left", anchor="n", pady=5, padx=10)

    DialogBox.Serial_enter(frame_Serial)

    def reload_window(choice):        
        ConfigJSON.update_value("system.theme",choice)
        window.destroy()
        os.execv(sys.executable, ['python'] + sys.argv)

    

    themes=["autumn","breeze","carrot","cherry","coffee","lavender","metal","midnight","patina","pink","rime","rose","sky","violet","yellow"]

    
    DialogBox.robot_display(frame_desktop)
    
    theme_select=ctk.CTkComboBox(frame_desktop, values=themes,command=reload_window)
    theme_select.set(current_theme)
    theme_select.pack(side="right",anchor="n",padx=5,pady=5)

    def switch():
        if k.get(): 
            print("light")
            ctk.set_appearance_mode("light")
            theme_icon.configure(image=theme_light)
            ConfigJSON.update_value("system.mode","light")
        else : 
            ctk.set_appearance_mode("dark")
            ConfigJSON.update_value("system.mode","dark")
            theme_icon.configure(image=theme_dark)
            print("dark")
    
    k=ctk.BooleanVar(value=current_mode=="light")


    
    theme_light=ctk.CTkImage(light_image=Image.open("src/icons/light.png"),size=(25,25))
    theme_dark=ctk.CTkImage(light_image=Image.open("src/icons/dark.png"),size=(25,25))
    theme_icon=ctk.CTkLabel(frame_desktop,width=5,text="")
    if current_mode=="light": theme_icon.configure(image=theme_light)
    else : theme_icon.configure(image=theme_dark)
    theme_icon.pack(side="left",anchor="n",padx=2,pady=2)
    
    theme_mode_switch=ctk.CTkSwitch(frame_desktop, variable=k, command=switch, text="")
    theme_mode_switch.pack(side="left",anchor="nw",padx=2,pady=5)
    
    
    
    
    
    button_widget.buttons(frame_left)
    
ui()
window.mainloop()
