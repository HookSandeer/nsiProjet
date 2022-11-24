#!########################## TKINTER :
# Create new tkinter windows
win = Tk()
win.title("Le jeu dont vous êtes le héro")
win.geometry("1280x720")

# Load the background image in the script:
imageBackground = PhotoImage(file = "imageWallpaper.png")

# Place the image in background
wallpaper = Label(win, image=imageBackground)
wallpaper.place(x = 0, y = 0)

# Console indication texte :

displayedtext = Label(win, text="Votre aventure => ", font=("Arial", 15), fg='black')
displayedtext.place(x=0, y=360)

# Create Text Zone 
dialogue = Text(win, width=80, height=8, font=("Arial", 15), bg='white', fg='black',)
dialogue.place(x=200, y=360)

# Create Next Button
nextButton = Button(win, text="Continuer ...", command=nextButton)
nextButton.place(x=0, y=400)

# Start Button :
startButton = Button(win, text="Commencer ...", command=startButton)
startButton.place(x=0, y=440)

# Text Animation


# Start the new tkinter windows
win.mainloop()
