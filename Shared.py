import tkinter as tk

root = tk.Tk()
input_frame = tk.Frame(master=root)
output_frame = tk.Frame(master=root)
filter_frame = tk.Frame(master=root)
sequence_frame = tk.Frame(master=root)
input_frame.grid(row=0, column=0)
output_frame.grid(row=0, column=1)
filter_frame.grid(row=1, column=0, columnspan=2)
sequence_frame.grid(row=0, column=2, rowspan=2)
recipe_panels = dict()
current_selected_filter = None

input_im = None
input_imtk = None
output_im = None
output_imtk = None
load_filename = None
save_filename = None
sequence_mode = False
