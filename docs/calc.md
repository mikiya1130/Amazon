# 計算、結果をclientへ返す

- [views.py](/measurevolume/views.py)
    - calc_volume()

---

- [x] コップ領域の2値画像受け取る
    - 検出失敗したとき例外: NotFoundGlassError
- [x] 割り箸のmm/pixel受け取る
    - 検出失敗したとき例外: NotFoundChopsticksError
- [x] 水の容量を計算
- [x] フロントに結果返す

```
    {
        exist_glass (boolean): コップの有無,
        exist_chopsticks (boolean): 割り箸の有無,
        volume (number): 容量(mL),
    }
```
