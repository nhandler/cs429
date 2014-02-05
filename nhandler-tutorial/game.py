# Game parameters
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BG_COLOR = (150, 150, 80)
CREEP_FILENAMES = [
	'bluecreep.png',
	'pinkcreep.png',
	'graycreep.png',
]
N_CREEPS = 20
CREEP_SPEED = 0.1	# 0.1 px/ms or 100 pixels per second

pygame.init()
screen = pygame.display.set_mode(
	(SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

# Create N_CREEPS random creeps
creeps = []
for i in range(N_CREEPS):
	creeps.append(Creep(screen,
						choice(CREEP_FILENAMES),
						(	randint(0, SCREEN_WIDTH),
							randint(0, SCREEN_HEIGHT)),
						(	choice([-1, 1]),
							choice([-1, 1])),
						CREEP_SPEED))
# The main game loop
while True:
    # Limit frame speed to 50 FPS
    time_passed = clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    # Redraw the background
    screen.fill(BG_COLOR)

    # Update and redraw all creeps
    for creep in creeps:
        creep.update(time_passed)
        creep.blitme()

    pygame.display.flip()
