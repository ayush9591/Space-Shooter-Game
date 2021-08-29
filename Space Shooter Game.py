import pygame
import sys
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([300, 511])
pygame.display.set_caption("Planet Game")

# variables
start = False
welcome = True
score = 0
life = 3
speed = 1
planet_x = 114
move_direction = 'right'
fired = False
bullet_y = 430
win = False
planet_index = 0
planets = ['gallery/Planet1.png', 'gallery/Planet2.png', 'gallery/Planet3.png', 'gallery/Planet4.png', 'gallery'
                                                                                                       '/Planet5.png']
exit_window = True
background = pygame.image.load('gallery/bg.png')
planet = pygame.image.load('gallery/Planet1.png')
space = pygame.image.load('gallery/spaceship.png')
bullet = pygame.image.load('gallery/bull.png')
MyImage = pygame.image.load('gallery/1.png')
# clock
clock = pygame.time.Clock()
# Font
font = pygame.font.SysFont(None, 30)


def show_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


def Welcome_Screen():
    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT or (event1.type == pygame.KEYDOWN and event1.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event1.type == pygame.KEYDOWN and event1.key == pygame.K_s:
                return
            else:
                screen.blit(background, [0, 0])
                show_text("Planet Game", (0, 255, 0), 88, 5)
                screen.blit(MyImage, [75, 30])
                # screen.blit(space, [123, 426])
                show_text("Game with AJ", (254, 64, 35), 80, 265)
                show_text("Press s for Start!", (223, 255, 0), 70, 305)
                show_text("High Score: " + str(h_score), (255, 105, 180), 70, 335)
                show_text("Esc for Exit!", (0, 0, 0), 70, 365)
                pygame.display.update()
                clock.tick(60)

def Final_Screen():
    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.KEYDOWN and event1.key == pygame.K_ESCAPE:
                return
            else:
                pygame.mixer.music.stop()
                screen.blit(background, [0, 0])
                show_text("Game Over!", (255, 0, 0), 90, 240)
                show_text("Press s for Restart!", (0, 255, 0), 45, 290)
                show_text("High Score: " + str(h_score), (255, 105, 180), 45, 320)
                show_text("Press any key for Exit!", (0, 0, 0), 45, 350)
                pygame.display.update()
                clock.tick(60)


# Loop
while exit_window:
    if not os.path.exists('h_score.txt'):
        with open('h_score.txt', 'w') as f:
            f.write("0")
    with open('h_score.txt', 'r') as f:
        h_score = int(f.read())
    if welcome:
        if score > h_score:
            h_score = score
            with open("h_score.txt", "w") as f:
                f.write(str(h_score))

        # reset variable
        score = 0
        speed = 1
        life = 3
        if start == True:
            Final_Screen()
        start = True
        Welcome_Screen()
        pygame.mixer.music.load('gallery/back.mp3')
        pygame.mixer.music.play()
        welcome = False
    # Events
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        fired = True
    if move_direction == 'right':
        planet_x = planet_x + speed
        if planet_x >= 234:
            move_direction = 'left'
    else:
        planet_x = planet_x - speed
        if planet_x <= 0:
            move_direction = 'right'
    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 65:
            fired = False
            if win:
                score += 10
                if score == (2 * speed - 1)*100:
                    speed += 1
                    life += 1
                win = False
                planet_index += 1
                if planet_index >= 5:
                    planet_index = 0
                planet = pygame.image.load(planets[planet_index])
                # planet_x = random.randrange(10, 230, 10)
            else:
                life = life - 1
                if life == 0:
                    welcome = True
            bullet_y = 430
    # blit
    screen.blit(background, [0, 0])
    screen.blit(planet, [planet_x, 30])
    screen.blit(bullet, [144, bullet_y])
    screen.blit(space, [123, 426])
    show_text("Score: " + str(score), (255, 191, 0), 5, 5)
    show_text("Life: " + str(life), (255, 0, 0), 220, 5)
    if bullet_y < 100 and 80 < planet_x < 150:
        win = True

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_window = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            welcome = True
pygame.quit()
