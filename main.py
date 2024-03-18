import math
from manim import *
from manim.utils.color.core import ManimColor


class PlayWithPositions(Scene):

    def showGrid(self):
        """
        Create and display a grid using a NumberPlane object.

        Parameters:
            None

        Returns:
            None
        """

        # Create a NumberPlane object
        grid = NumberPlane(
            # Customize the x-axis range
            x_range=(-13, 13, 0.25),
            # Customize the y-axis range
            y_range=(-10, 10, 0.25),
            background_line_style={
                "stroke_color": GREEN,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
            },
            # Adjust the ratio of faded lines
            faded_line_ratio=2,
        )

        # Display the grid
        self.add(grid)

    def isPrime(self, n):
        """
        Check if a number is prime.

        Parameters:
            n (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def construct(self):
        """
        Construct the animation by initializing variables, generating squares, and playing the animation.

        Parameters:
            None

        Returns:
            None
        """
        self.initialize_variables()
        self.generate_squares()
        self.play_animation()

    def initialize_variables(self):
        """
        Initialize variables for the animation.

        Parameters:
            None

        Returns:
            None
        """

        # The order in which the spiral will go, the vector group to add the squares to, and the starting square
        DIRECTIONS_LIST = [UP, RIGHT, DOWN, LEFT]
        squares = VGroup()
        lastSquare = Square(0.0625)

        # The order of colors to follow, the initial index and alpha value, and the alpha value step
        COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
        currentColorIndex = 0
        currentAlphaValue = 0.1
        alphaStep = 0.1

        # The amount of number of total sides, the current 
        # direction index and number counter, as well square side length and initial extend amount
        loopIteration = 500
        moveDirectionIndex, numberCounter = 0, 0
        extend = 1
        SIDE_LENGTH = 0.02083

        # Set as attributes to the class
        self.DIRECTIONS_LIST = DIRECTIONS_LIST
        self.squares = squares
        self.lastSquare = lastSquare
        self.COLORS = COLORS
        self.currentColorIndex = currentColorIndex
        self.currentAlphaValue = currentAlphaValue
        self.alphaStep = alphaStep
        self.loopIteration = loopIteration
        self.moveDirectionIndex = moveDirectionIndex
        self.numberCounter = numberCounter
        self.extend = extend
        self.SIDE_LENGTH = SIDE_LENGTH

    def generate_squares(self):
        """
        Generate squares based on certain conditions.

        This method generates squares based on the values of which are prime. The squares are added to a VGroup called 'squares'.

        Parameters:
            None

        Returns:
            None
        """
        # The code snippet generates squares based on certain conditions and adds them to a VGroup called `squares`.

        for _ in range(self.loopIteration + 1):
            # Iterate self.loopIteration + 1 times

            for turnIncrement in range(2):
                # Iterate twice
                for steps in range(self.extend):
                    # Iterate self.extend times

                    # Create a new square next to the lastSquare in the direction specified by moveDirectionIndex
                    newSquare = Square(side_length=self.SIDE_LENGTH).next_to(
                        self.lastSquare, self.DIRECTIONS_LIST[self.moveDirectionIndex], self.SIDE_LENGTH)

                    # Update lastSquare and numberCounter
                    self.lastSquare = newSquare.copy()
                    self.numberCounter += 1

                    # Set the fill color of the new square
                    newSquare.set_fill(self.COLORS[self.currentColorIndex])

                    if self.isPrime(self.numberCounter):
                        # If numberCounter is prime, interpolate the fill color between the current color and the next color
                        color = self.COLORS[self.currentColorIndex].interpolate(
                            self.COLORS[(self.currentColorIndex + 1) % len(self.COLORS)], self.currentAlphaValue)

                        # Set the stroke width and fill opacity of the new square
                        newSquare.set_stroke(width=0.0)
                        newSquare.set_fill(color, 1)

                        # Increment currentAlphaValue and update currentColorIndex
                        self.currentAlphaValue += self.alphaStep

                        # If Resets the alpha value and moves to next color
                        if self.currentAlphaValue > 1.0:
                            self.currentAlphaValue = 0.1
                            self.currentColorIndex = (
                                self.currentColorIndex + 1) % len(self.COLORS)

                        # Add the new square to the squares VGroup
                        self.squares.add(newSquare.copy())

                # Increment moveDirectionIndex and wrap around to the beginning of DIRECTIONS_LIST
                self.moveDirectionIndex += 1
                self.moveDirectionIndex %= len(self.DIRECTIONS_LIST)

            # Increment extend and decrement loopIteration
            self.extend += 1

    def play_animation(self):
        """
        Play the animation by writing the squares and waiting for a specified duration.

        Parameters:
            None

        Returns:
            None
        """
        self.play(Write(self.squares))
        self.wait(3)
