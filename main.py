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
        self.initialize_variables()
        self.generate_squares()
        self.play_animation()

    def initialize_variables(self):
        DIRECTIONS_LIST = [UP, RIGHT, DOWN, LEFT]
        squares = VGroup()
        lastSquare = Square(0.0625)

        COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK]
        currentColorIndex = 0
        currentAlphaValue = 0.1
        alphaStep = 0.1

        loopIteration = 500
        moveDirectionIndex, numberCounter = 0, 0
        extend = 1
        SIDE_LENGTH = 0.02083

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
        for _ in range(self.loopIteration + 1):
            for turnIncrement in range(2):
                for steps in range(self.extend):
                    newSquare = Square(side_length=self.SIDE_LENGTH).next_to(
                        self.lastSquare, self.DIRECTIONS_LIST[self.moveDirectionIndex], self.SIDE_LENGTH)

                    self.lastSquare = newSquare.copy()
                    self.numberCounter += 1
                    newSquare.set_fill(self.COLORS[self.currentColorIndex])

                    if self.isPrime(self.numberCounter):
                        color = self.COLORS[self.currentColorIndex].interpolate(
                            self.COLORS[(self.currentColorIndex + 1) % len(self.COLORS)], self.currentAlphaValue)

                        newSquare.set_stroke(width=0.0)
                        newSquare.set_fill(color, 1)

                        self.currentAlphaValue += self.alphaStep

                        if self.currentAlphaValue > 1.0:
                            self.currentAlphaValue = 0.1
                            self.currentColorIndex = (
                                self.currentColorIndex + 1) % len(self.COLORS)

                        self.squares.add(newSquare.copy())

                self.moveDirectionIndex += 1
                self.moveDirectionIndex %= len(self.DIRECTIONS_LIST)

            self.extend += 1
            self.loopIteration -= 1

    def play_animation(self):
        self.play(Write(self.squares))
        self.wait(3)
