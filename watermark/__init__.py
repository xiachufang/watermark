# coding: utf-8

from io import BytesIO

from os import path
from PIL import Image, ImageDraw, ImageFont


_PREFIX = path.abspath(path.dirname(__file__))


def add_chu_studio_watermark(f, user_name, std_weight=None, std_height=None):
    '''watermark tool for chu_studio
    :param f: file name or a file object
    :param user_name: lecturer name to add
    :param std_weight: expect img width
    :param std_height: expect img height
    :returns: string value of new img
    :exception : ValueError if original img does not match expect width and height
    '''
    image = Image.open(f)

    w, h = image.size
    if std_weight and std_height:
        if w != std_weight or h != std_height:
            raise ValueError()

    # 水印水平中线距图片底边的偏移量
    offset = 177
    # 黑白水印 icon
    watermark = {
        'white': Image.open(path.join(_PREFIX, 'static/water-white.png')),
        'black': Image.open(path.join(_PREFIX, 'static/water-black.png'))
    }
    # 加载字体
    font40 = ImageFont.truetype(path.join(_PREFIX, 'static/SourceHanSansCN-Heavy.otf'), size=40)
    mw = mh = 81

    # 确保图片模式为 RGB，大小与原图一致
    img = Image.new("RGB", image.size)

    # 粘贴原图
    img.paste(image, (0, 0))

    # 初始化 Draw 对象
    draw = ImageDraw.Draw(img)

    # 设置 chustudio logo 及讲师名
    tw, th = draw.textsize(user_name, font=font40)

    area = img.crop(((w - (tw + mw + 20)) / 2, h - offset - 50, w - (w - (tw + mw + 20)) / 2, h - offset + 50))
    area_rgba = area.histogram()

    rs, gs, bs = area_rgba[:256], area_rgba[256:512], area_rgba[512:768]
    r = sum(rs) and sum([i * x for i, x in enumerate(rs)]) / sum(rs) or 0
    g = sum(gs) and sum([i * x for i, x in enumerate(gs)]) / sum(gs) or 0
    b = sum(bs) and sum([i * x for i, x in enumerate(bs)]) / sum(bs) or 0

    # 用 YIQ 确定水印颜色
    # https://24ways.org/2010/calculating-color-contrast/
    yiq = (r * 299 + g * 587 + b * 114) / 1000
    color = 'black' if yiq >= 128 else 'white'

    draw.text(((w - mw - tw) / 2.0 + mw, h - offset - th / 2), user_name, fill=color, font=font40)
    img.paste(watermark[color], (int((w - mw - tw) / 2), h - offset - int(mh / 2)), mask=watermark[color])

    new_file = BytesIO()
    img.save(new_file, image.format, quality=100)
    return new_file.getvalue()
