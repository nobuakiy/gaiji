# 外字変換プログラム

| ファイル名 | 内容 |
| ---------- | ---- |
| gaiji.py | メインプログラム |
| filelist.txt | 入力するファイルの一覧 |
| TRANS_MAP.csv | 外字,変換後の漢字 の形式の変換テーブル |
| DATAFILE1.DAT | テストデータ。外字が入っているのは DATAFILE1.DATのみ |

* TRANS_MAP.csv は、速度のチェックのために500件ぐらい入ってますが、文字コードとしてあり得ないものも入っています。
* filelist.txtに、入力ファイルの一覧を書いてください。先頭が # のものは、スキップします

実行例
```DOS
C:\Users\myname\gaiji>python gaiji.py
```
