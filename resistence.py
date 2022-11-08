from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("Resistence Calculator")
root.iconbitmap(r'resistor.ico')
root.resizable(width = False, height = False)
root.geometry("565x620+150+150")

Resistence = Frame(root)
Resistence.grid()


operator  = ''
text_input = StringVar()
text_input1 = StringVar()


def buttonclick(numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator)
	text_input1.set(operator)

def btnClear():
    global operator
    operator = ''
    text_input.set('0')
    text_input1.set('0')	
    Ohm_DisplayΩ = Label(Resistence,text = "Ω    +" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W, 
					bg = "skyblue",fg = "black", ).grid(row = 13, column = 4 , pady = 1 )
    Ohm1_DisplayΩ = Label(Resistence,text = "Ω   —" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W, 
					bg = "skyblue",fg = "black", ).grid(row = 14, column = 4 , pady = 1 )


def multiplier(num):
	firstnum = int(Ohm_Display.get())
	result = firstnum * num 
	rounded_result = round(result , 6)
	text_input.set(rounded_result)
	text_input1.set(rounded_result)	
	
def tolreance(num1):
	current_result = float(Ohm_Display.get())
	the_mistake = current_result * (num1 / 100)
	rounded_mistake = round(the_mistake , 6)
	final_result = rounded_mistake + current_result
	rounded_final_result = round(final_result , 3)
	Minus_final_result2 = current_result - rounded_mistake
	rounded_Minus_final_result2 = round(Minus_final_result2 , 3)
	
	if rounded_final_result > 1000000:
		final_result1 = rounded_final_result / 1000000
		rounded_final_result1 = round(final_result1 , 8)
		final_result2 = rounded_Minus_final_result2 / 1000000
		rounded_final_result2 = round(final_result2 , 8)
		Ohm_DisplayΩ = Label(Resistence,text = "MΩ   +" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W , 
					bg = "skyblue",fg = "black", ).grid(row = 13, column = 4 , pady = 1 )
		Ohm1_DisplayΩ = Label(Resistence,text = "MΩ  —" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W, 
					bg = "skyblue",fg = "black", ).grid(row = 14, column = 4 , pady = 1 )
		text_input.set(rounded_final_result1)
		text_input1.set(rounded_final_result2)

	elif rounded_final_result > 1000:
		final_result1 = rounded_final_result / 1000
		rounded_final_result1 = round(final_result1 , 6)
		final_result2 = rounded_Minus_final_result2 / 1000
		rounded_final_result2 = round(final_result2 , 6)
		Ohm_DisplayΩ = Label(Resistence,text = "KΩ   +" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W , 
					bg = "skyblue",fg = "black", ).grid(row = 13, column = 4 , pady = 1 )
		Ohm1_DisplayΩ = Label(Resistence,text = "KΩ  —" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W, 
					bg = "skyblue",fg = "black", ).grid(row = 14, column = 4 , pady = 1 )
		text_input.set(rounded_final_result1)
		text_input1.set(rounded_final_result2)	

	else:
		text_input.set(rounded_final_result)
		text_input1.set(rounded_Minus_final_result2)
	

		

# THIS IS THE FIRST BAND WITH IT'S COLORS==========================================================================

Band1_display = Label(Resistence,text = " First line " , width = 10 , height = 2 , font = ('arial',13,'bold') ,
							 bg = "skyblue" , fg = "black" ).grid(row = 0 , column = 0 , pady = 1 , padx = 5)

btn_black1 = Button(Resistence,text ="Black",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "black" ,fg = "white",command = lambda:buttonclick(0) ).grid(row = 1 , column = 0 , pady = 1 ) 

btn_brown1 = Button(Resistence,text ="Brown",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "brown" ,fg = "black",command = lambda:buttonclick(1) ).grid(row = 2 , column = 0 , pady = 1 )

btn_red1 = Button(Resistence,text ="Red",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "red" ,fg = "black",command = lambda:buttonclick(2) ).grid(row = 3 , column = 0 , pady = 1 )

btn_orange1 = Button(Resistence,text ="Orange",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "orange" ,fg = "black",command = lambda:buttonclick(3) ).grid(row = 4 , column = 0 , pady = 1 )

