import textwrap
from playscript.conv.fountain import psc_from_fountain

fountain_str = textwrap.dedent('''\
    Title: ろくでなしの冒険
    Author: アラン・スミシ

    # 登場人物

    六郎
    七郎

    # シーン１

    六郎と七郎、登場。

    @六郎
    どうする？

    @七郎
    帰って寝る

    > おわり
''')

script = psc_from_fountain(fountain_str)

for line in script.lines:
    type_ = line.type.name
    name = getattr(line, 'name', '')
    text = getattr(line, 'text', '')

    print(type_, name, text)
