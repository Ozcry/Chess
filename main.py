import pygame

# Inicializando o Pygame e criando a Janela

pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Chess")

def draw():
    display.fill([19, 173, 235])

gameLoop = True

if __name__ == "__main__":    
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print('Apertou W!')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    print('Soltou W!')
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print('segurando W!')
            
        draw()
        pygame.display.update()


