import os
import tempfile
import shutil

from flask import Flask, request
from pytube import YouTube
from auditok import split

# pylint: disable=invalid-name
app = Flask(__name__)
TEMP_FILENAME = "temp"


def get_regions(url, dirpath):
    yt = YouTube(url)
    for stream in yt.streams.filter(mime_type="audio/webm"):
        stream.download(dirpath, TEMP_FILENAME)
        regions = split(os.path.join(dirpath, TEMP_FILENAME + ".webm"))
        return {"regions": list(regions)}
    return ("No avaiable webm audios", 404)


@app.route("/healthz")
def health():
    return ("", 204)


@app.route("/")
def hello_world():
    url = request.args.get("url")
    if not url:
        return ("url is empty", 400)
    dirpath = tempfile.mkdtemp()
    try:
        return get_regions(url, dirpath)
    # pylint: disable=broad-except
    except Exception as e:
        return (str(e), 500)
    finally:
        shutil.rmtree(dirpath)
