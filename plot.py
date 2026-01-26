# 画像をN枚表示するスクリプト

import matplotlib.pyplot as plt
import mnist
import numpy as np

# one_hot_label=Trueのとき
# 10個の0, 1の数値が入っているリストがあり、該当数値をインデックスとしたとき、そのインデックスの要素が１となる。
# つまり4のときは[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]というふうになる
# one_hot_label=Falseのとき
# リストにならず普通の数値になる
# つまり4のときは4が返る
data = mnist.load_mnist(flatten = False, one_hot_label=False)
# 返り値は(訓練画像, 訓練ラベル), (テスト画像, テストラベル)となる。

training_idx = 0
test_idx = 1
image_idx = 0
label_idx = 1

for i in range(5):
    print(data[training_idx][image_idx][i].shape)
    
    plt.imshow(data[training_idx][image_idx][i][0])
    print(data[training_idx][1][label_idx])
    plt.show()
