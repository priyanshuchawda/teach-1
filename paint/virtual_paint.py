import tkinter as tk
from tkinter.colorchooser import askcolor


class VirtualPaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Paint")
        
        # Canvas setup
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Current settings
        self.current_color = "black"
        self.brush_size = 5
        
        # Bind events
        self.canvas.bind("<B1-Motion>", self.paint)
        
        # Tools frame
        self.tools_frame = tk.Frame(root)
        self.tools_frame.pack(fill=tk.X)
        
        # Buttons
        color_button = tk.Button(self.tools_frame, text="Choose Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(self.tools_frame, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        size_label = tk.Label(self.tools_frame, text="Brush Size:")
        size_label.pack(side=tk.LEFT, padx=5)
        
        self.size_slider = tk.Scale(self.tools_frame, from_=1, to=20, orient=tk.HORIZONTAL)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT, padx=5)

    def choose_color(self):
        color = askcolor()[1]
        if color:
            self.current_color = color

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, outline=self.current_color)

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualPaintApp(root)
    root.mainloop()

