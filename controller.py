# For RESTful API
# http://flask.pocoo.org/docs/1.0/
from flask import Flask, jsonify, json

import numpy as np
# OpenCV for transforming images
# https://docs.opencv.org/2.4/modules/refman.html
# https://opencv-python-tutroals.readthedocs.io/en/latest/index.html
import cv2 

import model as m

# For AWS
#import boto3

app = Flask(__name__)

# GET /
# Home page - view actions
@app.route('/', methods=['GET'])
def main():
    return jsonify(m.getData()['start'])

# GET /<image>
# Get image
@app.route('/<image>', methods=['GET'])
def actions(image):
    m.generateData(image)
    return jsonify(m.getData()['actions'])

# GET /<image>/flip_h
# Flip image horizontally
@app.route('/<image>/flip_h', methods=['GET'])
def flipHorizontally(image):
    # read image
    img = cv2.imread(image)
    # flip horizontally
    img = cv2.flip(img, 0)
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/flip_v
# Flip image vertically
@app.route('/<image>/flip_v', methods=['GET'])
def flipVertically(image):
    # read image
    img = cv2.imread(image)
    # flip vertically
    img = cv2.flip(img, 1)
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/rotate_n
# Rotate n degrees
@app.route('/<image>/rotate_n/<n>', methods=['GET'])
def rotateN(image, n):
    # read image
    img = cv2.imread(image)
    rows, cols, _ = img.shape
    # rotate by n degrees
    M = cv2.getRotationMatrix2D((cols/2, rows/2), int(n), 1)
    img = cv2.warpAffine(img, M, (cols, rows))
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/grayscale
# Convert to grayscale
@app.route('/<image>/grayscale', methods=['GET'])
def toGrayscale(image):
    # read image and convert to grayscale
    img = cv2.imread(image, 0)
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/resize/<width>/<height>
# Resize
@app.route('/<image>/resize/<width>/<height>', methods=['GET'])
def resize(image, width, height):
    # read image
    img = cv2.imread(image)
    # resize image
    img = cv2.resize(img, (int(width), int(height)))
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/thumbnail
# Generate thumbnail
@app.route('/<image>/thumbnail', methods=['GET'])
def toThumbnail(image):
    # read image
    img = cv2.imread(image)
    # resize to thumbnail size
    img = cv2.resize(img, (75, 100))
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/rotate_l
# Rotate left
@app.route('/<image>/rotate_l', methods=['GET'])
def rotateLeft(image):
    # read image
    img = cv2.imread(image)
    rows, cols, _ = img.shape
    # rotate by 90 degrees left
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
    img = cv2.warpAffine(img, M, (cols, rows))
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])

# GET /<image>/rotate_r
# Rotate right
@app.route('/<image>/rotate_r', methods=['GET'])
def rotateRight(image):
    # read image
    img = cv2.imread(image)
    rows, cols, _ = img.shape
    # rotate by 90 degrees right
    M = cv2.getRotationMatrix2D((cols/2, rows/2), -90, 1)
    img = cv2.warpAffine(img, M, (cols, rows))
    # save changes
    cv2.imwrite(image, img)
    return jsonify(m.getData()['actions'])


if __name__ == '__main__':
    app.run()
