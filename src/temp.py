import customtkinter as ctk

# Initialize main window
ctk.set_appearance_mode("Dark")  # Modes: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")

class InteractiveFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=220)  # Set width & height inside frame
        self.place(x=10, y=10)  # Position the frame

        # === BUTTONS (Left Margin, Stacked) ===
        self.button1 = ctk.CTkButton(self, text="Button 1", width=120)
        self.button2 = ctk.CTkButton(self, text="Button 2", width=120)
        self.button3 = ctk.CTkButton(self, text="Button 3", width=120)

        self.button1.place(x=10, y=20)
        self.button2.place(x=10, y=60)
        self.button3.place(x=10, y=100)

        # === CTkSlider (Above Segmented Button) ===
        self.slider = ctk.CTkSlider(self, from_=0, to=100, width=300, command=self.update_progress)
        self.slider.place(x=140, y=10)

        # === SWITCH & CHECKBOX (Middle Section) ===
        self.switch = ctk.CTkSwitch(self, text="Switch", width=100)
        self.switch.place(x=140, y=50)

        self.checkbox = ctk.CTkCheckBox(self, text="Check", width=100)
        self.checkbox.place(x=250, y=50)

        # === RADIO BUTTONS (Middle Right) ===
        self.radio_var = ctk.StringVar(value="1")
        self.radio1 = ctk.CTkRadioButton(self, text="Option 1", variable=self.radio_var, value="1", width=120)
        self.radio2 = ctk.CTkRadioButton(self, text="Option 2", variable=self.radio_var, value="2", width=120)
        self.radio1.place(x=140, y=80)
        self.radio2.place(x=140, y=105)

        # === SEGMENTED BUTTON (Full Width Below) ===
        self.segmented_var = ctk.StringVar(value="A")
        self.segmented_button = ctk.CTkSegmentedButton(self, values=["A", "B", "C"], variable=self.segmented_var, width=300)
        self.segmented_button.place(x=140, y=140)

        # === CUSTOM VERTICAL PROGRESS BAR (Right Side) ===
        self.progress_label = ctk.CTkLabel(self, text="0%", font=("Arial", 14))
        self.progress_label.place(x=450, y=10)

        self.progress = ctk.CTkProgressBar(self, orientation="vertical", height=150, width=20)
        self.progress.place(x=450, y=40)
        self.progress.set(0)  # Initialize at 0

    def update_progress(self, value):
        """Update progress bar based on slider value."""
        self.progress.set(float(value) / 100)
        self.progress_label.configure(text=f"{int(value)}%")

# === Main application ===
root = ctk.CTk()
root.geometry("520x250")  # Slightly larger to accommodate everything
root.title("Updated Layout with Vertical Progress Bar")

frame = InteractiveFrame(root)

root.mainloop()
