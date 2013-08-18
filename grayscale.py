from PIL import Image
import	PIL
import	Tkinter
import	sys


#python grayscale.py image.jpg

picture = sys.argv[1]

def grayscale(image):
	newpic=Image.open(image).convert('RGB')
	pix=newpic.load()
	w,h = newpic.size
	for i in range(w):
		for j in range(h):
			r,g,b = pix[i,j]
			newPixel = (r + g + b) / 3
			pix[i,j]= (newPixel, newPixel, newPixel)
	newpic.save("gray.jpg")

def main():
	grayscale(picture)

main()
