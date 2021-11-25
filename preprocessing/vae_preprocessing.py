# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Provides utilities to preprocess images.

The preprocessing steps for VGG were introduced in the following technical
report:

  Very Deep Convolutional Networks For Large-Scale Image Recognition
  Karen Simonyan and Andrew Zisserman
  arXiv technical report, 2015
  PDF: http://arxiv.org/pdf/1409.1556.pdf
  ILSVRC 2014 Slides: http://www.robots.ox.ac.uk/~karen/pdf/ILSVRC_2014.pdf
  CC-BY-4.0

More information can be obtained from the VGG website:
www.robots.ox.ac.uk/~vgg/research/very_deep/
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

slim = tf.contrib.slim

def preprocess_for_train(images, output_height, output_width):
  image_list = []
  for image in images:
    image = tf.expand_dims(image, 0)
    image = tf.image.resize_bilinear(image, [output_height, output_width], align_corners=False)
    image = tf.squeeze(image)
    image.set_shape([output_height, output_width, 3])
    image = tf.to_float(image)
    image = image/255.0
    image_list.append(image)
  return image_list


def preprocess_for_eval(images, output_height, output_width):
  image_list = []
  for image in images:
    image = tf.expand_dims(image, 0)
    image = tf.image.resize_bilinear(image, [output_height, output_width], align_corners=False)
    image = tf.squeeze(image)
    image.set_shape([output_height, output_width, 3])
    image = tf.to_float(image)
    image = image/255.0
    image_list.append(image)
  return image_list


def preprocess_image(images, box, height, width, output_height, output_width, is_training=True):

  if is_training:
    return preprocess_for_train(images, output_height, output_width)
  else:
    return preprocess_for_eval(images, output_height, output_width)
