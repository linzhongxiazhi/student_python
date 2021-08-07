from tkinter import *
import tkinter.messagebox

def middle(width, height):
    system_metrics = get_system_metrics()
    window_x_position = (system_metrics[0] - width) // 2
    window_y_position = (system_metrics[1] - height) // 2
    return window_x_position, window_y_position


