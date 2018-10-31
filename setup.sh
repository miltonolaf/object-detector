#!/usr/bin/env bash

echo "Downloading pre-trained models ..."
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz
wget http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_11_06_2017.tar.gz
wget http://download.tensorflow.org/models/object_detection/rfcn_resnet101_coco_11_06_2017.tar.gz
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gz
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_resnet_v2_atrous_coco_11_06_2017.tar.gz
wget ftp://mi.eng.cam.ac.uk/pub/mttt2/models/vgg16.npy

echo "Extracting downloaded models ..."
tar -xvzf models/ssd_mobilenet_v1_coco_11_06_2017.tar.gz
tar -xvzf models/ssd_inception_v2_coco_11_06_2017.tar.gz
tar -xvzf models/rfcn_resnet101_coco_11_06_2017.tar.gz
tar -xvzf models/faster_rcnn_resnet101_coco_11_06_2017.tar.gz
tar -xvzf models/faster_rcnn_inception_resnet_v2_atrous_coco_11_06_2017.tar.gz
