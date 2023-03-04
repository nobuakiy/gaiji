# 外字変換プログラム

| ファイル名 | 内容 |
| ---------- | ---- |
| gaiji.py | メインプログラム |
| gaijicython.pyx | CythonでC言語に変換する用のプログラム。同じ名前だとよくないと思って、ちょっと変えた。内容はgaiji.pyとほとんど同じ |
| gaijicython.cp39-win_amd64.pyd | Cythonでコンパイルした結果のモジュール。Pythonで呼び出すことができる |
| callgaiji.py | Cythonでコンパイルしたモジュールを呼び出すためのプログラム。Cythonのときのメインプログラム |
| setup.py | Cythonのコンパイルに使用する |
| filelist.txt | 入力するファイルの一覧 |
| TRANS_MAP.csv | 外字,変換後の漢字 の形式の変換テーブル |
| testdata/DATAFILE1.DAT | テストデータ。 |
| testdata/DATAFILE2.DAT | 速度計測用テストデータ。 |
| copy_datafile.cmd | 速度計測用のDATAFILE2.DATをコピーして数を増やす |

## 説明
* TRANS_MAP.csvは変換テーブルです。SHIFT_JISの文字コードを16進数表記で入れてください
* TRANS_MAP.csv は、速度のチェックのために500件ぐらい入ってますが、文字コードとしてあり得ないものも入っています。
* filelist.txtに、入力ファイルの一覧を書いてください。先頭が # のものは、スキップします。
* 入力ファイルの文字コードは、SHIFT_JIS固定です。
* テストデータのうち、外字が入っているのは DATAFILE1.DATのみです。
* 速度調査をするときには、copy_datafile.cmdを実行して、データファイルの数を増やしてください。
* testdata/DATAFILE2.DATは、1行1690文字、1万行、31Mbyte近くあります。
* 私の環境のpythonは、3.9.15です。

## 実行例
```DOS
(base) D:\nobuakiy\projects\gaiji>mkdir resultdata

(base) D:\nobuakiy\projects\gaiji>python gaiji.py
ファイル名,行数,外字件数,変換不可外字件数
DATAFILE1.DAT, 5, 6, 1
DATAFILE2.DAT, 10800, 0, 0

処理時間: 9.8680592

外字出現件数
F040: 1
F041: 1
F042: 1
F043: 1
F044: 1

TRANS_MAP.csvに記述のない外字
F340: 1

(base) D:\nobuakiy\projects\gaiji>python gaiji.py
ファイル名, 行数, 外字件数, 変換不可外字件数
DATAFILE1.DAT, 5, 6, 1
DATAFILE2.DAT, 10800, 0, 0

処理時間: 7.8049874

外字出現件数
F040: 1
F041: 1
F042: 1
F043: 1
F044: 1

TRANS_MAP.csvに記述のない外字
F340: 1

(base) D:\nobuakiy\projects\gaiji>
```

## Cythonを使ってみた。
CythonでC言語に変換するところから、やっているが、pydファイルがあれば、最後の python callgaiji.py だけで実行できる。
変換するところからやるには、MicrosoftのCコンパイラのインストールが必要になる。
処理時間は、約11秒で普通のPythonの1/6になっている。十分な処理速度で、これ以上の高速化は必要ない。
これはSSDの場合の速度です。

業務プログラムとして実行するなら、1分なのか10秒なのかは大した違いがない。変換テーブル(TRANS_MAP.csv)を作成しているなら、はやいほうがうれしいかも。

```DOC
(base) D:\nobuakiy\projects\gaiji>python setup.py build_ext --inplace
Compiling gaijicython.pyx because it changed.
[1/1] Cythonizing gaijicython.pyx
gaijicython.c
gaijicython.c(5204): warning C4244: '関数': 'Py_ssize_t' から 'int' への変換です。データが失われる可能性があります。
   ライブラリ build\temp.win-amd64-cpython-39\Release\gaijicython.cp39-win_amd64.lib とオブジェクト build\temp.win-amd64-cpython-39\Release\gaijicython.cp39-win_amd64.exp を作成中
コード生成しています。
コード生成が終了しました。

(base) D:\nobuakiy\projects\gaiji>python callgaiji.py
ファイル名, 行数, 外字件数, 変換不可外字件数
DATAFILE1.DAT, 5, 6, 1
DATAFILE2.DAT, 10800, 0, 0

外字出現件数
F040: 1
F041: 1
F042: 1
F043: 1
F044: 1

TRANS_MAP.csvに記述のない外字
F340: 1

処理時間: 1.2350613

(base) D:\nobuakiy\projects\gaiji>
```