btn_yellow1 = Button(Resistence,text ="Yellow",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "yellow" ,fg = "black",command = lambda:buttonclick(4) ).grid(row = 5 , column = 0 , pady = 1 )

btn_green1 = Button(Resistence,text ="Green",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "green" ,fg = "black",command = lambda:buttonclick(5) ).grid(row = 6 , column = 0 , pady = 1 )

btn_blue1 = Button(Resistence,text ="Blue",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "blue" ,fg = "white",command = lambda:buttonclick(6) ).grid(row = 7 , column = 0 , pady = 1 )

btn_violet1 = Button(Resistence,text ="Violet",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "violet" ,fg = "black",command = lambda:buttonclick(7) ).grid(row = 8 , column = 0 , pady = 1 )

btn_grey1 = Button(Resistence,text ="Grey",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "grey" ,fg = "black",command = lambda:buttonclick(8) ).grid(row = 9 , column = 0 , pady = 1 )

btn_white1 = Button(Resistence,text ="White",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "white" ,fg = "black",command = lambda:buttonclick(9) ).grid(row = 10 , column = 0 , pady = 1 )

# HERE COMES THE CLEAR BUTTON ============================================================================================

btn_clear = Button(Resistence,text =" CLEAR ",width = 40 , height = 3 , font = ('arial',10,'bold') ,
 					bg = "light green" ,fg = "black",command = btnClear ).grid(row = 11 ,rowspan = 2 , column = 0 , columnspan = 3 , pady = 1 )



# THIS IS THE SECOND BAND WITH IT'S COLORS==========================================================================

Band2_display = Label(Resistence,text = " Second line " , width = 10 , height = 2 , font = ('arial',13,'bold') ,
							 bg = "skyblue" , fg = "black" ).grid(row = 0 , column = 1 , pady = 1, padx = 3)

btn_black2 = Button(Resistence,text ="Black",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "black" ,fg = "white",command = lambda:buttonclick(0) ).grid(row = 1 , column = 1 , pady = 2  ) 

btn_brown2 = Button(Resistence,text ="Brown",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "brown" ,fg = "black",command = lambda:buttonclick(1) ).grid(row = 2 , column = 1 , pady = 2 )

btn_red2 = Button(Resistence,text ="Red",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "red" ,fg = "black",command = lambda:buttonclick(2) ).grid(row = 3 , column = 1 , pady = 2 )

btn_orange2 = Button(Resistence,text ="Orange",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "orange" ,fg = "black",command = lambda:buttonclick(3) ).grid(row = 4 , column = 1 , pady = 2 )

btn_yellow2 = Button(Resistence,text ="Yellow",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "yellow" ,fg = "black",command = lambda:buttonclick(4) ).grid(row = 5 , column = 1 , pady = 2 )

btn_green2 = Button(Resistence,text ="Green",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "green" ,fg = "black",command = lambda:buttonclick(5) ).grid(row = 6 , column = 1 , pady = 2 )

btn_blue2 = Button(Resistence,text ="Blue",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "blue" ,fg = "white",command = lambda:buttonclick(6) ).grid(row = 7 , column = 1 , pady = 2 )

btn_violet2 = Button(Resistence,text ="Violet",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "violet" ,fg = "black",command = lambda:buttonclick(7) ).grid(row = 8 , column = 1 , pady = 2 )

btn_grey2 = Button(Resistence,text ="Grey",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "grey" ,fg = "black",command = lambda:buttonclick(8) ).grid(row = 9 , column = 1 , pady = 2 )

btn_white2 = Button(Resistence,text ="White",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "white" ,fg = "black",command = lambda:buttonclick(9) ).grid(row = 10 , column = 1 , pady = 2 )


# THIS IS THE THIRD BAND WITH IT'S COLORS==========================================================================

Band3_display = Label(Resistence,text = " Third line " , width = 10 , height = 2 , font = ('arial',13,'bold') ,
							 bg = "skyblue" , fg = "black" ).grid(row = 0 , column = 2 , pady = 1, padx = 3)

