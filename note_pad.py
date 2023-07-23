import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def save_as_file():
    file_location = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ["all files", "*.*"]])
    # "Text Files", "*.txt" -> kalau kita memilih 'Text Files" dibagian "save as type" pada saat mau save file, maka kita hanya diperolehkan untuk menyimpan file dengan tipe .txt
    # "all files", "*.*"] -> kalau kita memilih 'All Files" dibagian "save as type" pada saat mau save file, maka kita bisa menyimpan file dengan jenis apapun
    
    if not file_location:
        return
    
    with open(file_location, "w") as file_output:
        text = text_box.get(1.0, tk.END)
        file_output.write(text)
    file_name = file_location.split("/")[-1]
    window.title(f"{file_name} - {file_location}")

def open_file():
    file_location = filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ["all files", "*.*"]])
    
    with open(file_location, "r") as file:
        text = file.read()
    
    text_box.insert(tk.END,text)
    file_name = file_location.split("/")[-1]
    window.title(f"{file_name} - {file_location}")


window  = tk.Tk()
window.title("Note Pad")
window.geometry("700x600")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame1.grid(row=0, column=0)

# membuat menu bar
menubar = tk.Menu(frame1)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label= "New", font=('consolas',10))
file_menu.add_command(label= "New Window", font=('consolas',10))
file_menu.add_command(label= "Open", font=('consolas',10), command= open_file)
file_menu.add_command(label= "Save", font=('consolas',10))
file_menu.add_command(label= "Save As", font=('consolas',10), command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Page Set Up", font=('consolas',10))
file_menu.add_command(label="Print", font=('consolas',10))
file_menu.add_separator()
file_menu.add_command(label="Exit", font=('consolas',10))

edit_menu = tk.Menu(menubar, tearoff= 0)
edit_menu.add_command(label = "Undo", font=('consolas',10))
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", font=('consolas',10))
edit_menu.add_command(label = "Copy", font=('consolas',10))
edit_menu.add_command(label = "Paste", font=('consolas',10))
edit_menu.add_command(label = "Delete", font=('consolas',10))
edit_menu.add_separator()
edit_menu.add_command(label = "Search With Bing", font=('consolas',10))
edit_menu.add_command(label = "Find", font=('consolas',10))
edit_menu.add_command(label = "Find Next", font=('consolas',10))
edit_menu.add_command(label = "Find Previous", font=('consolas',10))
edit_menu.add_command(label = "Replace", font=('consolas',10))
edit_menu.add_command(label = "Go To", font=('consolas',10))
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", font=('consolas',10))
edit_menu.add_command(label = "Time/Date", font=('consolas',10))

format_menu = tk.Menu(menubar, tearoff=0)
format_menu.add_checkbutton(label='Word Warp', font=('consolas',10))
format_menu.add_command(label = "Font", font=('consolas',10))

view_menu = tk.Menu(menubar, tearoff =0)
view_menu.add_command(label = "Zoom", font=('consolas',10))
view_menu.add_checkbutton(label = "Status Bar", font=('consolas',10))

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="View Help", font=('consolas',10))
help_menu.add_command(label="Send Feedback", font=('consolas',10))
help_menu.add_separator()
help_menu.add_command(label="About Notepad", font=('consolas',10))


menubar.add_cascade(label="File", menu= file_menu, font='consolas') # 'menu' untuk mengisi pilihan 
menubar.add_cascade(label="Edit", menu=edit_menu, font='consolas')
menubar.add_cascade(label="Format", menu=format_menu, font='consolas')
menubar.add_cascade(label="View", menu=view_menu, font='consolas')
menubar.add_cascade(label="Help", menu=help_menu, font='consolas')



scroll_bar = ttk.Scrollbar(window)
scroll_bar.grid(row=0, column=0, sticky="ens")


text_box = tk.Text(window, font=('consolas', 12))
text_box.grid(row=0, column=0, sticky="news")

window.mainloop()