#!/usr/bin/env python3

import time

# 経過時間を保持する変数
keika_time = 0

# while文を使って繰り返し処理
while(keika_time < 20):
    # 1秒間待機する
    time.sleep(1)
    # 経過時間を更新する
    keika_time = keika_time + 1
    # 経過時間を画面に表示
    print("経過時間: {} 秒".format(keika_time))