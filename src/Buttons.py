import customtkinter as ctk
from Data_sharing import comm_port_send
class button_widget:
    
    def buttons(frame):

        def on_click(string):
            comm_port_send.put(string)
            print(string)
        
        button1 = ctk.CTkButton(frame, text="Button 1", command=lambda: on_click("button 1 pressed"))
        button1.pack(side="top", pady=10, padx=10, anchor="w")

        
        button2 = ctk.CTkButton(frame, text="Button 2", command=lambda: on_click("button 2 pressed"))
        button2.pack(side="top", pady=10, padx=10, anchor="w")

        
        button3 = ctk.CTkButton(frame, text="Button 3", command=lambda: on_click("button 3 pressed"))
        button3.pack(side="top", pady=10, padx=10, anchor="w")

        
        button4 = ctk.CTkButton(frame, text="Button 4", command=lambda: on_click("button 4 pressed"))
        button4.pack(side="top", pady=10, padx=10, anchor="w")



