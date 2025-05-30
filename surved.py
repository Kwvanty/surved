from pygame import *
import pygame
from random import randint
font.init()
pygame.mixer.init()



a2 = 0
a3 = 0
a4 = 0
a7 = 0
a8 = 0
a9 = 0

b4 = 0

font = font.Font(None, 30)
font2 = pygame.font.SysFont('Comicsansms', 50)

Builder_on = font2.render('Режим будівництва увімкнено', True, (0, 255, 0))
Builder_off = font2.render('Режим будівництва вимкнено', True, (255, 0, 0))

window = pygame.display.set_mode((1000, 700))
background1 = transform.scale(image.load('bg.jpg'), (1000, 700))
screen_width = 1200
screen_heigth = 708

class Game_Spaite():
    def __init__(self, x, y, width, height, filename):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = transform.scale(pygame.image.load(filename), (width, height))
    def show(self):
        window.blit(self.image, self.rect)

class Player(Game_Spaite):
    def __init__(self, x, y, width, height, filename):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = transform.scale(pygame.image.load(filename), (width, height))
    def show(self):
        window.blit(self.image, self.rect)

heart = Game_Spaite(50, 200, 30, 30, 'heart.png')
heart1 = Game_Spaite(50, 240, 30, 30, 'heart.png')
heart2 = Game_Spaite(50, 280, 30, 30, 'heart.png')
heart3 = Game_Spaite(50, 320, 30, 30, 'heart.png')
heart4 = Game_Spaite(50, 360, 30, 30, 'heart.png')
heart5 = Game_Spaite(50, 400, 30, 30, 'heart.png')
heart6 = Game_Spaite(50, 440, 30, 30, 'heart.png')
heart7 = Game_Spaite(50, 480, 30, 30, 'heart.png')
heart8 = Game_Spaite(50, 520, 30, 30, 'heart.png')
heart9 = Game_Spaite(50, 560, 30, 30, 'heart.png')


inventory_cell_sellect = Game_Spaite(10, 200, 30, 30, 'inventory_select.png')
inventory_cell1 = Game_Spaite(10, 200, 30, 30, 'inventory.png')
inventory_cell2 = Game_Spaite(10, 240, 30, 30, 'inventory.png')
inventory_cell3 = Game_Spaite(10, 280, 30, 30, 'inventory.png')
inventory_cell4 = Game_Spaite(10, 320, 30, 30, 'inventory.png')
inventory_cell5 = Game_Spaite(10, 360, 30, 30, 'inventory.png')
inventory_cell6 = Game_Spaite(10, 400, 30, 30, 'inventory.png')
fps = pygame.time.Clock()

player = Player(500, 500, 25, 35, 'player.png')
player_in_the_water_img = Player(500, 500, 25, 35, 'player_w.png')

def draw_grid():
    for line in range(0, 100):
        pygame.draw.line(window, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(window, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_heigth))
mouse_x, mouse_y = pygame.mouse.get_pos()
a10 = 0
tile_size = 60
a5 = randint(300, 700)
a6 = randint(300, 700)
tree = Game_Spaite(500, 500, 120, 120, 'tree.png')
Cobblestounik = Game_Spaite(500, 500, 120, 120, 'stone_block.png')
wood_log = Game_Spaite(0, 0, 20, 20, 'wood_log.png')
wood_log_in_inventory_o = Game_Spaite(10, 200, 40, 40, 'wood_log.png')
wood_block_in_inventory1 = Game_Spaite(15, 605, 25, 25, 'wood_block.png')
wood_block_in_inventory2 = Game_Spaite(15, 245, 25, 25, 'wood_block.png')
apple = Game_Spaite(0, 0, 20, 20, 'apple.png')
apple_in_inventory_o = Game_Spaite(10, 280, 40, 40, 'apple.png')

zombie = Player(-100, -100, 25, 35, 'zombie.png')

player_hit_up = Game_Spaite(-100, -100, 9, 5, 'null.png')
player_hit_down = Game_Spaite(-100, -100, 9, 5, 'null.png')
player_hit_left = Game_Spaite(-100, -100, 5, 9, 'null.png')
player_hit_right = Game_Spaite(-100, -100, 5, 9, 'null.png')

