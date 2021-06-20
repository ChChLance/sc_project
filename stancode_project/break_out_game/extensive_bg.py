"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10       # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels). orin:15
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = -7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'gray'
        self.pad_offset = paddle_offset
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.radius = ball_radius
        self.ball = GOval(self.radius*2, self.radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width - self.radius * 2) / 2, y=window_height-paddle_offset-ball_radius*2.1)

        # Default initial velocity for the ball
        vx = random.random()
        if vx > 0.5:
            vx = -vx-1
        else:
            vx = vx+1

        self.__dx = vx * 1.5
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.count = 0
        onmouseclicked(self.start_game)
        onmousemoved(self.control_paddle)

        # Draw bricks
        self.brick_rows = BRICK_ROWS
        self.brick_columns = BRICK_COLS
        for j in range(BRICK_ROWS):
            for i in range(BRICK_COLS):
                x_index = i*(brick_width+BRICK_SPACING)
                y_index = BRICK_OFFSET + j*(brick_height+BRICK_SPACING)
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True

                if j <= 1:
                    brick_color = 'red'
                elif j <= 3:
                    brick_color = 'orange'
                elif j <= 5:
                    brick_color = 'yellow'
                elif j <= 7:
                    brick_color = 'green'
                else:
                    brick_color = 'blue'

                self.brick.fill_color = brick_color
                self.brick.color = 'black'
                self.window.add(self.brick, x=x_index, y=y_index)
        # Brick attributes
        self.brick_h = BRICK_HEIGHT
        self.brick_w = BRICK_WIDTH

        # Scoreboard settings
        self.scoreboard = GLabel('Your score: 0')
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, x=0, y=self.window.height)

        # Autopilot settings
        self.auto_count = 0
        self.turn_on = 0
        self.autopilot = GLabel('')
        self.autopilot.font = '-20'
        self.window.add(self.autopilot, x=self.window.width/2.5, y=self.window.height)

    def control_paddle(self, m):
        if self.turn_on == 0:
            if m.x >= self.window.width - self.paddle.width/2:
                self.paddle.x = self.window.width - self.paddle.width
            elif m.x < 0:
                self.paddle.x = 0
            else:
                self.paddle.x = m.x - self.paddle.width/2

    def start_game(self, m):  # Can work only when ball at the start point!
        if self.ball.x == (self.window.width - self.radius * 2) / 2 and self.ball.y == self.window.height - self.pad_offset - self.radius * 2.1:
            self.count = self.count + 1
        self.auto_count = self.auto_count + 1
        if self.auto_count == 10:
            self.turn_on = 1

    def autopilot(self):
        self.paddle.x = self.ball.x

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_reset(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = self.window.height-self.pad_offset-self.radius*2.1

    def ball_detect_object(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            return self.window.get_object_at(self.ball.x, self.ball.y)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y) is not None:
            return self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        elif self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is not None:
            return self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        elif self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height) is not None:
            return self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        else:
            return False

    def add_text(self, content, x, y):
        text = GLabel(content)
        text.font = '-40'
        self.window.add(text, x, y)

    def remove_ball(self):
        self.window.remove(self.ball)

    def add_score(self, x):
        self.scoreboard.text = 'Your score: ' + str(x)

    def show_auto(self):
        self.window.add(self.autopilot)

    def add_autopilot(self):
        self.autopilot.text = 'Autopilot mode'


