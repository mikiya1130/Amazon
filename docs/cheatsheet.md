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

## python manage.pyの実行

### runserver

VSCodeの拡張機能「Task Runner(sanaajani.taskrunnercode)」を入れるとExplorerペインの一番下に「TASK RUNNER」ってタブが追加されます。  
その中の`runserver`クリックで`python manage.py runserver`相当のコマンドを実行できます。  

### test(6/27現在テスト未作成)

同じく「TASK RUNNER」タブの`test`でテスト実行できます。  
どのテストを実行するか入力してEnterしてください。  
空白のままEnterで全てのテストを実行します。  
`python manage.py test <test_label>`相当。  


## ファイルのリネーム、移動、削除

```
git mv <from> <to>
git rm <file>
```
を使う。

## モジュール追加したい場合

`pip install`したら[requirements.txt](../requirements.txt)に追記  
