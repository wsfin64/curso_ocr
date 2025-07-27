import pytesseract
from pytesseract import Output
import cv2

img = cv2.imread('./imagens/content/teste_manuscrito_01.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Configuração do Tesseract OCR para manuscrito
# config_tesseract = '--psm 6 --oem 1'  # PSM 6 para bloco de texto único, OEM 1 para LSTM OCR
resutado = pytesseract.image_to_data(rgb, lang='por', output_type=Output.DICT)
# print(resutado)

min_conf = 40

def caixa_texto(resultado, img, cor = (255, 100, 0)):
        x = resultado['left'][i]
        y = resultado['top'][i]
        w = resultado['width'][i]
        h = resultado['height'][i]
        cv2.rectangle(img, (x, y), (x + w , y + h), cor, 2)
        cv2.putText(img, resultado['text'][i], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255))

        return x, y, img
            
img_copia = img.copy()

for i in range(0, len(resutado['text'])):
    if int(resutado['conf'][i]) > min_conf:
        x, y, img_copia = caixa_texto(resutado, img_copia)
        print(x, y)
cv2.imshow('Texto Detectado', img_copia)
cv2.waitKey(0)