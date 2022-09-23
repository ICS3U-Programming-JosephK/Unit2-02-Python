#!/usr/bin/env python3
# Created by: Ms Raffin and borrowed by Joseph
# Created on: Sep. 23, 2022
# This program asks the user for the length and
# width of the rectangle in mm. It then
# calculates and displays the area and
# perimeter.
import math


def main():
    # introduction
    print("Today we will calculate the area and")
    print("perimeter of a rectangle")
    # obtaining input from the user
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # process / calculation
    area = length * width
    perimeter = 2 * (length + width)

    # output of the result
    print("")
    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))


if __name__ == "__main__":
    main()
