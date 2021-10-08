import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd ='C:\\Users\\Nikita Sharma\\Tesseract\\tesseract.exe'

def readImg(imagePath):
    img = cv2.imread(imagePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (800, 700))
    return img
   
def detectChars(img):
    img2char = pytesseract.image_to_string(img)
    print(img2char)
    imgbox = pytesseract.image_to_boxes(img)
    imgH, imgW, _ = img.shape
    for boxes in imgbox.splitlines():
        boxes = boxes.split(" ")
        x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
        cv2.rectangle(img,(x,imgH-y), (w,imgW-h), (0,0,255), 3)
        cv2.putText(img, boxes[0], (x, imgH-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow('Detected Characters', img)
    cv2.waitKey(0)

detectChars(readImg("sample1.png"))
detectChars(readImg("sample2.png"))
