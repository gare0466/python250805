import os
import shutil
import glob

# 다운로드 폴더 경로
download_dir = r"C:\Users\student\Downloads"

# 이동할 폴더 경로 (다운로드 폴더 하위에 생성)
dest_dirs = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 폴더 생성 함수
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 파일 이동 함수
def move_files(patterns, dest_folder):
    ensure_dir(dest_folder)
    for pattern in patterns:
        for file in glob.glob(os.path.join(download_dir, pattern)):
            shutil.move(file, os.path.join(dest_folder, os.path.basename(file)))

# 각 폴더별로 파일 이동 (다운로드 폴더 하위에 생성)
for folder, patterns in dest_dirs.items():
    dest_path = os.path.join(download_dir, folder)
    move_files(patterns, dest_path)

print("파일 분류 및 이동이 완료되었습니다.")