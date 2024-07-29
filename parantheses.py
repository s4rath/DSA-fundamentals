#check for valid parantheses 
#for example 
# (){}[] ---> valid 
# (}) -----> invalid 


inp='([}]){}'


closing=[')','}',']']
pair={
    ')':'(',
    '}':'{',
    ']':'['
}

st=[]
flag=0

for i in inp:
    if i in closing:
        if len(st)>0:
            p=st.pop()
            if p!=pair[i]:
                print("not valid")
                flag=1
                break
            else:
                continue
        else:
            print("not valid")
            flag=1
            break
    st.append(i)
    
if len(st)>0:
    if flag==0:
        print('invalid')
else:
    if flag==0:
        print("valid")
    

