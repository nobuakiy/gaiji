"""
外字変換プログラム
"""
import time

# 初期設定 定数
buff_length = 1000 * 1000 # 1Mbytes
kanji_start1 = int('80', 16)
kanji_end1   = int('9F', 16)
kanji_start2 = int('E0', 16)
kanji_end2   = int('FF', 16)
gaiji_start = int('F0', 16)
gaiji_end   = int('F9', 16)
CHAR_LF = 13  # b'\n'

converted_map = {}
not_converted_map = {}

def main():

    # 外字変換テーブル取得
    trans_map = {}
    for line in open('TRANS_MAP.csv'):
        key_str, value_str = line.split(',')
        trans_map[int(key_str, 16)] = int(value_str, 16)

    # ファイル名一覧取得
    file_list = []
    for fname in open('filelist.txt'):
        if (fname.startswith('#')):
            continue
        file_list.append(fname.rstrip('\r\n'))

    # 全てのファイルに対して処理
    print("ファイル名,行数,外字件数,変換不可外字件数")
    for filename in file_list:
        out_filename = 'out_' + filename
        with open(filename, "rb") as f:
            count_gaiji = 0 # 外字の件数
            not_converted_gaiji = 0 # 変換できなかった外字
            count_line = 0  # 行数
            # 1M単位で、一気読み
            input_buffer = f.read(buff_length)
            output_buffer = bytearray()
            
            is_kanji_first = False  # 漢字の1バイト目かどうか
            while input_buffer:
                for ch in input_buffer:
                    # 前回の文字が漢字の1バイト目なら、今回は2バイト目
                    if is_kanji_first:
                        is_kanji_first = False
                        ch2 = ch
                        # 外字の範囲かどうか
                        if gaiji_start <= ch1 and ch1 <= gaiji_end:
                            count_gaiji += 1
                            gaiji = (ch1 << 8) + ch2
                            if gaiji in trans_map:
                                converted = trans_map[gaiji] 
                                if gaiji in converted_map:
                                    converted_map[gaiji] += 1
                                else:
                                    converted_map[gaiji] = 1
                                output_buffer.append((converted >> 8) & 0xff)
                                output_buffer.append(converted & 0xff)
                                continue
                            else:
                                not_converted_gaiji += 1
                                if gaiji in converted_map:
                                    not_converted_map[gaiji] += 1
                                else:
                                    not_converted_map[gaiji] = 1
                        output_buffer.append(ch1)
                        output_buffer.append(ch2)
                    # 漢字の1バイト目なら、取っておいて、2バイト目を読んだときに処理
                    elif (kanji_start1 <= ch and ch <= kanji_end1) or (kanji_start2 <= ch and ch <= kanji_end2):
                        is_kanji_first = True
                        ch1 = ch
                    # 漢字に関係ないならそのまま出力
                    else:
                        if ch == CHAR_LF:
                            count_line += 1
                        output_buffer.append(ch)

                fout = open(out_filename, "wb")
                fout.write(output_buffer)
                output_buffer.clear()
                input_buffer = f.read(buff_length)

            print(filename, count_line, count_gaiji, not_converted_gaiji, sep=',')


start = time.perf_counter()
main()
print('\n処理時間:', time.perf_counter() - start)

print('\n外字出現件数')
for key in converted_map:
    print(hex(key), ':', converted_map[key])

print('\nTRANS_MAP.csvに記述のない外字')
for key in not_converted_map:
    print(hex(key), ':', not_converted_map[key])