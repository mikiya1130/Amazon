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

### pyenv(この環境限定でPythonのversionを変更する用)(3.8.5じゃなかったら作業)(pyenv使ったことないので、ネットの方が参考なるかも)

(pyenvのインストールは省略(調べて))  
```
pyenv versions
```
3.8.5がなければインストール可能なバージョン確認、インストール  
```
pyenv install -l
pyenv install 3.8.5
```
もう一度`pyenv versions`で3.8.5にアスタリスク付いてなければ↓  
```
pyenv local 3.8.5  # カレントディレクトリ以下ではこのバージョンを使う
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

## 【任意】VSCode拡張機能追加

### 推奨拡張機能

- Python(ms-python.python),
- Python Docstring Generator(njpwerner.autodocstring),
- Git History(donjayamanne.githistory),
- Task Runner(forbeslindesay.forbeslindesay-taskrunner),

EXTENSIONSペインの「RECOMMENDED」タブ内に表示されてるはず。  
フロント関連はなくてごめんなさい。  
Dockerの場合は自動でインストールされます  
