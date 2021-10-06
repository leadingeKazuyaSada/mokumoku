from playscript.conv import fountain, html


def main():
    with open('example.fountain', encoding='utf-8-sig') as f:
        psc = fountain.psc_from_fountain(f.read())

    html_str = html.psc_to_html(psc)
    with open('out.html', 'w', encoding='utf-8') as f:
        f.write(html_str)


if __name__ == '__main__':
    main()
