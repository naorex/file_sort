import os
from windows_to_linux_path import windows_to_wsl

# 対象のフォルダパスを指定
folder_path = windows_to_wsl(input('作業するフォルダのパスを入力: '))

# 変更後のファイル名の接頭辞を指定
prefix = input('ファイル名の接頭辞を指定(imgなど): ')

# 読み込む拡張子を指定
extension = '.' + input('読み込む対象の拡張子を指定(pngなど): ')

# ファイル名の開始番号を指定
start_number = int(input('ファイル名の開始番号を指定(over 1): '))

# フォルダ内のファイル名の一覧を取得して作成時刻順にソート
file_list = sorted(os.listdir(folder_path), key=lambda x: os.stat(
    os.path.join(folder_path, x)).st_ctime)

# ========================================================================================================
# この方法では、os.listdir() 関数でフォルダ内のファイル名の一覧を取得した後、
# sorted() 関数を使ってファイル作成時刻でソートしています。sorted() 関数の key 引数には、
# ファイルの作成時刻を取得するために、os.stat() 関数でファイルのステータス情報を取得し、st_ctime 属性を指定しています。
# ========================================================================================================

# ファイル名を一括で変更する
for i, file_name in enumerate(file_list):
    if file_name.endswith(extension):
        # 新しいファイル名を作成
        new_file_name = f"{prefix}{start_number + i - 1}{extension}"
        # ファイル名を変更
        os.rename(os.path.join(folder_path, file_name),
                  os.path.join(folder_path, new_file_name))
