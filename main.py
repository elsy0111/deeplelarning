<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

limx = -5
minx = limx
maxx = 5

def f(x):
    y = (x-1)**2
    return y

def lim(x):
    h = 1e-4
    lim = (f(x + h) - f(x - h))/(2*h)
    return lim

def b(x):
    b = f(x) - (lim(x) * x)
    return b

def line(x,limx):   
    y = lim(limx) * x + b(limx)
    return y

x = np.arange(minx,maxx,0.01)
y = f(x)

while(limx < maxx):

    limx += 0.1
    y1 = line(x,limx)

    plt.xlim(minx,maxx)
    plt.ylim(-5,20)

    plt.plot(x,y1)
    plt.plot(x,y)

    plt.pause(0.01)
    plt.clf()
=======
# playground-dataライブラリのplygdataパッケージを「pg」という別名でインポート
import plygdata as pg

# 問題種別で「分類（Classification）」を選択し、
# データ種別で「2つのガウシアンデータ（TwoGaussData）」を選択する場合の、
# 設定値を定数として定義
PROBLEM_DATA_TYPE = pg.DatasetType.ClassifyTwoGaussData

# 各種設定を定数として定義
TRAINING_DATA_RATIO = 0.5  # データの何％を訓練【Training】用に？ (残りは精度検証【Validation】用) ： 50％
DATA_NOISE = 0.0           # ノイズ： 0％

# 定義済みの定数を引数に指定して、データを生成する
data_list = pg.generate_data(PROBLEM_DATA_TYPE, DATA_NOISE)

# データを「訓練用」と「精度検証用」を指定の比率で分割し、さらにそれぞれを「データ（X）」と「教師ラベル（y）」に分ける
X_train, y_train, X_valid, y_valid = pg.split_data(data_list, training_size=TRAINING_DATA_RATIO)

print("---------X_train--------")
print(X_train)
print("---------y_train--------")
print(y_train)
>>>>>>> origin/master
