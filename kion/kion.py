#!/usr/bin/env python3

# ライブラリのインポート
import csv
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('font', family='Noto Sans CJK JP')
os.environ["QT_LOGGING_RULES"] = "*=false"

# 読み出したデータを保持する配列
hizuke_data = []
kion_data = []

# CSVファイルを開く
with open("kion.csv") as f:
    # 開いたCSVファイルからデータを取り出す
    rows = csv.reader(f)
    # 取り出したデータを1行ずつ処理
    for row in rows:
        # 日付のデータを取り出す
        hizuke = row[0]
        # 気温のデータを取り出す
        kion = float(row[1])

        #############################
        # 条件分岐の練習
        #############################
        # 気温が30度以上だったら
        if kion >= 30:
            print("{}は気温が30度以上ありました。".format(hizuke))
        #############################

        # 取り出したデータを配列に追加
        hizuke_data.append(hizuke)
        kion_data.append(kion)

# グラフを描画するための設定
plt.xticks(rotation=30)
plt.xlabel("-日付-")
plt.ylabel("-気温-")
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.2, top=0.9)

# グラフを作成
graph = plt.plot(hizuke_data, kion_data)
# グラフを画像にして保存
plt.savefig("kion_graph.png")
print("気温のグラフを作成しました。")
