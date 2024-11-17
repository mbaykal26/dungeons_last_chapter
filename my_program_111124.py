import pgzrun
import random
from pgzhelper import *
# Pencerenin Çizimi

mod = "menu"
winner = 0
attack = 0
puan = 0
enemy_list_index = -1
TITLE = "Stranger Skulls" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
map_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     
          ] # Hücüm Gücü ve Sağlık bilgisi


class Sprite(Actor):
    def __init__(self, normal):
        super().__init__(normal)
        self.health = 100
        self.attack = 5
        self.normal = normal
        #self.bad = bad
        self.enemies = []
        self.pos = (50, 50)
        topleft = (50,50)
        self.images = [normal]
        self.direction = "right"
    # vx = 5
    # vy = 5

    def update(self):
        if (keyboard.right or keyboard.d) and self.x + 50 < WIDTH:
            self.x += 2
            #self.images = [normal]
            #self.image = 'karakter'
            self.direction = "right"
            self.image = "karakter_right_attack" if keyboard.right else "karakter"  # Use 
        elif (keyboard.left or keyboard.a) and self.x - cell.width > cell.width - 30:
            self.x -= 2
            #self.images = []
            #self.image = 'sol'
            self.direction = "left"
            self.image = "karakter_sol_attack" if keyboard.left else "karakter" 
        elif (keyboard.down or keyboard.s) and self.y + 100 < HEIGHT:
            self.y += 2
        elif (keyboard.up or keyboard.w) and self.y + 50 > 100:
            self.y -= 2        


cell = Sprite("sinir")
cell1 = Sprite("zemin")
cell2 = Sprite("catlak")
cell3 = Sprite("kemikler")
cross = Sprite("carpi")
cross.pos = (770, 30)
set_sound = Sprite("bonus")
set_sound.pos = (550, 250)
exit_the_game = Sprite("bonus")
exit_the_game.pos = (400, 420)
play_the_game = Sprite("bonus")
play_the_game.pos = (250, 250)
screen_w = 16 # Ekranın enindeki hücre sayısı
height_h = 17# Ekranın boyundaki hücre sayısı
cell.width = 50
cell.height = 50
game_over = Actor("game_over")
WIDTH = cell.width * screen_w
HEIGHT = cell.height * height_h 
    
# Başrol Karakteri
my_character = Sprite('karakter')
my_character.images = ["karakter", "karakter_right_attack"]
#my_character_left.images = ["sol", "karakter_sol_attack"]
my_character.fps = 5
my_character.health = 100
my_character.attack = 5
my_character.top = cell.height
my_character.left = cell.width
arkaplan2 = Actor("arkaplan2")
walking_toggle = True
image_change_interval = 0.25  # Adjust this for a longer duration if needed

# Düşmanların Oluşturulması
enemies = []
def form_enemies():
    for i in range(10):
        x = random.randint(2, 15) * 50
        y = random.randint(2, 14) * 50
        enemy = Sprite("dusman")
        enemy.topleft = (x, y)
        enemy.health = random.randint(10, 20)
        enemy.attack = random.randint(5, 10)
        enemy.bonus = random.randint(0, 2)
        enemy.images = ["dusman", "dusman_flipped_running"]   #en son eklenenlerden
        enemy.direction = random.randint(-100, -80)
        enemies.append(enemy)

form_enemies()
# print(f"dusman.direction:{dusman.direction}")
# print(f"dusman.health:{dusman.direction}")
# print(f"dusman_numara:{dusman_numara}")
# Bonuses
hearts = []
swords = []


