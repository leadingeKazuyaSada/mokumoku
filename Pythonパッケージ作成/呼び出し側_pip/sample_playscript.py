# import json

from playscript import PSc, PScLine, PScLineType
from playscript.conv.json import psc_dump

lines = []

lines.append(PScLine(
    line_type=PScLineType.TITLE,
    text='タイトル'))

lines.append(PScLine(
    line_type=PScLineType.AUTHOR,
    text='著者名'))

lines.append(PScLine(
    line_type=PScLineType.CHARSHEADLINE,
    text='登場人物'))

lines.append(PScLine(
    line_type=PScLineType.CHARACTER,
    name='キャラクタ'))

lines.append(PScLine(
    line_type=PScLineType.H1,
    text='柱'))

lines.append(PScLine(
    line_type=PScLineType.DIRECTION,
    text='ト書き'
))

lines.append(PScLine(
    line_type=PScLineType.DIALOGUE,
    name='名前',
    text='セリフ'
))

psc = PSc.from_lines(lines)
with open('./psc.json', mode='w', encoding='utf-8') as f:
    psc_dump(psc, f, indent=4)

print('Done.')
