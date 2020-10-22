import turtle


from images import Image

#pull in image
filename = input("Enter the file name: ")

def sepia(image):
    ##Converts to sepia colors
    x = 150
    y = 150
    (red, green, blue) = image.getPixel(x, y)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
                
#call sepia function and show image
def main(filename):
    image = Image(filename)
    print("Close the image window to continue. ")
    image.draw()
    sepia(image)
    print("Close the image window to quit. ")
    image.draw()

if __name__ == "__main__":
   main(filename)


