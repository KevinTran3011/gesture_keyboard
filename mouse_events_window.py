import tkinter as tk


class Application(tk.Frame):
    def __init__(self, window_width, window_height, master=None):
        super().__init__(master)  # Call tk.Frame.__init__(master)
        self.master = master

        # Create a frame and place it in the window
        frame = tk.Frame(self.master, width=window_width, height=window_height)
        frame.pack()

        # Create a canvas and place it in the frame
        self.canvas = tk.Canvas(frame, bg='red')
        self.canvas.place(x=100, y=20, width=500, height=240)



if __name__ == '__main__':
    master = tk.Tk()
    window_width = 700
    window_height = 300
    # Define window size
    master.geometry(str(window_width) + 'x' + str(window_height))
    app = Application(window_width, window_height, master=master)
    app.mainloop()
