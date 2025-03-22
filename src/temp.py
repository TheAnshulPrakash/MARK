import customtkinter as ctk

# Initialize the main window
root = ctk.CTk()
root.geometry("400x300")
root.title("CTk Pack Customization Demo")

# Create buttons with different pack options
btn1 = ctk.CTkButton(root, text="Top Fill X", fg_color="blue")
btn1.pack(side="top", fill="x", padx=5, pady=5)

btn2 = ctk.CTkButton(root, text="Bottom Fill X", fg_color="green")
btn2.pack(side="bottom", fill="x", padx=5, pady=5)

btn3 = ctk.CTkButton(root, text="Left Expand Y", fg_color="red")
btn3.pack(side="left", fill="y", expand=True, padx=5, pady=5)

btn4 = ctk.CTkButton(root, text="Right Expand Y", fg_color="purple")
btn4.pack(side="right", fill="y", expand=True, padx=5, pady=5)

btn5 = ctk.CTkButton(root, text="Center Expand Both", fg_color="orange")
btn5.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# Run the application
root.mainloop()
