from tkinter import Tk, BOTH, Canvas, Text, Scrollbar, RIGHT, Y

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze solver")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        
        # Create a Text widget
        self.text_widget = Text(self.root, wrap="word", width=40, height=10)
        self.text_widget.pack(side="left", fill="both", expand=True)

        # Create a vertical scrollbar
        scrollbar = Scrollbar(self.root, command=self.text_widget.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Associate the scrollbar with the Text widget
        self.text_widget.config(yscrollcommand=scrollbar.set)

        self.running = True
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.root.destroy()

# Instantiate the Window class
win = Window(10, 10)

# Insert some text into the Text widget for demonstration purposes
win.text_widget.insert("1.0", "Test Text")


win.wait_for_close()
