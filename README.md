# watermark

[![Build Status](https://travis-ci.org/xiachufang/watermark.svg?branch=master)](https://travis-ci.org/xiachufang/watermark) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python2.svg?style=social)

Tools for Watermarking Pictures


## Install

```
$ pip install -e .
```

## Usage

```python
>>> from watermark import add_chu_studio_watermark
>>> marked_image = add_chu_studio_watermark("/path/to/image", "This is a watermark")
>>> with open('/path/to/marked_image', 'wb') as f:
>>>     f.write(marked_image)
```
