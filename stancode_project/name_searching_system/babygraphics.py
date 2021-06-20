"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'black']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_range = CANVAS_WIDTH - 2*GRAPH_MARGIN_SIZE
    interval = x_range / len(YEARS)
    return GRAPH_MARGIN_SIZE + int(year_index * interval)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def get_y_coordinate(rank, total_rank_num):
    """
    Input:
        rank(str): The rank of the name in certain year
        total_rank_num(int): Total rank number
    Returns:
        y_coordinate (int): The y coordinate of the vertical line associated
                              with the specified year.
    """
    rank = int(rank)
    y_range = CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE
    y_interval = y_range / total_rank_num
    return GRAPH_MARGIN_SIZE + int((rank-1)*y_interval)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for n in range(len(lookup_names)):
        v_name = lookup_names[n]
        color_index = n % len(COLORS)  # Deal with color

        for i in range(len(YEARS)):
            cur_x = get_x_coordinate(CANVAS_WIDTH, i)
            if i == 0:  # First point -> just get the point
                if str(YEARS[i]) in name_data[v_name]:  # The name is in the rank in certain year
                    cur_y = get_y_coordinate(name_data[v_name][str(YEARS[i])], 1000)
                    canvas.create_text(cur_x+TEXT_DX, cur_y, text=v_name + ' ' + name_data[v_name][str(YEARS[i])],
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                else:  # The name is not in the rank in certain year -> y = *
                    cur_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_text(cur_x+TEXT_DX, cur_y, text=v_name+' *', anchor=tkinter.SW, fill=COLORS[color_index])
            else:  # We have two points -> draw line
                if str(YEARS[i]) in name_data[v_name]:  # The name is in the rank in certain year
                    cur_y = get_y_coordinate(name_data[v_name][str(YEARS[i])], 1000)
                    canvas.create_text(cur_x+TEXT_DX, cur_y, text=v_name + ' ' + name_data[v_name][str(YEARS[i])],
                                       anchor=tkinter.SW, fill=COLORS[color_index])
                else:  # The name is not in the rank in certain year -> y = *
                    cur_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    canvas.create_text(cur_x+TEXT_DX, cur_y, text=v_name + ' *', anchor=tkinter.SW, fill=COLORS[color_index])
                canvas.create_line(prev_x, prev_y, cur_x, cur_y, width=LINE_WIDTH, fill=COLORS[color_index])
            prev_x = cur_x
            prev_y = cur_y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
