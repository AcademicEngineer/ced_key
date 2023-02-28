# CED_KEY
cedの電子錠化

## 開発規則
* ブランチ名は"frontend" or "backend" or "device", ある程度出来たらmainにマージ.

## ディレクトリ構造
```
.
+- backend  /* Python */
|
+- frontend  /* React */
|  +- admin
|  +- client
|
+- device  /* Raspberry Pi */
```

## デバイス側の設定
GPIOを使用する時はプログラム実行前にデーモンを起動する必要あり
```
$ sudo pigpiod
```
もしくは，起動時に読み込む `/etc/rc.local` に以下を記述
```
pigpiod
```

## 参考記事
[スマートドアロックを自作しました](https://ehbtj.com/electronics/diy-smart-lock/)