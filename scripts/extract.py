import argparse
import requests
import zipfile
import io
import os

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="url to download data")
args = vars(parser.parse_args())

def ensure_url_is_accessible(URL):
    r = requests.get(URL)
    if not r.ok:
        print("Download link expired. Please update download link")
    else:
        download_and_unzip_files(r.content)


def download_and_unzip_files(content):
    current_directory = os.getcwd()
    target_parent_dir = os.path.join(current_directory, r"tmp_unzip_path")
    if not os.path.exists(target_parent_dir):
        os.mkdir(target_parent_dir)
    try:
        z = zipfile.ZipFile(io.BytesIO(content))
        z.extractall(target_parent_dir)
    except Exception as e:
        print(e)
    else:
        print("unzipped successfully")


ensure_url_is_accessible(args.get("url"))
