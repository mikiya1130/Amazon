# 画像取得、serverへ渡す

- [index.html](/measurevolume/templates/measurevolume/index.html)
- [style.css](/measurevolume/static/measurevolume/css/style.css)
- [script.js](/measurevolume/static/measurevolume/js/script.js)

---

- [x] サイトアクセス時に自動でカメラのリアルタイム映像を出力
    - (カメラの使用許可出す)
    - カメラ取得できない場合の例外処理
- [x] Webカメラの映像から定期的にフレームを取得
- [x] 画像ファイルに変換
    - 解像度: 長辺(横)840px以下
- [x] 画像ファイルをサーバー側に渡す
```
リクエスト
    - エンドポイントURL: calc_volume/
    - メソッド: POST
    - タイプ: json
    - データ: {img_base64: <base64エンコード>}
```
