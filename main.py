import turtle
import pandas
image='blank_states_img.gif'
my_screen= turtle.Screen()
my_screen.addshape(image)
turtle.shape(image)
game_is_on=True
states_guessed=0
LIVES=5
FONT=('Courier',8, 'bold')
ALIGNMENT ='center'

data=pandas.read_csv('50_states.csv')
all_states=data.state.to_list()
all_x=data.x.to_list()
all_y=data.y.to_list()

#writes the answer on map
def answer_on_map(answer,goto_cord,Lives):
    writer_turtle=turtle.Turtle()
    writer_turtle.hideturtle()
    writer_turtle.speed('fastest')
    writer_turtle.penup()
    writer_turtle.color('black')
    writer_turtle.goto(goto_cord)
    writer_turtle.write(f'{answer}', align=ALIGNMENT, font=FONT)

guessed_states=[]
while game_is_on:
    #dialouge box is created
    answer=my_screen.textinput(f'{states_guessed}/50 Guess a state','Your guess:').title()
    if answer in guessed_states:
        print('Already guessed')

    elif answer in all_states:
       idx=all_states.index(answer)
       X= all_x[idx]
       Y= all_y[idx]
       goto_cord=(X,Y)
       answer_on_map(answer,goto_cord,LIVES)
       guessed_states.append(answer)
       states_guessed+=1

    else:
        LIVES-=1
        print(f'Wrong guess\nLives remaining: {LIVES}\n')

    if states_guessed==50 or LIVES==0 or answer=='Exit':
        break

guessed_state=set(guessed_states)
all_states=set(all_states)
missed_states=all_states.difference(guessed_state)
missed_states=list(missed_states)
missed_states.sort()

missed_states_data={
    'States you missed':missed_states,
}
missed_states_file=pandas.DataFrame(missed_states_data)
missed_states_file.to_csv('Missed_states.csv')