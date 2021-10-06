import pickle

from psc_parse import PscClass, JumanPsc
from psc_parse.model import predict

print(f'{PscClass.CHARACTER.value=}')

JUMAN_COMMAND = 'jumanpp_v2'
JUMAN_OPTION = r'--config=C:\ProgramData\jumanpp\model\jumandic.conf'


def main():
    # 形態素解析器
    juman = JumanPsc(
        command=JUMAN_COMMAND, option=JUMAN_OPTION)

    # 予測モデル
    with open('model.pkl', 'rb') as f:
        tree = pickle.load(f)

    # 台本を行に分けて、各行の種類を予測する
    lines = [
        '怠け者の国',
        '　　詠み人知らず',
        '',
        '登場人物',
        '　　男',
        '　　女',
        '',
        '第一幕',
        '',
        '男「飯は？」',
        '女「ないよ」',
        '',
        '　　おわり'
    ]
    classes = predict(juman, tree, lines)
    for c in classes:
        print(PscClass(c))


if __name__ == '__main__':
    main()
