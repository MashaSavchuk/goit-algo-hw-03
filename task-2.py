import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Створення вікна та налаштування черепахи
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.color("blue")
    t.speed(20)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Запит у користувача на рівень рекурсії
    level = int(input("Введіть рівень рекурсії (ціле число більше 0): "))

    # Виклик функції для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, level, 300)
        t.right(120)

    # Завершення програми при натисканні клавіші Enter
    window.mainloop()

if __name__ == "__main__":
    main()
