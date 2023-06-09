import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("Please input positibe number for width and height")

try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("Please input positibe number for width and height")

try:
    right_triangle = figure.area_right_triangle(width, height)
    print(right_triangle)
except ValueError:
    print("Please input positibe number for width and height")