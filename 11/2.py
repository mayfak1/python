scores = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ",
}
word=input().upper()
res=0
k=0
while(k!=len(word)):
    for i in scores:
        for j in range(len(scores[i])):
            if k==len(word):break
            if scores[i][j]==word[k]:
                res+=i
                k+=1
print(res)