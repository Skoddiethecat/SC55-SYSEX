inputString = input("Input display text:")

if len(inputString) > 32:
    print("Input too long, try again.")
    quit()

exclusiveStatus = 0xF0
manufacturerID = 0x41
deviceID = 0x10
modelID = 0x45
commandID = 0x12
EOX = 0xF7

address1 = 0x10
address2 = 0x00
address3 = 0x00

runningSum = address1 + address2 + address3

outputList = [exclusiveStatus, manufacturerID, deviceID, modelID, commandID,
              address1, address2, address3]

for i in inputString:
    runningSum = runningSum + ord(i)
    outputList.append(ord(i))

checksum = (128 - (runningSum % 128))

outputList.append(checksum)
outputList.append(EOX)

outputString = ''

for i in outputList:
    outputString = outputString + format(i, '02X') + ' '

print(inputString)
print(outputString)
