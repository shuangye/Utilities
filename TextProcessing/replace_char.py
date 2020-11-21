import sys

interpunctions_en = [
    ',',    '.',    ';',    ':',    '?',    '!',     
    '(', ')',   '[', ']',
];

interpunctions_zh = [
    '，',    '。',    '；',    '：',    '？',    '！',
    '（', '）',   '【', '】'
];


def main(from_set, to_set, path):
    with open(path, encoding = 'utf-8') as file_in:
        for line in file_in:
            for ch in line:
                if ch in from_set:
                    i = from_set.index(ch)
                    print(to_set[i], end = '')
                else:
                    print(ch, end = '')
    


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: {} <target> <path>'.format(sys.argv[0]));
    else:
        target = sys.argv[1]
        path = sys.argv[2]
        if target == 'zh':
            main(interpunctions_en, interpunctions_zh, path)
        elif target == 'en':
            main(interpunctions_zh, interpunctions_en, path)
        else:
            print('unsupported target {}'.format(target))
