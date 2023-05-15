<h1 align="center"> Files compressor </h1> <br>

<p align="center">
  A simple api to handle file compression, using ffmpeg.
</p>


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Features](#features)
- [Quick Start](#quick-start)
- [Testing](#testing)


## Introduction

This a simple API to handle file compression, using fastapi to handle the requests and ffmpeg to compress the files. The file must be sended as form-data.

## Features
  - Video compression

## Quick Start
create a virtualenv and install the requirements:
```bash
$ python3 -m venv venv 
$ pip install -r requirements.txt
$ source ./venv/bin/activate
```

run the app: 
```bash
$ python main.py
```

app will be served by uvicorn in local, but for production is better use gunicorn. 

to compression works, you'll need to install ffmpeg in your machine.

## Testing

```python
def compress_video(file):
    res = requests.post('http://127.0.0.1:8000/compress_form_data_video', data={'filename': file.filename, 'ext': file.filename.split('.')[-1]}, files={'file': file})
    
    if res.status_code >= 200 and res.status_code < 300:
       return res.content
    raise Exception('Cannot compress video')
```

