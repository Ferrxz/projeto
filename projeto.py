import pygame

# Inicializa o Pygame
pygame.init()

# Configuração da tela/imagens
campo = pygame.image.load('./imagem/campo.png')
campo = pygame.transform.scale(campo, [1280, 720])
bola = pygame.image.load('./imagem/bola.png')
bola = pygame.transform.scale(bola, [46, 46])

# Configuração de jogadores
jogador1 = pygame.image.load('./imagem/jogador1.png')
jogador1 = pygame.transform.scale(jogador1, [78, 146])
jogador2 = pygame.image.load('./imagem/jogador2.png')
jogador2 = pygame.transform.scale(jogador2, [78, 146])

# Posição inicial do jogador e velocidade
py_jogador1 = 300
py_jogador2 = 300  # Posição vertical inicial do jogador 2
speed = 6

# Flags de tecla
tecla_w = False
tecla_s = False

# Configuração da janela
janela = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Janela")

# Loop principal
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                tecla_w = True
            if event.key == pygame.K_s:
                tecla_s = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                tecla_w = False
            if event.key == pygame.K_s:
                tecla_s = False

    # Movimentação do jogador 1
    if tecla_w and py_jogador1 > 0:
        py_jogador1 -= speed
    if tecla_s and py_jogador1 < 720 - 146:  # 720 é a altura da tela, 146 é a altura do jogador
        py_jogador1 += speed

    # Movimentação do jogador 2 (usando as teclas de seta)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and py_jogador2 > 0:
        py_jogador2 -= speed
    if keys[pygame.K_DOWN] and py_jogador2 < 720 - 146:  # Respeitando o limite da tela
        py_jogador2 += speed

    # Desenha tudo na tela
    janela.blit(campo, (0, 0))
    janela.blit(jogador1, (100, py_jogador1))  # Posiciona o jogador 1
    janela.blit(jogador2, (1100, py_jogador2))  # Posiciona o jogador 2 no lado oposto
    janela.blit(bola, (619, 339))  # Posiciona a bola (ajuste conforme necessário)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()


