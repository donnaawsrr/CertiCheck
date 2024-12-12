import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def verify_signature(filepath):
    """Verify the digital signature of the given executable."""
    try:
        # Use signtool.exe for verification if it's available
        result = subprocess.run(
            ["signtool", "verify", "/pa", filepath],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return "Signature is valid."
        else:
            return result.stderr.strip()
    except FileNotFoundError:
        return "signtool.exe not found. Please ensure it's installed and available in PATH."

def browse_file():
    """Open a file dialog to select an executable file."""
    filepath = filedialog.askopenfilename(
        title="Select an Executable File",
        filetypes=[("Executable Files", "*.exe")]
    )
    if filepath:
        file_path_var.set(filepath)

def check_signature():
    """Check the signature of the selected file."""
    filepath = file_path_var.get()
    if not filepath or not os.path.isfile(filepath):
        messagebox.showerror("Error", "Please select a valid executable file.")
        return

    result = verify_signature(filepath)
    result_text_var.set(result)

# Create the main application window
app = tk.Tk()
app.title("CertiCheck - EXE Signature Verifier")
app.geometry("500x300")
app.resizable(False, False)

# Define StringVars for dynamic updates
file_path_var = tk.StringVar()
result_text_var = tk.StringVar()

# Create GUI components
frame = tk.Frame(app, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

file_label = tk.Label(frame, text="Executable File:")
file_label.grid(row=0, column=0, sticky=tk.W, pady=5)

file_entry = tk.Entry(frame, textvariable=file_path_var, width=40)
file_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(frame, text="Browse...", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

verify_button = tk.Button(frame, text="Verify Signature", command=check_signature)
verify_button.grid(row=1, column=0, columnspan=3, pady=10)

result_label = tk.Label(frame, text="Result:")
result_label.grid(row=2, column=0, sticky=tk.W, pady=5)

result_text = tk.Label(frame, textvariable=result_text_var, wraplength=400, justify="left")
result_text.grid(row=3, column=0, columnspan=3, sticky=tk.W, pady=5)

# Run the main event loop
app.mainloop()
