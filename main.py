#!/usr/bin/env python
'''Fotos_highres_with_Names.
Take a photo using a USB or Raspberry Pi camera.
'''

import os
import time
import json
import requests
import numpy as np
import cv2
import boto3
import sys
import subprocess
from io import BytesIO
from farmware_tools import device, app

# Configura las credenciales
s3 = boto3.client('s3',
                  aws_access_key_id='ASIAYR36TGDD6JHXHJXX',
                  aws_secret_access_key='vStKc+nAH/MZ1hEYM+Ws9Zx/DghcmZd1qHgGn/ta')

# Selecciona el bucket de destino
bucket_name = 'farmbot-photos-uniandes'

def upload_image_to_s3(s3,bucket_name,file):
    s3.upload_file(file, bucket_name, 'ruta/de/destino/imagen.jpg')


if __name__ == '__main__':
    try:
        CAMERA = os.environ['camera']
    except (KeyError, ValueError):
        CAMERA = 'USB'  # default camera
    image =cv2.VideoCapture(0)
    ret, frame = image.read()
    _, buffer = cv2.imencode('.jpg', frame)
    img_bytes = BytesIO(buffer).getvalue()
    upload_image_to_s3(s3,bucket_name,BytesIO(img_bytes))

