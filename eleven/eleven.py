import random
#opens the txt file in read mode
f = open("txt-eleven.txt","r")
#test the mode if it's read
if f.mode == 'r':
    txt = f.read()
    #punct = all of the punctation
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    keim = ""
    for char in txt:
        #if character is not a punct make a space
        if char not in punct:
            keim = keim + char
    #split where there is space
    keim1=keim.split(" ")
    keim1_len= len(keim1)
    keim2=[]
    #s for space
    s=" "
    for i in range(0,keim1_len-2):
            x = keim1[i]
            y = keim1[i+1]
            z = keim1[i+2]
            w = x + s + y + s + z
            keim2.append(w)
    random.shuffle(keim2)
    keim3=' '.join(keim2)
    print keim3
