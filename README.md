# 外字変換プログラム

| ファイル名 | 内容 |
| ---------- | ---- |
| gaiji.py | メインプログラム |
| filelist.txt | 入力するファイルの一覧 |
| TRANS_MAP.csv | 外字,変換後の漢字 の形式の変換テーブル |
| DATAFILE1.DAT | テストデータ。 |
| DATAFILE2.DAT | 速度計測用テストデータ。 |
| copy_datafile.cmd | 速度計測用のDATAFILE2.DATをコピーして数を増やす |

* TRANS_MAP.csvは変換テーブルです。SHIFT_JISの文字コードを16進数表記で入れてください
* TRANS_MAP.csv は、速度のチェックのために500件ぐらい入ってますが、文字コードとしてあり得ないものも入っています。
* filelist.txtに、入力ファイルの一覧を書いてください。先頭が # のものは、スキップします。
* 入力ファイルの文字コードは、SHIFT_JIS固定です。
* テストデータのうち、外字が入っているのは DATAFILE1.DATのみです。
* 速度調査をするときには、copy_datafile.cmdを実行して、
* DATAFILE2.DATは、1行1690文字、1万行、31Mbyte近くあります。
* 私の環境のpythonは、3.9.15です。python2では動かないと思います。python3なら、たぶん動く。

実行例
```DOS
(base) D:\nobuakiy\projects\gaiji>python gaiji.py   
ファイル名,行数,外字件数,変換不可外字件数
DATAFILE1.DAT,5,6,1
DATAFILE2.DAT,10800,0,0
DATAFILE3.DAT,10800,0,0
DATAFILE4.DAT,10800,0,0
DATAFILE5.DAT,10800,0,0
DATAFILE6.DAT,10800,0,0
DATAFILE7.DAT,10800,0,0
DATAFILE8.DAT,10800,0,0
DATAFILE9.DAT,10800,0,0
DATAFILE10.DAT,10800,0,0

処理時間: 64.7598322

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
