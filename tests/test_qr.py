import pytest
from stablediffusionqrcode import qr
import random


VALID_QR_TYPE= 'qrcode.image.pil.PilImage'
SAMPLE_QR = qr.make_qr_from_link("ABC")

@pytest.fixture
def make_qr_from_link():
    return qr.make_qr_from_link

def test_qr_type(make_qr_from_link, input=random.random()):
    result = type(make_qr_from_link(input))
    assert isinstance(result, str)

def test_qr_output(make_qr_from_link, input="ABC"):
    result = make_qr_from_link(input)
    assert result == SAMPLE_QR