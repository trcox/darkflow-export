from darkflow.net.build import TFNet

import cv2

options = {"model": "cfg/yolo-voc.cfg", "load": "weights/yolo-voc.weights", "threshold": 0.1}
tfnet = TFNet(options)

imgcv = cv2.imread("./darkflow/sample_img/sample_dog.jpg")
result = tfnet.return_predict(imgcv)

print(result)
