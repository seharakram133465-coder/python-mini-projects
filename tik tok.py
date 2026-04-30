
import tkinter as tk
from tkinter import filedialog , messagebox

def new_file():
    text.delete(1.0,tk.END)


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".text",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".text",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'w') as file:
            text.delete(1.0,tk.END)
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("info" , "file save successfully!")

root=tk.Tk()
root.title("simple text editor")
root.geometry("1000x800")

menu=tk.Menu(root)
root.config(menu=menu)
file_manu=tk.Menu(menu)
menu.add_cascade(label="File" , menu=file_manu)
file_manu.add_command(label="New" , command=new_file)
file_manu.add_command(label="Open" , command=open_file)
file_manu.add_command(label="Save" , command=save_file)
file_manu.add_separator()
file_manu.add_command(label="Exit" , command=root.quit)

text = tk.Text(root,wrap=tk.WORD, font=("Helvetica" , 12) , fg="red")
text.pack(expand=tk.YES , fill=tk.BOTH)

root.mainloop()