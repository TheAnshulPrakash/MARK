import customtkinter as ctk

from SerialComm import SerialCommunication
from data_json import ConfigJSON
class button_widget:
    
    def widgets(frame):

        def on_click(widget_name, value=None):
            from Data_sharing import comm_port_send
            if value is not None:
                print(f"{widget_name}: {value}")
                comm_port_send.put(f"{widget_name}: {value}")
                                   
                
            else:
                comm_port_send.put(f"{widget_name} Clicked")
                print(f"{widget_name} Clicked")

   

        button1 = ctk.CTkButton(frame, text="Button 1", width=120, command=lambda: on_click("Button 1"))
        button2 = ctk.CTkButton(frame, text="Button 2", width=120, command=lambda: on_click("Button 2"))
        button3 = ctk.CTkButton(frame, text="Button 3", width=120, command=lambda: on_click("Button 3"))

        button1.place(x=10, y=20)
        button2.place(x=10, y=60)
        button3.place(x=10, y=100)

        def slider_callback(value):
            on_click("Slider", f"{int(value)}%")

        slider = ctk.CTkSlider(frame, from_=0, to=100, width=300, command=slider_callback)
        slider.place(x=140, y=10)

        switch = ctk.CTkSwitch(frame, text="Switch", width=100, command=lambda: on_click("Switch", "ON" if switch.get() else "OFF"))
        switch.place(x=140, y=50)

        checkbox = ctk.CTkCheckBox(frame, text="Check", width=100, command=lambda: on_click("Checkbox", "Checked" if checkbox.get() else "Unchecked"))
        checkbox.place(x=250, y=50)

        radio_var = ctk.StringVar(value="1")

        radio1 = ctk.CTkRadioButton(frame, text="Option 1", variable=radio_var, value="1", width=120, command=lambda: on_click("Radio Button", "Option 1"))
        radio2 = ctk.CTkRadioButton(frame, text="Option 2", variable=radio_var, value="2", width=120, command=lambda: on_click("Radio Button", "Option 2"))

        radio1.place(x=140, y=80)
        radio2.place(x=140, y=105)

        segmented_var = ctk.StringVar(value="A")

        segmented_button = ctk.CTkSegmentedButton(frame, values=["A", "B", "C"], variable=segmented_var, width=300,
        command=lambda value: on_click("Segmented Button", value))
        segmented_button.place(x=140, y=140)
        
        current_temp=float(ConfigJSON.get_value("robot.comm.Temperature"))
        print(f"Temperature : {current_temp}")
        global progress,progress_label
        progress_label = ctk.CTkLabel(frame, text="0%", font=("Arial", 14))
        progress_label.configure(text=f"{int(current_temp)}%")
        progress_label.place(x=450, y=10)

       
        progress = ctk.CTkProgressBar(frame, orientation="vertical", height=150, width=20)
        progress.place(x=450, y=40)
        progress.set(0)
        
        progress.set(current_temp/100)

    def Temperature(value):
        progress.set(float(value) / 100)
        progress_label.configure(text=f"{int(value)}%")

        


