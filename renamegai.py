import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os,re
from PIL import Image,ImageTk
import ctypes
global photo


class window:
    def __init__(self):

        self.entry2 = None
        self.root=root=tkinter.Tk()  #first line of tkinter
        self.root.title('image rename')  #title of the window
        self.root.resizable(False, False)  # fixed window size

        # Tell the operating system to use the program's own dpi adaptation
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # Get the zoom factor of the screen
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # Set program zoom
        self.root.tk.call('tk', 'scaling', ScaleFactor / 75)

        img = Image.open('image/back233.gif')
        photo = ImageTk.PhotoImage(img)
        label=tkinter.Label(root,image=photo)
        label.place(x=0, y=0)  # Choose file location
        label=tkinter.Label(root,text='Select the file:',font=('Microsoft Yahei',12),bg="#9AB8EE")#select file tag
        label.place(x=20,y=60)#Choose file location
        label=tkinter.Label(root,text='Example: Input image(1) files named: image1, image2...',font=('Microsoft Yahei',10),bg="#9AB8EE")#note labels
        label.place(x=20,y=165)#Note the location
        label=tkinter.Label(root,text='Note: Brackets are in English',font=('Microsoft Yahei',10),bg="#9AB8EE")#note labels
        label.place(x=20,y=190)#Note the location



        self.theLB = tkinter.Listbox(root,selectmode='entended',width=50,bg='CornflowerBlue')#Build lists and scroll bars
        self.theLB.pack(side='left',fill='both')#show list
        self.theLB.place(x=70,y=250)#The position of the list # vertical scroll bar component

 
        self.buttonview1 = tkinter.Button(root, text='preview', font=('Microsoft Yahei', 15),relief='flat',fg='white',bg='CornflowerBlue',  # preview button
                                             command=self.view)  # Browse button click event
        self.buttonview1.place(x=560, y=340)  #The location of the browse button


        menu=tkinter.Menu(self.root)  #Create home directory at root
        helpmenu= tkinter.Menu(menu, tearoff=False)  #Create subdirectory tearoff=0 menu cannot be independent
        menu.add_cascade(label='help', menu=helpmenu)  #Set the menu name label='Help', add a subdirectory in the main directory
        #Add subdirectory menu with name, and command
        helpmenu.add_radiobutton(label='Instructions for use', command=self.introduct, font=('Bold', 10))#Add usage instructions and click events
        self.root.config(menu=menu)  #Put home directory in root

        self.status=tkinter.StringVar()#When using interface programming, sometimes it is necessary to track the change of the value of the variable to ensure that the change of the value can be displayed on the interface at any time
        #self.entry1=tkinter.Entry(root)可以用get()方法，但是self.entry1=tkinter.Entry(root).place(x=150, y=80)不能get()方法
        self.entry1=tkinter.Entry(root,width=45,relief='flat')#Add picture text box
        self.entry1.place(x=130,y=65)#text box position
        self.entry3 = tkinter.Entry(root, width=45, relief='flat',bg='LightSteelBlue')#input format text box
        self.entry3.place(x=130, y=125)#Enter the rich text box location
        self.entry3.insert(0,"()" )
        #naming format

        label = tkinter.Label(root, text='Naming format:', font=('Microsoft Yahei', 12), bg="#9AB8EE")
        # file format tag
        label.place(x=20, y=120)
        # file format location
        self.buttonbrowser1=tkinter.Button(root,text='browse',font=('Microsoft Yahei',10),relief='flat',fg='white',bg='CornflowerBlue',    #browse button
                                                                                  command=self.browser)#浏览按钮的点击事件
        self.buttonbrowser1.place(x=560,y=53)#The location of the browse button
 
        self.buttonconv=tkinter.Button(root,text='start',font=('Microsoft Yahei',10),relief='flat',fg='white',bg='CornflowerBlue',#start button
                                        command=self.conv)#start button click event
        self.buttonconv.place(x=560,y=115)#location of start button
        self.labelstatus = tkinter.Label(root,fg='red',font=('Microsoft Yahei',12), textvariable=self.status,bg="#9AB8EE")  #Completed variable label
        self.labelstatus.place(x=550, y=190)#the position of the completed label
 
        self.buttonclear1 = tkinter.Button(root, text='empty', font=('Microsoft Yahei', 15), relief='flat', fg='white',
                                          bg='CornflowerBlue',  # browse button
                                          command=self.clearall)  # Browse button click event
        self.buttonclear1.place(x=560, y=260)  # The location of the browse button
        self.root.minsize(700, 535)
        self.root.maxsize(700, 535)
        self.root.mainloop()  # mainloop enters event (message) loop refresh component once event is detected

 
 
    def clearall(self):
         directory = ' '
         savepath = ' '
         self.theLB.delete(0,tkinter.END)
         self.entry1.delete(0, tkinter.END)
         self.entry3.delete(0, tkinter.END)
 
    def introduct(self):#Describe the function of displaying the window
         #messageboxpopup
         tkinter.messagebox.showerror('help', '''
        Enter the prefix + (label) in the format
         If there is no input in the format, the automatic labels will be 1, 2, 3...
         After renaming, please click the clear button first

        Note: (1) The format cannot contain '/'; (2) The variable brackets are English brackets; (3) Back up the file before naming
         ''')





    def browser(self):
        '''Select the file browse box'''
        directory=tkinter.filedialog.askopenfilenames(title='browse', filetypes=[('JPG', '*.jpg'), ('JPGE', '*.jpge'), ('PNG', '*.png')])#Choose what file to open in the format of the Choose File dialog, returning the filename
        with open('filenames.txt','w') as f:#Python's with statement automatically calls the try finally structure and the close() method and stores the filename in filenames.txt
            for i in directory:#Iterate over the added filenames
                f.write(i)     #write to txt file
                f.write('\n')   #Write end marker\n
                self.theLB.insert(tkinter.END,i)

        if directory:      # Determine whether to choose
            self.entry1.delete(0,tkinter.END)#Clear the contents of the browse text line first
            self.entry1.insert(tkinter.END,set(directory))#Add the content of the browsed image to the browse text line

    def view(self):
        viewimg0=self.theLB.get("active")
        photo = Image.open(viewimg0)
        photo.show()





    def savepath(self):
        '''Save path browse box'''

        savepath = tkinter.filedialog.askdirectory(title='browse', filetypes=[('JPG', '*.jpg'), ('JPGE', '*.jpge'), ('PNG', '*.png')])#Choose what file to open in the format of the Choose File dialog, return

        if savepath:
            self.entry2.delete(0,tkinter.END)
            self.entry2.insert(tkinter.END,savepath)
    def read_filenames(self):#Read stored filename
        with open('filenames.txt','r') as f:#Or that Python comes with simplified paragraphs
            for i in f.readlines():#read line in file
                yield i.replace('\n', '')#yield character This loop skips the replace execution the first time, and recycles from the replace execution the second time
    def renameall(self,examplename):#rename module
        i=0
        for c in self.read_filenames():#generated by calling the function
            filenametype =c.split('/')[-1]  #Cut off all the previous paths and only keep the file name
            filep = c.replace(filenametype, '')  #I don't understand this line
            filetype = filenametype.split('.')[-1]  #Cut off file suffix
            if examplename == '':#If no format for renaming is entered
                newname0 = filep + str(i + 1) + "." + filetype  # Then the modified new file name is the original name + serial number (starting from 1) +. suffix
                newname = newname0.strip()#Remove all spaces in the newname0 string to prevent carriage returns or spaces before and after the filename string
                os.renames(c, newname)#Rename the traversed file c to the new file name
                self.theLB.insert(i + 1, newname)#Add a new one to the list first
                self.theLB.delete(i)#Delete the old one and add a new one here, because the first line cannot be deleted for a long time.
            else:
                pat = re.compile("(?<=\()\S+(?=\))")  # (?<=exp) is a string that starts with exp, but does not contain itself.\S matches any non-whitespace character
                sn0=re.findall(pat, examplename)[0].replace('(', '').replace(')', '')
                if sn0!=' ':
                    sn = int(sn0)  # Returns a list with () characters

                    newname0 = filep + examplename.replace('%d' % sn, '%d' % (sn + i)) + "." + filetype
                    newname = newname0.strip().replace('(', '').replace(')', '')
                    os.rename(c, newname)
                    self.theLB.insert(i + 1, newname)
                    self.theLB.delete(i)
                else:  # No numbers matched

                    newname0 = filep + examplename + str(i + 1) + "." + filetype  # Add the sequence number to the input side starting from 1
                    newname = newname0.strip()
                    newname = newname.replace('(', '').replace(')', '')  # Remove all spaces in the string newname0 and remove the parentheses
                    os.renames(c, newname)  # rename action
                    self.theLB.insert(i + 1, newname)
                    self.theLB.delete(i)
            i+=1#number+1



    def conv(self):
        filepaths= self.entry1.get()#Get the browsed file address
        examplename= self.entry3.get()  #Get the characters of the input template
        if filepaths == '':#if entry1 is empty
            tkinter.messagebox.showerror('Python tkinter', 'Please select an image')#Prompt no picture selected
            return
        try:
            self.renameall(examplename)#Execute the rename function
        except Exception as e:#Throw an exception
            print(e)
        self.status.set('Named successfully')#Variable label set to named success


#window=window()#Display window


