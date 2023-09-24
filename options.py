from pygame import Rect

class GameObject:
    def __init__(self, x, y, w, h, speed=(0,0)):
        """
        Initialize the GameObject with the given position, size, and speed.

        Args:
            x (int): The x-coordinate of the top-left corner of the GameObject.
            y (int): The y-coordinate of the top-left corner of the GameObject.
            w (int): The width of the GameObject.
            h (int): The height of the GameObject.
            speed (tuple, optional): The speed of the GameObject in the x and y directions.
                Defaults to (0, 0).

        Returns:
            None
        """
        self.bounds = Rect(x, y, w, h)
        self.speed = speed

    @property
    def left(self):
        """
        Get the left x-coordinate of the GameObject.

        Returns:
            int: The left x-coordinate of the GameObject.
        """
        return self.bounds.left

    @property
    def right(self):
        """
        Get the right x-coordinate of the GameObject.

        Returns:
            int: The right x-coordinate of the GameObject.
        """
        return self.bounds.right

    @property
    def top(self):
        """
        Get the top y-coordinate of the GameObject.

        Returns:
            int: The top y-coordinate of the GameObject.
        """
        return self.bounds.top

    @property
    def bottom(self):
        """
        Get the bottom y-coordinate of the GameObject.

        Returns:
            int: The bottom y-coordinate of the GameObject.
        """
        return self.bounds.bottom

    @property
    def width(self):
        """
        Get the width of the GameObject.

        Returns:
            int: The width of the GameObject.
        """
        return self.bounds.width

    @property
    def height(self):
        """
        Get the height of the GameObject.

        Returns:
            int: The height of the GameObject.
        """
        return self.bounds.height

    @property
    def center(self):
        """
        Get the center coordinates of the GameObject.

        Returns:
            tuple: The center coordinates of the GameObject in the form (x, y).
        """
        return self.bounds.center

    @property
    def centerx(self):
        """
        Get the x-coordinate of the center of the GameObject.

        Returns:
            int: The x-coordinate of the center of the GameObject.
        """
        return self.bounds.centerx

    @property
    def centery(self):
        """
        Get the y-coordinate of the center of the GameObject.

        Returns:
            int: The y-coordinate of the center of the GameObject.
        """
        return self.bounds.centery

    def draw(self, surface):
        """
        Draw the GameObject on the given surface.

        Args:
            surface: The surface to draw the GameObject on.

        Returns:
            None
        """
        pass

    def move(self, dx, dy):
        """
        Move the GameObject by the given amount in the x and y directions.

        Args:
            dx (int): The amount to move the GameObject in the x direction.
            dy (int): The amount to move the GameObject in the y direction.

        Returns:
            None
        """
        self.bounds = self.bounds.move(dx, dy)

    def update(self):
        """
        Update the GameObject's position based on its speed.

        Returns:
            None
        """
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)