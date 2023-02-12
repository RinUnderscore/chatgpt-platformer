import pygame

# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Load the player image and set its rect
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (200,200))
player_rect = player_image.get_rect()

# Set initial player position
player_rect.x = 400
player_rect.y = 500

# Set player speed and gravity
speed_x = 0
speed_y = 0
gravity = 0.3

# Set platforms
platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(200, 400, 400, 50),
    pygame.Rect(100, 300, 200, 50),
    pygame.Rect(500, 200, 100, 50)
]

# Set camera position
camera_x = 0
camera_y = 0

# Set game loop flag
running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        speed_x = -5
    if keys[pygame.K_RIGHT]:
        speed_x = 5
    if keys[pygame.K_UP]:
        speed_y = -5
    if not keys[pygame.K_UP]:
        speed_y = 0
        
    # Apply gravity
    speed_y += gravity

    # Update player position
    player_rect.x += speed_x
    player_rect.y += speed_y

    # Check for platform collisions
    for platform in platforms:
        if player_rect.colliderect(platform):
            player_rect.bottom = platform.top
            speed_y = 0

    # Update camera position
    camera_x = player_rect.x - 400
    camera_y = player_rect.y - 300

    # Keep camera within the level bounds
    if camera_x < 0:
        camera_x = 0
    if camera_y < 0:
        camera_y = 0
    if camera_x > 800:
        camera_x = 800
    if camera_y > 600:
        camera_y = 600

    # Fill the screen with a solid color
    screen.fill((255, 255, 255))

    # Draw the platforms
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 0), platform.move(-camera_x, -camera_y))

    # Draw the player
    screen.blit(player_image, player_rect.move(-camera_x, -camera_y))

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
