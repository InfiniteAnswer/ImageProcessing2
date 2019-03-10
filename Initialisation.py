from Callbacks import *
import Shared
import tkinter as tk
from LayoutConfig import *
from RecipePanel import RecipePanel

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
        frame.grid(row=0, column=2, sticky=tk.N)
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
                              length=SLIDER_LENGTH
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


class generate_filter_frame:
    def __init__(self):
        self.generate_filter_recipe_listbox()
        self.generate_filter_controls()

    def generate_filter_controls(self):
        self.filter_controls_frame = tk.Frame(master=Shared.filter_frame)
        self.filter_controls_frame.grid(row=0, column=1, sticky=tk.NW)
        self.add_button = tk.Button(master=self.filter_controls_frame,
                                    text="Add",
                                    command=add_button_callback)
        self.output_as_input_button = tk.Button(master=self.filter_controls_frame,
                                                text="Use output as input",
                                                command=use_output_as_input_callback)
        self.sequence_mode_variable = tk.IntVar()
        self.sequence_mode_variable.set(1)
        self.single_filter_mode_button = tk.Radiobutton(master=self.filter_controls_frame,
                                                        text="Single filter",
                                                        variable=self.sequence_mode_variable,
                                                        value=1,
                                                        command=mode_callback)
        self.sequence_mode_button = tk.Radiobutton(master=self.filter_controls_frame,
                                                   text="Sequence",
                                                   variable=self.sequence_mode_variable,
                                                   value=2,
                                                   command=mode_callback)
        self.dummy_layout_spacer = tk.Frame(master=self.filter_controls_frame)

        self.add_button.pack(anchor=tk.NW, fill=tk.X)
        self.output_as_input_button.pack(anchor=tk.NW)
        self.dummy_layout_spacer.pack(anchor=tk.NW, pady=PADY)
        self.single_filter_mode_button.pack(anchor=tk.NW)
        self.sequence_mode_button.pack(anchor=tk.NW)

    def generate_filter_recipe_listbox(self):
        self.listbox = tk.Listbox(master=Shared.filter_frame,
                                  height=int(HEIGHT_FILTER_FRAME / FONT_POINTS_2_PIXELS))
        self.listbox.grid(row=0, column=0, sticky=tk.NW, padx=PADX)
        self.listbox.bind('<<ListboxSelect>>', self.filter_listbox_onselect)
        for key in Shared.recipe_panels:
            self.listbox.insert(tk.END, key)

    def filter_listbox_onselect(self, evt):
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


def initialise():
    generate_recipe_panels()
    Shared.filter_frame_contents = generate_filter_frame()
