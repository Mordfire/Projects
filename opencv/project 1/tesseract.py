import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread(r"C:\Users\jojo\Desktop\4.png")
text = pytesseract.image_to_string(image,"eng")
print(text)