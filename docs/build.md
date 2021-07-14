# 環境構築

## クローン

```
git clone https://github.com/mikiya1130/Amazon.git
```
```
cd Amazon
```
```
code .  # vscode使うなら
```

## 開発環境作成(pyenv + venv)

```
python -V
```
で3系であること確認(違ったら`python3`かwinなら多分`py`。以降読み替えで)  
```
cd <project root dir>
```

### pyenv(この環境限定でPythonのversionを変更する用)(3.7.xじゃなかったら作業)(pyenv使ったことないので、ネットの方が参考なるかも)

(pyenvのインストールは省略(調べて))  
```
pyenv versions
```
3.7.xがなければインストール可能なバージョン確認、インストール  
```
pyenv install -l
pyenv install 3.7.x
```
もう一度`pyenv versions`で3.7.xにアスタリスク付いてなければ↓  
```
pyenv local 3.7.x  # カレントディレクトリ以下ではこのバージョンを使う
```

### venv(この環境限定でモジュールをインストールする用)

```
python -m venv venv
```
gitignoreの都合上、ディレクトリ名(後ろのvenv)は任意やけどvenvのままで  
```
.\venv\Scripts\activate  # win
. venv/bin/activate  # linux
```
```
pip install -r requirements.txt
```

## 開発環境作成(Docker)

1. root権限無しでdockerコマンド動くようにする
    - winならDocker Desktop for Windowsインストールするだけで良かったかな？
    - wsl周りの設定必要やったかも
1. vscodeにRemote Containers拡張機能入れる
1. vscodeでReopen in Container

## Djangoのシークレットキー生成

```
python generate_secretkey_setting.py > .env
```
を実行。  

generate_secretkey_setting.pyはDjangoのシークレットキーを生成して標準出力するプログラム。  
結果を.envファイルに書き込む。  
amazon/settings.pyには定数SECRET_KEYを環境変数から読み込む設定を書いています。  

## 水検出で使用する学習済み重みのDL

1. (ここ)[https://drive.google.com/file/d/1K9q-HwQpR6swK5zrclBFzg_kTX7dGGTR/view?usp=sharing]から学習済みの重みをDL
1. `measurevolume/detect/`に`TrainedModelWeiht1m_steps_Semantic_TrainedWithLabPicsAndCOCO_AllSets.torch`を配置する

## 【任意】VSCode推奨設定

### settings.json

`.vscode/settings.json`に[ここ](https://github.com/mikiya1130/Amazon/blob/0231e0cb09/.vscode/settings.json)の内容をコピペ  

### 拡張機能の追加

- Python(ms-python.python),
- Python Docstring Generator(njpwerner.autodocstring),
- Git History(donjayamanne.githistory),

EXTENSIONSペインの「RECOMMENDED」タブ内に表示されてるはず。  
フロント関連はなくてごめんなさい。  
Dockerの場合は自動でインストールされます  
