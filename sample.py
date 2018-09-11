from darkflow.net.build import TFNet

options_motor = {
    "model": "mini_motor/yolo-voc.backup.19.cfg", #hacknet_110717_i48000
    "load": "mini_motor/yolo-voc.backup.19.weights", #darknet19_448.conv.23.weights
    "threshold": 0.1,
    "labels": "mini_motor/image.names",
    "demo": "camera",
    "gpu": 0.5,
    "address": 'localhost',
    "port": 48051,
    "UDP": True}

options_7_class = {
    "model": "7_class/yolo-voc.backup.50.cfg", #hacknet_110717_i48000
    "load": "7_class/yolo-voc.backup.50.weights", #darknet19_448.conv.23.weights
    "threshold": 0.1,
    "labels": "7_class/image.names",
    "demo": "camera",
    "gpu": 0.5,
    "address": 'localhost',
    "port": 48051,
    "UDP": True}

options_24_class = {
    "model": "motor_recognition/cfg/yolo-voc.backup.41.cfg", #hacknet_110717_i48000
    "load": "motor_recognition/weights/yolo-voc.backup.41.weights", #darknet19_448.conv.23.weights
    "threshold": 0.1,
    "labels": "motor_recognition/image.names",
    "demo": "camera",
    "gpu": 0.5,
    "address": 'localhost',
    "port": 48051,
    "UDP": True}

	# options_hype_patlite
options = {
    "model": "cfg/yolo-voc-hyperion.cfg",
    "load": "weights/yolo-voc_50000.weights",
    "threshold": 0.1,
    "labels": "image.names",
    "demo": "camera",
    "gpu": 0.5,
    "address": 'localhost',
    "port": 48051,
    "UDP": True}
	
tfnet = TFNet(options)

# which camera should be used (OS defaults built in webcam to 0)
cameraNum = 0

#imgcv = cv2.imread("./darkflow/sample_img/sample_dog.jpg")
#result = tfnet.return_predict(imgcv)
tfnet.camera(cameraNum)
exit("Demo Stopped, exiting.")