btn_black3 = Button(Resistence,text ="Black",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "black" ,fg = "white",command = lambda:buttonclick(0) ).grid(row = 1 , column = 2 , pady = 2  ) 

btn_brown3 = Button(Resistence,text ="Brown",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "brown" ,fg = "black",command = lambda:buttonclick(1) ).grid(row = 2 , column = 2 , pady = 2 )

btn_red3 = Button(Resistence,text ="Red",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "red" ,fg = "black",command = lambda:buttonclick(2) ).grid(row = 3 , column = 2 , pady = 2 )

btn_orange3 = Button(Resistence,text ="Orange",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "orange" ,fg = "black",command = lambda:buttonclick(3) ).grid(row = 4 , column = 2 , pady = 2 )

btn_yellow3 = Button(Resistence,text ="Yellow",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "yellow" ,fg = "black",command = lambda:buttonclick(4) ).grid(row = 5 , column = 2 , pady = 2 )

btn_green3 = Button(Resistence,text ="Green",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "green" ,fg = "black",command = lambda:buttonclick(5) ).grid(row = 6 , column = 2 , pady = 2 )

btn_blue3 = Button(Resistence,text ="Blue",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "blue" ,fg = "white",command = lambda:buttonclick(6) ).grid(row = 7 , column = 2 , pady = 2 )

btn_violet3 = Button(Resistence,text ="Violet",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "violet" ,fg = "black",command = lambda:buttonclick(7) ).grid(row = 8 , column = 2 , pady = 2 )

btn_grey3 = Button(Resistence,text ="Grey",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "grey" ,fg = "black",command = lambda:buttonclick(8) ).grid(row = 9 , column = 2 , pady = 2 )

btn_white3 = Button(Resistence,text ="White",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "white" ,fg = "black",command = lambda:buttonclick(9) ).grid(row = 10 , column = 2 , pady = 2 )


# THIS IS THE FOURTH BAND WITH IT'S COLORS==========================================================================

Band4_display = Label(Resistence,text = " Multiplier " , width = 10 , height = 2 , font = ('arial',13,'bold') ,
							 bg = "skyblue" , fg = "black" ).grid(row = 0 , column = 3 , pady = 1, padx = 4)

btn_black4 = Button(Resistence,text ="Black",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "black" ,fg = "white",command = lambda: multiplier(1) ).grid(row = 1 , column = 3 , pady = 2  ) 

btn_brown4 = Button(Resistence,text ="Brown",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "brown" ,fg = "black",command = lambda: multiplier(10) ).grid(row = 2 , column = 3 , pady = 2 )

btn_red4 = Button(Resistence,text ="Red",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "red" ,fg = "black",command = lambda: multiplier(100) ).grid(row = 3 , column = 3 , pady = 2 )

btn_orange4 = Button(Resistence,text ="Orange",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "orange" ,fg = "black",command = lambda: multiplier(1000) ).grid(row = 4 , column = 3 , pady = 2 )

btn_yellow4 = Button(Resistence,text ="Yellow",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "yellow" ,fg = "black",command = lambda: multiplier(10000) ).grid(row = 5 , column = 3 , pady = 2 )

btn_green4 = Button(Resistence,text ="Green",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "green" ,fg = "black",command = lambda : multiplier(100000) ).grid(row = 6 , column = 3 , pady = 2 )

btn_blue4 = Button(Resistence,text ="Blue",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "blue" ,fg = "white",command = lambda: multiplier(1000000) ).grid(row = 7 , column = 3 , pady = 2 )

btn_violet4 = Button(Resistence,text ="Violet",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "violet" ,fg = "black",command = lambda: multiplier(10000000) ).grid(row = 8 , column = 3 , pady = 2 )

btn_grey4 = Label(Resistence,text ="Grey",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "grey" ,fg = "black" ).grid(row = 9 , column = 3 , pady = 2 )

btn_white4 = Label(Resistence,text ="White",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "white" ,fg = "black" ).grid(row = 10 , column = 3 , pady = 2 )

btn_silver4 = Button(Resistence,text ="Silver",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "silver" ,fg = "black",command = lambda: multiplier(0.01) ).grid(row = 11 , column = 3 , pady = 2 )

