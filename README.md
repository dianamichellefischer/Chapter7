"""
CH7_P8_P9
"""

import turtle

from images import Image

adjustBy = ('0')

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
            
#Defines the sepia function
def sepia(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
                lum = r + g + b
                image.setPixel(x, y, (lum, lum, lum))
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
                lum = r + g + b
                image.setPixel(x, y, (lum, lum, lum))
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
                lum = r + g + b
                image.setPixel(x, y, (lum, lum, lum))
                
#Defines the lighten function                
def lighten(image, adjustBy):
    """Converts the argument image to a lighter version"""
    adjustBy = input("By how much should this be lightened? ")
    adjustBy = int(adjustBy) 
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * adjustBy)
            g = int(g * adjustBy)
            b = int(b * adjustBy)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
            
#Defines the darken function    
def darken(image, adjustBy):
    """Converts the argument image to a darker version"""
    adjustBy = input("By how much should this be darkened? ")
    adjustBy = int(adjustBy) 
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r / adjustBy)
            g = int(g / adjustBy)
            b = int(b / adjustBy)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
            


#Defines the colorfilter function 
#def colorfilter(image, (r, g, b)):



#call function, ask for choise and show image
def main():
    print ("                 *   Options to Choose From   *")
    print ("")
    print ("                 * Grayscale to Sepia = 1     *")
    print ("                 *             Lighen = 2     *")
    print ("                 *             Darken = 3     *")
    print ("                 *        ColorFilter = 4     *")
    print ("")
    print ("")
    command = input("Enter the number of what you would like to do with your image: ")
    if command == ('1'):
        grayscale(image)
        image.draw()
        sepia(image)
        image.draw()
    elif command == ('2'):
        lighten(image, adjustBy)
        image.draw()
    elif command == ('3'):
        darken(image, adjustBy)
        image.draw()
    else:
        #colorfilter
        image.draw()

if __name__ == '__main__':
    main()

