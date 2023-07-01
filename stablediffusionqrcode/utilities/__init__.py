import PIL.Image
from diffusers.utils import load_image


def resize_for_condition_image(input_image: PIL.Image.Image, resolution: int):
    input_image = input_image.convert("RGB")
    input_image = input_image.resize((768,768))
    W, H = input_image.size
    k = float(resolution) / min(H, W)
    H *= k
    W *= k
    H = int(round(H / 64.0)) * 64
    W = int(round(W / 64.0)) * 64
    img = input_image.resize((W, H), resample=PIL.Image.LANCZOS)
    return img


def get_image_from_url(url: str = "https://s3.amazonaws.com/moonup/production/uploads/noauth/KfMBABpOwIuNolv1pe3qX.jpeg"):
    """
    Returns a PIL Image object from a URL.
    """
    if url:
        return load_image(url)
    else:
        return load_image("https://s3.amazonaws.com/moonup/production/uploads/noauth/KfMBABpOwIuNolv1pe3qX.jpeg")

def get_prompt(prompt: str = "a bilboard in NYC with a qrcode"):
    if prompt:
        return prompt
    else:
        return "a bilboard in NYC with a qrcode"