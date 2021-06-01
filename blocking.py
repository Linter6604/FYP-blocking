from tkinter import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Website Blocker")

Label(root, text ='WEBSITE BLOCKER' , font ='arial 18 bold').pack()

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

Label(root, text ='Enter Website :' , font ='arial 13 bold').place(x= 5 ,y=60)
Websites = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 140,y = 60)

def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Website already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

def Unblocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website not in file_content:
                Label(root, text = 'Website already Unblocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                existing_websites = file_content.split('\n')
                existing_websites = [x for x in existing_websites if website[0:-2] not in x]
                host_file.truncate(0)
                host_file.seek(0)
                host_file.write("\n".join(existing_websites))
                Label(root, text="Unblocked", font='arial 12 bold').place(x=230, y=200)

                Label(root, text = "Unblocked", font = 'arial 12 bold').place(x=230,y =200)


block1 = Button(root, text = 'Block',font = 'arial 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block1.place(x = 230, y = 150)

block2 = Button(root, text = 'Unblock',font = 'arial 12 bold',pady = 5,command = Unblocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')
block2.place(x = 330, y = 150)


root.mainloop()
