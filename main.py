import pygame
import random, sys, time
import nltk
from nltk.corpus import words
nltk.download('words')
nltk.download('punkt')

pygame.init()
current_time = time.time()
random.seed(current_time)
# Load the set of words from NLTK
word_list = set(words.words())
# Seting up the display
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()

# color
def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
colors = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "DIM_GRAY": (105,105,105)
}

# button
class Button:
    def __init__(self, x, y, width, height, text, active_color, inactive_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.color = self.inactive_color
        self.textColor = colors['BLACK']
        self.origional_textColor = self.textColor
        self.font_size = min(self.width // len(self.text) + 10, self.height)
        self.font = pygame.font.Font(None, self.font_size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 2)
        text_surface = self.font.render(self.text, True, self.textColor)
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            self.color = self.active_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True
                    self.textColor = self.active_color
                    self.color = self.active_color
        else:
            self.color = self.inactive_color
            self.textColor = self.origional_textColor

    def reset(self):
        self.clicked = False
        self.color = self.inactive_color
        self.textColor = self.origional_textColor
restartGame = Button((WIDTH // 2) - 50, (HEIGHT // 2) - 50, 100, 100, "Play", colors['RED'], colors['BLACK'])

# text
class Text:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.textColor = colors["BLACK"]
        self.font_size = 32
        self.font = pygame.font.Font(None, self.font_size)
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','qu', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

    def updateText(self, new_text):
        self.text = new_text  # Update the text attribute
        self.text_surface = self.font.render(self.text, True, self.textColor)
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)

# update
def updateTimer(ms, ss, mm, hh):
    ms += 1
    if ms >= 60:
        ms = 0
        ss += 1
    if ss >= 60:
        ss = 0
        mm += 1
    if mm >= 60:
        mm = 0
        hh += 1
    return ms, ss, mm, hh

ms, ss, mm, hh = 0, 0, 0, 0
computerPoints, playerPoints = 0, 0
turns = 0
show_timer = Text(64, 32/2, f"{ms}:{ss}:{mm}:{hh}")
show_points = Text(480, 32/2, f"Computer Points: {computerPoints}    Player Points {playerPoints}")
show_truns = Text((WIDTH // 2) - 16, 80, f"Turns: {turns}")

# create board
letters_list = []
for x in range(4):
   for y in range(4):
       show_letter = Text((WIDTH // 2) - 32 * x, (HEIGHT // 2) - 32 * y, "")
       show_letter.updateText(random.choice(show_letter.abc).upper())
       letters_list.append(show_letter)

# MultiLine
class MultiLineInput:
    def __init__(self, x, y, width, height, font, text_color=(255, 255, 255), background_color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text_color = text_color
        self.background_color = background_color
        self.lines = [""]
        self.max_lines = height // font.get_height()  # Calculate the max number of lines that can fit in the input box
        self.cursor_position = [0, 0]  # Line index, char index

    def add_char(self, char):
        line, char_idx = self.cursor_position
        self.lines[line] = self.lines[line][:char_idx] + char + self.lines[line][char_idx:]
        self.cursor_position[1] += 1

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.enter_line()
            elif event.key == pygame.K_BACKSPACE:
                self.delete_char()
            else:
                self.add_char(event.unicode)

    def enter_line(self):
        line, char_idx = self.cursor_position
        new_line = self.lines[line][char_idx:]  # Split the line at the cursor
        self.lines[line] = self.lines[line][:char_idx]  # Keep the first part of the split in the current line
        self.lines.insert(line + 1, new_line)  # Insert the new line
        self.cursor_position = [line + 1, 0]  # Move the cursor to the start of the new line

    def delete_char(self):
        line, char_idx = self.cursor_position
        if char_idx > 0:  # If not at the start of the line, delete a character
            self.lines[line] = self.lines[line][:char_idx - 1] + self.lines[line][char_idx:]
            self.cursor_position[1] -= 1
        elif line > 0:  # At the start of the line, merge with the previous line
            self.cursor_position = [line - 1, len(self.lines[line - 1])]
            self.lines[line - 1] += self.lines[line]
            del self.lines[line]

    def draw(self, surface):
        surface.fill(self.background_color, self.rect)
        y_offset = 0
        for line in self.lines:
            text_surface = self.font.render(line, True, self.text_color)
            surface.blit(text_surface, (self.rect.x, self.rect.y + y_offset))
            y_offset += self.font.get_height()

    def read_words_per_line(self):
        """ Returns a list of lists, each containing words from the corresponding line. """
        words_per_line = [line.split() for line in self.lines]
        return words_per_line
    
    def clear_input(self):
        """ Resets the text lines and cursor position. """
        self.lines = [""]
        self.cursor_position = [0, 0]
show_MultiLineInput = MultiLineInput(10,(HEIGHT // 2) + 50,WIDTH - 20,(HEIGHT // 2) - 60,font = pygame.font.Font(None, 32), background_color=colors['DIM_GRAY'])

# Create a function to check if a word can be formed from the given letters
def generate_words():
    word_list = set(words.words())
    num_random_words = random.randint(1,20)
    # Create a function to check if a word can be formed from the given letters
    def is_valid_word(word, letters):
        letters_list = list(letters)
        for letter in word:
            if letter in letters_list:
                letters_list.remove(letter)
            else:
                return False
        return True
    
    valid_words = [word for word in word_list if is_valid_word(word, get_collect_letters())]
    if len(valid_words) > 0:
        random_slice = random.sample(valid_words, min(num_random_words, len(valid_words)))
    else:
        random_slice = []
    print(random_slice)
    return random_slice

""" check if letters are in the board """
def get_collect_letters():
    return set(letter.text.lower() for letter in letters_list)

def boardCheck(word):
    collect_letters = get_collect_letters()
    form_word = all(char.lower() in collect_letters for char in word)
    return form_word

""" Check if a word uses the same letter more than once """
def has_unique_letters(word):
    seen_letters = set()
    for letter in word:
        if letter in seen_letters:
            return False
        seen_letters.add(letter)
    return True

# deeper level of points
def Deeper_CalculatePoints(string):
    string_size = len(string)
    if 'qu' in string:
        string_size += 2 
    # Return points based on adjusted string size using conditional expressions
    if string_size >= 8:
        return 7
    elif string_size == 7:
        return 5
    elif string_size == 6:
        return 3
    elif string_size == 5:
        return 2
    elif string_size >= 3:
        return 1
    else:
        return 0
    
# points
def CalculatePoints(words_list):
    repeated_words = set()
    total_points = 0

    for word in words_list:
        for normalized_word in word:
            normalized_word = word.lower()
            if len(normalized_word) >= 3 and normalized_word not in repeated_words and has_unique_letters(normalized_word):
                if normalized_word in word_list:
                    if boardCheck(normalized_word):
                        repeated_words.add(normalized_word)
                        total_points += Deeper_CalculatePoints(normalized_word)
    try:
        show_MultiLineInput.clear_input()
    except:
        pass
    return total_points

# loop
def main():
    global turns, ms, ss, mm, hh, computerPoints, playerPoints
    totalPoints = random.choice(["50","100"])
    last_minute = 0
    endGame = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            show_MultiLineInput.handle_event(event)
            restartGame.handle_event(event)
            if restartGame.clicked:
                restartGame.reset()
                last_minute = 0
                endGame = False
                ms, ss, mm, hh = 0, 0, 0, 0
                computerPoints, playerPoints = 0, 0
                turns = 0
        screen.fill(colors["WHITE"])
        # game
        if endGame == False:
            # timer
            ms, ss, mm, hh = updateTimer(ms, ss, mm, hh)
            show_timer.updateText(f"{ms}:{ss}:{mm}:{hh}")
            show_timer.draw(screen)
            # board
            for letter in letters_list:
                letter.draw(screen)
            # MultiLine Input
            show_MultiLineInput.draw(screen)
            # end round
            if ss - last_minute > 3:
                turns += 1
                playerPoints += CalculatePoints(show_MultiLineInput.read_words_per_line())
                computerPoints += CalculatePoints(generate_words())
                last_minute = ss
                for letter in letters_list:
                    letter.updateText(random.choice(show_letter.abc).upper())
            # change endGame state
            if (computerPoints >= int(totalPoints) or playerPoints >= int(totalPoints)):
                endGame = True
        # points
        show_points.updateText(f"Computer Points: {computerPoints}    Player Points {playerPoints}")
        show_points.draw(screen)
        # turns
        show_truns.updateText(f"Turns: {turns}")
        show_truns.draw(screen)
        if endGame:
            show_points.x = WIDTH // 2
            restartGame.draw(screen)
        else:
            show_points.x = 480
        # This is to update the scene
        clock.tick(64)
        pygame.display.flip()
        pygame.display.update()

if __name__ == "__main__":
    main()
