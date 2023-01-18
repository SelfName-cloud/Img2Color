import requests
from requests.structures import CaseInsensitiveDict
import base64
import json
from image_test import image_base


def main():
    url = "https://stablehorde.net/api/v2/find_user"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["apikey"] = "WOHBRWNWvqbOZIVzOXhjRQ"

    resp = requests.get(url, headers=headers)
    print(resp.text)


def posting():
    with open(r'/photo_example/face.jpg', 'rb') as f:
        image_sting = base64.b64encode(f.read())
        #print(image_sting)
    #print(type(image_sting))

    url = "https://stablehorde.net/api/v2/generate/async"

    headers = CaseInsensitiveDict()

    headers["Accept"] = "*/*"
    headers["apikey"] = "uDxgeY7nXkjqMXiTj4YEug"
    headers["Content-Type"] = "application/json"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "stablehorde.net"
    headers["Origin"] = "https://aqualxx.github.io"
    headers["Referer"] = "https://aqualxx.github.io/"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"


    data = """{
      "prompt": "pencil sketch",
      "params": {
        "sampler_name": "k_lms",
        "toggles": [
          1,
          4
        ],
        "cfg_scale": 5,
        "denoising_strength": 0.4,
        "seed": "124",
        "height": 896,
        "width": 640,
        "seed_variation": 124,
        "use_gfpgan": true,
        "use_real_esrgan": true,
        "use_ldsr": true,
        "use_upscaling": true,
        "steps": 70,
        "n": 5
      },
      "nsfw": true,
      "trusted_workers": true,
      "censor_nsfw": false,
      "workers": [
        "all_workers"
      ],
      "models": [
        "stable_diffusion"
      ],
      "source_image": "",
      "source_processing": "img2img"
    }"""

    data_test = json.dumps({
      "prompt": "pencil sketch",
      "params": {
        "sampler_name": "k_lms",
        "toggles": [
          1,
          4
        ],
        "cfg_scale": 5,
        "denoising_strength": 0.4,
        "seed": "124",
        "height": 128,
        "width": 128,
        "seed_variation": 124,
        "use_gfpgan": False,
        "use_real_esrgan": False,
        "use_ldsr": False,
        "use_upscaling": False,
        "steps": 10,
        "n": 5
      },
      "nsfw": True,
      "trusted_workers": False,
      "censor_nsfw": False,
      "models": [
        "stable_diffusion"
      ],
      "source_image": image_base,
      "source_processing": "img2img"
    })

    resp = requests.post(url, headers=headers, data=data_test)

    print(resp.text)


def test():
    url = "https://stablehorde.net/api/v2/generate/sync"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["apikey"] = "wVbbonSmPTKH1er4Q5yQpQ"

    data = '{"prompt":"A horde of stable robots", "params":{"n":1, "width": 256, "height": 256}}'

    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.text)


if __name__ == '__main__':
    posting()
    #test()
    #main()



