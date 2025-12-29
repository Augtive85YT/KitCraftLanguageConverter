plus1 = ":softA:"
plus5 = ":softBoop:"
plus7 = ":softB:"
plus15 = ":softCharm:"
split = ":softDerp:"


strin = input("String to convert (Only alphabetical characters, excluding spaces): ").upper()
strout = ""

while strin.isalpha() == False:
    strin = input("String to convert: ").upper()

for i in strin:
    val = ord(i) - 64
    fifteen = int(val / 15)
    seven = int((val - (fifteen * 15)) / 7)
    five = int((val - ((fifteen * 15) + (seven * 7))) / 5)
    one = val - ((fifteen * 15) + (seven * 7) + (five * 5))
    strout += plus1 * one + plus5 * five + plus7 * seven + plus15 * fifteen + split

print("")
print(strout)
print("")
print("Length of output: " + str(len(strout)))