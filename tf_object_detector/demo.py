from tf_object_detector.config import Config
import click

from tf_object_detector.architectures import object_detection
import cv2
import tensorflow as tf


CAMERA_MODE = 'camera'
STATIC_MODE = 'static'
IMAGE_SIZE = 320


class Demo(object):
    """docstring for Demo."""

    def __init__(self, model_name='ssd'):
        super(Demo, self).__init__()
        self.cfg = Config()
        self.cfg.config_definition()
        model_DIR = self.cfg.DEMO_MODELS[model_name]
        self.net = object_detection.Net(graph_fp='%s/%s/frozen_inference_graph.pb' % (self.cfg.DOWNLOADED_MODELS_DIR, model_DIR),
                                        labels_fp='data/label.pbtxt',
                                        num_classes=90,
                                        threshold=0.6)

    def exec(self, mode=CAMERA_MODE, image=''):
        if mode == STATIC_MODE:
            img_fp = self.cfg.IMAGES_DIR + '/' + image
            img = cv2.imread(img_fp)
            self.net.predict(img=img, display_img=img)
            cv2.waitKey()
            cv2.destroyAllWindows()
        elif mode == CAMERA_MODE:
            cap = cv2.VideoCapture(0)

            while True:
                with tf.device('/gpu:0'):
                    ret, frame = cap.read()
                    in_progress = self.net.get_status()
                    if ret and (not in_progress):
                        resize_frame = cv2.resize(frame, (IMAGE_SIZE, IMAGE_SIZE))
                        self.net.predict(img=resize_frame, display_img=frame)
                    else:
                        click.echo('[Warning] drop frame or in progress')
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            cap.release()
            cv2.destroyAllWindows()


def demo_download():
    import sys
    if sys.version_info[0] >= 3:
        from urllib.request import urlretrieve
    else:
        from urllib import urlretrieve
    import tarfile

    model_url = 'http://download.tensorflow.org/models/object_detection/'
    cfg = Config()
    cfg.config_definition()
    downloaded_models_dir = cfg.DOWNLOADED_MODELS_DIR

    for model, file in cfg.DEMO_MODELS.items():
        click.echo('Downloading all demo models...')
        click.echo('This may take a while.')
        urlretrieve(model_url + file + '.tar.gz', downloaded_models_dir + '/' + file)
        tf = tarfile.open(downloaded_models_dir + '/' + file + '.tar.gz')
        tf.extractall()
