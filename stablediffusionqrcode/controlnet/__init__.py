import os
import torch
from diffusers import ControlNetModel, DDIMScheduler, StableDiffusionControlNetImg2ImgPipeline


class StableDiffusion:
    def __init__(self, *args, **kwargs):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def controlnet(self, model="DionTimmer/controlnet_qrcode-control_v1p_sd15",  *args, **kwargs):
        return ControlNetModel.from_pretrained(model, torch_dtype=torch.float32)

    def create_pipe(self, model="runwayml/stable-diffusion-v1-5", *args, **kwargs):
        pipe = StableDiffusionControlNetImg2ImgPipeline.from_pretrained(
            model,
            controlnet=self.controlnet(),
            safety_checker=None,
            cache_dir=os.getenv("cache_dir", "./models"))

        pipe.to(self.device)
        pipe.enable_attention_slicing()
        pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
        return pipe