zombie_agro_hit_up = Game_Spaite(-100, -100, 1000, 500, 'null.png')
zombie_agro_hit_down = Game_Spaite(-100, -100, 1000, 500, 'null.png')
zombie_agro_hit_left = Game_Spaite(-100, -100, 500, 1000, 'null.png')
zombie_agro_hit_right = Game_Spaite(-100, -100, 500, 1000, 'null.png')

pickaxe = Game_Spaite(10, 320, 30, 30, 'pickaxe.png')
craft_pickaxe = Game_Spaite(40, 600, 30, 30, 'pickaxe.png')

player_menu = Game_Spaite(-400, 570, 50, 70, 'player.png')
zombie_menu = Game_Spaite(-570, 570, 50, 70, 'zombie.png')

startmenu = transform.scale(image.load('startmenu.jpg'), (1000, 700))
button_play = Game_Spaite(400, 300, 200, 80, 'button_play.jpg')
button_exit = Game_Spaite(400, 400, 200, 80, 'button_exit.jpg')

Cobblestone_inventory = Game_Spaite(10, 320, 30, 30, 'stone_block.png')

shaht = Game_Spaite(-300, -300, 300, 200, 'shaht.png')

p = False

def spawn(a, d):
    a.show()
    d = True
    return d

def kill(a, b):
    a.rect.x = -100
    a.rect.y = -100
    b = False
    return b

