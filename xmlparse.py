import xml.etree.ElementTree as etree
for i in range(5):
    tree = etree.parse('d://Keywords/news{}.xml'.format(i))
    print('d://Keywords/news{}.xml'.format(i))
    root = tree.getroot()

    for e in root.findall('.//w/ana[1]'):
         print(e.attrib['lex'])
         
