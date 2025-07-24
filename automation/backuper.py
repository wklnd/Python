import zipfile, os
from datetime import datetime

src_folder = "./folder_to_backup"
backup_name = f"backup_{datetime.now():%Y-%m-%d}.zip"

with zipfile.ZipFile(backup_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(src_folder):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, src_folder)
            zipf.write(full_path, arcname)

print(f"Backup created: {backup_name}")
