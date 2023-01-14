import pygame

gameState = "Menu"

glitchBkg = pygame.image.load('images/glitch.png')
glitchBkgRect = [0,0,1920,1080]
glitchBkgPatchNumber = 0
glitchBkgNumPatches = 34
glitchBkgFrameRate = 1

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    pygame.font.init()
    surfaceSize = (1920, 1080)   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize))

    #-----------------------------Declare Variables------------------------------------------#
    global glitchBkg
    global glitchBkgRect
    global glitchBkgPatchNumber
    global glitchBkgNumPatches
    global glitchBkgFrameRate
    glitchFontSize = 100
    decreaseMenuText = False
    currentMenuColor = "Red"
    randomMenuColor = (255, 0, 0)
    menuColorTimer = 0

#-----------------------------Main Program Loop---------------------------------------------#
    while True:       
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        if(gameState == "Menu"):
            glitchFont = pygame.font.Font('fonts/glitch.ttf', glitchFontSize)
            menuText = glitchFont.render("PIXELS", 1, randomMenuColor)
            if menuColorTimer == 180:
                if(currentMenuColor == "Red"):
                    currentMenuColor = "Green"
                    randomMenuColor = (0,255,0)
                    menuColorTimer = 0
                elif(currentMenuColor == "Green"):
                    currentMenuColor = "Blue"
                    randomMenuColor = (0,0,255)
                    menuColorTimer = 0
                elif(currentMenuColor == "Blue"):
                    currentMenuColor = "Red"
                    randomMenuColor = (255,0,0)
                    menuColorTimer = 0

            if (frameCount % glitchBkgFrameRate == 0):    #Only change the animation frame once every {glitchBkgFrameRate} frames
                if (glitchBkgPatchNumber < glitchBkgNumPatches-1) :
                    glitchBkgPatchNumber += 1
                    glitchBkgRect[0] += glitchBkgRect[2]  #Shift the "display window" to the right along the sprite sheet by the width of the image
                else:
                    glitchBkgPatchNumber = 0           #Reset back to first patch
                    glitchBkgRect[0] -= glitchBkgRect[2]*(glitchBkgNumPatches-1)  #Reset the rect position of the rect back too

            mainSurface.blit(glitchBkg, (0,0), glitchBkgRect)
            mainSurface.blit(menuText,menuText.get_rect(center=(surfaceSize[0]//2, 420)))

            if(not decreaseMenuText):
                if(glitchFontSize < 200):
                    glitchFontSize += 1
                else: decreaseMenuText = True
            elif(decreaseMenuText):
                if(glitchFontSize > 100):
                    glitchFontSize -= 1
                else:
                    decreaseMenuText = False
        
        pygame.display.flip()
        clock.tick(frameRate) #Force frame rate to be slower
        menuColorTimer += 1

    pygame.quit()     # Once we leave the loop, close the window.

main()