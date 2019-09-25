# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:31:04 2019

@author: James
"""

root = tkinter.Tk()

root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar=tkinter.Menu(root)
root.config(menu=menu_bar)
#create the menubar labels
run_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=run_menu)
run_menu.add_command(label="run model", command=run)
run_menu.add_command(label="kill", command=kill)
Sheep_entry = tkinter.Entry(root, textvariable=num_of_sheep)
Sheep_entry.pack()


tkinter.mainloop() 