import pygame
import os


# Format of name: "\Living_room"
def rename(path, name):
    head, tail = os.path.split(path)
    ext = str(tail).split('.')
    new_name = head + name + '.' + ext[-1]
    for i in range(1, 10):
        if os.path.isfile(new_name):
            new_name = head + name + '_' + str(i) + '.' + ext[-1]
    os.rename(path, new_name)


directory = "D:\Test"
file_path = []
for root, subdirectories, files in os.walk(directory):
    for file in files:
        file_path.append(str(os.path.join(root, file)))

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Labeling")

running = True
clock = pygame.time.Clock()
BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('sans', 38)
start = font.render('Start Labeling', True, WHITE)
living_room = font.render('Living Room', True, WHITE)
bedroom = font.render('Bedroom', True, WHITE)
bathroom = font.render('Bathroom', True, WHITE)
kitchen = font.render('Kitchen', True, WHITE)
dining_room = font.render('Dining room', True, WHITE)
street_view = font.render('Street view', True, WHITE)
exterior = font.render('Exterior', True, WHITE)
discard = font.render('Discard', True, WHITE)

i = -1
DEFAULT_IMAGE_SIZE = (500, 500)
DEFAULT_IMAGE_POSITION = (50, 50)
discard_list = []

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    if i != -1 and i < len(file_path):
        image = pygame.image.load(file_path[i])
        image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        screen.blit(image, DEFAULT_IMAGE_POSITION)

    # pygame.draw.rect(screen, BLACK, (50, 50, 600, 400))
    # pygame.draw.rect(screen, WHITE, (55, 55, 590, 390))

    # Vẽ mấy cái button
    pygame.draw.rect(screen, BLACK, (700, 50, 250, 50))
    screen.blit(start, (720, 50))

    pygame.draw.rect(screen, BLACK, (700, 120, 250, 50))
    screen.blit(living_room, (720, 120))

    pygame.draw.rect(screen, BLACK, (700, 190, 250, 50))
    screen.blit(bedroom, (720, 190))

    pygame.draw.rect(screen, BLACK, (700, 260, 250, 50))
    screen.blit(bathroom, (720, 260))

    pygame.draw.rect(screen, BLACK, (700, 330, 250, 50))
    screen.blit(kitchen, (720, 330))

    pygame.draw.rect(screen, BLACK, (700, 400, 250, 50))
    screen.blit(dining_room, (720, 400))

    pygame.draw.rect(screen, BLACK, (700, 470, 250, 50))
    screen.blit(street_view, (720, 470))

    pygame.draw.rect(screen, BLACK, (700, 540, 250, 50))
    screen.blit(exterior, (720, 540))

    pygame.draw.rect(screen, BLACK, (700, 610, 250, 50))
    screen.blit(discard, (720, 610))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 700 < mouse_x < 950 and 50 < mouse_y < 100:
                i += 1
                print('Press Start')

            if i != -1 and i < len(file_path):
                if 700 < mouse_x < 950 and 120 < mouse_y < 170:
                    rename(file_path[i], '\Living_room')
                    i += 1
                    print('Press Living room')

                if 700 < mouse_x < 950 and 190 < mouse_y < 240:
                    rename(file_path[i], '\Bedroom')
                    i += 1
                    print('Press Bedroom')

                if 700 < mouse_x < 950 and 260 < mouse_y < 310:
                    rename(file_path[i], '\Bathroom')
                    i += 1
                    print('Press Bathroom')

                if 700 < mouse_x < 950 and 330 < mouse_y < 380:
                    rename(file_path[i], '\Kitchen')
                    i += 1
                    print('Press Kitchen')

                if 700 < mouse_x < 950 and 400 < mouse_y < 450:
                    rename(file_path[i], '\Dining_room')
                    i += 1
                    print('Press Dining room')

                if 700 < mouse_x < 950 and 470 < mouse_y < 530:
                    rename(file_path[i], '\Street_view')
                    i += 1
                    print('Press Street view')

                if 700 < mouse_x < 950 and 540 < mouse_y < 590:
                    rename(file_path[i], '\Exterior')
                    i += 1
                    print('Press Exterior')

                if 700 < mouse_x < 950 and 610 < mouse_y < 660:
                    discard_list.append(file_path[i])
                    i += 1
                    print('Press Discard')

    pygame.display.flip()

pygame.quit()

for i in range(len(discard_list)):
    os.remove(discard_list[i])