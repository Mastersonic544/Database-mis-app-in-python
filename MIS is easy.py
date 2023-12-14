from tkinter import *

root = Tk()


root.geometry('500x350')
root.iconbitmap('medipol.ico')
root.title("MIS is easy")

#Functions:
def liste(ch):
    t=[]
    a=''
    for i in range(len(ch)):
        if ch[i]==',':
            t.append(float(a))
            a=''
        else:
            a+=str(ch[i])
    t.append(float(a))
    return t

def somme(t):
    x=0
    for i in range(len(t)):
        x+=t[i]
    return x

def mid(t):
    x=0
    n=len(t)
    if n%2!=0:
        x=t[int(n/2)]
    else:
        x=(t[int(n/2)]+t[int((n/2)-1)])/2
    return x


def calcul(x):
    inp = ch.get("1.0",'end-1c')
    t=liste(inp)
    v=sorted(t)
    vv=str(v)
    x.config(text='Result:\nYour list: '+str(t)+'\nSorted: '+vv+'\nList length: '+str(len(t))+'\nSUM: '+str(somme(t))+'\nAVG: '
             +str(round((somme(t)/len(t)),3))+'\nMid:'+str(mid(v)))











#Tkinter:
titre=Label(root, text="Enter a list such as: 1,2,3,4...")
ch=Text(root, height=5, width=25)
res=Label(root,text='Result:')
calc = Button(root, height = 2, width = 20, text ="Calculate", command=lambda:calcul(res))


titre.pack()
titre.place(relx=0.5, rely=0.1, anchor='center')
ch.pack()
ch.place(relx=0.5, rely=0.25, anchor='center')
calc.pack()
calc.place(relx=0.5, rely=0.45, anchor='center')
res.pack()
res.place(relx=0.5, rely=0.55, anchor='n')


mainloop()