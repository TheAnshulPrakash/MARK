import customtkinter as ctk
from Data_sharing import comm_port_send

class DialogBox:
    def output_box(parent):
        global box
        box = ctk.CTkTextbox(parent)
        box.pack(fill="both",padx=10,pady=5,side="bottom",expand = True)
        box.configure(state="disabled")

    def text_whisper(string):
        box.configure(state="normal")
        box.insert("end",string)
        box.configure(state="disabled")
        
        
        
    def Serial_Box(parent):
        global Ser_Out        
        Ser_Out=ctk.CTkTextbox(parent)        
        Ser_Out.pack(fill="both",padx=10,pady=5,side="bottom",expand = True)
        Ser_Out.configure(state="disabled")
    
    
    def Serial_enter(parent):
        #ctk.CTkLabel(parent, text="Send Command:")
    
        entry = ctk.CTkEntry(parent,placeholder_text="Send Command...")  
        entry.pack(side="left", anchor="n", pady=5, padx=10,fill= "both",expand=True) 
        def send(event):
            user_input = entry.get()
            print("User Input:", user_input)
            comm_port_send.put(user_input)
            entry.delete(0, ctk.END)

        entry.bind("<Return>", send)



    def text_serial(string):
        Ser_Out.configure(state="normal")
        Ser_Out.insert("end",string)
        Ser_Out.configure(state="disabled")

    def clear_text_1():
        Ser_Out.configureg(state="normal")
        Ser_Out.delete("1.0", ctk.END)
        Ser_Out.configure(state="disabled")
        

    def get_text():
        return box.get(0, ctk.END).strip()

    def clear_text():
        box.configure(state="normal")
        box.delete("1.0", ctk.END)
        box.configure(state="disabled")

    def robot_display(parent):
        global display
        display=ctk.CTkTextbox(parent,height=150)
        display.pack(side="bottom",expand=True,fill="x",anchor="s",padx=5,pady=5)
        display.configure(state="disabled")

    def robot_command(string):        
        display.configure(state="normal")
        display.insert("end",string)
        display.configure(state="disabled")


