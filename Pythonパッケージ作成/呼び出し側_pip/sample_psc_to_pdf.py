from playscript.conv import fountain, pdf


def main():
    with open('example2.fountain', encoding='utf-8-sig') as f:
        psc = fountain.psc_from_fountain(f.read())

    pdf_stream = pdf.psc_to_pdf(psc)
    with open('out2.pdf', 'wb') as f:
        f.write(pdf_stream.read())


if __name__ == '__main__':
    main()
