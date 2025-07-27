import pytesseract
from PIL import Image


img = Image.open('./imagens/content/livro01.jpg')

print(pytesseract.image_to_osd(img))