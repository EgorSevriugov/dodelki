inp = open("input.txt","r")
tra = open("outputs.txt","w")
voc = open("voc.txt","r")
trans = voc.readlines()
tran = {}
text = inp.read()
print(trans)
for i in range(len(trans)):
    tran[trans[i][:trans[i].index("\t-\t")]] = trans[i][trans[i].index("\t-\t")+1:-1]
text.replace("!","").replace("?","").replace("!","")
text = text.lower()
listt = text.split()
translate = ""
for i in listt:
    if i in tran:
        translate += tran[i] + " "
tra.write(translate)
