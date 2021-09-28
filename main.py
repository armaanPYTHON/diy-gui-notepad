from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from tkinter.ttk import Combobox
import time



def main():
    
    root = Tk()
    root.title('Notepad')
    root.geometry('600x500')
    root.iconbitmap('icon/icon.ico')

    filelist = []


    frame = Frame(root)
    frame.pack(fill=BOTH, expand=1)

    textbox = Text(frame, bd=0)
    textbox.pack(fill=BOTH, expand=1)

#---------------SAVE FUNCTIONS--------------------
    def saveas(e=None):

        filelist.clear()
        filename = filedialog.asksaveasfilename(title='Save As', defaultextension=(
            ("TXT Files", '*.txt'),
            ("DAT Files", '*.dat')),
            filetypes=(
            ("TXT Files", '*.txt'),
            ("DAT Files", '*.dat')))
        filelist.append(filename)

        f = open(filename, 'w')
        f.write(textbox.get('1.0', END))

    def save(e=None):
        try:
            if os.path.isfile(filelist[0]):
                f = open(filelist[0], 'w')
                f.write(textbox.get('1.0', END))
                f.close()
            else:
                saveas()
        except:
            saveas()



#----------------FILE FUNCTIONS=------------------
    def new(e=None):
        x = messagebox.askyesno('New Document', 'Do you want to save this document?')
        if x == 1:
            save()
            textbox.delete('1.0', END)
        else:
            textbox.delete('1.0', END)

    def openfile(e=None):
        filelist.clear()
        filename = filedialog.askopenfilename(title='Open Document', defaultextension=(
            ("TXT Files", '*.txt'),
            ("DAT Files", '*.dat')),
            filetypes=(
            ("TXT Files", '*.txt'),
            ("DAT Files", '*.dat')))

        filelist.append(filename)
        
        f = open(filename, 'r')
        textbox.insert(END, f.read())
        f.close()


    def restart(e=None):
        root.destroy()
        time.sleep(1)
        main()


#-------------------COLORMODE FUNCTIONS------------------
    def colormode(e=None):
        f = open('files/colormode.txt', 'r')
        if f.read() == 'dark':
            textbox.config(fg='white', bg='#212120', insertbackground='white')
        else:
            textbox.config(bg='white', fg='black', insertbackground='black')

    def darkmode(e=None):
        f = open('files/colormode.txt', 'w')
        f.write('dark')
        f.close()
        colormode()

    def lightmode(e=None):
        f = open('files/colormode.txt', 'w')
        f.write('light')
        f.close()
        colormode()


#------------------FONT FUNCTIONS-----------------------
    def reg_font():
        fonts = []

        f = open('files/font.txt', 'r')
        for item in f.readlines():
            item = item.strip('\n')
            fonts.append(item)
        f.close()

        textbox.config(font=(fonts[0], int(fonts[1])))

    def font(e=None):
        win = Toplevel()
        win.title('Adjust Font settings')
        win.geometry('300x300')

        Label(win, text='Font Style: ').grid(row=0, column=0)
        Label(win, text='Font Size: ').grid(row=1, column=0)
        Label(win, text='Font Weight: ').grid(row=2, column=0)

        fonts = [
            'Arial',
            'Times New Roman'
        ]
        font_weight = [
            'Bold',
            'Italic',
            'Regular'
        ]

        fs = Combobox(win, values=fonts, width=20)
        fs.grid(row=0, column=1)
        fz = Spinbox(win, from_=1, to=100, width=20)
        fz.grid(row=1, column=1, pady=5)
        fw = Combobox(win, values=font_weight, width=20)
        fw.grid(row=2, column=1)
        fs.set(fonts[0])
        fw.set(font_weight[2])

        def sub(e=None):
            f = open('files/font.txt', 'w')
            f.write(
                fs.get() + '\n' +
                str(fz.get()) + '\n'+
                fw.get() + '\n'
            )

            win.destroy()

            fonts = []

            f = open('files/font.txt', 'r')
            for item in f.readlines():
                item = item.strip('\n')
                fonts.append(item)
            f.close()

            textbox.config(font=(fonts[0], int(fonts[1])))



        Button(win, text='Submit', bd=0, bg='white', command=sub).grid(row=3, column=0, columnspan=2)

        win.bind('<Return>', sub)
        
    

    #----------MENU----------------
    menu = Menu(root)
    root.config(menu=menu)
    file = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=new)
    file.add_command(label='Open File', command=openfile)
    file.add_separator()
    file.add_command(label='Save', command=save)
    file.add_command(label='Save As', command=saveas)
    file.add_separator()
    file.add_command(label='Restart App', command=restart)
    file.add_command(label='Exit App', command=root.destroy)

    edit = Menu(menu, tearoff=0)
    menu.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Adjust Font', command=font)

    view = Menu(menu, tearoff=0)
    menu.add_cascade(label='View', menu=view)
    view.add_command(label='Dark Mode', command=darkmode)
    view.add_command(label='Light Mode', command=lightmode)
    


    #------------BINDINGS----------
    root.bind('<Control-n>', new)
    root.bind('<Control-s>', save)
    root.bind('<Control-o>', openfile)
    root.bind('<Control-r>', restart)
    root.bind('<Control-d>', darkmode)
    root.bind('<Control-l>', lightmode)
    root.bind('<Control-f>', font)

    reg_font()
    colormode()

    mainloop()
main()