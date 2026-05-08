from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title('Image Slideshow Viewer')

Image_path = [
    r"C:\Users\I AM WEB DEVELOPER\Downloads\sam-moghadam-cU5TUyEaZXQ-unsplash.jpg",
    r"C:\Users\I AM WEB DEVELOPER\Downloads\dery-triyatna-nx_se_oS8fc-unsplash.jpg",
    r"C:\Users\I AM WEB DEVELOPER\Downloads\marlene-celine-nordvik-zh7pqPE8gCc-unsplash.jpg",
    r"C:\Users\I AM WEB DEVELOPER\Downloads\octavio-fossatti-wW177LpJYV0-unsplash.jpg",
    r"C:\Users\I AM WEB DEVELOPER\Downloads\elisabeth-arnold-iax-dra8eco-unsplash.jpg"
]

image_size = (600, 400)

# images load
images = []

for path in Image_path:
    image = Image.open(path)
    image = image.resize(image_size)
    photo = ImageTk.PhotoImage(image)
    images.append(photo)

# cycle for slideshow
slideshow = cycle(images)

# label
label = tk.Label(root)
label.pack(pady=20)

def update_photo():
    photo = next(slideshow)

    label.config(image=photo)
    label.image = photo

    root.after(3000, update_photo)

def start_slideshow():
    update_photo()

play_button = tk.Button(
    root,
    text="Play Slideshow",
    command=start_slideshow
)

play_button.pack()

root.mainloop()

