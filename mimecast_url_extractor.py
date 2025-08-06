
import tkinter as tk
from tkinter import filedialog, messagebox
import re
import quopri

def extract_url_from_file(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    # Decode quoted-printable encoding
    decoded_data = quopri.decodestring(raw_data).decode('utf-8', errors='ignore')

    # Find the first href="..." URL
    match = re.search(r'href="([^"]+)"', decoded_data)
    if match:
        return match.group(1)
    return None

def select_file_and_extract_url():
    file_path = filedialog.askopenfilename(
        title="Select Mimecast Large File Send File",
    )
    if not file_path:
        return

    url = extract_url_from_file(file_path)
    if url:
        show_url_window(url)
    else:
        messagebox.showerror("URL Not Found", "No valid URL found in the selected file.")

def show_url_window(url):
    url_window = tk.Toplevel()
    url_window.title("Extracted URL")
    url_window.geometry("600x250")

    label = tk.Label(url_window, text="Copy the extracted URL below:", font=("Arial", 12))
    label.pack(pady=10)

    text_box = tk.Text(url_window, wrap="word", height=4)
    text_box.insert("1.0", url)
    text_box.config(state="normal")
    text_box.pack(padx=10, pady=5, fill="both", expand=True)

    text_box.focus()
    text_box.tag_add("sel", "1.0", "end")

# Main GUI
root = tk.Tk()
root.title("Mimecast URL Extractor")
root.geometry("400x100")

label = tk.Label(root, text="Click the button below to select a Mimecast file", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Select File", command=select_file_and_extract_url, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
