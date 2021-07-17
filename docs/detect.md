# 水検出・割り箸検出

## 水検出(関数名： detect_water_area())

- [detect_water_area.py](/measurevolume/detect/detect_water_area.py)
    - detect_water_area()

---

- ~~[ ] コップ領域検出 -> 切り取り~~
    - コップが検出できなかった場合
    - 例外throw: NotFoundGlassError
- ~~[ ] コップのエッジ検出~~
- [x] 水の領域を表した2値画像
- [x] 2値画像返す -> server

## 割り箸検出(関数名： get_chopsticks_length_per_pixel())

- [get_chopsticks_length_per_pixel.py](/measurevolume/detect/get_chopsticks_length_per_pixel.py)
    - get_chopsticks_length_per_pixel()

---

- [x] 割り箸検出
    - 割り箸が検出できなかった場合
    - 例外throw: NotFoundChopsticksError
- [x] mm/pixel求める(割り箸の長さ21cmを基準に)
- [x] mm/pixel返す -> server
