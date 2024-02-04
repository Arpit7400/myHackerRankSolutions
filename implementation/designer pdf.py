def designerPdfViewer(h, word):
    # Write your code here
    lst=[]
    for i in range(len(word)):
        k=ord(word[i])-97
        lst.append(h[k])
    return max(lst)*len(word)


h=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
word="zabc"
print(designerPdfViewer(h,word))