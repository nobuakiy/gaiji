# 外字変換プログラム

| ファイル名 | 内容 |
| ---------- | ---- |
| gaiji.py | メインプログラム |
| filelist.txt | 入力するファイルの一覧 |
| TRANS_MAP.csv | 外字,変換後の漢字 の形式の変換テーブル |
| DATAFILE1.DAT | テストデータ。 |

* TRANS_MAP.csv は、速度のチェックのために500件ぐらい入ってますが、文字コードとしてあり得ないものも入っています。
* filelist.txtに、入力ファイルの一覧を書いてください。先頭が # のものは、スキップします。
* テストデータのうち、外字が入っているのは DATAFILE1.DATのみです。残りは、速度調査に使用しました。
* DATAFILE3.dat～DATAFILE10.datのファイルは、同じ内容です。1行1690文字、1万行、31Mbyte近くあります。
* 私の環境のpythonは、3.9.15です。python2では動かないと思います。python3なら、たぶん動く。

実行例
```DOS
(base) D:\nobuakiy\projects\gaiji>python gaiji.py
ファイル名,行数,外字件数,変換不可外字件数
DATAFILE1.DAT,5,6,1
DATAFILE2.DAT,7,0,0
DATAFILE3.dat,10800,0,0
DATAFILE4.dat,10800,0,0
DATAFILE5.dat,10800,0,0
DATAFILE6.dat,10800,0,0
DATAFILE7.dat,10800,0,0
DATAFILE8.dat,10800,0,0
DATAFILE9.dat,10800,0,0
DATAFILE10.dat,10800,0,0

処理時間: 67.6591614

converted
0xf040 : 1
0xf041 : 1
0xf042 : 1
0xf043 : 1
0xf044 : 1

not converted
0xf340 : 1

(base) D:\nobuakiy\projects\gaiji>

```
