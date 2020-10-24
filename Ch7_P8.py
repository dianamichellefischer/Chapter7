



import turtle


from images import Image

#Accepts the input of an image
image = Image(input("Enter the file name: "))




#Defines the grayscale function

def grayscale(image):
    """Converts the argument image to grayscale"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
            





def sepia(image):
    ##Converts to sepia colors
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
                image.setPixel(x, y, (red, green, blue))
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
                image.setPixel(x, y, (red, green, blue))
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
                image.setPixel(x, y, (red, green, blue))
                
                





#call sepia function and show image
def main():
    grayscale(image)
    sepia(image)
    image.draw()

if __name__ == "__main__":
   main()


