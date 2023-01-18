import requests
from requests.structures import CaseInsensitiveDict
import json


class StableHordeAPI:
    def __init__(self, apikey):
        self.apikey = apikey
        self.accept = "application/json"
        self.Accept = "*/*"
        self.content_type = "application/json"
        self.connection = "keep-alive"
        self.host = "stablehorde.net"
        self.origin = "https://aqualxx.github.io"
        self.referer = "https://aqualxx.github.io/"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

    def _get(self, url, headers): #http method get
        response = requests.get(url, headers=headers)
        return response.text

    def _post(self, url, headers, data): #http method post
        response = requests.post(url, headers=headers, data=data)
        return response.text

    def _delete(self, url, headers): #http method delete
        response = requests.delete(url, headers=headers)
        return response.text

    def find_user(self): #looks user details on api key
        url = "https://stablehorde.net/api/v2/find_user"

        headers = CaseInsensitiveDict()
        headers["accept"] = self.accept
        headers["apikey"] = self.apikey

        return self._get(url=url, headers=headers)

    def generate_async(self, prompt, image_base, sync=False, sampler_name="k_lms", cfg_scale=10,
                       denoising_strength=0.4, seed=124, height=960, width=640, steps=60, n=5): #initiate an async request to generate image

        url = ""

        if sync:
            url = "https://stablehorde.net/api/v2/generate/sync"
        else:
            url = "https://stablehorde.net/api/v2/generate/async"

        headers = CaseInsensitiveDict()

        headers["Accept"] = self.Accept
        headers["apikey"] = self.apikey
        headers["Content-Type"] = self.content_type
        headers["Connection"] = self.connection
        headers["Host"] = self.host
        headers["Origin"] = self.origin
        headers["Referer"] = self.referer
        headers["User-Agent"] = self.user_agent

        data = json.dumps(
            {
            "prompt": prompt,
            "params": {
                "sampler_name": sampler_name,
                "toggles": [
                    1,
                    4
                ],
                "cfg_scale": cfg_scale,
                "denoising_strength": denoising_strength,
                "seed": str(seed),
                "height": height,
                "width": width,
                "seed_variation": seed,
                "use_gfpgan": True,
                "use_real_esrgan": False,
                "use_ldsr": False,
                "use_upscaling": False,
                "karras": True,
                "steps": steps,
                "n": n
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

        return self._post(url=url, headers=headers, data=data)

    def check_generate(self, worker_id: str): #check status of an async generation request image
        url = "https://stablehorde.net/api/v2/generate/check/{}".format(worker_id)

        headers = CaseInsensitiveDict()
        headers["accept"] = self.accept

        return self._get(url=url, headers=headers)

    def pop_generate(self):
        pass

    def generate_status(self, worker_id: str):
        url = "https://stablehorde.net/api/v2/generate/status/{}".format(worker_id)

        headers = CaseInsensitiveDict()
        headers["accept"] = self.accept

        return self._get(url=url, headers=headers)

    def delete_generate_status(self, worker_id: str):
        url = "https://stablehorde.net/api/v2/generate/status/{}".format(worker_id)

        headers = CaseInsensitiveDict()
        headers['accept'] = self.accept

        return self._delete(url=url, headers=headers)

    def submit_generate(self, worker_id, generation, seed):
        url = "https://stablehorde.net/api/v2/generate/submit"
        data = json.dumps({"id": worker_id, "generation": generation, "seed": seed})

        headers = CaseInsensitiveDict()

        headers["Accept"] = self.Accept
        headers["apikey"] = self.apikey
        headers["Content-Type"] = self.content_type
        headers["Connection"] = self.connection
        headers["Host"] = self.host
        headers["Origin"] = self.origin
        headers["Referer"] = self.referer
        headers["User-Agent"] = self.user_agent

        return self._post(url=url, headers=headers, data=data)


