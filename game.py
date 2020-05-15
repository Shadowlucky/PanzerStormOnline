import pygame
from threading import *
from client_base import Network


def check_data(check):
    if len(check) > 3:
        return True
    elif check[0] not in ['create', 'change', 'delete']:
        return True
    if check[0] != 'delete':
        for i in check[1].split(','):
            try:
                int(i)
            except:
                return True
    return False


class Spawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, x, y):
        self.x += x
        self.y += y

    def get_coord(self):
        return f'{self.x},{self.y}'


class Wall:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self, display):
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(display, self.color, rect)


class Player:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, display):
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(display, self.color, rect)


class OtherPlayer:
    def __init__(self, x, y, w, h, name, address):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.address = address
        self.color = pygame.Color('blue')

        font = pygame.font.Font(None, 30)
        self.text = font.render(name, 1, (100, 100, 100))
        self.text_x = self.x + self.w // 2 - self.text.get_width() // 2
        self.text_y = self.y - 10

    def draw(self, display):
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(display, self.color, rect)
        display.blit(self.text, (self.text_x, self.text_y))

    def change(self, x, y):
        self.x = x
        self.y = y
        self.text_x = self.x + self.w // 2 - self.text.get_width() // 2
        self.text_y = self.y - 10


def thread():
    global n, other_players, key_send
    while True:
        reply = n.recv().split('$')
        for data in reply:
            data = data.split(';')
            if not data and data[0] == 'ok':
                pass
            elif data[0] == 'coords':
                x, y = data[1].split(',')
                if data[3] not in [i[1] for i in other_players]:
                    other_players.append(
                        [OtherPlayer(spawn.x + int(x), spawn.y + int(y), 40, 40, data[2], data[3]),
                         data[3]])
                else:
                    for enemy in other_players:
                        if enemy[0].address == data[3]:
                            enemy[0].change(spawn.x + int(x), spawn.y + int(y))
            elif data[0] == 'delete':
                for enemy in other_players:
                    if enemy[0].address == data[1]:
                        other_players.remove([enemy[0], data[1]])
                        continue
            if not running:
                break
            key_send = True


def move_objects(x, y):
    for wall in walls:
        wall.x -= x
        wall.y -= y
    for enemy in other_players:
        enemy[0].x -= x
        enemy[0].y -= y
        enemy[0].text_x -= x
        enemy[0].text_y -= y
    spawn.x -= x
    spawn.y -= y


def main(server, player_name='player'):
    global spawn, walls, running, key_send, n, other_players

    n = Network(server)
    other_players = []
    key_send = True

    pygame.init()
    pygame.display.set_caption('PZSO')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)

    your_name = player_name

    color_background = pygame.Color('black')
    color_wall = pygame.Color('gray')
    color_player = pygame.Color('yellow')
    color_spawn = pygame.Color('green')

    p_w, p_h = 40, 40
    p_x, p_y = (width - p_w) // 2, (height - p_h) // 2
    player = Player(p_x, p_y, p_w, p_h, color_player)
    move = 3
    fps = 50
    clock = pygame.time.Clock()

    spawn = Spawn(width // 2, height // 2, color_spawn)

    threading = Thread(target=thread)
    threading.start()

    delta_coord = f'{player.x - spawn.x},{player.y - spawn.y}'
    key_send = False
    n.send(f'{delta_coord};{your_name}')

    walls = [Wall(30, 30, 100, 20, color_wall), Wall(130, 30, 100, 20, color_wall)]

    running = True

    while running:
        button_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if button_pressed[pygame.K_UP] or button_pressed[pygame.K_DOWN] or \
                button_pressed[pygame.K_LEFT] or button_pressed[pygame.K_RIGHT]:
            if button_pressed[pygame.K_UP]:
                move_objects(0, -move)
            if button_pressed[pygame.K_DOWN]:
                move_objects(0, move)
            if button_pressed[pygame.K_LEFT]:
                move_objects(-move, 0)
            if button_pressed[pygame.K_RIGHT]:
                move_objects(move, 0)
            if key_send:
                delta_coord = f'{player.x - spawn.x},{player.y - spawn.y}'
                key_send = False
                n.send(f'{delta_coord};{your_name}')
        try:
            screen.fill(color_background)
        except:
            pygame.quit()
        if other_players:
            for enemy in other_players:
                enemy[0].draw(screen)

        player.draw(screen)

        for wall in walls:
            wall.draw(screen)

        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    ip = ''
    main(ip)
    pygame.quit()
