import base64


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./com_ineuron_apparel/predictor_yolo_detector/inference/images/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
