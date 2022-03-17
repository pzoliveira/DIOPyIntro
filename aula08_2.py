def lttrscntr(wrdLst):
    cntr = []
    for wrd in wrdLst:
        cntr.append(len(wrd))
    return cntr


def totaloflttrs(wrdLst):
    cntr = 0
    for wrd in wrdLst:
        cntr += len(wrd)
    return cntr

if __name__ == '__main__':
    animals = ['dog', 'elephant', 'bird']
    print(lttrscntr(animals))
