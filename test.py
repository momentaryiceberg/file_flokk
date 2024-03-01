import tkinter as tk

# DELETE = listbox.delete(2)        <-- index

# Skilar völdum atriðum úr listboxinu
def listbox_selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))

root = tk.Tk()

listbox = tk.Listbox(root, activestyle='dotbox', selectmode="multiple")
listbox.insert(1, "Nachos")
listbox.insert(2, "Súrmjólk")
listbox.insert(3, "Ryðdeig")
listbox.insert(4, "Ókyngingur")

listbox.pack()

takki = tk.Button(root, text="Prenta valið", command=listbox_selected_item).pack()


root.mainloop()

