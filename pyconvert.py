import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import utility

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

root = tk.Tk()
root.title("Image Format Converter")

# Set window size
window_width = root.winfo_screenwidth() * 0.30
window_height = root.winfo_screenheight() * 0.1
root.geometry(f"{int(window_width)}x{int(window_height)}")

# Frame for folder selection
folder_frame = ttk.Frame(root)
folder_frame.pack(padx=10, pady=10, fill=tk.X)

folder_label = ttk.Label(folder_frame, text="Folder Location:")
folder_label.grid(row=0, column=0, padx=(0, 5), sticky="w")

folder_entry = ttk.Entry(folder_frame)
folder_entry.grid(row=0, column=1, sticky="ew")

browse_button = ttk.Button(folder_frame, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=(5, 0), sticky="ew")

# Frame for image format selection
format_frame = ttk.Frame(root)
format_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

source_label = ttk.Label(format_frame, text="Source Format:")
source_label.grid(row=0, column=0, padx=(0, 5), sticky="w")

source_var = tk.StringVar()
source_dropdown = ttk.Combobox(format_frame, textvariable=source_var, values=["jpg", "png", "dds"], state="readonly")
source_dropdown.current(0)
source_dropdown.grid(row=0, column=1, padx=(0, 20))

target_label = ttk.Label(format_frame, text="Target Format:")
target_label.grid(row=0, column=2, padx=(20, 5), sticky="w")

target_var = tk.StringVar()
target_dropdown = ttk.Combobox(format_frame, textvariable=target_var, values=["jpg", "png", "dds"], state="readonly")
target_dropdown.current(1)
target_dropdown.grid(row=0, column=3)

# Configure columns to expand
folder_frame.grid_columnconfigure(1, weight=1)
format_frame.grid_columnconfigure(1, weight=1)

root.mainloop()