btn_gold4 = Button(Resistence,text ="Gold",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "gold" ,fg = "black" ,command = lambda: multiplier(0.1)).grid(row = 12 , column = 3 , pady = 2 )


# THIS IS THE FIFTH BAND WITH IT'S COLORS==========================================================================

Band5_display = Label(Resistence,text = " Tolerance " , width = 10 , height = 2 , font = ('arial',13,'bold') ,
							 bg = "skyblue" , fg = "black" ).grid(row = 0 , column = 4 , pady = 1, padx = 2)

btn_black5 = Label(Resistence,text ="Black",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "black" ,fg = "white" ).grid(row = 1 , column = 4 , pady = 2  ) 

btn_brown5 = Button(Resistence,text ="Brown",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "brown" ,fg = "black",command = lambda:tolreance(1) ).grid(row = 2 , column = 4 , pady = 2 )

btn_red5 = Button(Resistence,text ="Red",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "red" ,fg = "black",command = lambda:tolreance(2) ).grid(row = 3 , column = 4 , pady = 2 )

btn_orange5 = Label(Resistence,text ="Orange",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "orange" ,fg = "black" ).grid(row = 4 , column = 4 , pady = 2 )

btn_yellow5 = Label(Resistence,text ="Yellow",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "yellow" ,fg = "black" ).grid(row = 5 , column = 4 , pady = 2 )

btn_green5 = Button(Resistence,text ="Green",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "green" ,fg = "black",command = lambda:tolreance(0.5) ).grid(row = 6 , column = 4 , pady = 2 )

btn_blue5 = Button(Resistence,text ="Blue",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "blue" ,fg = "white",command = lambda:tolreance(0.25) ).grid(row = 7 , column = 4 , pady = 2 )

btn_violet5 = Button(Resistence,text ="Violet",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "violet" ,fg = "black",command = lambda:tolreance(0.1) ).grid(row = 8 , column = 4 , pady = 2 )

btn_grey5 = Button(Resistence,text ="Grey",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "grey" ,fg = "black",command = lambda:tolreance(0.05) ).grid(row = 9 , column = 4 , pady = 2 )

btn_white5 = Label(Resistence,text ="White",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "white" ,fg = "black" ).grid(row = 10 , column = 4 , pady = 2 )

btn_silver5 = Button(Resistence,text ="Silver",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "silver" ,fg = "black",command = lambda:tolreance(10) ).grid(row = 11 , column = 4 , pady = 2 )

btn_gold5 = Button(Resistence,text ="Gold",width = 12 , height = 1 , font = ('arial',10,'bold') ,
 					bg = "gold" ,fg = "black",command = lambda:tolreance(5) ).grid(row = 12 , column = 4 , pady = 2 )


Ohm_Display = Entry(Resistence, font = ('arial',35,'bold'),textvariable = text_input ,bg = "skyblue", bd = 12, width = 16 , justify = RIGHT)
Ohm_Display.grid(row = 13, column = 0 , columnspan = 4, pady = 1  )
Ohm_Display.insert(0, "0")

Ohm1_Display = Entry(Resistence, font = ('arial',35,'bold'),textvariable = text_input1 ,bg = "skyblue", bd = 12, width = 16 , justify = RIGHT)
Ohm1_Display.grid(row = 14, column = 0 , columnspan = 4, pady = 1  )
Ohm1_Display.insert(0, "0")


Ohm_DisplayΩ = Label(Resistence,text = "Ω    +" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W, 
					bg = "skyblue",fg = "black", ).grid(row = 13, column = 4 , pady = 1 )

Ohm1_DisplayΩ = Label(Resistence,text = "Ω   —" ,width = 5 , height = 2, font = ('arial',22,'bold'), anchor = W, 
					bg = "skyblue",fg = "black", ).grid(row = 14, column = 4 , pady = 1 )




def exit():
	exit = tkinter.messagebox.askyesno("Resistence Calculator", "Do you really want to quit the program ? ")
	if exit > 0:
		root.destroy()
		


menubar = Menu(Resistence)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File" , menu = filemenu)
filemenu.add_command(label = "Exit", command = exit)


root.config(menu = menubar)


root.mainloop()