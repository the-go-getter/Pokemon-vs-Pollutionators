import turtle
import random
import time

'''##########################################################'''
###PLEASE PLAY THE GAME IN FULLSCREEN FOR OPTIMAL EXPERIENCE.###
'''##########################################################'''

# Direction angles for turtle
north = 90
east = 0
west = 180
south = 270

# Step value for character movements
step = 10

# Number of villains per level, labels to denote level and difficulty
villain_count = 10
level = 1
difficulty = 1

# Inputting all the game data
heroes = ['images/001.gif', 'images/004.gif', 'images/007.gif', 'images/025.gif']
bullet_types = ['images/leafs.gif', 'images/flame.gif', 'images/wave.gif', 'images/thunder.gif']
backgrounds = ['images/grass.gif', 'images/fire.gif', 'images/water.gif', 'images/electric.gif']
highscore = 'highscores.txt'

# Registering the shapes for hero and bullets
for i in range(4):
    turtle.register_shape(heroes[i])
    turtle.register_shape(bullet_types[i])

# Code for the opening screen
turtle.speed(0)
turtle.pu()
turtle.ht()
screen = turtle.Screen()
screen.title("Pokemons vs Pollutionators")
screen.bgcolor('white')
turtle.color('black')
start_str = "The game will begin in a few seconds, get ready!"
turtle.setpos(0, 0)
turtle.write(start_str, align='center', font=("Arial", 20, "bold"))
time.sleep(4)
turtle.undo()

'''##############################'''
###ALL FUNCTIONS ARE DEFINED HERE###
'''##############################'''


def euclidean(x1, y1, x2, y2):
    '''
        Name: euclidean
        Input: four numbers(ints or floats), representing two coordinates(x1,y1,x2,y2)
        Returns: a float, the euclidean distance between two coordinates
        Function: Gives the distance between two coordinates calculated by using
                  the classic distance formula in math.
    '''

    # X and Y are the squares of the difference between second and first
    # location's respective coordinates.

    X = (x2 - x1) ** 2
    Y = (y2 - y1) ** 2
    euclidean_dist = (X + Y) ** 0.5
    return euclidean_dist


def die(score_keeper):
    ''' Function die
        Params: An object of class score_keeper
        Returns: Nothing. Displays the game over message.
    '''
    turtle.goto(0, 0)
    turtle.color('red')
    gameover_str = "GAME OVER, your score was " + str(score_keeper.score)
    turtle.write(gameover_str, align='center', font=("Arial", 20, "bold"))
    top_score = fetch_highscore(highscore)
    if score_keeper.score > int(top_score[0]):
        turtle.goto(0, -75)
        turtle.color('yellow')
        turtle.write("Congratulations! You've made a highscore\nPlease enter your name in the python shell terminal",
                     align='center', font=("Arial", 20, "bold"))
        file_processor(score_keeper.score, highscore)
    else:
        turtle.goto(0, -50)
        turtle.write("Better luck next time.", align='center', font=("Arial", 20, "bold"))


def hero_selector(hero, bullet):
    ''' Function hero_selector
        Params: Two objects, one of class hero and  another of bullet.
        Returns: Nothing. Selects the hero, bullet type and background.
    '''
    num = random.randint(0, 3)
    hero.t.shape(heroes[num])
    bullet.t.shape(bullet_types[num])
    screen.bgpic(backgrounds[num])
    screen.setup(800, 800)

def fetch_highscore(highscore):
    ''' Function fetch_highscore
        Params: A string containing the file name with the highscore data
        Returns: A list with the top score and the top scorer's name.
    '''
    try:
        infile = open(highscore, 'r')
        top_score = infile.readlines()
        for i in range(len(top_score)):
            # Removing all the '\n' characters
            top_score[i] = top_score[i].replace('\n', '')
        infile.close()
        return top_score
    except OSError:
        print("The highscore.txt file doesn't exist. Please restore the file or"
              "create a new one.")
        return []


def file_processor(score, highscore):
    """ Function file_processor
        Params: An int with the current player's score and a string containing
                the file name with the highscore data.
        Returns: Nothing. Prompts the new top scorer for their name and writes
                 everything into a file
    """
    try:
        top_score = fetch_highscore(highscore)
        top_score_int = top_score[0]
        name = input("Please enter your name: ")
        score_name = str(score) + "\n" + name
        if score > int(top_score_int):
            outfile = open(highscore, 'w')
            outfile.write(score_name)
            outfile.close()
    except OSError:
        print("The highscore.txt file doesn't exist. Please restore the file or"
              "create a new one.")


def game_over(hero, villains):
    ''' Function game_over
        Params: Two objects, one of class hero and  another of villain.
        Returns: A boolean which is true if the hero collides with a villain.
    '''
    for villain in villains:
        if euclidean(villain.villain.xcor(), villain.villain.ycor(), hero.t.xcor(), hero.t.ycor()) < 68:
            die(score_keeper)
            return True
        return False


