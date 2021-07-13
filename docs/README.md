# 開発者用README

## 役割分担

- Local [@raylicola](https://github.com/raylicola)
    - フロントエンド
- Server [@mhrwh](https://github.com/mhrwh)
    - サーバーサイド(水検出処理除く)
- Detection [@hiro6260000](https://github.com/hiro6260000) [@mikiya1130](https://github.com/mikiya1130)
    - 水検出

## タスクと流れ

1. [画像取得、serverへ渡す](post.md) @Local
1. [clientから画像受け取り、水検出処理ファイルへ渡す](controller.md) @Server
1. [水検出・割り箸検出](detect.md) @Detection
1. [計算、結果をclientへ返す](calc.md) @Server
1. [serverから水の容量取得、ブラウザ表示](print.md) @Local

## 運用方針

### ブランチ

- `master`
    - リリースできるもの
    - 直接pushはNG
    - `develop`からのmergeのみ
- `develop`
    - 各々このブランチを基準にcheckout、pull req

- `<user id>/***`
    - 作業ブランチ

### コミット時のコメント

- 特に統一はしないけど、こだわりなければ[このサイト](https://www.tam-tam.co.jp/tipsnote/program/post16686.html)のスタイルを参考に(個人的にはprefixの末尾に:付けないけど)
    - この前会話してたときの人のリポジトリも参考に
    - 2行目を空行は推奨

### 自動フォーマット

- black使用
- ~~vscode使うなら特に気にせんでいいように設定したはず(保存すると勝手に走るはず)~~
- 環境によって`.vscode`フォルダをGit管理するとまずかったので、各自`.vscode/settings.json`に[ここ](https://github.com/mikiya1130/Amazon/blob/0231e0cb09/.vscode/settings.json)の内容をコピペ推奨

## 推奨環境

- VSCode
- Python 3.8.5
- モジュールは[requirements.txt](../requirements.txt)参照

開発環境が絶対このバージョンでなくてはならないわけではないけど、この環境でテストしてmergeすることにします  

## チートシート

- [環境構築](build.md)
- [チートシート](cheatsheet.md)
