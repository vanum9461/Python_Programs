def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
if __name__ == "__main__":
    s=str(input())
    l=list(s.split(" "))
    l2=[]
    for i in l:
        p=reverse(i)
        l2.append(p)
    print(" ".join(l2))
        