class Creep(Sprite):
    """ A creep sprite that bounces of walls and changes its
        direction from time to time.
    """

    def __init__(
            self, screen, img_filename, init_position,
            init_direction, speed):
        """ Create a new Creep.

            screen:
                The screen on which the creep lives (must be a
                pygame Surface object, such as pygame.display)

            img_filename:
                Image file for the creep.

            init_position:
                A vec2d or a pair specifying the initial position
                of the creep on the screen.

            init_direction:
                A vec2d or a pair specifying the initial direction
                of the creep. Must have an angle that is a
                multiple of 45 degrees.

            speed:
                Creep speed, in pixels/millisecond (px/ms)
        """

	def update(self, time_passed):
		# Maybe it's time to change the direction?
		self._change_direction(time_passed)

		# Make the creep point in the correct direction.
		# Since our direction vector is in screen coordinates
		# (i.e. right bottom is 1, 1), and rotate() rotates
		# counter-clockwise, the angle must be inverted to
		# work correctly.
		self.image = pygame.transform.rotate(
			self.base_image, -self.direction.angle)

		# Compute and apply the displacement to the position
		# vector. The displacement is a vector, having the angle
        # of self.direction (which is normalized to not affect
        # the magnitude of the displacement)
        displacement = vec2d(
            self.direction.x * self.speed * time_passed,
            self.direction.y * self.speed * time_passed)
        self.pos += displacement

    def blitme(self):
        """ Blit the creep onto the screen that was provided in
            the constructor
        """
        # The creep image is placed at self.pos.
        # To allow for smooth movement even when the creep rotates
        # and the image size changes, its placement is always
        # centered.
        draw_pos = self.image.get_rect().move(
            self.pos.x - self.image_w / 2,
            self.pos.y - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

        # When the image is rotated, its size is changed.
        # We must take the size into account for detecting
        # collisions with the walls.
        (self.image_w, self.image_h) = self.image.get_size()
        bounds_rect = self.screen.get_rect().inflate(
                        -self.image_w, -self.image_h)

        if self.pos.x < bounds_rect.left:
            self.pos.x = bounds_rect.left
            self.direction.x *= -1
        elif self.pos.x > bounds_rect.right:
            self.pos.x = bounds_rect.right
            self.direction.x *= -1
        elif self.pos.y < bounds_rect.top:
            self.pos.y = bounds_rect.top
            self.direction.y *= -1
        elif self.pos.y > bounds_rect.bottom:
            self.pos.y = bounds_rect.bottom
            self.direction.y *= -1
