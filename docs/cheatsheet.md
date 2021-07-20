# チートシート

## 仮想環境(venv)出入り

### 入る

```
.\venv\Scripts\activate  # win
. venv/bin/activate  # linux
```

### 出る

```
deactivate
```

## 作業ブランチの用意

```
git checkout develop
```
```
git checkout -b <ブランチ名>
```
↑ブランチ作成+移動  
(`git branch <ブランチ名>; git checkout <ブランチ名>;`相当)  

## リモート→ローカル(git pull)

```
git pull origin 
```

## ローカル→リモート(git push)

```
git push -u origin HEAD
```
`HEAD`=`@`=`最新コミット(ここでは現在のブランチの意味)`  
-uオプション付けたなら次回からは`git push`でOK  

仮にググって出てきても、-fオプションは注意  
相談してからでよろしくお願いします  

## developの変更を作業ブランチに取り込み

```
git merge --no-ff origin/develop
```

## python manage.py

テストサーバー起動  

```
python manage.py runserver
```

停止は`Ctrl-c`

テスト実行

```
python manage.py test <test_label>
```

## ファイルのリネーム、移動、削除

```
git mv <from> <to>
git rm <file>
```
を使う。

## モジュール追加したい場合

`pip install`したら[requirements.txt](../requirements.txt)に追記  
