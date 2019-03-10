import tkinter as tk
from LayoutConfig import *


def create_root():
    root = tk.Tk()
    input_frame = tk.Frame(master=root)
    input_frame.grid(row=0, column=0)
    return root


def create_output_frame():
    output_frame = tk.Frame(master=root)
    output_frame.grid(row=0, column=1)
    return output_frame


def create_filter_frame():
    filter_frame = tk.LabelFrame(master=root,
                                 text="Filters",
                                 width=WIDTH_FILTER_FRAME,
                                 height=HEIGHT_FILTER_FRAME)
    filter_frame.grid(row=1, column=0, columnspan=2)
    filter_frame.columnconfigure(0, minsize=WIDTH_FILTER_LISTBOX)
    filter_frame.columnconfigure(1, minsize=WIDTH_FILTER_CONTROL_FRAME)
    filter_frame.columnconfigure(2, minsize=WIDTH_FILTER_SLIDER_FRAME)
    filter_frame.grid_propagate(0)
    return filter_frame


def create_sequence_frame():
    sequence_frame = tk.LabelFrame(master=root,
                                   text="Sequence",
                                   width=WIDTH_SEQUENCE_FRAME,
                                   height=HEIGHT_MAIN_WINDOW)
    sequence_frame.grid(row=0, column=2, rowspan=2)
    sequence_frame.columnconfigure(0, minsize=WIDTH_SEQUENCE_FRAME)
    sequence_frame.grid_propagate(0)
    return sequence_frame


root = create_root()
output_frame = create_output_frame()
filter_frame = create_filter_frame()
sequence_frame = create_sequence_frame()

filter_frame_contents = None

recipe_panels = dict()

current_selected_filter = None

input_im = None
input_imtk = None
output_im = None
output_imtk = None
load_filename = None
save_filename = None
sequence_mode = False
