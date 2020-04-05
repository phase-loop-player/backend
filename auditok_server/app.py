import os
import tempfile
import shutil

from flask import Flask, request
from pytube import YouTube
from auditok import split

# pylint: disable=invalid-name
app = Flask(__name__)
TEMP_FILENAME = "temp"


def get_regions(url, dirpath, min_duration, max_duration):
    yt = YouTube(url)
    for stream in yt.streams.filter(mime_type="audio/webm"):
        stream.download(dirpath, TEMP_FILENAME)
        regions = split(
            os.path.join(dirpath, TEMP_FILENAME + ".webm"),
            min_duration,
            max_duration,
        )
        return {"regions": list(regions)}
    return ("No avaiable webm audios", 404)


@app.route("/healthz")
def health():
    return ("", 204)


@app.route("/api/regions")
def get_url_audio_regions():
    url = request.args.get("url")
    if not url:
        return ("url is empty", 400)
    min_duration = float(request.args.get("min_duration", 3))
    max_duration = float(request.args.get("max_duration", 7))
    dirpath = tempfile.mkdtemp()
    try:
        return get_regions(url, dirpath, min_duration, max_duration)
    # pylint: disable=broad-except
    except Exception as e:
        return (str(e), 500)
    finally:
        shutil.rmtree(dirpath)
