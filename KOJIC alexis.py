def medianOdd(mylist):
    listlength=len(mylist)
    sortedvalues=sorted(mylist)
    middleindex=int(((listlength+1)/2)-1)
    return sortedvalues[middleindex]
    
from PIL import Image 
li=[]
for i in range(1,10): 
    nomfic="./Project1Images/"+str(i)+".png"        
    li.append(Image.open(nomfic))
for i in range(9):
     print(li[i].format, li[i].size, li[i].mode)    
newim = Image.new('RGB', li[0].size)
newimpixels=newim.load()
for i in range(li[0].size[0]):    
    for j in range(li[0].size[1]):
        lired=[]
        ligreen=[]
        liblue=[]
        for k in range(9):
            pixels=li[k].load()
            lired.append(pixels[i,j][0])
            ligreen.append(pixels[i,j][1])
            liblue.append(pixels[i,j][2])
        medianred=medianOdd(lired)
        mediangreen=medianOdd(ligreen)
        medianblue=medianOdd(liblue)
        newimpixels[i,j]=(medianred,mediangreen,medianblue)
newim.save("./medianimage.png","png")
        
