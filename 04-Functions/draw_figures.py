#duze problemy z tym
import figures
import turtle

# Ustawienie okna
window = turtle.Screen()
window.bgcolor("lightgreen")

# Utworzenie żółwia
pen = turtle.Turtle()
pen.speed(5)

# --- 1. KWADRATY ---
figures.draw_square(pen, 80)

pen.penup()
pen.goto(-150, 100)
pen.pendown()
figures.draw_square(pen, 50)

# --- 2. TRÓJKĄTY ---
pen.penup()
pen.goto(150, 100)
pen.pendown()
figures.draw_triangle(pen, 90)

pen.penup()
pen.goto(150, -100)
pen.pendown()
figures.draw_triangle(pen, 60)

# --- 3. PROSTOKĄTY ---
pen.penup()
pen.goto(-150, -100)
pen.pendown()
figures.draw_rectangle(pen, 100, 50)

pen.penup()
pen.goto(0, -150)
pen.pendown()
figures.draw_rectangle(pen, 70, 35)

# Zakończenie
pen.hideturtle()
window.mainloop()