fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line
    numstart = x.find('0')
    num=x[numstart:len(x)]
    count = count + 1
    total = total + float(num)
average = total/count
print("Average spam confidence:", average)