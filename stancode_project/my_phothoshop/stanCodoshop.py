"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    return ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    sum_red = sum_green = sum_blue = 0
    for p in pixels:
        sum_red = sum_red + p.red
        sum_green = sum_green + p.green
        sum_blue = sum_blue + p.blue
    lst = list()
    lst.append(int(sum_red / len(pixels)))
    lst.append(int(sum_green / len(pixels)))
    lst.append(int(sum_blue / len(pixels)))
    return lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg_lst = get_average(pixels)
    for i in range(len(pixels)):
        if i == 0:
            min_d = get_pixel_dist(pixels[i], avg_lst[0], avg_lst[1], avg_lst[2])
            best_p = pixels[i]
        else:
            if get_pixel_dist(pixels[i], avg_lst[0], avg_lst[1], avg_lst[2]) < min_d:
                min_d = get_pixel_dist(pixels[i], avg_lst[0], avg_lst[1], avg_lst[2])
                best_p = pixels[i]
    return best_p


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            each_p = result.get_pixel(x, y)
            temp_lst = []
            for i in images:  # make pixels(temp_lst) for get_best_pixel
                temp_lst.append(i.get_pixel(x, y))
            best_p = get_best_pixel(temp_lst)
            each_p.red = best_p.red
            each_p.green = best_p.green
            each_p.blue = best_p.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
