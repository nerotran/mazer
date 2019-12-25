# Libraries
import pygame

# maze level model
mazes = [
    [
            "wwwwwwwwwwwwwwwwwwwwwww",
            "w                     w",
            "w                     D",
            "w                     w",
            "wwwwwwwwwwwwwwwwwwwwwww"
    ]
    ,
    [
        "wwwwwwwwwwwwwwwwwwwww",
        "w  ww               w",
        "w  ww               w",
        "w      w  w  www  www",
        "w      w  w  w      w",
        "w  wwwww  w  w      w",
        "w  w      w  wwwwwwww",
        "w  w      w         w",
        "wwww  wwwwwwwwwwwwwww",
        "w     w             w",
        "w     w             w",
        "wwww       wwwwwww  w",
        "w  w       wwwwwww  w",
        "w  wwww          w  w",
        "w  w  w          w  w",
        "wwwwwwwwwwwwwwwwwwDDw"
    ]
    ,
    [
        "wwwwwwwwwwwwwwwwwwwwwwww",
        "w  w                   w",
        "w  w      wwwwwwwwwww  w",
        "w  w      w         w  w",
        "w  w      w         w  w",
        "w  wwwwwwww  wwwww  w  w",
        "w            w   w  w  w",
        "w            w   w  w  w",
        "www  wwwwwwwww   w  w  w",
        "w                w  w  w",
        "w                w  w  w",
        "wwwwwwwwwwwwwwwwww  w  w",
        "w                   w  w",
        "w                   w  w",
        "w  wwwwwwwwwwwwwwwwww  w",
        "w                      w",
        "w                      w",
        "wwwwwwwwwwwwwwwwwwwwwDDw",

    ]
    ,
    [
        "wwwwwwwwwwwwwwwwwwwwwww",
        "w     w  w            w",
        "w     w  w            w",
        "w  w  w  w  wwwwwwww  w",
        "w  w  w  w  w         w",
        "wwww  w     w         www",
        "w     w     wwww   w    w",
        "w     wwww     wwwww    w",
        "w  wwwwwwwwww     wwww  w",
        "w        wwwwwww     w  w",
        "w        w     w     w  w",
        "wwwwwww  w  w  wwww  w  w",
        "w     w     w        w  w",
        "w     w     w        w  w",
        "w  w  w  wwwwwwwwwwwww  w",
        "w  w     w              w",
        "w  w     w              w",
        "wwwwwwwwwwDDwwwwwwwwwwwww"

    ]
    ,
    [
        "wwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
        "w    w   w w     w           w",
        "wwww www w w w   wwwww  w    w",
        "w    w   w   w   w      w    w",
        "w  w     www w   w     ww    w",
        "ww wwwww w   w   w      w    w",
        "w  w         w          ww   w",
        "w    wwwww  www  w      w    w",
        "wwwwww  w    w   wwwwwwww wwww",
        "w    w  w    www w      w w  w",
        "wwwwww ww    w wwwww  w w    w",
        "w                  w  w wwww w",
        "wwww   w  ww    wwww  w      w",
        "w      w   w    w     w    w w",
        "w      w   w    w     w   wwww",
        "w      w   ww   w  w  w      w",
        "w      w   w    w  w  w   ww w",
        "w      w   w    w  w  w   w  w",
        "wwwwwwwwwwwwwwwwwwwwwwwwwwwDDw"
    ]

]

pygame.init()

# Color tuples
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Display properties
FPS = 30
display_width = 800
display_height = int(display_width * 2 / 3)
clock = pygame.time.Clock()
block_size = display_width / 32
level = 0

def message_to_screen(msg, color, fontSize, x_axis, y_axis):
    '''
    pass in the message as a string, the color tuple, the integer for font size,
    and the position of the message and the function will print it to the game's screen
    '''
    font = pygame.font.SysFont(None, fontSize)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x_axis, y_axis])

def levelMessage():
    '''
    This function will display all the message for each and individual level by checking the global variable "level"
    and using the "message_to_screen" function.
    '''
    if level == 0:

        # Message for the player at the tutorial level
        message_to_screen("Level: Tutorial",
                          red, 20, display_width / 120, display_height - (display_height / 1.05))
        message_to_screen("Welcome!",
                          red, 30, display_width / 2.5, display_height - (display_height / (1.05 + 0.1)))
        message_to_screen("The goal of this game is to get to the 'door' (blue tile) to escape from the maze.",
                          red, 30, display_width / 30, display_height - (display_height / (1.05 + 0.2)))
        message_to_screen( "Use arrow keys: left, right, up, down to move around the maze. Have fun!",
                          red, 30, display_width / 30, display_height - (display_height / (1.05 + 0.27)))

    else:
        message_to_screen("Level: " + str(level), red, 20, display_width / 120, display_height - (display_height / 1.05))


# Create a game display
gameDisplay = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("Mazer")

