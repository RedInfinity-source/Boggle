# imports
import random
import ursina
from ursina import *
import enchant
from PyDictionary import PyDictionary

# the english dictionary 
dict = PyDictionary()
d = enchant.Dict("en_US")

ursina.SmoothFollow = True

def update():
    global SC, MM
    if end_game == False:
        # this is the timmer sc = secounds, mm = minits
        # timer
        SC += 1
        if SC == 60:
            SC = 0
            MM += 1
        timer.text = '{}:{}'.format(MM,SC)
        # new bord
        if MM == 60:
            letter_list = []
            MM = 0
            for item in cube_list:
                abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
                letter = random.choice(abc)
                item.text = letter
                if letter == 'j' or letter == 'x' or letter == 'z' or letter == 'q':
                    item.text_color = color.red
                else:
                    item.text_color = color.black
                letter_list.append(item.text)
        #pints
        Points.text = 'points: {}'.format(points)
    else:
        end = Text(text = 'end of the game'.upper(),color = color.black,scale = 4,origin = (0,0))


app = Ursina()
# eng of the game
end_game = False
# timer
MM,SC = 0,0
timer = Text(text = '{}:{}'.format(MM,SC),position=(0,0.4),scale = 2,color = color.black)

# the letter desplaed on the bord
points = 0
Points = Text(text = 'points: {}'.format(points),position=(-0.05,0.35),scale = 2)
class Letter(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__()
        self.parent = scene
        self.position = position
        self.model = 'cube'
        self.color = color.white
        self.texture = 'white_cube'
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
        letter = random.choice(abc)
        self.text = letter
        if self.text == 'j' or self.text == 'x' or self.text == 'z' or self.text == 'q':
            self.text_color = color.red
        else:
            self.text_color = color.black
        self.highlight_color = self.color
        self.text_origin = (0, 0, -0.7)

# making the words and definitions from your input
class Word(Button):
    def __init__(self, input,position=(0,0,0)):
        super().__init__()
        global points
        self.parent = scene
        self.position = position
        self.text = input
        self.color = color.white
        if len(self.text) > 2:
            if d.check(self.text) == True:
                self.text_color = color.black
                self.tooltip = Tooltip(text=str(dict.meaning(self.text)))
                # check iff the letters are there
                check = 0
                input_list = list(self.text)
                for x in input_list:
                    if x in letter_list:
                        check = 1
                    else:
                        check = 0
                        break

                if check == 1:
                    # add more points
                    points += len(self.text)
                    if 'j' in self.text or 'x' in self.text or 'z' in self.text in self.text or 'q' in self.text:
                        points *= 2
            else:
                self.text_color = color.red
                self.tooltip = Tooltip(text='"{}" is not a word'.format(self.text))
        else:
            self.text_color = color.red
            self.tooltip = Tooltip(text='"{}" is to short'.format(self.text))
        self.highlight_color = self.color

# input filed and submit button
field = InputField(y=-.29, x = 0.06,limit_content_to='abcdefghijklmnopqrstuvwxyz ')

copy_list = []
number_of_inputs = -2
wx = -2
def submit():
    global number_of_inputs,wx, end_game
    if field.text not in copy_list:
        number_of_inputs += 1
        word = Word(input=field.text,position = (wx,number_of_inputs))
        if word.y == 6:
            if word.y == 6 and wx == -4:
                end_game = True
            wx -= 1
            number_of_inputs = -2
            word.y = -2
        copy_list.append(field.text)
    else:
        print_on_screen(text = 'you have already used that word',position = (-0.1,-0.33))
    field.text = ''

Button('Submit', scale=.1,y=-.29, x = 0.35,color=color.cyan.tint(-.4),on_click=submit).fit_to_text()

# add the words to the display
letter_list = []
cube_list = []
for y in range(4):
    for x in range(4):
        cube = Letter(position = (x,y))
        cube_list.append(cube)
        letter_list.append(cube.text)

# camera
camera.y = 1.5
camera.x = 1
app.run()
