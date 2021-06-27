# serverから水の容量取得、ブラウザ表示

- [index.html](/measurevolume/templates/measurevolume/index.html)
- [style.css](/measurevolume/static/measurevolume/css/style.css)
- [script.js](/measurevolume/static/measurevolume/js/script.js)

---

```
レスポンス
    - 200 OK
        {
            exist_glass (boolean): コップの有無,
            exist_chopsticks (boolean): 割り箸の有無,
            volume (number): 容量(mL),
        }
    - 500番台エラー処理
```
- [ ] コップあり、割り箸あり
    - 画像に重ね合わせて表示
- [ ] コップ無し
    - メッセージ「コップを写してください」
- [ ] 割り箸無し
    - メッセージ「割り箸を写してください」
- [ ] サーバーエラー対応

---

- [ ] 表示する映像はディスプレイ(ブラウザのウィンドウ)をはみ出さない最大サイズ
    - 上下or左右どちらかだけに帯(どちらにも出ないこともある、両方には出ない)
- [ ] 【ex】スマホの向き検出→横持ち推奨alert
    - Webアプリなのでセンサは使わない？
    - 横幅取得して、閾値で判定？