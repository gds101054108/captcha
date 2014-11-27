# coding: utf-8

import sys

if not hasattr(sys, 'pypy_version_info'):
    from io import BytesIO
    from captcha.image import ImageCaptcha, WheezyCaptcha

    def test_image_generate():
        captcha = ImageCaptcha()
        data = captcha.generate('1234')
        assert isinstance(data, BytesIO)

        captcha = WheezyCaptcha()
        data = captcha.generate('1234')
        assert isinstance(data, BytesIO)
