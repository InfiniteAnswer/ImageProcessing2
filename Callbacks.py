import Shared


def callback1():
    print("callback1 complete")
    return True


def callback2():
    print("callback2 complete")
    return True


def trace_handler(name):
    print("name: ", name)
    Shared.recipe_panels[name].callback()


def filter_update_handler(name):
    Shared.recipe_panels[name].callback()


def add_button_callback():
    pass


def use_output_as_input_callback():
    pass


def mode_callback():
    pass
