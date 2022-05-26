
def encode(input):
    ansStr = ''.join(format(ord(i), '08b') for i in input)
    return ansStr

def decode(input):
    decNo = 0

    aa = str(input)
    binNo = list(aa)

    for i in range(len(binNo)):
        if binNo[i] == "1":
            decNo = decNo + 1 * 2 ** (len(binNo) - (i+1))
    return decNo

action = input("Encode or Decode (E/D): ")
if(not (action == "E" or action == "D")):
    print("error: unacceptble input")
    exit()
text = input("Input string: ")

if(action == "E"):
    output = encode(text)
    print(f"output: >{output}<")
else:
    output = decode(text)
    print(f"output: >{output}<")


