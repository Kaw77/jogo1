import pygame


print('Configurações iniciais')
pygame.init()
cria_janela = pygame.display.set_mode(size=(600, 480))
print('Configurações finais')

print('Começa o loop')
while True:
    #checar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
