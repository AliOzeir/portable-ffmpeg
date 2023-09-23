from setuptools import setup
import wget 
import hashlib 
import tarfile 
import os 

out_file = "portable_ffmpeg/ffmpeg.tar.xz"
url = 'https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-5.1.1-amd64-static.tar.xz' 
out_dir = "portable_ffmpeg/"

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def extract():
    with tarfile.open(out_file) as f:
        f.extractall(out_dir)
        
def ffmpegDownload():
    if os.path.exists(out_file) and calculate_md5(out_file) == "4cbbe32169c4ec79a0969d5c92cbcaff":
        extract()
        return 
    
    if os.path.exists(out_file):
        os.remove(out_file)
    
    wget.download(url, out=out_file)
    extract()
    
setup(
    name='portable-ffmpeg',
    version='0.1',
    packages=['portable_ffmpeg'],
    license='MIT',
    include_package_data=True,
    package_data={'portable_ffmpeg': ['ffmpeg-5.1.1-amd64-static/*']},
    install_requires=['wget'],
)

ffmpegDownload()