import re


def convert(arg: str):
    '''
    渡された引数argに対し、1文字ずつスペースを入れて返す。
    '''
    pattern_before = r'(.)'
    pattern_after = r'\1 '

    # 変換
    s = re.sub(
        pattern_before,
        pattern_after,
        arg
    )

    pattern_before = r'\s(ゃ|ゅ|ょ|ぁ|ぃ|ぅ|ぇ|ぉ|ャ|ュ|ョ|ァ|ィ|ゥ|ェ|ォ)'
    pattern_after = r'\1'
    # 変換
    s = re.sub(
        pattern_before,
        pattern_after,
        s
    )

    pattern_before = r'\s{2,}'
    pattern_after = r' '
    # 変換
    s = re.sub(
        pattern_before,
        pattern_after,
        s
    )

    return s


if __name__ == '__main__':
    pass
