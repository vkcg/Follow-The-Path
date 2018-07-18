import pygame
import random
import sys
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
 
class Block(pygame.sprite.Sprite):
    speed=0
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])



 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
obstracle_list = pygame.sprite.Group()
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

##obstracles##
#1            
block = Block(BLACK, 10, 20)
block.image = pygame.image.load("images\\met1.png").convert()
block.image.set_colorkey(WHITE)
     
# Set a random location for the block
block.rect.x = 330
block.rect.y = 20
block.speed=1
     
# Add the block to the list of objects
obstracle_list.add(block)
all_sprites_list.add(block)

#2
block = Block(BLACK, 10, 20)
block.image = pygame.image.load("images\\met1.png").convert()
block.image.set_colorkey(WHITE)
     
# Set a random location for the block
block.rect.x = 270
block.rect.y = 70
block.speed=1
     
# Add the block to the list of objects
obstracle_list.add(block)
all_sprites_list.add(block)

#3
block = Block(BLACK, 10, 20)
block.image = pygame.image.load("images\\met1.png").convert()
block.image.set_colorkey(WHITE)
     
# Set a random location for the block
block.rect.x = 350
block.rect.y = 70
block.speed=1
     
# Add the block to the list of objects
obstracle_list.add(block)
all_sprites_list.add(block)

#4
block = Block(BLACK, 30, 20)
block.image = pygame.image.load("images\\met2.png").convert()
block.image.set_colorkey(BLACK)
     
# Set a random location for the block
block.rect.x = 300
block.rect.y = 220
block.speed=1
     
# Add the block to the list of objects
obstracle_list.add(block)
all_sprites_list.add(block)

#5
block = Block(BLACK, 30, 20)
block.image = pygame.image.load("images\\met2.png").convert()
block.image.set_colorkey(BLACK)
     
# Set a random location for the block
block.rect.x = 380
block.rect.y = 220
block.speed=1
     
# Add the block to the list of objects
obstracle_list.add(block)
all_sprites_list.add(block)

##END##

### 
# This represents a block

block = Block(BLACK, 300, 400)
block.image = pygame.image.load("images\\s1.png").convert()
block.image.set_colorkey(BLACK)
 
# Set a random location for the block
block.rect.x = -50
block.rect.y = 0
 
# Add the block to the list of objects
block_list.add(block)
all_sprites_list.add(block)

block = Block(BLACK, 300, 400)
block.image = pygame.image.load("images\\s2.png").convert()
block.image.set_colorkey(BLACK)
 
# Set a random location for the block
block.rect.x = 450
block.rect.y = 0
 
# Add the block to the list of objects
block_list.add(block)
all_sprites_list.add(block)

#wall

# This represents a block
block = Block(BLACK, 600, 10)
 
# Set a random location for the block
block.rect.x = 0
block.rect.y = 0
 
# Add the block to the list of objects
block_list.add(block)
all_sprites_list.add(block)

#end wall
    
### 
# Create a RED player block
player = Block(RED, 20, 30)
player.image = pygame.image.load("images\\player.png").convert()
player.image.set_colorkey(WHITE)
all_sprites_list.add(player)
 


def game():
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    score = 0
    hit=0
    #Text
    font = pygame.font.Font(None,25)
#sound
    done=False
    click_sound = pygame.mixer.Sound("audio\\new.ogg")

    screen.fill(BLACK)
    screen1 = pygame.image.load("images\\screen1.png").convert()
    screen.blit(screen1, [0, 0])
    pygame.draw.rect(screen,WHITE,[320,340,60,40],5)
    text1=font.render("CLICK",True,RED)
    screen.blit(text1,[325,345])
    pygame.display.flip()
    flag=False
    while not flag:
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                cpos=pygame.mouse.get_pos()# checking click position
                if ((cpos[0]>320 and cpos[0]<380) and (cpos[1]>340 and cpos[1]<380)):
                    flag = True


  
    click_sound.play()
    for block in obstracle_list:
                    block.rect.y=random.randrange(-50,-10)
                    block.rect.x=random.randrange(300,380)
                    block.speed=random.randrange(1,5)

                # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    click_sound.stop()
                    pygame.mouse.set_visible(1)
                    game()
                if event.key == pygame.K_q:
                    done = True
     
        # Clear the screen
        screen.fill(WHITE)
        pygame.mouse.set_visible(0)
        if hit <=0: 
            # Get the current mouse position. This returns the position
            # as a list of two numbers.
            pos = pygame.mouse.get_pos()
         
            # Fetch the x and y out of the list,
               # just like we'd fetch letters out of a string.
            # Set the player object to the mouse location
            player.rect.x = pos[0]
            player.rect.y = pos[1]
            

            for block in obstracle_list:                
                if block.rect.y >380:
                    score+=1
                    block.rect.y=-20
                    block.rect.x=random.randrange(250,430)
                    block.speed=random.randrange(1,5)
                block.rect.y+=block.speed
                

                    
         
            # See if the player block has collided with anything.
            blocks1_hit_list = pygame.sprite.spritecollide(player, block_list, False)
            blocks2_hit_list = pygame.sprite.spritecollide(player, obstracle_list, False)

            
            
            # Check the list of collisions.
            for block in blocks1_hit_list:
                hit += 1
                click_sound.stop()
                click_sound = pygame.mixer.Sound("audio\\laser5.ogg")
                click_sound.play()
            for block in blocks2_hit_list:
                hit += 1
                click_sound.stop()
                click_sound = pygame.mixer.Sound("audio\\laser5.ogg")
                click_sound.play()
                
         
            # Draw all the spites
            all_sprites_list.draw(screen)
            
            #Score On Screen
            text=font.render("Score : "+str(score),True,RED)
            screen.blit(text,[600,10])
        else:
            #Game Over
            
            
            pygame.mouse.set_visible(1)
            screen1 = pygame.image.load("images\\gameover1.png").convert()
            screen.blit(screen1, [0, 0])
            
            screen.blit(text,[600,10])
        
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # Limit to 60 frames per second
        clock.tick(60)
    pygame.quit()
    sys.exit()
    
game()



