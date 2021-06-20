"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from extensive_bg import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts
my_life = NUM_LIVES


def main():
    """
    extensive version:
    1. add scoreboard
    2. if click over 10 times, you can turn on autopilot mode
    """
    global my_life
    graphics = BreakoutGraphics()
    ball = graphics.ball
    window = graphics.window
    vx = vy = 0
    # Add animation loop here!
    controller = 0  # controller = 0 --> click can work
    remove_count = 0
    para_paddle = 0  # Avoid ball too large, making sure that ball exit the paddle

    while my_life > 0:
        if graphics.ball_detect_object():
            if graphics.paddle is not graphics.ball_detect_object() and graphics.scoreboard is not graphics.ball_detect_object() and graphics.autopilot is not graphics.ball_detect_object():  # detect bricks
                vy = -vy
                window.remove(graphics.ball_detect_object())
                remove_count = remove_count + 1
                graphics.add_score(remove_count)

                if remove_count == graphics.brick_rows * graphics.brick_columns:
                    graphics.add_text('You win!', graphics.window.width / 3.5, graphics.window.height / 2)
                    break
            else:  # detect paddle
                if para_paddle == 0 and ball.y + ball.height <= graphics.paddle.y + graphics.paddle.height:
                    vy = -vy
                    para_paddle = 1
        else:  # detect nothing
            para_paddle = 0  # reset para_paddle, which means ball fully exit paddle

        if ball.x < 0 or ball.x > window.width - ball.width:  # hit the wall
            vx = -vx
        if ball.y <= 0:  # hit the upper floor
            vy = -vy
        if ball.y > window.height - ball.height:  # hit the ground floor
            my_life = my_life - 1
            graphics.ball_reset()
            vx = vy = 0
            controller = 0  # open click

        if controller == 0:
            if graphics.count == 1:
                vx = graphics.get_dx()
                vy = graphics.get_dy()
                graphics.count = 0
                controller = 1

        ball.move(vx, vy)

        # For autopilot
        if graphics.auto_count == 10:
            graphics.ball_reset()
            vx = 10
            vy = -10
            graphics.paddle.x = ball.x - ball.width/2 - (graphics.paddle.width/2 - ball.width/2)
            graphics.paddle.fill_color = 'red'
            graphics.add_autopilot()
        if graphics.auto_count >= 10:
            graphics.paddle.move(vx, 0)
        pause(FRAME_RATE)

    graphics.remove_ball()
    if remove_count != graphics.brick_rows * graphics.brick_columns:
        graphics.add_text('GGGGGGGGGGGGG', graphics.window.width / 5, graphics.window.height / 2)


if __name__ == '__main__':
    main()
