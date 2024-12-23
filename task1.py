import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    # Retrieve data from the entry widgets
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    
    # Validate that all fields are filled
    if name == "" or email == "" or age == "":
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        # Process the data (you can store it or print it)
        messagebox.showinfo("Registration Success", f"Thank you for registering!\nName: {name}\nEmail: {email}\nAge: {age}")
        # Optionally, clear the form fields after submission
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_age.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Set window size
root.geometry("300x250")

# Create Labels and Entry widgets for each field
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)

entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_age = tk.Label(root, text="Age:")
label_age.pack(pady=5)

entry_age = tk.Entry(root)
entry_age.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
