from Callbacks import *
from RecipePanel import RecipePanel
import Shared
import tkinter as tk
import LayoutConfig


recipe_list = [
    ["recipe 1", callback1, ["s1", 0, 1, 0.1]],
    ["recipe 2", callback2, ["s1", 0, 1, 0.1], ["s2", 0, 1, 0.1]],
    ["recipe 3", callback1, ["s1", 0, 1, 0.1]]
    ]


def generate_recipe_panels():
    for recipe_line in recipe_list:
        name = recipe_line[0]
        callback = recipe_line[1]
        frame = tk.Frame(Shared.filter_frame)
        frame.grid(row=0, column=2)
        frame.grid_remove()
        slider_list = list()
        variable_list = list()
        for slider_ID, slider_data in enumerate(recipe_line[2:]):
            variable = tk.DoubleVar()
            variable.trace("w", lambda *args, name=name: trace_handler(name))
            slider = tk.Scale(master=frame,
                              label=slider_data[0],
                              from_=slider_data[1],
                              to=slider_data[2],
                              resolution=slider_data[3],
                              variable=variable,
                              orient=tk.HORIZONTAL,
                              length=LayoutConfig.slider_length
                              )
            slider.grid(row=slider_ID)
            slider_list.append(slider)
            variable_list.append(variable)
        recipe_panel = RecipePanel(name=name,
                                   frame=frame,
                                   callback=callback,
                                   slider_list=slider_list,
                                   variable_list=variable_list)
        Shared.recipe_panels[name] = recipe_panel


def generate_filter_recipe_listbox():
    listbox = tk.Listbox(Shared.filter_frame)
    listbox.grid(row=0, column=0)
    listbox.bind('<<ListboxSelect>>', filter_listbox_onselect)
    for key in Shared.recipe_panels:
        listbox.insert(tk.END, key)


def filter_listbox_onselect(evt):
        widget = evt.widget
        index = int(widget.curselection()[0])
        selected_recipe_name = widget.get(index)
        previously_selected_recipe_name = Shared.current_selected_filter
        callback = Shared.recipe_panels[selected_recipe_name].callback
        print('You selected item %d: "%s"' % (index, selected_recipe_name))
        try:
            Shared.recipe_panels[previously_selected_recipe_name].frame.grid_remove()
        except:
            pass
        Shared.recipe_panels[selected_recipe_name].frame.grid()
        Shared.current_selected_filter = selected_recipe_name
        callback()


def generate_filter_frame():
    generate_recipe_panels()
    generate_filter_recipe_listbox()
    #generate_filter_controls()


def initialise():
    generate_filter_frame()