import customtkinter as ctk 


app =ctk.CTk()
app.title('calculer')
app.geometry('300x500')

def sum():
    try:
        ex = input_box.get().replace('×','*').replace('÷','/')
        re = eval(ex)
        output_box.configure(text=f'{re}')
    except:
        output_box.configure(text='error')
        
        
def delq():
    num = input_box.get()
    input_box.delete(len(num)-1,'end')
    
    
def cle():
    input_box.delete(0,'end')
    output_box.configure(text='')
    
def button(text,x,y,command, w=50,h=50,hover='red',color='#242424'):
    return ctk.CTkButton(
        app,
        font=('Arial',24,'bold'),
        corner_radius=10,
        command=command,
        width=w,height=h,
        fg_color=color,
        hover_color=hover,
        text=text
    ).place(x=x,y=y)
    
    
input_box =ctk.CTkEntry(
    app,
    font=('Arial',24,'bold'),
    width=280,
    height=15,
    justify='right',
    fg_color='#242424',
    border_color='#242424'
)

input_box.place(x=10,y=15)


output_box =ctk.CTkLabel(
    app,
    font=('Arial',24,'bold'),
    width=280,
    height=15,
    text="",
    text_color='#d4770f'
)

output_box.place(x=10,y=80)


button('C',14,140, cle, hover='#d4770f')
button('D',88,140, delq, hover='#d4770f')
button('%',165,140,lambda: input_box.insert('end','%'), hover='#d4770f')
button('÷',235,140,lambda: input_box.insert('end','÷'), hover='#d4770f')

button('7',14,210,lambda: input_box.insert('end','7'))
button('8',88,210,lambda: input_box.insert('end','8'))
button('9',165,210,lambda: input_box.insert('end','9'))
button('×',235,210,lambda: input_box.insert('end','×'), hover='#d4770f')



button('4',14,275,lambda: input_box.insert('end','4'))
button('5',88,275,lambda: input_box.insert('end','5'))
button('6',165,275,lambda: input_box.insert('end','6'))
button('-',235,275,lambda: input_box.insert('end','-'), hover='#d4770f')


button('1',14,340,lambda: input_box.insert('end','1'))
button('2',88,340,lambda: input_box.insert('end','2'))
button('3',165,340,lambda: input_box.insert('end','3'))
button('+',235,340,lambda: input_box.insert('end','+'), hover='#d4770f')


button('0',14,405,lambda: input_box.insert('end','0'))
button('.',88,405,lambda: input_box.insert('end','.'))
button('=',165,405, sum , w=120, hover='#d4770f')




app.mainloop()