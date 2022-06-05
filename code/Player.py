import pygame
from Settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, position, object_sprites, groups, attack):
        super().__init__(groups)
        # Bild Drawn
        self.position = position
        self.image =  pygame.image.load(Settings.imagepath('Attack.png')).convert_alpha() # Bild in ordnerstruktur 
        self.image = pygame.transform.scale(self.image, Settings.player_size)                                       # Position des Bildes
        self.rect = self.image.get_rect(topleft =self.position)
        self.mask = pygame.mask.from_surface(self.image) 
        self.hitbox = self.rect.inflate(Settings.hitboxplayer_x, Settings.hitboxplayer_y)                                              # Masken für Kollisionserkennung
        
        # Setup
        self.import_player_assets()

        
        
        self.status = 'down'
        self.frame_index = 0

        self.animation_speed = Settings.animation_speed
        
       # player Movement    
        self.movement = pygame.math.Vector2()              # Bewegungsvektor [Settings.directon_x, Settings.directon_y]
        self.speed = Settings.player_speed                  # Geschwindigkeit
        self.attacking = False                             # Angriff
        self.attack_cooldown = Settings.attacking_cooldown # Angriff Cooldown
        self.attack_timer = None
        self.attack = attack
      
      
        self.object_sprites = object_sprites              # Gruppe aller Objekte
                                                            # print(self.movement)
    def import_player_assets(self):
        character_path = Settings.path['player']
        self.animations = { 'up' :[], 'down': [], 'left': [], 'right': [], 'right_idle': [], 'left_idle': [], 
            'up_idle': [], 'down_idle': [], 'right_attack': [], 'left_attack': [], 'up_attack': [], 
            'down_attack': [],'left_roll': [], 'right_roll': [], 'up_roll': [], 'down_roll': []}
        

        
        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            #self.image = import_folder.surface_list.append(Settings.imagepath('Attack.png')) 
            self.animations[animation] = import_folder(full_path)
            #print (self.animations[animation])
        #print(self.animations)

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
            print('attack')

        # spells
        if rightclick and not self.attacking:
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks()
            print('spell')
        # roll
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks()
            print('roll')



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
        #print (self.animations)
        animation = self.animations[self.status]

        # animation.append(Settings.imagepath('Attack.png'))
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation) :
            self.frame_index = 0
            
        # print(int(self.frame_index))  
        # print (animation)

        self.image = animation[int(self.frame_index)]

        #self.rect = self.image.get_rect(center = self.hitbox.center)
        

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

    # def collison(self):
    #     colide = pygame.sprite.spritecollide(self, self.object_sprites, False)
    #     if colide: 
    #         self.rect.left = colide[0].rect.right
    #         self.rect.top = colide[0].rect.bottom

    #     print(colide)


    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_timer >= self.attack_cooldown:
                self.attacking = False
            #     self.attack_timer = None
            #     self.attack_timer = pygame.time.get_ticks()
            # elif pygame.time.get_ticks() - self.attack_timer > self.attack_cooldown:
            #     self.attacking = False
            #     self.attack_timer = None

    def update(self):
        self.keys()
        self.cooldowns()
        self.get_status()
        self.anim()
        self.move()
