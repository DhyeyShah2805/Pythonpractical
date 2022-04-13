from PIL import Image

image1 = Image.open(r'C:\Users\Dhyey Shah\OneDrive\Pictures\result.jpg')
img = image1.convert('RGB')
img.save(r'C:\Users\Dhyey Shah\OneDrive\Documents\result.pdf')
