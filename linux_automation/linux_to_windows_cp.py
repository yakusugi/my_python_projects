import shutil
import os

src_dir = "/shares/smb/seagate_hdd_5tb/archive_dir/archives"
dst_dir = "//192.168.0.39/mnt/d/skynew_ubuntuserver_backup/seagate_hdd_5tb/save_point"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
shutil.copytree(src_dir, dst_dir)