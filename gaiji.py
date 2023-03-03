"""
外字変換プログラム
"""

# 初期設定 定数
buff_length = 1000 * 1000 # 1Mbytes
kanji_start1 = int('80', 16)
kanji_end1   = int('9F', 16)
kanji_start2 = int('E0', 16)
kanji_end2   = int('FF', 16)
gaiji_start = int('F1', 16)
gaiji_end   = int('F9', 16)
CHAR_LF = b'\n'

# 初期設定 変数
line_count = 1

# 外字変換テーブル取得
trans_map = {}
for line in open('TRANS_MAP.csv'):
    key_str, value_str = line.split(',')
    trans_map[int(key_str, 16)] = int(value_str, 16)

# ファイル名一覧取得
file_list = []
for fname in open('filelist.txt'):
    file_list.append(fname.rstrip('\r\n'))
print (file_list)

# 全てのファイルに対して処理
for filename in file_list:
    with open(filename, "rb") as f:
        # 1M単位で、一気読み
        input_buffer = f.read(buff_length)
        output_buffer = bytearray(input_buffer)
        is_kanji_first = False
        while input_buffer:
            for ch in input_buffer:
                if is_kanji_first:
                    is_kanji_first = False
                    ch2 = ch
                    if gaiji_start <= ch1 and ch1 <= gaiji_end:
                        gaiji = (ch1 << 8) + ch2
                        converted = trans_map[gaiji] 
                elif (kanji_start1 <= ch and ch <= kanji_end1) or (kanji_start2 <= ch and ch <= kanji_end2):
                    is_kanji_first = True
                    ch1 = ch

                else:
                    if ch == CHAR_LF:
                        line_count += 1

            input_buffer = f.read(buff_length)

