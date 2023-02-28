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


## 中央サーバ側の設定
`server/setting.json` に以下のように各電子錠の名前とIPアドレスを対応付ける．また，フォームの回答を収集するスプレッドシートの名前，GoogleカレンダーのIDを指定する．
```
{
  "place": {
    "部屋1": "192.168.100.49",
    "部屋2": "192.168.100.37"
  },
  "sheetName": "CED電子錠（島崎個人Googleアカウントで作成）（回答）",
  "calendarId": "{カレンダーID}"
}
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
