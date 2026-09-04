import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon Jeu")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Boucle principale du jeu
def main():
    clock = pygame.time.Clock()
    running = True

    # Variables de jeu (à définir selon le type de jeu)
    player_position = [WIDTH // 2, HEIGHT // 2]
    player_velocity = [0, 0]

    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Autres touches à définir pour le jeu
                elif event.key == pygame.K_UP:
                    player_velocity[1] = -5
                elif event.key == pygame.K_DOWN:
                    player_velocity[1] = 5
                elif event.key == pygame.K_LEFT:
                    player_velocity[0] = -5
                elif event.key == pygame.K_RIGHT:
                    player_velocity[0] = 5
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player_velocity[1] = 0
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player_velocity[0] = 0

        # Mise à jour de la logique du jeu
        player_position[0] += player_velocity[0]
        player_position[1] += player_velocity[1]

        # Dessin à l'écran
        screen.fill(BLACK)  # Fond d'écran
        pygame.draw.rect(screen, WHITE, (*player_position, 50, 50))  # Dessine un carré représentant le joueur

        pygame.display.flip()  # Met à jour l'écran
        clock.tick(60)  # Limite le jeu à 60 images par seconde

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
