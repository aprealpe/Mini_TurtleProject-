import turtle
window = turtle.Screen()
window.bgcolor("blue")

def draw_hexagonedown(nick,a,ini,long,y,w):
    nick.color("red")
    nick.speed(2)
    nick.seth(w)
    for i in range(1,3,1):
            if i % 2 == 0:
                nick.right(a)
            else:
                nick.right(a)
            nick.forward(long)
            if(ini==i):
                nick.left(45-a)
                draw_flower(nick, a,0, long/2,y,w)
    nick.left(45-a)

def draw_hexagoneup(nick,a,ini,long,y,w):
    nick.color("red")
    nick.speed(2)
    nick.seth(w+180)
    for i in range(2,4,1):
            if i % 2 == 0:
                nick.right(a)
            else:
                nick.right(a)
            nick.forward(long)
    nick.left(45-a)
    if(y==8):
        window.exitonclick()
    else:
        draw_hexagonedown(nick,a,2,long,y,w+45)


def draw_flower(nick,a,ini,long,yz,w):
    y=0
    if(yz%2==0):
        nick.color("purple")
    else:
        nick.color("green")
   
    nick.speed(20)
    while y < 40:
            y=y+1
            for i in range(1,5,1):
                if i % 2 == 0:
                    nick.right(90-a)
                else:
                    nick.right(90+a)
                nick.forward(long)
            nick.left(45-a)
    if(ini==0):
        yz=yz+1
        draw_hexagoneup(nick,a,2,long*2,yz,w)

nick = turtle.Turtle()
nick.shape("turtle")

draw_hexagonedown(nick,55,2,100,0,0)