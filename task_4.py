
import os
import sys
import shutil
from datetime import datetime

def backup_files(src, dst):
    # Check existence
    if not os.path.exists(src):
        print("Error: Source directory does not exist.")
        return
    
    if not os.path.exists(dst):
        print("Error: Destination directory does not exist.")
        return

    for file in os.listdir(src):
        src_path = os.path.join(src, file)

        if os.path.isdir(src_path):
            continue  # Skip subfolders

        dst_path = os.path.join(dst, file)

        # If file exists → append timestamp
        if os.path.exists(dst_path):
            name, ext = os.path.splitext(file)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            dst_path = os.path.join(dst, f"{name}_{timestamp}{ext}")

        shutil.copy2(src_path, dst_path)
        print(f"Copied: {file} → {dst_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source> <destination>")
    else:
        backup_files(sys.argv[1], sys.argv[2])
