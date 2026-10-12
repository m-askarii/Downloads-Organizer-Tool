from pathlib import Path
import shutil
import time

downloads = Path.home() / "Downloads"

video_extensions = [
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm",
    ".m4v", ".mpg", ".mpeg", ".3gp", ".3g2", ".ts", ".mts",
    ".m2ts", ".ogv", ".rm", ".rmvb", ".vob", ".asf", ".divx",
    ".f4v", ".amv", ".mxf"
]

audio_extensions = [
    ".mp3", ".aac", ".wav", ".flac", ".alac", ".ogg", ".oga",
    ".wma", ".m4a", ".aiff", ".aif", ".opus", ".mid", ".midi",
    ".amr", ".ac3", ".ape", ".mka", ".ra", ".au", ".dsf", ".dff"
]

image_extensions = [
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif",
    ".webp", ".svg", ".heic", ".heif", ".avif", ".ico", ".raw",
    ".cr2", ".cr3", ".nef", ".arw", ".dng", ".orf", ".rw2",
    ".pef", ".srw", ".jfif", ".pjpeg", ".pjp", ".apng", ".jpe"
]

videos = 0
audios = 0
images = 0
pdfs_docxs = 0
others = 0

for item in downloads.iterdir():
    if item.is_file():

        extension = item.suffix.lower()

        if extension in video_extensions:
            destination = downloads / "videos"
            videos += 1

        elif extension in audio_extensions:
            destination = downloads / "audios"
            audios += 1

        elif extension in image_extensions:
            destination = downloads / "images"
            images += 1

        elif extension in {".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt"}:
            destination = downloads / "pdfs & docxs"
            pdfs_docxs += 1

        else:
            destination = downloads / "others"
            others += 1

        destination.mkdir(exist_ok=True)

        shutil.move(item, destination)

print("📊Organizational Summary:")
print()
print(f"   {'🎞️Videos':<16}: {videos}")
print(f"   {'🎙️Audios':<16}: {audios}")
print(f"   {'🖼️Images':<16}: {images}")
print(f"   {'📜PDFs & DOCXs':<15}: {pdfs_docxs}")
print(f"   {'📂Others':<15}: {others}")
print()
print("-" * 30)

input("Press ENTER to exit...")