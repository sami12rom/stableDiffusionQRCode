import argparse
import sys
import qr
from utilities import *
from controlnet import StableDiffusion
import torch
from datetime import datetime

# add argument passing capability
parser=argparse.ArgumentParser()
parser.add_argument("--qr_source", help="Link or string to make qr code")
parser.add_argument("--image_to_combine", help="link to image to combine")
args=parser.parse_args()
print(f"Args: {args}")

output_location = f"""../output/qr_{datetime.now().strftime("%Y-%m-%dT%H-%M-%S")}.png"""

# create QR code and image input
qr_source = qr.make_qr_from_link(args.qr_source)
image_to_combine = get_image_from_url(args.image_to_combine)

# create stable diffusion pipeline
pipe = StableDiffusion().create_pipe()

# picture to diffuse
init_image = resize_for_condition_image(image_to_combine, 768)
condition_image = resize_for_condition_image(qr_source, 768)
generator = torch.manual_seed(123121231)


try:
    image = pipe(prompt="a bilboard in NYC with a qrcode",
                 negative_prompt="ugly, disfigured, low quality, blurry, nsfw",
                 image=init_image,
                 control_image=condition_image,
                 width=768,
                 height=768,
                 guidance_scale=20,
                 controlnet_conditioning_scale=1.5,
                 generator=generator,
                 strength=0.9,
                 num_inference_steps=10,
                 )
    image.images[0].save(output_location)
    print("image diffused...")

except Exception as e:
    print(f"Error: {e}")
