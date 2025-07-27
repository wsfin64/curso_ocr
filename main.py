import pytesseract
import numpy as np
import cv2

img = cv2.imread('./imagens/content/teste01.jpg')

# É realmente necessário converter a imagem para RGB? Aparentemente não, mas é uma boa prática para garantir compatibilidade com diferentes formatos de imagem.
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

texto: str = pytesseract.image_to_string(rgb)
print(texto)

# Utilizando o idioma português
img = cv2.imread('./imagens/content/teste02.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
texto = pytesseract.image_to_string(rgb, lang='por')
print(texto)
