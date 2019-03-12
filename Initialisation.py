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
    listbox = None
    filter_controls_frame = None

    def __init__(self):
        listbox = generate_filter_frame.generate_filter_recipe_listbox()
        filter_controls_frame, widget_dict = generate_filter_frame.generate_filter_controls()
        filter_controls_frame.widget_dict = widget_dict

    @staticmethod
    def generate_filter_controls():
        filter_controls_frame = tk.Frame(master=Shared.filter_frame)
        filter_controls_frame.grid(row=0, column=1, sticky=tk.NW)
        add_button = tk.Button(master=filter_controls_frame,
                                    text="Add",
                                    command=add_button_callback)
        output_as_input_button = tk.Button(master=filter_controls_frame,
                                                text="Use output as input",
                                                command=use_output_as_input_callback)
        sequence_mode_variable = tk.IntVar()
        sequence_mode_variable.set(1)
        single_filter_mode_button = tk.Radiobutton(master=filter_controls_frame,
                                                        text="Single filter",
                                                        variable=sequence_mode_variable,
                                                        value=1,
                                                        command=mode_callback)
        sequence_mode_button = tk.Radiobutton(master=filter_controls_frame,
                                                   text="Sequence",
                                                   variable=sequence_mode_variable,
                                                   value=2,
                                                   command=mode_callback)
        dummy_layout_spacer = tk.Frame(master=filter_controls_frame)

        add_button.pack(anchor=tk.NW, fill=tk.X)
        output_as_input_button.pack(anchor=tk.NW)
        dummy_layout_spacer.pack(anchor=tk.NW, pady=PADY)
        single_filter_mode_button.pack(anchor=tk.NW)
        sequence_mode_button.pack(anchor=tk.NW)
        widget_dict = dict()
        widget_dict["add_button"] = add_button
        widget_dict["output_as_input_button"] = output_as_input_button
        widget_dict["single_filter_mode_button"] = single_filter_mode_button
        widget_dict["sequence_mode_button"] = sequence_mode_button
        return (filter_controls_frame, widget_dict)

    @staticmethod
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

    @staticmethod
    def generate_filter_recipe_listbox():
        listbox = tk.Listbox(master=Shared.filter_frame,
                                  height=int(HEIGHT_FILTER_FRAME / FONT_POINTS_2_PIXELS))
        listbox.grid(row=0, column=0, sticky=tk.NW, padx=PADX)
        listbox.bind('<<ListboxSelect>>', generate_filter_frame.filter_listbox_onselect)
        for key in Shared.recipe_panels:
            listbox.insert(tk.END, key)
        return listbox


class generate_input_frame:
    def __init__(self):
        input_label = tk.Label(master=Shared.input_frame,
                               image=Shared.input_imtk,
                               )
        input_label.grid(row=0, column=0)
        load_button = tk.Button(master=Shared.input_frame,
                                text="Load",
                                command=load_file_callback)
        load_button.grid(row=1, column=0)
        Shared.input_frame.widget_dict = dict()
        Shared.input_frame.widget_dict["input_label"] = input_label
        Shared.input_frame.widget_dict["load_button"] = load_button


class generate_output_frame:
    def __init__(self):
        output_label = tk.Label(master=Shared.output_frame,
                               image=Shared.output_imtk,
                               )
        output_label.grid(row=0, column=0)
        save_button = tk.Button(master=Shared.output_frame,
                                text="Load",
                                command=save_file_callback)
        save_button.grid(row=1, column=0)
        Shared.output_frame.widget_dict = dict()
        Shared.output_frame.widget_dict["output_label"] = output_label
        Shared.output_frame.widget_dict["save_button"] = save_button


def initialise():
    generate_recipe_panels()
    generate_input_frame()
    generate_output_frame()
    Shared.filter_frame_contents = generate_filter_frame()
    print(Shared.input_frame.widget_dict)
