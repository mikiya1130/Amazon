# clientから画像受け取り、水検出処理ファイルへ渡す

- [views.py](/measurevolume/views.py)
    - calc_volume()

---

- [x] 画像データ受け取り
```
- エンドポイントURL: calc_volume/
- メソッド: POST
- タイプ: json
- データ: {img_base64: <base64エンコード>}
```
- [x] base64 -> opencvで扱えるデータに変換
- [x] 水検出処理に画像を渡す
    - 関数名： detect_water_area()
    - 引数： img
- [x] 割り箸検出処理に画像を渡す
    - 関数名： get_chopsticks_length_per_pixel()
    - 引数： img
