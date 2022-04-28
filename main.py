##


from tkinter import *
import time
import random

game_running = True

game_width = 700                    #задаем размеры поля и обЪекта
game_height = 700                   #
snake_mob = 14                      #
snake_color1 = "green"              #задаем цвет обЪекта
snake_color2 = "purple"             #

virtual_game_x = game_width//snake_mob
virtual_game_y = game_height//snake_mob

snake_x=virtual_game_x//2
snake_y=virtual_game_y//2
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 3

tk = Tk()
tk.title('Snake Game on Python')
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0 )
canvas.pack()
tk.update()

eat_color1 = "yellow"             
eat_color2 = "red"
eat_list = []
eat_size = 10
for i in range (eat_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x*snake_mob,y*snake_mob,x*snake_mob+snake_mob,y*snake_mob+snake_mob,fill=eat_color1) 
    id2 = canvas.create_oval(x*snake_mob+2,y*snake_mob+2,x*snake_mob+snake_mob-2,y*snake_mob+snake_mob-2,fill=eat_color2)
    
    eat_list.append ([x, y, id1, id2])
print(eat_list)

bomb_color4 = "pink"             
bomb_color3 = "black"
bomb_list = []
bomb_size = 10
for i in range (bomb_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id3 = canvas.create_oval(x*snake_mob,y*snake_mob,x*snake_mob+snake_mob,y*snake_mob+snake_mob,fill=bomb_color4) 
    id4 = canvas.create_oval(x*snake_mob+2,y*snake_mob+2,x*snake_mob+snake_mob-2,y*snake_mob+snake_mob-2,fill=bomb_color3)
    
    bomb_list.append ([x, y, id3, id4])
print(bomb_list)


def snake_paint_mob(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x*snake_mob,y*snake_mob,x*snake_mob+snake_mob,y*snake_mob+snake_mob,fill=snake_color1) 
    id2 = canvas.create_rectangle(x*snake_mob+2,y*snake_mob+2,x*snake_mob+snake_mob-2,y*snake_mob+snake_mob-2,fill=snake_color2)
    snake_list.append ([x,y,id1,id2])
    print(snake_list)

snake_paint_mob(canvas, snake_x, snake_y)

def check_can_we_delete_snake_mob():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])

def check_if_we_found_eat ():
    global snake_size
    for i in range(len(eat_list)):
        if eat_list [i] [0] == snake_x and eat_list [i] [1] == snake_y:
            #print("found!!!")
            snake_size = snake_size + 1
            canvas.delete(eat_list [i] [2])
            canvas.delete(eat_list [i] [3])
    #print(snake_x, snake_y)

def check_if_we_found_bomb ():
    global snake_size
    for i in range(len(bomb_list)):
        if bomb_list [i] [0] == snake_x and bomb_list [i] [1] == snake_y:
            #print("found!!!")
            snake_size = snake_size - 1
            canvas.delete(bomb_list [i] [2])
            canvas.delete(bomb_list [i] [3])
    #print(snake_x, snake_y)
    

def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav

    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_mob()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_mob()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_mob()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_mob()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_mob(canvas, snake_x, snake_y)
    check_if_we_found_eat ()
    check_if_we_found_bomb()

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)

def game_over():
    global game_running
    game_running = False

def check_if_granica():
    global game_running
    if snake_y >virtual_game_y or snake_y<0 or snake_y>virtual_game_y or snake_y<0:
        game_over()

def check_we_touch_snake(f_x, f_y):
    global game_running
    if not (snake_x_nav == 0 and snake_y_nav == 0):
        for i in range(len(snake_list)):
            if snake_list [i] [0] == f_x and snake_list [i] [1] == f_y:
                print('death!')
                game_running = False


while game_running :
    check_if_we_found_bomb()
    check_can_we_delete_snake_mob()
    check_if_we_found_eat ()
    check_if_granica()
    check_we_touch_snake(snake_x + snake_x_nav, snake_y + snake_y_nav)

    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_mob(canvas, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)

tk.update()
tk.mainloop()

def fun_nothing (event):
    pass
canvas.bind_all("<KeyPress-Left>", fun_nothing)
canvas.bind_all("<KeyPress-Right>", fun_nothing)
canvas.bind_all("<KeyPress-Up>", fun_nothing)
canvas.bind_all("<KeyPress-Down>", fun_nothing)

tk.update()