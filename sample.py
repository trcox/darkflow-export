from darkflow.net.build import TFNet

options = {
    "model": "cfg/yolo-voc-hyperion.cfg",
    "load": "weights/yolo-voc_50000.weights",
    "threshold": 0.1,
    "labels": "image.names",
    "demo": "camera",
    "gpu": 0.5,
    "address": 'localhost',
    "port": 48051,
    "UDP": True,
    "json": True}
tfnet = TFNet(options)

#imgcv = cv2.imread("./darkflow/sample_img/sample_dog.jpg")
#result = tfnet.return_predict(imgcv)
tfnet.camera()
exit("Demo Stopped, exiting.")
