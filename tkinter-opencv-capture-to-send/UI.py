import tkinter as tk  # python 3
from tkinter import font as tkfont
from tkinter.constants import BOTH  # python 3
import photoCapture
import sendMail


class CaptureToSend(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.capturedImageName = ""

        self.title_font = tkfont.Font(
            family="Helvetica", size=18, weight="bold", slant="italic"
        )

        width = 400
        height = 300

        # get screen width and height
        screenWidth = self.winfo_screenwidth()  # width of the screen
        screenHeight = self.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = int((screenWidth / 2) - (width / 2))
        y = int((screenHeight / 2) - (height / 2))

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.title("Capture & Send")

        self.attributes("-topmost", True)
        self.update()
        self.attributes("-topmost", False)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # for F in (StartPage, PageOne, PageTwo):
        for F in (StartPage, SendPhotoToEmail):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, imageName=""):
        """Show a frame for the given page name"""
        if imageName != "":
            print(imageName)
            self.capturedImageName = imageName
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=300, pady=75)
        self.controller = controller
        label = tk.Label(
            self,
            text="Capture & Send",
            font=controller.title_font
        )
        label.pack(side="top", fill=BOTH, pady=10)

        # button1 = tk.Button(self, text="Start",
        # command = lambda: controller.show_frame("SendPhotoToEmail"))
        button1 = tk.Button(
            self,
            text="Start",
            command=lambda: photoCapture.photoCapture(self.controller),
        )

        # button2 = tk.Button(self, text="Go to Page Two",
        # command = lambda: controller.show_frame("PageTwo"))
        button1.pack()
        # button2.pack()


class SendPhotoToEmail(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=400, height=300, pady=75)
        self.controller = controller
        label = tk.Label(self, text="Send Photo", font=controller.title_font)
        label.pack(side="top", fill=BOTH, pady=10)

        emailInput = tk.Text(self, height=1, width=40)
        emailInput.pack(side="top", pady=20)

        button = tk.Button(
            self,
            text="Send",
            command=lambda: sendCapturedImage(emailInput, self.controller),
        )
        button.pack()


def sendCapturedImage(emailInput, app):
    receiverEmail = emailInput.get("1.0", "end-1c")
    emailInput.delete("1.0", "end-1c")
    app.show_frame("StartPage", app.capturedImageName)
    sendMail.sendMail(receiverEmail, app.capturedImageName)
