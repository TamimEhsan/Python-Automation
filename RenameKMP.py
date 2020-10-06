import os
def KMPSearch(pat, txt , lps): 
    M = len(pat) 
    N = len(txt) 
    j = 0 
    i = 0 
    while i < N: 
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M: 
            return (i-j)
            j = lps[j-1]
	    	
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1] 
            else:
                i += 1
    return -1

def computeLPSArray(pat, M, lps): 
    len = 0
    lps[0]
    i = 1
    while i < M: 
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1



path = input("enter the dir: ")
prefix = input("enter the prefix to be matched: ")
digit = input("the number of characted in the expected string ( 7 for roll usually): ")
digit = int(digit)
tot = 0
num = 0
M = len(prefix)
lps = [0]*M
unchanged = []
changed = []
computeLPSArray(prefix, M, lps)
for filename in os.listdir(path):
    tot+=1
    extension = os.path.splitext(filename)[1]
    index = KMPSearch(prefix, filename, lps)
    if index == -1 or index+digit>len(filename):
        unchanged.append(filename)
        continue
    num+=1
    roll = filename[index:index+digit]
    turn_filename = filename[:index]+filename[index+digit:]
    new_filename = roll+"_"+turn_filename # or roll+"_"+filename
    temp = [filename,new_filename]
    changed.append(temp)
    #os.rename(os.path.join(path,filename),os.path.join(path,new_filename))

print("Can Change "+str(num)+" files of total "+str(tot)+" files")
print("\nUnchanged files are :\n=================")
for file in unchanged:
    print(file)
print("\nAnd the following will be changed as mentioned:\n================")
for names in changed:
    print(names[0]+"   ---->   "+names[1])
ans = input("Do you want to rename the files? (y/n):")
ans = ans.lower()
if ans == "n":
    print("Exiting program")
else:
    for names in changed:
        os.rename(os.path.join(path,names[0]),os.path.join(path,names[1]))
    print("Complete.....")
