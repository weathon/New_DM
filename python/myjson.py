def list2json(lists,keys):
    result=[]
    lenght=len(keys)
    for i in lists:
        thisline={}
        #lists is a table
        for j in range(lenght):
            #print((i,j))
            thisline[keys[j]]=lists[i][j]
        result.append(thisline)
    return result
if __name__=="__main__":
    print(eval(input()))
        