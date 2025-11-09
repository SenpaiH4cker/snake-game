import pygame, random
pygame.init()
w, h = 500, 500
win = pygame.display.set_mode((w, h))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
black, green, red = (0, 0, 0), (0, 100, 0), (255, 0, 0),
size, speed = 10, 15
x, y, dx, dy = w // 2, h // 2, 0, 0
snake, length = [], 1
food = [random.randrange(0, w - size, size),random.randrange(0, h - size, size)]
def draw_snake():
    for s in snake:
        pygame.draw.rect(win, green, (*s, size, size))
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT and dx == 0:
                dx, dy = -size, 0
            elif e.key == pygame.K_RIGHT and dx == 0:
                dx, dy = size, 0
            elif e.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -size
            elif e.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, size
    x += dx
    y += dy
    if x < 0 or x >= w or y < 0 or y >= h:
        run = False
    win.fill(black)
    pygame.draw.rect(win, red, (*food, size, size))
    head = [x, y]
    snake.append(head)
    if len(snake) > length: 
        snake.pop(0)
    if head in snake[:-1]:
        run = False
    draw_snake()
    pygame.display.update()
    if x == food[0] and y == food[1]:
        food = [random.randrange(0, w - size, size),random.randrange(0, h - size, size)]
        length += 1
    clock.tick(speed)
pygame.quit()