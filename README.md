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

## 参考記事
[スマートドアロックを自作しました](https://ehbtj.com/electronics/diy-smart-lock/)

## セキュリティ設定
- [ ] sshのポート番号を22 -> 15022に変更
- [ ] fail2banの導入 (デーモン化)
- [ ] solのみ閲覧制限
- [ ] raspberrypiのパスワード変更
- [ ] firewall(ufw)の導入 (15022以外deny)
- [ ] ipの固定