# Code for the scoreboard after the game begins
turtle.goto(350, 335)
turtle.color('white')
turtle.pd()
turtle.width(30)
turtle.goto(-350, 335)
turtle.color('black')
turtle.width(5)
turtle.pu()
turtle.goto(200, 325)
turtle.write("Score: ", font=("Arial", 16, "bold"))
turtle.goto(-350, 325)
top_score = fetch_highscore(highscore)
top_score_str = str(top_score[0]) + ' by ' + str(top_score[1])
highscore_str = "Highscore: " + top_score_str
turtle.write(highscore_str, font=("Arial", 16, "bold"))
turtle.ht()

'''############################'''
###ALL CLASSES ARE CREATED HERE###
'''############################'''


class hero:
    t = turtle.Turtle()
    t.penup()
    t.setheading(north)
    t.speed(0)
    t.goto(0, -280)

    def key_up(self):
        hero.t.penup()
        hero.t.setheading(north)
        hero.t.forward(step)
        print(hero.t.pos())

    def key_left(self):
        hero.t.penup()
        hero.t.setheading(west)
        hero.t.forward(step)
        hero.t.setheading(north)
        print(hero.t.pos())

    def key_right(self):
        self.t.penup()
        self.t.setheading(east)
        self.t.forward(step)
        self.t.setheading(north)
        print(self.t.pos())

    def key_down(self):
        hero.t.penup()
        hero.t.setheading(south)
        hero.t.forward(step)
        hero.t.setheading(north)
        print(hero.t.pos())


class aliens():
    villain_chars = ['images/trash_1.gif', 'images/trash_2.gif', 'images/trash_3.gif', 'images/trash_4.gif']

    for alien in villain_chars:
        turtle.register_shape(alien)

    def __init__(self):
        self.villain = turtle.Turtle()
        self.alien_shape = random.choice(aliens.villain_chars)
        self.villain.shape(self.alien_shape)
        self.x = random.randint(-300, 300)
        self.y = random.randint(150, 300)
        self.villain.penup()
        self.villain.speed(0)
        self.villain.goto(self.x, self.y)

    def die(self):
        self.villain.ht()


class bullets():

    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.state = False
        self.t.speed(3)

    def shoot(self):
        self.t.st()
        self.t.state = True


class score_keeper():

    def __init__(self):
        self.t = turtle.Turtle()
        self.t.penup()
        self.score = 0
        self.t.speed(0)
        self.t.goto(350, 325)
        self.t.hideturtle()

    def update_score(self):
        self.t.undo()
        self.t.hideturtle()
        turtle.ht()
        self.t.write(self.score, align='right', font=("Arial", 16, "bold"))


'''############################'''
###THE MAIN PROGRAM STARTS HERE###
'''############################'''

##   Creating the necessary objects
hero = hero()
bullet = bullets()
score_keeper = score_keeper()
villains = []

##    Creating multiple villain objects and storing them in a list named villains
for i in range(villain_count):
    new_villain = aliens()
    villains.append(new_villain)

##    Selecting a random pokemon as the hero
hero_selector(hero, bullet)

##    Code for taking user input during the game
screen = turtle.Screen()
screen.onkey(hero.key_up, 'Up')
screen.onkey(hero.key_down, 'Down')
screen.onkey(hero.key_right, 'Right')
screen.onkey(hero.key_left, 'Left')
screen.onkey(bullet.shoot, ' ')
screen.listen()

##    Code to fix a bug where the hero does not die if the user gives no input
##    after the game starts.
game_over(hero, villains)

while True:

    ##    Code to break out of while loop and stop if the hero dies
    if game_over(hero, villains):
        break

    ##    Code for bullet movement and killing the pollutionators
    if bullet.t.state:
        bullet.t.setheading(north)
        bullet.t.forward(68)

        # Code for killing a villain when shot by a bullet
        for villain in villains:
            if euclidean(villain.villain.xcor(), villain.villain.ycor(), bullet.t.xcor(), bullet.t.ycor()) < 50:
                bullet.t.state = False
                bullet.t.goto(hero.t.pos())
                bullet.t.ht()
                villain.villain.ht()
                villains.remove(villain)
                score_keeper.score += 10
                score_keeper.update_score()

    # Code to bring back the bulllet to the hero's position for the next shot
    else:
        bullet.t.speed(0)
        bullet.t.goto(hero.t.pos())

    # Code to change the bullet's state after the shot
    if bullet.t.ycor() >= 350:
        bullet.t.state = False
        bullet.t.ht()

    ##    Code for moving the villains
    for i in range(len(villains)):

        if villains[i].x > 350:
            villains[i].x = -350
            # As the difficulty increases, the villains come down faster
            villains[i].y -= 50 + (difficulty * 10)
        # As the level increases, the villains move faster
        villain_step = step - i + (level * 5)
        villains[i].x += villain_step
        villains[i].villain.goto(villains[i].x, villains[i].y)

    ##    Code for transitioning into the next level after all the villains die
    if len(villains) == 0:
        level += 1
        turtle.goto(0, 325)
        levelup_str = "Level " + str(level) + " is loading..."
        turtle.write(levelup_str, align='center', font=("Arial", 16, "bold"))
        time.sleep(3)
        turtle.undo()
        hero_selector(hero, bullet)
        for i in range(villain_count):
            new_villain = aliens()
            villains.append(new_villain)

screen.mainloop()
