from tkinter import *
import random

GAME_WIDTH=800
GAME_HEIGHT=700
SPEED=50
BODY_PART=3
SPACE_SIZE=50
# BODY_SIZE=50
FOOD_SIZE=50
SNAKE_COLOR="#03ffdd"
FOOD_COLOR="#ff0357"
BG_COLOR="#000000"

class Snake:
    def __init__(self):
        self.body_size=BODY_PART
        self.coordinates=[]
        self.squares=[]
        

        for i in range(0,BODY_PART):
            self.coordinates.append([0,0])

        for x, y  in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
            self.squares.append(square)

def next_move(snake,food):
    x,y =snake.coordinates[0]

    if direction=='up':
        y-=SPACE_SIZE
    elif direction=='down':
        y+=SPACE_SIZE
    elif direction=='right':
        x+=SPACE_SIZE
    elif direction=='left':
        x-=SPACE_SIZE
    
    snake.coordinates.insert(0,[x,y])
    
    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        score_label.config(text='Score:{}'.format(score))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED,next_move,snake,food)



class Food:
    
    def __init__(self):

        x=random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates=[x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food") #to ensure that oval has width and height of the sace size we add space size

def change_direction(new_direction):

    global direction
    
    if direction=='up' and new_direction!='down':
        direction=new_direction
    elif direction=='down' and new_direction!='up':
        direction=new_direction
    elif direction=='left' and new_direction!='right':
        direction=new_direction
    elif direction=='right' and new_direction!='left':
        direction=new_direction

def check_collisions(snake):
    x,y=snake.coordinates[0]

    if x<0 or x>window_width:
        
        return True
    elif y<0 or y>window_height:
        return True
    
    for body_parts in snake.coordinates[1:]:
        if x==body_parts[0] and y==body_parts[1]:
            return True
    
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(window.winfo_width()/2,window.winfo_height()/2,
                       text="GAME OVER",font=("consolas","70"),fill="red")

window=Tk()
window.title("Snake game")
window.resizable(False,False)  #prevents your window from resizing 
direction='down'
score=0
score_label=Label(window,text="Score:{}".format(score),font=("comicraft",40))
score_label.pack()

canvas=Canvas(window,height=GAME_HEIGHT,width=GAME_WIDTH,bg=BG_COLOR)
canvas.pack()
window.update()
# to center the window
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x_pos=int(screen_width/2-window_width/2)
y_pos=int(screen_height/2-window_height/2)
window.geometry("{}x{}+{}+{}".format(window_width,window_height,x_pos,y_pos))

snake=Snake() #object for snake and food class
food=Food()
next_move(snake,food)

window.bind("<Up>",lambda x:change_direction('up'))
window.bind("<Down>",lambda x:change_direction('down'))
window.bind("<Left>",lambda x:change_direction('left'))
window.bind("<Right>",lambda x:change_direction('right'))
window.mainloop()