def gameloop():
    '''
    The main function that runs the game.
    '''

    # Build the maze
    global level
    wall_maze, door_maze = buildMaze(mazes[level])

    # Game flags
    gameExit = False
    levelOver = False
    gameOver = False

    # Player's properties
    movementSpeed_x = 0
    movementSpeed_y = 0
    player_x = display_width / 10
    player_y = display_height / 1.2
    speed = block_size / 2

    while not gameExit: #running game loop

        # When the player finish a level
        while levelOver:
            gameDisplay.fill(white)
            message_to_screen("Press Q to quit",
                              red, 40, display_width / 7, display_height / 3 )
            message_to_screen("Press N for next level", red, 40,
                              display_width / 7, display_height / 3 + 40)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    levelOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        levelOver = False
                    elif event.key == pygame.K_n:
                        level += 1
                        levelOver = False
                        gameloop()

        # When the player finish the last level.
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("This is the end. Thank you for playing!", red, 40,
                              display_width / 7, display_height / 3)
            message_to_screen("Press Q to quit.",
                              red, 40, display_width / 3.5, display_height / 3 + 40)
            message_to_screen("Press A to play again.",
                              red, 40, display_width / 3.5, display_height / 3 + 80)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_a:
                        level = 0
                        gameOver = False
                        gameloop()

        # Event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:

        # Movement control
                # Change in player's velocity when certain keys are pressed
                if movementSpeed_y == 0:
                    if event.key == pygame.K_LEFT:
                        movementSpeed_x = -speed
                    if event.key == pygame.K_RIGHT:
                        movementSpeed_x = speed
                if movementSpeed_x == 0:
                    if event.key == pygame.K_DOWN:
                        movementSpeed_y = speed
                    if event.key == pygame.K_UP:
                        movementSpeed_y = -speed

            # Stop the player's movement when the keys are no longer pressed
            if event.type == pygame.KEYUP and event.type != pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or \
                        event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    movementSpeed_x = 0
                    movementSpeed_y = 0



        # Player's velocity
        player_x += movementSpeed_x
        player_y += movementSpeed_y

        # Rendering
        gameDisplay.fill(white)
        mazer = player(block_size, player_x, player_y)
        movingSprites = pygame.sprite.Group()
        movingSprites.add(mazer)
        wall_maze.draw(gameDisplay)
        door_maze.draw(gameDisplay)
        movingSprites.draw(gameDisplay)
        levelMessage()
        pygame.display.update()

        clock.tick(FPS) # FPS tick

        # Player-door interaction
        if pygame.sprite.spritecollideany(mazer, door_maze):
            if level == len(mazes) - 1:
                gameOver = True
            else:
                levelOver = True


        # Wall Collision
        if movementSpeed_x > 0 and movementSpeed_y == 0:
            if pygame.sprite.spritecollideany(mazer, wall_maze):
                movementSpeed_x = 0
                player_x -= speed
        elif movementSpeed_x < 0 and movementSpeed_y == 0:
            if pygame.sprite.spritecollideany(mazer, wall_maze):
                movementSpeed_x = 0
                player_x += speed

        elif movementSpeed_y > 0 and movementSpeed_x == 0:
            if pygame.sprite.spritecollideany(mazer, wall_maze):
                movementSpeed_y = 0
                player_y -= speed
        elif movementSpeed_y < 0 and movementSpeed_x == 0:
            if pygame.sprite.spritecollideany(mazer, wall_maze):
                movementSpeed_y = 0
                player_y += speed

    pygame.quit()
    quit()

class asset(pygame.sprite.Sprite): # Base class for all assets in the game

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

class player(asset): # Class for player

    def __init__(self, size, x, y):

        # Image properties for player
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(red)
        self.rect = self.image.get_rect()

        # Player's position
        self.rect.x = x
        self.rect.y = y

class wall(asset): # Class for wall blocks

    def __init__(self, size, x , y):

        # Image properties for wall
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(black)
        self.rect = self.image.get_rect()

        # Wall's position
        self.rect.x = x
        self.rect.y = y

class door(asset): # Class for doors

    def __init__(self, size, x, y):
        # Image properties for door
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(blue)
        self.rect = self.image.get_rect()

        # Door's position
        self.rect.x = x
        self.rect.y = y

def buildMaze(Maze): # Maze - graphic generator
    '''
    Pass in the string of the maze model,
    the function will return the maze's objects as sprite groups for rendering.
    '''

    # Create sprite groups for Maze's objects
    wall_list = pygame.sprite.Group()
    door_list = pygame.sprite.Group()

    # The starting position of the maze
    pos_x = display_width / 10 - block_size
    pos_y = display_height / 1.2 + block_size

    # The loop that generate the maze's graphical properties based on the maze model string
    for row in Maze:
        for space in row:

            # Check for the type of maze's object then add it to the sprite group for rendering
            if space == "w":
                wall_maze = wall(block_size, pos_x, pos_y)
                wall_list.add(wall_maze)
            elif space == "D":
                door_maze = door(block_size, pos_x, pos_y)
                door_list.add(door_maze)

        # Move to a new position after an object is done
            pos_x += block_size
        pos_y -= block_size
        pos_x = display_width / 10 - block_size

    return wall_list, door_list

# Run the game
gameloop()