if 'Kwvanty' != 'gey':
    class World():
        def __init__(self, data):
            self.tile_list = []
            grass_block_img = pygame.image.load('grass_block.png')
            stone_block_img = pygame.image.load('stone_block.png')
            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(grass_block_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(stone_block_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                window.blit(tile[0], tile[1])


    

    class Objekts_in_the_world():
        def __init__(self, data_obj):
            self.tile_list_obj = []
            crafting_table_img = pygame.image.load('crafting_table.png')
            wood_block_img = pygame.image.load('wood_block.png')
            row_count_obj = 0
            for row_obj in data_obj:
                col_count_obj = 0
                for tile_obj in row_obj:
                    if tile_obj == 1:
                        img_obj = pygame.transform.scale(crafting_table_img, (tile_size, tile_size))
                        img_rect_obj = img_obj.get_rect()
                        img_rect_obj.x = col_count_obj * tile_size
                        img_rect_obj.y = row_count_obj * tile_size
                        tile_obj = (img_obj, img_rect_obj)
                        self.tile_list_obj.append(tile_obj)
                    if tile_obj == 2:
                        img_obj = pygame.transform.scale(wood_block_img, (tile_size, tile_size))
                        img_rect_obj = img_obj.get_rect()
                        img_rect_obj.x = col_count_obj * tile_size
                        img_rect_obj.y = row_count_obj * tile_size
                        tile_obj = (img_obj, img_rect_obj)
                        self.tile_list_obj.append(tile_obj)
                    col_count_obj += 1
                row_count_obj += 1

        def draw(self):
            for tile_obj in self.tile_list_obj:
                window.blit(tile_obj[0], tile_obj[1])    

    tile_size_inv = 30

    class Craft():
        def __init__(self, data_inv):
            self.tile_list_inv = []
            inventory_img = pygame.image.load('inventory.png')
            row_count_inv = 0
            for row_inv in data_inv:
                col_count_inv = 0
                for tile_inv in row_inv:
                    if tile_inv == 1:
                        img_inv = pygame.transform.scale(inventory_img, (tile_size_inv, tile_size_inv))
                        img_rect_inv = img_inv.get_rect()
                        img_rect_inv.x = col_count_inv * tile_size_inv + 10
                        img_rect_inv.y = row_count_inv * tile_size_inv + 601
                        tile_inv = (img_inv, img_rect_inv)
                        self.tile_list_inv.append(tile_inv)
                    col_count_inv += 1
                row_count_inv += 1

        def draw(self):
            for tile_inv in self.tile_list_inv:
                window.blit(tile_inv[0], tile_inv[1])   
    tile_size_inv1 = 30
    class INVENTORY():
        def __init__(self, data_inv1):
            self.tile_list_inv1 = []
            inventory_img = pygame.image.load('inventory.png')
            row_count_inv1 = 0
            for row_inv1 in data_inv1:
                col_count_inv1 = 0
                for tile_inv1 in row_inv1:
                    if tile_inv1 == 1:
                        img_inv1 = pygame.transform.scale(inventory_img, (tile_size_inv, tile_size_inv))
                        img_rect_inv1 = img_inv1.get_rect()
                        img_rect_inv1.x = col_count_inv1 * tile_size_inv1 + 10
                        img_rect_inv1.y = row_count_inv1 * tile_size_inv1 + 10
                        tile_inv = (img_inv1, img_rect_inv1)
                        self.tile_list_inv1.append(tile_inv)
                    col_count_inv1 += 1
                row_count_inv1 += 1

        def draw(self):
            for tile_inv1 in self.tile_list_inv1:
                window.blit(tile_inv1[0], tile_inv1[1])   
    INVENTORY_data_inv1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    Craft_data_inv = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    Objekts_in_the_world_data_obj = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    world_data_scene_1 = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [0, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
    ]
    world_data_scene_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    inv2 = INVENTORY(INVENTORY_data_inv1)
    inv = Craft(Craft_data_inv)
    obj = Objekts_in_the_world(Objekts_in_the_world_data_obj)
    world = World(world_data_scene_1)
    world2 = World(world_data_scene_2)
    world3 = World(world_data_scene_2)
    craftinghit = Game_Spaite(255, 135, 30, 30, 'crafting_table.png')
    def Check_collision(sprite, tiles):
        global gravitation, vel_y
        for tile in tiles:
            if sprite.colliderect(tile[1]):
                return True
        return False
    print(a5, a6)
    if Check_collision(tree.rect, world.tile_list):
        tree.rect.x = randint(0, 800)
        tree.rect.y = randint(0, 600)

    wood_log_in_inventory = 0
    wood_block_in_inventory = 0
    cell = 1
    selected = 1
    a1 = 1
    def player_in_the_water():
        global player_in_the_water_img, a1
        a1 = 0

menu_loop = True
game_loop = False

hp = 10
pl_sp = 4
Cobblestone_inv = 0
b1 = 0
b2 = 0
b3 = 0
b5 = 0
b6 = 0
open_shaht = 0
scene_y = 1
scene_x = 1
apples_in_inventory = 0
zombie_xp = 10
floos = 0
while menu_loop:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.rect.collidepoint(pygame.mouse.get_pos()):
                    menu_loop = False
                    game_loop = True
                if button_exit.rect.collidepoint(pygame.mouse.get_pos()):
                    menu_loop = False
    window.blit(startmenu, (0, 0))
    button_exit.show()
    button_play.show()
    player_menu.show()
    zombie_menu.show()
    zombie_menu.rect.x += 4
    player_menu.rect.x += 4
    if player_menu.rect.x >= 1600:
        player_menu.rect.x = -100
    if zombie_menu.rect.x >= 1600:
        zombie_menu.rect.x = -100
    fps.tick(60)
    pygame.display.update()

zombie.rect.x = 500
zombie.rect.y = 100

#        pygame.mixer.music.play(musik_1)
while game_loop:
    if floos != 0:
        floos -= 1
    if zombie.rect.colliderect(player.rect) and floos == 0:
        floos = 60
        hp -= 1
    zombie_agro_hit_up.rect.y = zombie.rect.y - 500
    zombie_agro_hit_up.rect.x = zombie.rect.x - 500
    zombie_agro_hit_down.rect.y = zombie.rect.y
    zombie_agro_hit_down.rect.x = zombie.rect.x - 500
    zombie_agro_hit_left.rect.y = zombie.rect.y - 500
    zombie_agro_hit_left.rect.x = zombie.rect.x - 500
    zombie_agro_hit_right.rect.y = zombie.rect.y - 500 
    zombie_agro_hit_right.rect.x = zombie.rect.x 

    


    b6 += 1
    if b6 >= 100:
        b6 = 0
        b5 += 1
    
    mouse_x, mouse_y = mouse.get_pos()
    row = mouse_y // tile_size
    col = mouse_x // tile_size
    if 'Kwvanty' != 'gey':

        window.blit(background1, (0, 0))
        if player.rect.x >= 1000 and scene_x == 1:
            scene_x += 1
            player.rect.x = 10
            zombie.rect.x = -10
        if player.rect.x <= 0 and scene_x == 2:
            scene_x -= 1
            zombie.rect.x = 800
            player.rect.x = 980
        if player.rect.y >= 700 and scene_y == 1:
            scene_y += 1
            player.rect.y = 10
            zombie.rect.y = 10
        if player.rect.y <= 0 and scene_y == 2:
            scene_y -= 1
            player.rect.y = 680
            zombie.rect.y = 680
        if scene_x == 2:
            world3.draw()
            b4 = 1
        else:
            b4 = 0
        if scene_y == 1 and scene_x == 1:
            tree.show()
            world.draw()
            obj.draw()
        if scene_y == 2 and scene_x != 2:
            world2.draw()
        a9 = 0
        if a3 != 0:
            a3 -= 1
        inventory_cell1.show()
        inventory_cell2.show()
        inventory_cell3.show()
        inventory_cell4.show()
        inventory_cell5.show()
        inventory_cell6.show()
        
        #zombie_agro_hit_up.show()
        #zombie_agro_hit_down.show()
        #zombie_agro_hit_left.show()
        #zombie_agro_hit_right.show()

        

        inventory_cell_sellect.show()
        if a7 == 0 and scene_y == 2:
            tree.show()
        if a7 == 1:
            wood_log.show() 
            apple.show()
        wood_log.rect.x = tree.rect.x + 20
        wood_log.rect.y = tree.rect.y + 20
        player_in_the_water_img.rect.x = player.rect.x
        player_in_the_water_img.rect.y = player.rect.y
        keys = pygame.key.get_pressed()
        m1, m2, m3 = pygame.mouse.get_pressed(num_buttons = 3)
        if b4 == 1:
            shaht.show()
            shaht.rect.x = 400
            shaht.rect.y = 100
        if b4 == 0:
            shaht.rect.x = -300
            shaht.rect.y = -300
        if m1:
            
            if tree.rect.collidepoint(pygame.mouse.get_pos()):
                a7 = 1
                apple.rect.x = tree.rect.x + 40
                apple.rect.y = tree.rect.y + 40
        if zombie_xp == 0:
            zombie.rect.x = randint(0, 1000)
            zombie.rect.y = randint(0, 700)
            zombie_xp = 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wood_block_in_inventory1.rect.collidepoint(pygame.mouse.get_pos()) and wood_log_in_inventory >= 1 and b3 == 1:
                    wood_log_in_inventory -= 1
                    wood_block_in_inventory += 4
                    a8 = 1
                if craftinghit.rect.collidepoint(pygame.mouse.get_pos()):
                    a3 = 10
                    a2 = 1
                    a4 = 1
                    b3 = 1
                if shaht.rect.collidepoint(pygame.mouse.get_pos()):
                    Cobblestone_inv += b5
                    b5 = 0
                if zombie.rect.collidepoint(pygame.mouse.get_pos()):
                    zombie_xp -= 1
        if m1 and cell == 3 and hp < 10 and apples_in_inventory >= 1:
            hp += 1
            apples_in_inventory -= 1

        if m2 and a3 == 0 and a10 == 0:
            a3 = 10
            cell += 1
            inventory_cell_sellect.rect.y += 40
        if cell == 7:
            cell = 1
            inventory_cell_sellect.rect.y = 200
        spawn(zombie, p)
        if not(Check_collision(zombie.rect, obj.tile_list_obj)):
            if player.rect.colliderect(zombie_agro_hit_up.rect):
                zombie.rect.y -= 2
            if player.rect.colliderect(zombie_agro_hit_down.rect):
                zombie.rect.y += 2
            if player.rect.colliderect(zombie_agro_hit_left.rect):
                zombie.rect.x -= 2
            if player.rect.colliderect(zombie_agro_hit_right.rect):
                zombie.rect.x += 2

        if Cobblestone_inv >= 1:
            Cobblestone_inventory.show()
        if m1 and a10 == 1 and Objekts_in_the_world_data_obj[row][col] == 0 and cell == 2 and wood_block_in_inventory >= 1:
            wood_block_in_inventory -= 1
            a9 = 1
            for i in range(2):
                obj = Objekts_in_the_world(Objekts_in_the_world_data_obj)
                Objekts_in_the_world_data_obj[row][col] = 2
        block_num = font.render(f'{wood_block_in_inventory}', True, (255, 255, 255))
        if a8 == 1:
            wood_block_in_inventory2.show()
            window.blit(block_num, (10, 240))
        if a4 == 1:
            inv.draw()
            wood_block_in_inventory1.show()
            craft_pickaxe.show()
        if not(Check_collision(player.rect, world.tile_list)):
            player_in_the_water()
            pl_sp = 2
        if Check_collision(player.rect, world.tile_list):
            a1 = 1
            pl_sp = 4
        if a1 == 0:
            player_in_the_water_img.show()
        if a1 == 1:
            player.show()
        
        if keys[pygame.K_d] and not(Check_collision(player_hit_right.rect, obj.tile_list_obj)):
            player.rect.x += pl_sp
        if keys[pygame.K_a] and not(Check_collision(player_hit_left.rect, obj.tile_list_obj)):
            player.rect.x -= pl_sp
        if keys[pygame.K_w] and not(Check_collision(player_hit_up.rect, obj.tile_list_obj)):
            player.rect.y -= pl_sp
        if keys[pygame.K_s]and not(Check_collision(player_hit_down.rect, obj.tile_list_obj)):
            player.rect.y += pl_sp
        if a10 == 0 and a3 == 0:
            if keys[pygame.K_z]:
                a10 = 1
                a3 = 10
                b1 = 300
                b2 = 0
        if a10 == 1  and a3 == 0:
            if keys[pygame.K_z]:
                a10 = 0
                a3 = 10
                b2 = 300
                b1 =0
        if a2 == 0 and a3 == 0:
            if keys[pygame.K_TAB]:
                a2 = 1
                a3 = 10
        if a2 == 1 and a3 == 0:
            if keys[pygame.K_TAB]:
                a2 = 0
                a3 = 10
                a4 = 0
                b3 = 0
        if a2 == 1:
            inv2.draw()
        if player.rect.colliderect(wood_log.rect) and a7 == 1:
            a7 = 0
            apples_in_inventory += randint(1, 2)

            wood_log_in_inventory += randint(4, 6)
            tree.rect.x = randint(0, 800)
            tree.rect.y = randint(0, 600)
        if keys[pygame.K_e]:
                a3 = 10
                a2 = 1
                a4 = 1
                wood_log.rect.x = randint(0, 800)
                wood_log.rect.y = randint(0, 600)
    if 'Kwvanty' != 'gey':
        apple_num = font.render(f'{apples_in_inventory}', True, (255, 255, 255))
        log_num = font.render(f'{wood_log_in_inventory}', True, (255, 255, 255))
        if apples_in_inventory >= 1:
            apple_in_inventory_o.show()
            window.blit(apple_num, (10, 280))
        if wood_log_in_inventory >= 1:
            wood_log_in_inventory_o.show()
            window.blit(log_num, (10, 200))
    if b1 != 0:
        b1 -= 2
        window.blit(Builder_on, (150, 10))
    if b2 != 0:
        b2 -= 2
        window.blit(Builder_off, (150, 10))
    if hp == 10:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
        heart4.show()
        heart5.show()
        heart6.show()
        heart7.show()
        heart8.show()
        heart9.show()
    if hp == 9:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
        heart4.show()
        heart5.show()
        heart6.show()
        heart7.show()
        heart8.show()
    if hp == 8:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
        heart4.show()
        heart5.show()
        heart6.show()
        heart7.show()
    if hp == 7:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
        heart4.show()
        heart5.show()
        heart6.show()
    if hp == 6:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
        heart4.show()
        heart5.show()
    if hp == 5:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
        heart4.show()
    if hp == 4:
        heart.show()
        heart1.show()
        heart2.show()
        heart3.show()
    if hp == 3:
        heart.show()
        heart1.show()
        heart2.show()
    if hp == 2:
        heart.show()
        heart1.show()
    if hp == 1:
        heart.show()
    if hp == 0:
        game_loop = False
    player_hit_up.rect.y = player.rect.y - 6
    player_hit_up.rect.x = player.rect.x
    player_hit_down.rect.y = player.rect.y + 27
    player_hit_down.rect.x = player.rect.x
    player_hit_left.rect.y = player.rect.y
    player_hit_left.rect.x = player.rect.x - 3
    player_hit_right.rect.y = player.rect.y
    player_hit_right.rect.x = player.rect.x + 23
    #player_hit_up.show()
    #player_hit_down.show()
    #player_hit_left.show()
    #player_hit_right.show()  

    fps.tick(60)
    pygame.display.update()
