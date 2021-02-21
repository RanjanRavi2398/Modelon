import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg


sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]


frame_layout=[
    [sg.T('Select Your option')],
    [sg.CB('Source Supply'),sg.CB('Transformation'),sg.CB('Consumption')],]


layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Energy Sankey Diagram', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text(' Select Your files or folders')],
   
    [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FileBrowse(file_types=(("", "*.mat"),))],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()],
    [sg.Listbox(values=('Coal','Petroleum','Nuclear','Renewable','Residential','Commercial','Industrial','Transportation'),size=(40,5)),sg.Frame('UserDefined Options',frame_layout,font='Any 14',title_color='red')],
    [sg.Ok()
   ],
    
    [sg.Text('_' * 80)],
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")]]
    

window = sg.Window('Modelon', layout, default_element_size=(90, 1), grab_anywhere=False,location=(3, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",)
draw_figure(window["-CANVAS-"].TKCanvas, fig)
event, values = window.read()
window.close()


sg.Popup('Title','The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)
