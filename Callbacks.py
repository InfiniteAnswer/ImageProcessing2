import Shared, LayoutConfig
import cv2
from PIL import Image, ImageTk


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


def load_file_callback():
    load_image()
    Shared.input_frame.widget_dict["input_label"].config(image=Shared.input_imtk)


def save_file_callback():
    pass


def load_image():
    im = cv2.imread(Shared.load_filename, -1)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    Shared.input_im = im_gray
    Shared.input_imtk = convert_to_tkImage(Shared.input_im)
    print("File loaded and converted")


def convert_to_tkImage(im):
    height, width = im.shape
    im_scale_factor = LayoutConfig.IMAGE_DISPLAY_WIDTH / width
    newX, newY = im.shape[1]*im_scale_factor, im.shape[0]*im_scale_factor
    scaled_image = cv2.resize(im, (int(newX), int(newY)))
    im_array = Image.fromarray(scaled_image)
    im_tk = ImageTk.PhotoImage(image=im_array)
    return  im_tk