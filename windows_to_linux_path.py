import re

def windows_to_wsl(windows_path):
    # WindowsドライブレターをWSL2のマウントポイントに変換
    path = re.sub(r'^([A-Za-z]):', r'/mnt/\1', windows_path)

    # バックスラッシュをフォワードスラッシュに変換
    path = path.replace('\\', '/')

    return path.lower()
