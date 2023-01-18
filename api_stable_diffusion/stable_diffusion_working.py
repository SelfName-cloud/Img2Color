from api_stable_diffusion.api import StableHordeAPI
import cv2 as cv
import numpy as np
from numpy import random
from PIL import Image
import base64
import json
import time
import os


class StableDiffusionWorking(StableHordeAPI):
    def __init__(self, image, apikey):
        super().__init__(apikey=apikey)
        self.image = image
        self.height, self.width, self.channels = cv.imdecode(np.fromstring(self.image, np.uint8), cv.IMREAD_COLOR).shape
        self.image_pencil_base = self.get_image_pencil_base64(self.image)
        self.image_base = self.convert_image_base64(self.image)
        #self.desc = desc

    def convert_image_base64(self, image):
        image_base = str(base64.b64encode(image))[2:-1]
        return image_base

    def get_image_pencil_base64(self, image):
        img = np.fromstring(image, np.uint8)
        img = cv.imdecode(img, cv.IMREAD_COLOR)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.medianBlur(img, 5)
        img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1) #1
        img = Image.fromarray(img, mode='L')
        path = r'api_stable_diffusion/temp/temp{}.png'.format(random.randint(0, 12000))
        img.save(path)
        with open(path, 'rb') as ff:
            file = ff.read()
        image_base_pencil = str(base64.b64encode(file))[2:-1]
        os.remove(path=path)
        return image_base_pencil

    def generate_image(self, image_base, prompt, **kwargs):

        height = int(64 * int(kwargs['height'] / 64))
        width = 64 * int((height * (self.width / self.height)) / 64)

        ids = json.loads(self.generate_async(prompt=prompt, image_base=image_base, sync=kwargs['sync'], sampler_name=kwargs['sampler_name'],
                                             cfg_scale=kwargs['cfg_scale'], denoising_strength=kwargs['denoising_strength'],
                                             seed=124, height=height, width=width, steps=kwargs['steps'], n=kwargs['n']))
        print(ids)
        if 'message' in ids.keys():
            message = {'error': ids['message']}
            return message

        while True:
            time.sleep(1)
            check = json.loads(self.check_generate(worker_id=ids['id']))
            print(check)
            if check['done']:
                break

        status = json.loads(self.generate_status(worker_id=ids['id']))
        img_dict = {}
        #for n_img in range(kwargs['n']):
        img_dict['first'] = status['generations'][0]['img'] #str(n_img)

        return img_dict

    def run_stable_diffusion(self):

        #if self.desc:
        #   pass

        image_paint = self.generate_image(image_base=self.image_base, prompt='oil painting', sync=False,
                                          sampler_name='k_lms', cfg_scale=10, denoising_strength=0.4, height=640, steps=60, n=1)

        image_pencil = self.generate_image(image_base=self.image_pencil_base, prompt='pencil sketch', sync=False,
                                          sampler_name='k_lms', cfg_scale=10, denoising_strength=0.3, height=640, steps=60, n=1)

        ready_data = {'image_paint': image_paint, 'image_pencil': image_pencil}

        return ready_data

