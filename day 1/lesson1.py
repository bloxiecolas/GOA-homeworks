from turtle import *


#we want to paint a house

#step 1: draw a square
speed (100)
width (7)

color ("purple")

forward (200)
left (90)

forward (200)

left (90)


forward (200)

left (90)

forward (200)

#end of square

#drawing a door

left (90)


forward (75)

color ("yellow")

left (90)

forward (100) #height of the door

right (90)

forward (50)

left (-90)

forward (100)

penup ()
goto (200, 200)

pendown ()

color ("red")


right (150)

forward (190)

right (-118)

forward (190)

end_fill()

exitonclick()


