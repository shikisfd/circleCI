import math
import os
import sys

# 第一引数に対象フォルダを指定 サンプル実行コマンド python dev\main.py data
args = sys.argv
targetFolder = args[1]

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

folderSize = get_dir_size('data')
print(folderSize)
 # return folderSize
