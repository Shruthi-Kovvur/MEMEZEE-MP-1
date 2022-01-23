from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFont
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename

root= Tk()
root.title('MemeZee')
root.geometry('1200x700')

#FIRST FRAME

#Adding background to main frame
load = Image.open('images\\logooo.jpg')
#bg_temp = PhotoImage(file = 'images\\logo.png')
bg_temp = ImageTk.PhotoImage(load)
bg = Label(root,image=bg_temp )
bg.place(x=0,y=0)

#Adding text to main frame
img1= PhotoImage(file = 'images\\logo.png')
t1=Label(root, image=img1,bg='#00015F')
t1.place(x=200,y=175)

def helpbox():
    global Img, img, img_path
    newWindow3 = Toplevel(root)
    newWindow3.title("About")
    newWindow3.geometry("1200x700")
    bg1 = Label(newWindow3, image=bg_temp)
    bg1.place(x=0, y=0)
    message = '''
    Dear User

        Thank you for using Memezee.
        Memezee is an application that helps us to create memes easily.  
        Memezee provides you features like:
        -image editing
        -text editing
        -saving
        It is a very easy and minimal.
         '''

    text_box = Text(
        newWindow3,
        height=12,
        width=100,
        bg='lightblue'
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(state='disabled')

#Function to choose image and Resizing it
def gridfor1():
    global Img, img, img_path
    newWindow = Toplevel(root)
    newWindow.title("Grid for 1")
    newWindow.geometry("1200x700")
    bg1 = Label(newWindow, image=bg_temp)
    bg1.place(x=0, y=0)

    # Creating horizontal bar in NewWindow
    v1 = DoubleVar()
    s1 = Scale(newWindow, variable=v1, from_=0, to=550, orient=HORIZONTAL, length=550,width=20,sliderlength=10,tickinterval=100)
    s1.place(x=100, y=550)

    # Creating vertical bar in NewWindow
    v2 = DoubleVar()
    s2 = Scale(newWindow, variable=v2, from_=0, to=400, orient=VERTICAL, length=400,width=20,sliderlength=10,tickinterval=100)
    s2.place(x=30, y=150)
    #s2.place(x=90,y=100)

    #Creating canvas in Choose Image Window
    global canvas1
    canvas1 = Canvas(newWindow, width=550, height=400, bg='#00015F')
    canvas1.place(x=100,y=150)

    # Functions to paint
    def get_x_and_y(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def paint(event):
        global lasx, lasy
        canvas1.create_line((lasx, lasy, event.x, event.y), fill=(draw1_combo.get()), width=2)
        lasx, lasy = event.x, event.y

    # Function to draw
    def draw():
        canvas1.bind("<Button-1>", get_x_and_y)
        canvas1.bind("<B1-Motion>", paint)


    #Button to Draw
    b5 = Button(newWindow, text="Draw", command= draw, bg='grey', fg='black',font=('ariel 15 bold'))
    b5.place(x=780, y=190)
    draw1 = Label(newWindow, text="Draw Colour:", font=("ariel 14 bold"))
    draw1.place(x=880, y=195)
    values_draw1 = ['red', 'green', 'black', 'yellow', 'pink', 'white']
    draw1_combo = ttk.Combobox(newWindow, values=values_draw1, font=('ariel 10 bold'))
    draw1_combo.place(x=1020, y=198)


    def choose_image1():
        global Img, img, img_path
        img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        Img = ImageTk.PhotoImage(img)
        canvas1.create_image(275, 200, image=Img)
        canvas1.image = Img
        # return Img
    # Button for Choose image
    b4 = Button(newWindow, text="Choose Image", command=choose_image1, bg='grey', fg='black',font=('ariel 15 bold'))
    b4.place(x=890, y=130)

    def Addtext():
        global img_path, img2, img3, img4
        img4 = Image.open(img_path)
        img4 = img4.convert('RGB')
        img4.thumbnail((550, 400))
        text_to_add = Text_entry.get()
        font = font_combo.get()
        myFont = ImageFont.truetype(font + '.ttf', int(fontc_combo.get()))
        img2 = ImageDraw.Draw(img4)
        img2.text((int(xaxis_combo.get()), int(yaxis_combo.get())), text_to_add, (colors_combo.get()), font=myFont)
        # Wait a couple seconds and then show image
        textadd.after(2, show_pic())
        img3 = ImageTk.PhotoImage(img4)
        canvas1.create_image(275, 200, image=img3)
        canvas1.image = img3

    def show_pic():
        # Show New Image
        global img, img_path
        img = PhotoImage(img_path)
        textadd.config(image=img)
        # Clear the entry box
        Text_entry.delete(0, END)

    def brightness(event):
        global img_path, img5, img6
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        for m in range(0, v2.get() + 1):
            imgg = ImageEnhance.Brightness(img)
            img5 = imgg.enhance(m)
            img6 = ImageTk.PhotoImage(img5)
            canvas1.create_image(275, 200, image=img6)
            canvas1.image = img6

    def rotate_image(event):
        global img_path, img7, img8
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img7 = img.rotate(int(rotate_combo.get()))
        img8 = ImageTk.PhotoImage(img7)
        canvas1.create_image(275, 200, image=img8)
        canvas1.image = img8

    def image_border(event):
        global img_path, img9, img10
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img9 = ImageOps.expand(img, border=int(border_combo.get()), fill=(borderr_combo.get()))
        img10 = ImageTk.PhotoImage(img9)
        canvas1.create_image(275, 200, image=img10)
        canvas1.image = img10
    # removes the garbage value
    Img = None
    img3 = None
    img6 = None
    img8 = None
    img10 = None

    def save():
        global img_path ,Img,img2, img3, img4,img5,img7,img6,img8,img9,img10
        # file=None
        ext = img_path.split(".")[-1]
        file = asksaveasfilename(defaultextension=f".{ext}",
                                 filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        if file:
            if canvas1.image == Img:
                img.save(file)
            elif canvas1.image == img6:
                img5.save(file)
            elif canvas1.image == img8:
                img7.save(file)
            elif canvas1.image == img10:
                img9.save(file)
            elif canvas1.image == img3:
                img4.save(file)

    def delete():
        canvas1.delete("all")
    b10 = Button(newWindow, text="Clear", bg='grey', fg='black', font=('ariel 15 bold'), command =delete)
    b10.place(x=1100, y=570)

    bt2 = Button(newWindow, text="Save", width=11, bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=save)
    bt2.place(x=900, y=570)

    btn4 = Button(newWindow, text="Add Text to Image", width=15, bg='grey', fg='black', font=('ariel 15 bold'),command=Addtext)
    btn4.grid(row=730, column=460, padx=670, pady=500)
    btn4.place(x=875, y=515)

    #Text Entry label
    textadd = Label(newWindow, image = img3)
    textadd.grid(row=700, column=460, padx=855, pady=470)
    # entry box
    Text_entry = Entry(newWindow, font=('ariel 15 bold'))
    Text_entry.grid(row=700, column=460, padx=855, pady=470)

    # X axis label
    xaxis= Label(newWindow, text="Xaxis:", font=("ariel 15 bold"))
    xaxis.place(x=965, y=270)
    values_xaxis = [10,50,100,150,200,250,300,350,400]
    xaxis_combo = ttk.Combobox(newWindow, values=values_xaxis, font=('ariel 10 bold'))
    xaxis_combo.place(x=1030,y=277)

    # Y axis label
    yaxis= Label(newWindow, text="Yaxis:", font=("ariel 15 bold"))
    yaxis.place(x=965, y=320)
    values_yaxis = [10,50,100,150,200,250,300,350,400]
    yaxis_combo = ttk.Combobox(newWindow, values=values_yaxis, font=('ariel 10 bold'))
    yaxis_combo.place(x=1030,y=327)

    #TextColour label
    colors= Label(newWindow, text="TextColour:", font=("ariel 15 bold"))
    colors.place(x=670, y=250)
    values_colors=['red','green','black','yellow','pink','white']
    colors_combo=ttk.Combobox(newWindow, values=values_colors, font=('ariel 10 bold'))
    colors_combo.place(x=795,y=257)

    #Font type label
    font= Label(newWindow, text="Text Font:", font=("ariel 15 bold"))
    font.place(x=670, y=350)
    values_font=['arial', 'Courier', 'Helvetica','Segoe Script', 'Times', 'normal', 'roman', 'italic']
    font_combo=ttk.Combobox(newWindow, values=values_font, font=('ariel 10 bold'))
    font_combo.place(x=795,y=357)

    #Font Size label
    fontc= Label(newWindow, text="Text Size:", font=("ariel 15 bold"))
    fontc.place(x=670, y=300)
    values_fontc = [10,14,18,22,26,30,34,38,42,46,50,54,58]
    fontc_combo = ttk.Combobox(newWindow, values=values_fontc, font=('ariel 10 bold'))
    fontc_combo.place(x=795,y=307)

    # Brightness label
    bright = Label(newWindow, text="Brightness:", font=("ariel 15 bold"))
    bright.place(x=640, y=8)
    v2 = IntVar()
    scale2 = ttk.Scale(newWindow, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
    scale2.place(x=770, y=10)

    # Rotate label
    rotate = Label(newWindow, text="Rotate:", font=("ariel 15 bold"))
    rotate.place(x=640, y=58)
    values = [0, 90, 180, 270, 360]
    rotate_combo = ttk.Combobox(newWindow, values=values, font=('ariel 10 bold'))
    rotate_combo.place(x=720, y=60)
    rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

    # Border label
    border = Label(newWindow, text="Add border:", font=("ariel 15 bold"))
    border.place(x=910, y=8)
    values2 = [i for i in range(10, 45, 5)]
    border_combo = ttk.Combobox(newWindow, values=values2, font=("ariel 10 bold"))
    border_combo.place(x=1035, y=10)
    border_combo.bind("<<ComboboxSelected>>", image_border)

    # Border Colour label
    borderr = Label(newWindow, text="BorderColour:", font=("ariel 14 bold"))
    borderr.place(x=890, y=58)
    values_borderr = ['red', 'green', 'black', 'yellow', 'pink', 'white']
    borderr_combo = ttk.Combobox(newWindow, values=values_borderr, font=('ariel 10 bold'))
    borderr_combo.place(x=1035, y=60)

#Function to create grid for 2 horizontal
def gridfor2_horizontal():
    global canvas2,IMG_H,image1_1,image1_2,img_path1_1,img_path1_2
    newWindow1 = Toplevel(root)
    newWindow1.title("Grid for 2")
    newWindow1.geometry("1200x700")
    bg2 = Label(newWindow1, image=bg_temp)
    bg2.place(x=0, y=0)

    v1 = DoubleVar()
    s1 = Scale(newWindow1, variable=v1, from_=0, to=550, orient=HORIZONTAL, length=550,width=20,sliderlength=10,tickinterval=100)
    s1.place(x=100, y=550)

    # Creating vertical bar in NewWindow
    v2 = DoubleVar()
    s2 = Scale(newWindow1, variable=v2, from_=0, to=400, orient=VERTICAL, length=400,width=20,sliderlength=10,tickinterval=100)
    s2.place(x=30, y=150)

    # Function to choose image
    def choose_image2_1():
        global  image1_1, image_path1_1,image1_2, image_path1_2,Img
        img_path1_1 = filedialog.askopenfilename(initialdir=os.getcwd())
        image1_1 = Image.open(img_path1_1)
        img_path1_2 = filedialog.askopenfilename(initialdir=os.getcwd())
        image1_2 = Image.open(img_path1_2)

        # Function to concat images horizontally
        def get_concat_h_resize(image1_1, image1_2, resize_big_image=True):
            global _image1_1, _image1_2, dst

            if image1_1.height == image1_2.height:
                _image1_1 = image1_1
                _image1_2 = image1_2
            elif (((image1_1.height > image1_2.height) and resize_big_image) or
                  ((image1_1.height < image1_2.height) and not resize_big_image)):
                _image1_1 = image1_1.resize((int(image1_1.width * image1_2.height / image1_1.height), image1_2.height),
                                            Image.BICUBIC)
                _image1_2 = image1_2
            else:
                _image1_1 = image1_1
                _image1_2 = image1_2.resize((int(image1_2.width * image1_1.height / image1_2.height), image1_1.height),
                                            Image.BICUBIC)
            dst = Image.new('RGB', (_image1_1.width + _image1_2.width, _image1_1.height))
            dst.paste(_image1_1, (0, 0))
            dst.paste(_image1_2, (_image1_1.width, 0))
            return dst

        # Concating 2 images and Adding it to canvas which is created here itslef
        get_concat_h_resize(image1_1, image1_2, resize_big_image=True).save('images\\pillow_concat_h_resize.jpg')
        IMG_H = Image.open('images\\pillow_concat_h_resize.jpg')
        IMG_H.thumbnail((550, 400))
        Img = ImageTk.PhotoImage(IMG_H)
        canvas2.create_image(275, 200, image=Img)
        canvas2.image = Img

    canvas2 = Canvas(newWindow1, width=550, height=400, bg='#00015F')
    canvas2.place(x=100, y=150)

    # Button for Choose image1
    b7 = Button(newWindow1, text="Choose Image\ntwice", command=choose_image2_1, bg='grey', fg='black',
                font=('ariel 15 bold'))
    b7.place(x=890, y=120)
    def get_x_and_y(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def paint(event):
        global lasx, lasy,img11,img_path, img12,img
        img_path = 'images\\pillow_concat_h_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img11=canvas2.create_line((lasx, lasy, event.x, event.y), fill=(draw1_combo.get()), width=2)
        lasx, lasy = event.x, event.y
        img12 = ImageTk.PhotoImage(img11)
        canvas2.create_image(275, 200, image=img12)
        canvas2.image = img12

    # Function to draw
    def draw():
        canvas2.bind("<Button-1>", get_x_and_y)
        canvas2.bind("<B1-Motion>", paint)

    #Button to Draw
    b5 = Button(newWindow1, text="Draw", command= draw, bg='grey', fg='black',font=('ariel 15 bold'))
    b5.place(x=780, y=190)
    draw1 = Label(newWindow1, text="Draw Colour:", font=("ariel 14 bold"))
    draw1.place(x=880, y=195)
    values_draw1 = ['red', 'green', 'black', 'yellow', 'pink', 'white']
    draw1_combo = ttk.Combobox(newWindow1, values=values_draw1, font=('ariel 10 bold'))
    draw1_combo.place(x=1020, y=198)

    def Addtext():
        global img_path, img2, img3, img4
        img_path='images\\pillow_concat_h_resize.jpg'
        img4 = Image.open(img_path)
        img4 = img4.convert('RGB')
        img4.thumbnail((550, 400))
        text_to_add = Text_entry.get()
        font = font_combo.get()
        myFont = ImageFont.truetype(font + '.ttf', int(fontc_combo.get()))
        img2 = ImageDraw.Draw(img4)
        img2.text((int(xaxis_combo.get()), int(yaxis_combo.get())), text_to_add, (colors_combo.get()), font=myFont)
        # Wait a couple seconds and then show image
        textadd.after(2, show_pic())
        img3 = ImageTk.PhotoImage(img4)
        canvas2.create_image(275, 200, image=img3)
        canvas2.image = img3

    def show_pic():
        # Show New Image
        global img, img_path
        img = PhotoImage(img_path)
        textadd.config(image=img)
        # Clear the entry box
        Text_entry.delete(0, END)

    def brightness(event):
        global img_path, img5, img6
        img_path = 'images\\pillow_concat_h_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        for m in range(0, v2.get() + 1):
            imgg = ImageEnhance.Brightness(img)
            img5 = imgg.enhance(m)
            img6 = ImageTk.PhotoImage(img5)
            canvas2.create_image(275, 200, image=img6)
            canvas2.image = img6

    def rotate_image(event):
        global img_path, img7, img8
        img_path = 'images\\pillow_concat_h_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img7 = img.rotate(int(rotate_combo.get()))
        img8 = ImageTk.PhotoImage(img7)
        canvas2.create_image(275, 200, image=img8)
        canvas2.image = img8

    def image_border(event):
        global img_path, img9, img10
        img_path = 'images\\pillow_concat_h_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img9 = ImageOps.expand(img, border=int(border_combo.get()), fill=(borderr_combo.get()))
        img10 = ImageTk.PhotoImage(img9)
        canvas2.create_image(275, 200, image=img10)
        canvas2.image = img10
    # removes the garbage value
    Img = None
    img3 = None
    img6 = None
    img8 = None
    img10 = None
    img12= None

    def save():
        global img_path ,Img,img2, img3, img4,img5,img7,img6,img8,img9,img10,img11,img12
        img_path = 'images\\pillow_concat_h_resize.jpg'
        # file=None
        ext = img_path.split(".")[-1]
        file = asksaveasfilename(defaultextension=f".{ext}",
                                 filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        if file:
            if canvas2.image == Img:
                img.save(file)
            elif canvas2.image == img6:
                img5.save(file)
            elif canvas2.image == img8:
                img7.save(file)
            elif canvas2.image == img10:
                img9.save(file)
            elif canvas2.image == img3:
                img4.save(file)
            elif canvas2.image == img12:
                img11.save(file)

    def delete():
        canvas2.delete("all")
    b10 = Button(newWindow1, text="Clear", bg='grey', fg='black', font=('ariel 15 bold'), command =delete)
    b10.place(x=1100, y=570)

    bt2 = Button(newWindow1, text="Save", width=11, bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=save)
    bt2.place(x=900, y=570)

    btn4 = Button(newWindow1, text="Add Text to Image", width=15, bg='grey', fg='black', font=('ariel 15 bold'),command=Addtext)
    btn4.grid(row=730, column=460, padx=670, pady=500)
    btn4.place(x=875, y=515)

    #Text Entry label
    textadd = Label(newWindow1, image = img3)
    textadd.grid(row=700, column=460, padx=855, pady=470)
    # entry box
    Text_entry = Entry(newWindow1, font=('ariel 15 bold'))
    Text_entry.grid(row=700, column=460, padx=855, pady=470)

    # X axis label
    xaxis= Label(newWindow1, text="Xaxis:", font=("ariel 15 bold"))
    xaxis.place(x=965, y=270)
    values_xaxis = [10,50,100,150,200,250,300,350,400]
    xaxis_combo = ttk.Combobox(newWindow1, values=values_xaxis, font=('ariel 10 bold'))
    xaxis_combo.place(x=1030,y=277)

    # Y axis label
    yaxis= Label(newWindow1, text="Yaxis:", font=("ariel 15 bold"))
    yaxis.place(x=965, y=320)
    values_yaxis = [10,50,100,150,200,250,300,350,400]
    yaxis_combo = ttk.Combobox(newWindow1, values=values_yaxis, font=('ariel 10 bold'))
    yaxis_combo.place(x=1030,y=327)

    #TextColour label
    colors= Label(newWindow1, text="TextColour:", font=("ariel 15 bold"))
    colors.place(x=670, y=250)
    values_colors=['red','green','black','yellow','pink','white']
    colors_combo=ttk.Combobox(newWindow1, values=values_colors, font=('ariel 10 bold'))
    colors_combo.place(x=795,y=257)

    #Font type label
    font= Label(newWindow1, text="Text Font:", font=("ariel 15 bold"))
    font.place(x=670, y=350)
    values_font=['arial', 'Courier', 'Helvetica','Segoe Script', 'Times', 'normal', 'roman', 'italic']
    font_combo=ttk.Combobox(newWindow1, values=values_font, font=('ariel 10 bold'))
    font_combo.place(x=795,y=357)

    #Font Size label
    fontc= Label(newWindow1, text="Text Size:", font=("ariel 15 bold"))
    fontc.place(x=670, y=300)
    values_fontc = [10,14,18,22,26,30,34,38,42,46,50,54,58]
    fontc_combo = ttk.Combobox(newWindow1, values=values_fontc, font=('ariel 10 bold'))
    fontc_combo.place(x=795,y=307)

    # Brightness label
    bright = Label(newWindow1, text="Brightness:", font=("ariel 15 bold"))
    bright.place(x=640, y=8)
    v2 = IntVar()
    scale2 = ttk.Scale(newWindow1, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
    scale2.place(x=770, y=10)

    # Rotate label
    rotate = Label(newWindow1, text="Rotate:", font=("ariel 15 bold"))
    rotate.place(x=640, y=58)
    values = [0, 90, 180, 270, 360]
    rotate_combo = ttk.Combobox(newWindow1, values=values, font=('ariel 10 bold'))
    rotate_combo.place(x=720, y=60)
    rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

    # Border label
    border = Label(newWindow1, text="Add border:", font=("ariel 15 bold"))
    border.place(x=910, y=8)
    values2 = [i for i in range(10, 45, 5)]
    border_combo = ttk.Combobox(newWindow1, values=values2, font=("ariel 10 bold"))
    border_combo.place(x=1035, y=10)
    border_combo.bind("<<ComboboxSelected>>", image_border)

    # Border Colour label
    borderr = Label(newWindow1, text="BorderColour:", font=("ariel 14 bold"))
    borderr.place(x=890, y=58)
    values_borderr = ['red', 'green', 'black', 'yellow', 'pink', 'white']
    borderr_combo = ttk.Combobox(newWindow1, values=values_borderr, font=('ariel 10 bold'))
    borderr_combo.place(x=1035, y=60)
    border_combo.bind("<<ComboboxSelected>>", image_border)

#grid for 2 images
def gridfor2_vertical():
    global canvas3,IMG_V,im1,im2,img_path1_1,img_path1_2,Img
    newWindow2 = Toplevel(root)
    newWindow2.title("Grid for 2")
    newWindow2.geometry("1200x700")
    bg2 = Label(newWindow2, image=bg_temp)
    bg2.place(x=0, y=0)

    v1 = DoubleVar()
    s1 = Scale(newWindow2, variable=v1, from_=0, to=550, orient=HORIZONTAL, length=550, width=20, sliderlength=10,
               tickinterval=100)
    s1.place(x=100, y=550)

    # Creating vertical bar in NewWindow
    v2 = DoubleVar()
    s2 = Scale(newWindow2, variable=v2, from_=0, to=400, orient=VERTICAL, length=400, width=20, sliderlength=10,
               tickinterval=100)
    s2.place(x=30, y=150)
    # Function to choose image
    def choose_image2_2():
        global  im1, image_path1_1,im2, image_path1_2
        img_path1_1 = filedialog.askopenfilename(initialdir=os.getcwd())
        im1 = Image.open(img_path1_1)
        img_path1_2 = filedialog.askopenfilename(initialdir=os.getcwd())
        im2 = Image.open(img_path1_2)

        def get_concat_v_resize(im1, im2 , resize_big_image=True):
            if im1.width == im2.width:
                _im1 = im1
                _im2 = im2
            elif (((im1.width > im2.width) and resize_big_image) or
                  ((im1.width < im2.width) and not resize_big_image)):
                _im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), Image.BICUBIC)
                _im2 = im2
            else:
                _im1 = im1
                _im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), Image.BICUBIC)
            dst = Image.new('RGB', (_im1.width, _im1.height + _im2.height))
            dst.paste(_im1, (0, 0))
            dst.paste(_im2, (0, _im1.height))
            return dst

        get_concat_v_resize(im1, im2, resize_big_image=True).save('images\\pillow_concat_v_resize.jpg')
        IMG_V = Image.open('images\\pillow_concat_v_resize.jpg')
        IMG_V.thumbnail((550, 400))
        Img = ImageTk.PhotoImage(IMG_V)
        canvas3.create_image(275, 200, image=Img)
        canvas3.image = Img
    #creating canvas
    canvas3 = Canvas(newWindow2, width=550, height=400, bg='#00015F')
    canvas3.place(x=100, y=150)

    # Button for Choose image
    b8 = Button(newWindow2, text="Choose Image\ntwice", command=choose_image2_2, bg='grey', fg='black',
                    font=('ariel 15 bold'))
    b8.place(x=890, y=120)

    def get_x_and_y(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def paint(event):
        global lasx, lasy,img11,img_path, img12,img
        img_path = 'images\\pillow_concat_v_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img11=canvas3.create_line((lasx, lasy, event.x, event.y), fill=(draw1_combo.get()), width=2)
        lasx, lasy = event.x, event.y
        img12 = ImageTk.PhotoImage(img11)
        canvas3.create_image(275, 200, image=img12)
        canvas2.image = img12

    # Function to draw
    def draw():
        canvas3.bind("<Button-1>", get_x_and_y)
        canvas3.bind("<B1-Motion>", paint)

    #Button to Draw
    b5 = Button(newWindow2, text="Draw", command= draw, bg='grey', fg='black',font=('ariel 15 bold'))
    b5.place(x=780, y=190)
    draw1 = Label(newWindow2, text="Draw Colour:", font=("ariel 14 bold"))
    draw1.place(x=880, y=195)
    values_draw1 = ['red', 'green', 'black', 'yellow', 'pink', 'white']
    draw1_combo = ttk.Combobox(newWindow2, values=values_draw1, font=('ariel 10 bold'))
    draw1_combo.place(x=1020, y=198)

    def Addtext():
        global img_path, img2, img3, img4
        img_path='images\\pillow_concat_v_resize.jpg'
        img4 = Image.open(img_path)
        img4 = img4.convert('RGB')
        img4.thumbnail((550, 400))
        text_to_add = Text_entry.get()
        font = font_combo.get()
        myFont = ImageFont.truetype(font + '.ttf', int(fontc_combo.get()))
        img2 = ImageDraw.Draw(img4)
        img2.text((int(xaxis_combo.get()), int(yaxis_combo.get())), text_to_add, (colors_combo.get()), font=myFont)
        # Wait a couple seconds and then show image
        textadd.after(2, show_pic())
        img3 = ImageTk.PhotoImage(img4)
        canvas3.create_image(275, 200, image=img3)
        canvas3.image = img3

    def show_pic():
        # Show New Image
        global img, img_path
        img = PhotoImage(img_path)
        textadd.config(image=img)
        # Clear the entry box
        Text_entry.delete(0, END)

    def brightness(event):
        global img_path, img5, img6
        img_path = 'images\\pillow_concat_v_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        for m in range(0, v2.get() + 1):
            imgg = ImageEnhance.Brightness(img)
            img5 = imgg.enhance(m)
            img6 = ImageTk.PhotoImage(img5)
            canvas3.create_image(275, 200, image=img6)
            canvas3.image = img6

    def rotate_image(event):
        global img_path, img7, img8
        img_path = 'images\\pillow_concat_v_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img7 = img.rotate(int(rotate_combo.get()))
        img8 = ImageTk.PhotoImage(img7)
        canvas3.create_image(275, 200, image=img8)
        canvas3.image = img8

    def image_border(event):
        global img_path, img9, img10
        img_path = 'images\\pillow_concat_v_resize.jpg'
        img = Image.open(img_path)
        img.thumbnail((550, 400))
        img9 = ImageOps.expand(img, border=int(border_combo.get()), fill=(borderr_combo.get()))
        img10 = ImageTk.PhotoImage(img9)
        canvas3.create_image(275, 200, image=img10)
        canvas3.image = img10

    # removes the garbage value
    Img = None
    img3 = None
    img6 = None
    img8 = None
    img10 = None
    img12= None

    def save():
        global img_path ,Img,img2, img3, img4,img5,img7,img6,img8,img9,img10,img11,img12
        img_path = 'images\\pillow_concatv_resize.jpg'
        # file=None
        ext = img_path.split(".")[-1]
        file = asksaveasfilename(defaultextension=f".{ext}",
                                 filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        if file:
            if canvas3.image == Img:
                img.save(file)
            elif canvas3.image == img6:
                img5.save(file)
            elif canvas3.image == img8:
                img7.save(file)
            elif canvas3.image == img10:
                img9.save(file)
            elif canvas3.image == img3:
                img4.save(file)
            elif canvas3.image == img12:
                img11.save(file)

    def delete():
        canvas3.delete("all")
    #buttons to window1
    bt2 = Button(newWindow2, text="Save", width=11, bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=save)
    bt2.place(x=900, y=570)

    btn4 = Button(newWindow2, text="Add Text to Image", width=15, bg='grey', fg='black', font=('ariel 15 bold'),command=Addtext)
    btn4.grid(row=730, column=460, padx=670, pady=500)
    btn4.place(x=875, y=515)

    b10 = Button(newWindow2, text="Clear", bg='grey', fg='black', font=('ariel 15 bold'), command =delete)
    b10.place(x=1100, y=570)

    #Text Entry label
    textadd = Label(newWindow2, image = img3)
    textadd.grid(row=700, column=460, padx=855, pady=470)
    # entry box
    Text_entry = Entry(newWindow2, font=('ariel 15 bold'))
    Text_entry.grid(row=700, column=460, padx=855, pady=470)

    # X axis label
    xaxis= Label(newWindow2, text="Xaxis:", font=("ariel 15 bold"))
    xaxis.place(x=965, y=270)
    values_xaxis = [10,50,100,150,200,250,300,350,400]
    xaxis_combo = ttk.Combobox(newWindow2, values=values_xaxis, font=('ariel 10 bold'))
    xaxis_combo.place(x=1030,y=277)

    # Y axis label
    yaxis= Label(newWindow2, text="Yaxis:", font=("ariel 15 bold"))
    yaxis.place(x=965, y=320)
    values_yaxis = [10,50,100,150,200,250,300,350,400]
    yaxis_combo = ttk.Combobox(newWindow2, values=values_yaxis, font=('ariel 10 bold'))
    yaxis_combo.place(x=1030,y=327)

    #TextColour label
    colors= Label(newWindow2, text="TextColour:", font=("ariel 15 bold"))
    colors.place(x=670, y=250)
    values_colors=['red','green','black','yellow','pink','white']
    colors_combo=ttk.Combobox(newWindow2, values=values_colors, font=('ariel 10 bold'))
    colors_combo.place(x=795,y=257)

    #Font type label
    font= Label(newWindow2, text="Text Font:", font=("ariel 15 bold"))
    font.place(x=670, y=350)
    values_font=['arial', 'Courier', 'Helvetica','Segoe Script', 'Times', 'normal', 'roman', 'italic']
    font_combo=ttk.Combobox(newWindow2, values=values_font, font=('ariel 10 bold'))
    font_combo.place(x=795,y=357)

    #Font Size label
    fontc= Label(newWindow2, text="Text Size:", font=("ariel 15 bold"))
    fontc.place(x=670, y=300)
    values_fontc = [10,14,18,22,26,30,34,38,42,46,50,54,58]
    fontc_combo = ttk.Combobox(newWindow2, values=values_fontc, font=('ariel 10 bold'))
    fontc_combo.place(x=795,y=307)

    # Brightness label
    bright = Label(newWindow2, text="Brightness:", font=("ariel 15 bold"))
    bright.place(x=640, y=8)
    v2 = IntVar()
    scale2 = ttk.Scale(newWindow2, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
    scale2.place(x=770, y=10)

    # Rotate label
    rotate = Label(newWindow2, text="Rotate:", font=("ariel 15 bold"))
    rotate.place(x=640, y=58)
    values = [0, 90, 180, 270, 360]
    rotate_combo = ttk.Combobox(newWindow2, values=values, font=('ariel 10 bold'))
    rotate_combo.place(x=720, y=60)
    rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

    # Border label
    border = Label(newWindow2, text="Add border:", font=("ariel 15 bold"))
    border.place(x=910, y=8)
    values2 = [i for i in range(10, 45, 5)]
    border_combo = ttk.Combobox(newWindow2, values=values2, font=("ariel 10 bold"))
    border_combo.place(x=1035, y=10)
    border_combo.bind("<<ComboboxSelected>>", image_border)

    # Border Colour label
    borderr = Label(newWindow2, text="BorderColour:", font=("ariel 14 bold"))
    borderr.place(x=890, y=58)
    values_borderr = ['red', 'green', 'black', 'yellow', 'pink', 'white']
    borderr_combo = ttk.Combobox(newWindow2, values=values_borderr, font=('ariel 10 bold'))
    borderr_combo.place(x=1035, y=60)
    border_combo.bind("<<ComboboxSelected>>", image_border)


#Adding Buttons to 1st frame
b1 =Button(root,text="Meme For 1 Picture", bg='grey', fg='black', font=('ariel 15 bold'), command= gridfor1)
b1.place(x=175,y=360)
b2 =Button(root,text="Meme For 2 Pictures\nHorizontal", bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE,command= gridfor2_horizontal)
b2.place(x=550,y=350)
b3 =Button(root,text="Meme For 2 Pictures\nVertical", bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE,command= gridfor2_vertical)
b3.place(x=950,y=350)
b9 = Button(root, text="Exit", width=11, bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE,
              command=root.destroy)
b9.place(x=1030, y=570)
b6 =Button(root,text="About", bg='grey', fg='black', font=('ariel 15 bold'), relief=GROOVE,command=helpbox)
b6.place(x=920,y=570)

root.mainloop()