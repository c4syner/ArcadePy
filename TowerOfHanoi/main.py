def main():
    #Init
    towerLength = 128
    arrays = [
        [],
        [],
        [],
    ]
    #Setup
    for i in range(towerLength):
        arrays[0].append(towerLength-i)
    print(arrays)
    targetArray = arrays[0]
    #Calculate
    moves = 0
    disks = towerLength
    while(disks > 0):
        if(disks == 1):
            arrays[-1].append(arrays[0].pop())
            print(arrays)
        else:
            disks -= 1
            continue
            print(arrays)
            arrays[-1].append(arrays[0].pop())
            print(arrays)
            disks -= 1
            continue
            print(arrays)
if(__name__ == "__main__"):
    main()