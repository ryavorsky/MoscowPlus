import xml.etree.ElementTree as etree
for i in range(11):
    tree = etree.parse('d://Keywords/news{}.xml'.format(i))
    print('\nd://Keywords/news{}.xml'.format(i))
    root = tree.getroot()

    res = dict()
    for e in root.findall('.//ana'):
        word = e.attrib['lex']
        if word in res:
            res[word] += 1
        else:
            res[word] =1
    words = list(res.keys())
    for w in words:
        if res[w] <= 2:
            del res[w]
    res1 = [[w,res[w]] for w in res]
    print(res)
         
