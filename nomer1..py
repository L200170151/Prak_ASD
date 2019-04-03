import mahasiswa as mhs

c1=mhs.mhsTIF("narendra",21,"solo",240000)
c2=mhs.mhsTIF("rendra",22,"klaten",220000)
c3=mhs.mhsTIF("gusti",23,"jogja",260000)
c4=mhs.mhsTIF("aji",24,"klaten",250000)
c5=mhs.mhsTIF("ganteng",25,"magelang",240000)
c6=mhs.mhsTIF("banget",26,"jakarta",250000)
c7=mhs.mhsTIF("pokoke",27,"solo",220000)

x = [c1, c2, c3, c4, c5, c6, c7]

def swap(x,a,b):
    temp=x[a]
    x[a]=x[b]
    x[b]=temp

def sort(x):
    n=len(x)
    for i in range(n-1):
        for j in range(n-i-1):
            if x[j].uang>x[j+1].uang:
                swap(x,j,j+1)
    for i in x:
        print(i.Nama)

sort(x)
