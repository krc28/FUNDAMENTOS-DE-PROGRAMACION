from tkinter import * 
main_window = Tk()
main_window.title ("Pochinki")
main_frame = Frame (main_window, 
                    bg = "#FF1493", 
                    height = 500 , 
                    width = 500 , 
                    padx = 50 , 
                    pady = 50, 
                    cursor = "arrow")
main_frame.pack()
title_label = Label(main_frame, 
                    text = "Hola soy Pochinki Pochinokona",
                    font= ("Times New Roman", 18),
                    fg = "#FF1493",
                    justify= CENTER)
title_label.pack()
imagen = PhotoImage(file = "EJERCICIOS\pochinki.png")
img_label = Label(main_frame, 
                  image = imagen,
                  bg = "#FF1493")              
img_label.pack()
boton = Button (main_frame,
                text = "Salúdame")
boton.pack()
main_window.mainloop()