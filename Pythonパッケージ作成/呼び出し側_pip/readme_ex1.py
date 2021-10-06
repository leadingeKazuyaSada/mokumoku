from playscript import PScLineType, PScLine, PSc

title = PScLine.from_text(PScLineType.TITLE, 'ろくでなしの冒険')
h1 = PScLine.from_text(PScLineType.H1, 'シーン１')
direction = PScLine.from_text(PScLineType.DIRECTION, '六郎と七郎、登場。')
dialogue1 = PScLine.from_text(PScLineType.DIALOGUE, '六郎「どうする？」')
dialogue2 = PScLine.from_text(PScLineType.DIALOGUE, '七郎「帰って寝る」')
endmark = PScLine.from_text(PScLineType.ENDMARK, 'おわり')

script = PSc(
    lines=[
        title,
        h1,
        direction,
        dialogue1,
        dialogue2,
        endmark,
    ]
)

for line in script.lines:
    type_ = line.type.name
    name = getattr(line, 'name', '')
    text = getattr(line, 'text', '')

    print(type_, name, text)
