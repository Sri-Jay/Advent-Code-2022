import csv
lst = []
sumoflist = 0
with open('input.csv') as f:
#with open('inputtrial.csv') as f:    
        contents = csv.reader(f)
        for row in contents:  
            if row != []:
                for i in row:          
                    sumoflist = sumoflist + int(i)                
            else:
                lst.append(sumoflist)
                sumoflist = 0
        m = max(lst)
        print(m)

#Part2
        lst.sort()
        print(sum(lst[-3:]))
