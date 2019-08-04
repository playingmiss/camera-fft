# camera-fft

# 概要、使い方
このプログラムは静止画をグレースケールで読み込み、フーリエ変換を行って、その逆変換をマウスイベントで行えるものである。

このコードを実行すると、計5つのウインドウが表示される。このうち、clickというタイトルのウインドウの画面にマウス操作を行うことでフーリエ逆変換を行うようになっている。
また、今回使用した画像をリポジトリにも投稿している

# 実行方法
python実行環境が整備されたコマンドプロンプトを用意してもらい、コードが存在するパスを入力したのちpython cvfft.pyで実行
# 実行ライブラリとバージョン 
- openCV 4.1.0
- matplotlib 3.0.3
- numpy 1.16.2

# 参考文献

マウスイベントの実装
- http://rasp.hateblo.jp/entry/2016/01/24/204539
- https://qiita.com/otakoma/items/04e525ac74b7191dffe6

フーリエ変換
- https://algorithm.joho.info/programming/python/opencv-fft-spectrum/
- https://www.hello-python.com/2018/02/16/numpy%E3%81%A8opencv%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E7%94%BB%E5%83%8F%E3%81%AE%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B%E3%81%A8%E9%80%86%E5%A4%89%E6%8F%9B/

# 実行結果例

![result](https://github.com/playingmiss/camera-fft/blob/master/cvfft.gif)
