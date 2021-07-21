# コップで計量

カメラで容量を測定するアプリ  
  
授業の一環で作成したものです  
現在、ローカルサーバー上でしか動きません  
  
開発者用READMEは[こちら](https://github.com/mikiya1130/Amazon/blob/master/docs/README.md)  

## 説明

- コップに入った液体の容量を計算してくれる
- 任意のコップで利用可能
- カメラがあれば使える

***デモ：***

![デモ動画](https://user-images.githubusercontent.com/63896499/126353857-6919be5a-173d-4cf1-87a4-37c5679e635e.mp4)(1回目50mL追加、2回目100mL追加)  
  
![water](https://user-images.githubusercontent.com/63896499/126361508-ff1f8ab8-d81e-4547-80e6-571268936071.png)
![chopsticks](https://user-images.githubusercontent.com/63896499/126361524-9de9b8f4-3b80-4538-8f30-85f277539c38.png)

## 開発メンバーと主な役割

- フロントエンド [@raylicola](https://github.com/raylicola)
- サーバーサイド [@mhrwh](https://github.com/mhrwh)
- 割り箸の検出 [@hiro6260000](https://github.com/hiro6260000)
- 液体の検出 [@mikiya1130](https://github.com/mikiya1130)

## 使用技術

- HTML
- CSS
- JavaScript + jQuery
- Django
- OpenCV
- PyTorch

## 環境

- Python3.7
- 8G+のメモリ(目安)
- 厚さの薄い透明のコップと暗い背景
- 長さ21cmの割り箸

## 使用方法

```
$ git clone https://github.com/mikiya1130/Amazon.git
$ cd Amazon
$ pip install -r requirements.txt
$ python generate_secretkey_setting.py > .env
```
[ここ](https://zenodo.org/record/3697767)か[ここ](https://drive.google.com/file/d/1wWGPoa7aKBlvml6Awe4AzJUbNlR72K6X/view?usp=sharing)から学習済みの重みをDL  
`measurevolume/detect/`に`TrainedModelWeiht1m_steps_Semantic_TrainedWithLabPicsAndCOCO_AllSets.torch`を配置する  
```
$ python manage.py runserver
```
[http://localhost:8000](http://localhost:8000)にアクセス
