def  maxSequence(seq):
    seq_len=len(seq)
    max = 0
    maxi = 0
    maxj = 0
    for i in range(0,seq_len-1):
        for j in range(i+1,seq_len):
            x = sum(seq[i:j])
            if max < x:
                max = x
                maxi = i
                maxj = j
    max_seq = seq[maxi:maxj]
    return max_seq

seq=[]
seq = input("Give me a list sequence: ")
print sum(maxSequence(seq)),":",maxSequence(seq)
