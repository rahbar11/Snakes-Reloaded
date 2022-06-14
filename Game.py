import sys
import pygame
pygame.init()

pygame.display.set_caption("Snakes Reloaded")

fps = 60
size = width, height = 900, 500
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

snake_parts = [[450, 330], [430, 330], [410, 330], [390, 330]]



def snake_movement(snake_parts, inner_box, snake_speed, snake_or_box_width, direction):
    if direction == '+x':
        new_position = [snake_parts[0][0] + snake_speed, snake_parts[0][1]]
    if direction == '-x':
        new_position = [snake_parts[0][0] - snake_speed, snake_parts[0][1]]
    if direction == '+y':
        new_position = [snake_parts[0][0], snake_parts[0][1] + snake_speed]
    if direction == '-y':
        new_position = [snake_parts[0][0], snake_parts[0][1] - snake_speed]
        
    snake_parts.insert(
        0, new_position)
    snake_parts.pop(-1)


def draw(box, inner_box, snake):
    screen.fill(black)
    pygame.draw.rect(screen, white, box)
    pygame.draw.rect(screen, black, inner_box)
    for snake_Rect in snake:
        pygame.draw.rect(screen, white, snake_Rect)
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    direction = '+x'
    frames = 0
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = '-y'
                if event.key == pygame.K_DOWN:
                    direction = '+y'
                if event.key == pygame.K_LEFT:
                    direction = '-x'
                if event.key == pygame.K_RIGHT:
                    direction = '+x'

        snake_speed = 20
        box_width, snake_width = 20, 20
        box = pygame.Rect(250, 50, 400, 400)
        inner_box = pygame.Rect(box.x + box_width, box.y + box_width,
                                box.width - box_width*2, box.height - box_width*2)
        snake = []
        for snake_part in snake_parts:
            x, y = snake_part
            snake_Rect = pygame.Rect(x, y, snake_width, snake_width)
            snake.append(snake_Rect)

        frames += 1
        if frames == 20:
            snake_movement(snake_parts, inner_box, snake_speed, snake_width, direction)
            frames = 0

        draw(box, inner_box, snake)


if __name__ == "__main__":
    main()
