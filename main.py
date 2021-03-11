import turtle
beth = turtle.Turtle()
beth.speed(0)

c = ['red','yellow','black']
index = 0
for distance in [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]:
  beth.color(c[index])
  beth.forward(distance)
  beth.left(90)
  index += 1
  if index > 2:
    index =