inp = open("input.txt","r")
wr = open("output.txt","w")
voc_russian = ""
Voc = dict()
translation = ""
vocabulary = open("voc.txt","r")
text_voc = vocabulary.readlines()
text_voc.pop()
for x in text_voc:
    ma = list(map(str,  x.split('\t-\t')))
    Voc[str(ma[1])[:-1]] = str(ma[0])
for y in Voc:
    voc_russian += str(y) +"\t-\t" + str(Voc[y]) + "\n"
wr.write(voc_russian)
