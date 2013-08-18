from PIL import Image
import	PIL
import	Tkinter
import	sys


#python grayscale.py nombredetuimagen.jpg

imagen = sys.argv[1]

def grayscale(image):
	newima=Image.open(image).convert('RGB')
	pix=newima.load()
	w,h = newima.size
	for i in range(w):
		for j in range(h):
			r,g,b = pix[i,j]
			newPixel = (r + g + b) / 3
			pix[i,j]= (newPixel, newPixel, newPixel)
	newima.save("gris.jpg")

def main():
	grayscale(imagen)

main()
