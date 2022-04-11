input = open("/Users/zhaoyifei/Desktop/D_207.txt", "r")
output = open("/Users/zhaoyifei/Desktop/D_207.xyz", "w")
n=1
for line in input:
        print(n)
        n = n + 1
        i =''
        output.write(str(i)+ line)
input.close()
output.close()
