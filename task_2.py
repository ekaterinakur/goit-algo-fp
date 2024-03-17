import turtle

def draw_pifagor_tree(branch_len, level):
    if level == 0:
        return

    turtle.forward(branch_len)
    turtle.left(45)
    draw_pifagor_tree(0.6 * branch_len, level-1)
    turtle.right(90)
    draw_pifagor_tree(0.6 * branch_len, level-1)
    turtle.left(45)
    turtle.backward(branch_len)

def main():
    level = int(input("Введіть рівень рекурсії: "))

    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()

    draw_pifagor_tree(100, level)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