def map_sketch_menu():
    for i in range(len(map_list)):
        for j in range(len(map_list[0])):
            if map_list[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif map_list[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif map_list[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()
            elif map_list[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw()

# THE BELOW FUNCTION ADDED LATELY ABOUT CHANGING ENEMY IMAGES CERTAIN AMOUNTS OF TIME IN A SECOND
def toggle_enemy_images():
    for enemy in enemies:
        # Alternate the enemy image between two versions
        if enemy.image == "dusman":
            enemy.image = "dusman_running"
        else:
            enemy.image = "dusman"

clock.schedule_interval(toggle_enemy_images, 0.5)

# def harita_cizim():
#     for i in range(len(map_list)):
#         for j in range(len(map_list[0])):
#             cell1.left = cell.width*j
#             cell1.top = cell.height*i
#             cell1.draw()
# if mod == "menu":
#     sounds.level1.play(-1)
# elif mod == "oyun":
#     sounds.level2.play()                                                                                                                                                                                                                                                                                                                                                        

def draw():
    if mod == "menu":
        screen.fill("#Ff3542")    # be commented otherwise correct it
        map_sketch_menu()
        #arkaplan2.draw()
        #sounds.thaelmines.play()
        #sounds.peacefuldays.play(1000)
        #sounds.sfx_sounds_interaction25.play()
        play_the_game.draw()
        screen.draw.text("Play\n", center = (250, 240), color = "black", fontsize = 35)
        screen.draw.text("Game\n", center = (250, 280), color = "black", fontsize = 35)
        set_sound.draw()
        screen.draw.text("Play\n", center = (550, 240), color = "black", fontsize = 35)
        screen.draw.text("Sound Off\n", center = (550, 280), color = "black", fontsize = 35) 
        exit_the_game.draw()
        screen.draw.text("Exit Game\n", center = (400, 430), color = "black", fontsize = 35) 
        screen.draw.text("What are these strange skulls! You gotta kill them off! You are the one! You can make it!!!\n", center = (400, 830), color = "black", fontsize = 25)
        #screen.draw.text(str(my_character.pos) + "\n", center = (600, 600), color = "black", fontsize = 35)
        #print(oyna.pos, set_sound.pos)


    elif mod == "play": 
        #if attack == 0:       
        sounds.thaelmines.play()
        sounds.winning.stop()
        sounds.loser.stop()

        screen.fill("#2f3542")
        map_sketch_menu()
        my_character.draw()
        screen.draw.text("Health:\n", center=(50, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(my_character.health) + "\n", center=(130, 835), color = 'black', fontsize = 37)
        screen.draw.text("Attack:\n", center=(700, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(my_character.attack) + "\n", center=(780, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(my_character.pos) + "\n", center = (425, 835), color = "black", fontsize = 37)
        #screen.draw.text(str(dusman.health) + "\n", center = (760, 600), color = "black", fontsize = 37)
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()
        cross.draw()


    elif mod == "play_sound_off":     
        sounds.thaelmines.stop()
        sounds.winning.stop()
        sounds.loser.stop()           
        screen.fill("#2f3542")
        map_sketch_menu()
        my_character.draw()
        screen.draw.text("Health:\n", center=(50, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(my_character.health) + "\n", center=(130, 835), color = 'black', fontsize = 37)
        screen.draw.text("Attack:\n", center=(700, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(my_character.attack) + "\n", center=(780, 835), color = 'black', fontsize = 37)
        for i in range(len(enemies)):
            enemies[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(swords)):
            swords[i].draw()
        sounds.thaelmines.stop()
            # sounds.level1.stop()
            # sounds.level2.stop()
        cross.draw()
            
    elif mod == "end":
        screen.fill("#2f3542")
        if winner == 1:
            sounds.thaelmines.stop()
            sounds.winning.play(1)
            game_over.draw()
            screen.draw.text("WE GOTTA WINNER!\n", center=(400, 100), color = 'cyan', fontsize = 46)
            screen.draw.text("Click the space button to enter the menu!\n", center=(400, 750), color = 'cyan', fontsize = 25)
            # cross.draw()
            # cross.pos = (775,50)
            #screen.fill("red")
            # sounds.thaelmines.play()
            # sounds.militarybase.stop()
            # sounds.level1.stop()
            # sounds.level2.stop()

        else:
            sounds.thaelmines.stop()
            sounds.winning.stop()
            sounds.loser.play(1)
            game_over.draw()
            #screen.fill("purple")
            screen.draw.text("You are such a LOSER!\n", center=(400,100), color = 'cyan', fontsize = 46)
            screen.draw.text("Click the space button to enter the menu!\n", center=(400, 750), color = 'cyan', fontsize = 25)
            # cross.draw()
            # cross.pos = (775,50)
            # sounds.thaelmines.play()
            # sounds.militarybase.stop()
            # sounds.level1.stop()
            # sounds.level2.stop()

# def toggle_walking_image():
#     global walking_toggle, enemies
#     # Alternate between 'enemy_walk1' and 'enemy_walk2' to create a walking effect
#     for enemy in enemies:
#         if walking_toggle:
#             enemy.image = 'dusman'
#         else:
#             enemy.image = 'dusman_running'
#         walking_toggle = not walking_toggle

def on_key_down(key):
    global enemies, mod, hearts, swords   # hearts and swords variables added lately
    previous_x = my_character.x
    previous_y = my_character.y    
    enemy_list_index = my_character.collidelist(enemies)
    if enemy_list_index != -1: #and karakter.image == "karakter":
        #my_character.images = ["karakter", "karakter_right_attack"]
        attack = 1
        sounds.thaelmines.stop()
        sounds.eating_effect.play()
        my_character.image = "karakter_right_attack"
        
        my_character.x = previous_x
        my_character.y = previous_y
        enemy = enemies[enemy_list_index]
        enemy.health -= my_character.attack
        my_character.health -= enemy.attack
        if enemy.health <= 0:
            if enemy.bonus == 1:
                heart = Sprite('kalp')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                sword = Sprite('kilic')
                sword.pos = enemy.pos
                swords.append(sword)
            enemies.pop(enemy_list_index)
    elif enemy_list_index != -1 and my_character.image == "sol":
        my_character.images.extend(["sol", "karakter_sol_attack"])
        attack = 1
        sounds.thaelmines.stop()
        sounds.eating_effect.play()
        my_character.image = "karakter_sol_attack"
        my_character.images = ["sol", "karakter_sol_attack"]
        my_character.x = previous_x
        my_character.y = previous_y
        enemy = enemy[enemy_list_index]
        enemy.health -= my_character.attack
        my_character.health -= enemy.attack
        if enemy.health <= 0:
            if enemy.bonus == 1:
                heart = Sprite('kalp')
                heart.pos = enemy.pos
                hearts.append(heart)
            elif enemy.bonus == 2:
                sword = Sprite('kilic')
                sword.pos = enemy.pos
                swords.append(sword)
        # if dusman.health <= 0:
            # if dusman.bonus == 1:
            #     kalp = Actor('kalp')
            #     kalp.pos = dusman.pos
            #     kalpler.append(kalp)
            # elif dusman.bonus == 2:
            #     kilic = Actor('kilic')
            #     kilic.pos = dusman.pos
            #     kiliclar.append(kilic)
            enemies.pop(enemy_list_index)
    else:
        attack = 0
        my_character.image = "karakter"
        sounds.eating_effect.stop()

    if mod == "end" and keyboard.space:
        mod = "menu"
        enemies = []
        form_enemies()
        my_character.health = 100
        my_character.attack = 5
        my_character.pos = (50,50)  
        swords = []
        hearts = []                 

def if_win():
    global mod, winner
    if enemies == [] and my_character.health > 0:
        mod = "end"
        winner = 1
    elif my_character.health <= 0:
        mod = "end"
        winner = -1
enemy_speed = 2
enemy_direction = 1  # 1 for forward, -1 for backward
# UPDATE FUNCTION PART      
def update():
    global puan, enemies, enemy_list_index, enemy_speed, enemy_direction
    my_character.update()    
    if keyboard.right or keyboard.left or keyboard.up or keyboard.down:  
        my_character.animate()    
    else:
        my_character.image = "karakter"
    if_win()    
    for i in range(len(hearts)):
        if my_character.colliderect(hearts[i]):
            sounds.winning.play()
            my_character.health += 10
            hearts.pop(i)
            break
    for i in range(len(swords)):
        if my_character.colliderect(swords[i]):
            sounds.winning.play()
            my_character.attack += 7
            swords.pop(i)
            break    

    for i in range(len(enemies)):
        enemies[i].x += enemy_speed * enemy_direction
        change_cooldown = 2
        # enemies[i].update()     #en son eklenen kodlardan
        # enemies[i].animate() #en son eklenen kodlardan 

        # Keep the enemy within screen bounds
        if enemies[i].x < 100 :   #and dusmanlar[i].distance_to(karakter) > 200
            enemies[i].x = 100
            enemy_direction = 1  # Move forward
        elif enemies[i].x > WIDTH - 100:  # and dusmanlar[i].distance_to(karakter) > 200
            enemies[i].x = WIDTH - 100
            enemy_direction = -1  # Move backward

    def change_direction():
        global enemy_direction
        # Randomly change the direction (1 or -1)
        enemy_direction = random.choice([-1, 1])

    # Set a timer to change the direction every 1 to 2 seconds
    clock.schedule_interval(change_direction, random.uniform(1, 2))
    
    for enemy in enemies:
        #print(alien.distance_to(hero)) 
        if enemy.distance_to(my_character) <= 100:
            enemy.point_towards(my_character)
            my_character.point_towards(enemy)
            enemy.image = "dusman_flipped_running"     # the figure must be replaced with the image "dusman_running"
            enemy.move_towards(my_character, 1)
            # dusman.move_in_direction(2)
            # dusman.animate()
        


    # clock.schedule(dusmanlar_right, 2.0)   
    # def dusmanlar_left():        
    #     for i in range(len(dusmanlar)):
    #         dusmanlar[i].x = dusmanlar[i].x - hucre.width
    #         break


def on_mouse_down(button, pos):
    global mod
    if mouse.LEFT and mod == "menu":
        if play_the_game.collidepoint(pos):            
            mod = "play"
        elif set_sound.collidepoint(pos):
            mod = "play_sound_off"
        elif exit_the_game.collidepoint(pos):
            exit()
    elif mouse.LEFT and mod == "play":
        if cross.collidepoint(pos):
            mod = "menu"
    elif mouse.LEFT and mod == "play_sound_off": 
        if cross.collidepoint(pos):
            mod = "menu"
    # elif mouse.LEFT and mod == "end":
    #     if cross.collidepoint(pos):
    #         mod = "menu"

pgzrun.go()
