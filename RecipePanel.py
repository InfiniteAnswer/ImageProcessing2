from Callbacks import *


class RecipePanel:
    def __init__(self, name, frame, callback, slider_list, variable_list):
        self.name = name
        self.frame = frame
        self.callback = callback
        self.slider_list = slider_list
        self.variable_list = variable_list
