import pytesseract
import numpy as np
import cv2

# img = cv2.imread('./imagens/content/teste01.jpg')

# # É realmente necessário converter a imagem para RGB? Aparentemente não, mas é uma boa prática para garantir compatibilidade com diferentes formatos de imagem.
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

# texto: str = pytesseract.image_to_string(rgb)
# print(texto)

# # Utilizando o idioma português
# img = cv2.imread('./imagens/content/teste02.jpg')
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# texto = pytesseract.image_to_string(rgb, lang='por')
# print(texto)

img = cv2.imread('./imagens/content/trecho-livro.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# CONFIGURAÇÃO DE PSM (Page Segmentation Mode)
# 1 - Automatic page segmentation with OSD (Orientation and Script Detection)
# 2 - Automatic page segmentation, but no OSD, or OCR
# 3 - Fully automatic page segmentation, but no OSD 
# 4 - Assume a single column of text of variable sizes
# 5 - Assume a single uniform block of vertically aligned text
# 6 - Assume a single uniform block of text
# 7 - Treat the image as a single text line
# 8 - Treat the image as a single word
# 9 - Treat the image as a single word in a circle
# 10 - Treat the image as a single character
# 11 - Sparse text. Find as much text as possible in no particular order.
# 12 - Sparse text with OSD
# 13 - Raw line. Treat the image as a single text line, but do not apply any layout analysis.
# 14 - Raw line with OSD


#configuração do Tesseract OCR
config_tesseract = '--psm 6'
texto = pytesseract.image_to_string(rgb, lang='por', config=config_tesseract)
print(texto)

img = cv2.imread('./imagens/content/saida.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#configuração do Tesseract OCR
config_tesseract = '--psm 7'
texto = pytesseract.image_to_string(rgb, lang='por', config=config_tesseract)
print(texto)