from playscript.conv.fountain import psc_from_fountain

with open('example.fountain', encoding='utf-8-sig') as f:
    s = f.read()

psc = psc_from_fountain(s)

for line in psc.lines:
    type_ = line.type.name
    name = getattr(line, 'name', '')
    text = getattr(line, 'text', '')

    print(type_, name, text)
