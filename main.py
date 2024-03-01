import tkinter as tk
from tkinter import filedialog
import os

def gluggi2():
    view_var = tk.StringVar(os.listdir(str(path_ent.get)))
    print(view_var)

    gluggi2 = tk.Toplevel(root)
    viewer = tk.Label(gluggi2, textvariable=view_var).pack()
    

def path_browse():
    folder_path = filedialog.askdirectory()
    path_ent.set(folder_path)

    #file_listbox.delete(0, tk.END)  # Clear the existing items in the listbox

    file_listbox

    # Get the list of files in the folder_path
    files = os.listdir(folder_path)

    # Insert each file into the file_listbox
    for file in files:
        file_listbox.insert(tk.END, file)



root = tk.Tk()
root.title("Flokkari")
root.geometry("500x300")

rammi_efri = tk.Frame(root).pack()

path_ent = tk.StringVar()
path_label = tk.Label(rammi_efri, text="Slóð sem unnið er í").pack()
path_entry = tk.Entry(rammi_efri, textvariable=path_ent).pack()
path_button = tk.Button(rammi_efri, text="Velja slóð", command=path_browse).pack()


rammi_nedri = tk.Frame(root).pack()

file_listbox = tk.Listbox(rammi_nedri, selectmode="multiple")
file_listbox.pack()

def select_file():
    selected_file = file_listbox.get(file_listbox.curselection())
    path_ent.set(selected_file)

select_button = tk.Button(rammi_nedri, text="Velja skrá", command=select_file)
select_button.pack()


gluggi2_button = tk.Button(root, text="Gluggi 2", command=gluggi2).pack()



root.mainloop()