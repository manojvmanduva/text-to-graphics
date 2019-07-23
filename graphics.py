from turtle import*
import random


screensize(1500,1500)
dot(1,"red")
bgcolor("white")
colormode(255)
speed(10)



hideturtle()
t = textinput("Text to Display","You see this on the output")
s = textinput("Text to Graphics","Please remove special characters and Capital Letters")


pensize(1)

w = s.split()
y = 0;


while y < len(w):
    word = w[y]
    print (y)
    print (word)
    y =y+1;
    r=random.randint(0,254);
    g=random.randint(0,254);
    b=random.randint(0,254);
    pencolor(r,g,b)
    fillcolor(r,g,b)
    forward(200)
    x = 0;

    begin_fill()
    while x < len(word):
        alpha = word[x]
        print (x)
        print (alpha)
        x = x+1;

        alphabet = ["0","a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z"]
        p = alphabet.index(alpha)
        print (p)
        circle (p*5)
        right(45)
    end_fill()
    tilt(90)

penup()
if len(w)>3:
    setpos(-(len(w)*50),0)
else :
    setpos(0,0)
pendown()
pencolor("black")
write(t, font=("Helvetica", 28, "normal"))
    
        










