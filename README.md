# Moguratataki
自動モグラたたきゲーム

Biglobe様のブラウザゲーム,もぐらたたきの攻略AI
http://www5b.biglobe.ne.jp/~chou3/Play/mogura/mogura.html

Pyautoguiを使って画像処理を行い,モグラが出てきた穴を自動でクリックする.

### 実行の前に
- センター位置キャリブレーション
下記手順でmoguratataki.pyを実行すると,はじめに画面中央のもぐらの穴にマウスカーソルが移動する．
この時,もぐらの穴の中心にマウスカーソルが合っていない場合は,以下の方法でキャリブレーションを実施のこと．

1. 「moguratataki.py」の38行目の"return 0"をコメントアウト解除する.
2. 「moguratataki.py」の28, 29行目のオフセット値を調整する．
3. 「moguratataki.py」を実行してもぐらの穴の中心にマウスカーソルが合うか確認する.
4. 中心に合っていれば,5へ.もし合わなければ2からやり直し.
5. 1で解除した"return 0"のコメントアウトを再びコメントアウトする.
6. 完了!

### 実行
1. ブラウザで「もぐらたたき」を開く
2. ターミナル(Ubuntuなら「端末」, Windowsならコマンドプロンプト)を開く
3. ブラウザとターミナルが重ならないようにPC画面上に配置する
4. ターミナル上で下記コマンドでPythonを実行する

```
$python3 moguratataki.py
```

5. もぐらたたきの「ゲーム開始」を押す
