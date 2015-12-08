inp = open("input.txt","r")
A = {}
maximum = 0
text = inp.read()
text.replace("!","").replace("?","").replace("!","")
text = text.lower()
listt = text.split()
print(text)
A = {x:listt.count(x) for x in listt}
for y in A:
    maximum = max(maximum,int(A[y]))
maximus = {A[num] :num for num in A}
print(maximum,maximus[maximum])
