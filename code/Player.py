import pygame
from Settings import *
from support import import_folder
from staticmethod import * 
from pygame import mixer

class Player(pygame.sprite.Sprite):
    def __init__(self, position, object_sprites, groups, attack):
        super().__init__(groups)

        # Bild Drawn
        self.position = position
        self.image =  pygame.image.load(static.imagepath('Attack.png')).convert_alpha() # Bild in ordnerstruktur 
        self.image = pygame.transform.scale(self.image, Settings.player_size)# Position des Bildes
        self.rect = self.image.get_rect(topleft =self.position)
        self.mask = pygame.mask.from_surface(self.image) 
        self.hitbox = self.rect.inflate(Settings.hitboxplayer_x, Settings.hitboxplayer_y)# Masken für Kollisionserkennung
        
        # Setup
        self.import_player_assets()

        pygame.mixer.init
        
        
        self.status = 'down'
        self.frame_index = 0

        self.animation_speed = Settings.animation_speed
        
       # player Movement    
        self.movement = pygame.math.Vector2()              # Bewegungsvektor [Settings.directon_x, Settings.directon_y]
        
        self.attacking = False                             # Angriff
        self.attack_cooldown = Settings.attacking_cooldown # Angriff Cooldown
        self.attack_timer = None
        self.attack = attack
        self.weapon_index = 0
        self.weapon_list = list(weapon.keys())[self.weapon_index]
        print(self.weapon_list)

      # stats
        self.stats = {'health': 100, 'max_health': 100, 'mana': 100, 'max_mana': 100, 'strength': 10, 'magic': 10, 'speed': 3, 'defense': 10, 'resistance': 10}
        self.health = self.stats['health']
        self.mana = self.stats['mana']
        self.strength = self.stats['strength']
        self.magic = self.stats['magic']
        self.defense = self.stats['defense']
        self.resistance = self.stats['resistance']
        self.max_health = self.stats['max_health']
        self.max_mana = self.stats['max_mana']
        self.exp = 100
        self.speed = self.stats['speed']
        self.object_sprites = object_sprites# Gruppe aller Objekte
              
    def import_player_assets(self):
        character_path = static.path['player']
        self.animations = { 'up' :[], 'down': [], 'left': [], 'right': [], 'right_idle': [], 'left_idle': [], 
            'up_idle': [], 'down_idle': [], 'right_attack': [], 'left_attack': [], 'up_attack': [], 
            'down_attack': [],'left_roll': [], 'right_roll': [], 'up_roll': [], 'down_roll': []}
        

        
        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = import_folder(full_path)
        
        

    def sound_attack(self):
        pygame.mixer.Sound
        self.attack_sound_volume = 0.1
        attack_sound = pygame.mixer.Sound(static.soundpath("attack.wav"))
        pygame.mixer.Sound.play(attack_sound)
        attack_sound.set_volume(self.attack_sound_volume)

    def keys(self):
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            self.movement.x = -1
            self.status = 'left'
            
           # print(self.movement)
        elif pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:          # Rechts und links Bewegung
            self.movement.x = 1
            self.status = 'right'
            #print(self.movement) 
        else:
            self.movement.x = 0
            #print(self.movement)
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            self.movement.y = -1
            self.status = 'up'
            #print(self.movement)
        elif pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:          # Oben und unten Bewegung
            self.movement.y = 1
            self.status = 'down'
            #print(self.movement)
        else: 
            self.movement.y = 0

        # Attack
        leftclick = pygame.mouse.get_pressed()==(1,0,0)
        rightclick = pygame.mouse.get_pressed()==(0,0,1)

        if leftclick and not self.attacking:
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks()
            self.attack()#
            self.sound_attack()

        # spells
        if rightclick and not self.attacking:
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks()
            self.attack()
            self.sound_attack()
        # roll
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks()
            self.attack()
            self.sound_attack()



    def get_status(self):
        # idle status
        if self.movement.x == 0 and self.movement.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        if self.attacking:
            self.movement.x = 0
            self.movement.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:    
                    self.status = self.status + '_attack'
        else: 
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def anim(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation) :
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        
    def move(self):
        if self.movement.magnitude() != 0:
            self.movement = self.movement.normalize() * self.speed
        self.hitbox.x += self.movement.x * self.speed 
        self.collison('senkrecht')
        self.hitbox.y += self.movement.y * self.speed 
        self.collison('wagerecht')
        self.rect.center = self.hitbox.center

    def collison(self, movement):
        if movement == ('senkrecht'):
            for object in self.object_sprites:
                if object.hitbox.colliderect(self.hitbox):                    #if object.hitbox.colliderect(self.hitbox):
                    if self.movement.x > 0: # Rechts
                        self.hitbox.right = object.hitbox.left
                    elif self.movement.x < 0: # Links
                        self.hitbox.left = object.hitbox.right
        if movement == ('wagerecht'):
            for object in self.object_sprites:
                if object.hitbox.colliderect(self.hitbox):
                    if self.movement.y > 0:
                        self.hitbox.bottom = object.hitbox.top
                    elif self.movement.y < 0:
                        self.hitbox.top = object.hitbox.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_timer >= self.attack_cooldown:
                self.attacking = False

    def update(self):
        self.keys()
        self.cooldowns()
        self.get_status()
        self.anim()
        self.move()
