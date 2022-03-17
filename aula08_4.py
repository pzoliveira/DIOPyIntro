if __name__ == '__main__':
    lttrs_cntr = lambda wrdLst: [len(wrd) for wrd in wrdLst]
    animaux = ['chien', 'chat', 'cheval']
    print(lttrs_cntr(animaux))

    sums = lambda a, b: a + b
    print(sums(3, 2))

    calc = {
        'sums': lambda a, b: a + b,
        'subtr': lambda a, b: a - b,
        'mult': lambda a, b: a * b,
        'divis': lambda a, b: a / b
    }
    print(type(calc))
    adds = calc['sums']
    diffs = calc['subtr']
    tms = calc['mult']
    dvsn = calc['divis']
    print(adds(4, 6))
    print(diffs(11, 6))
    print(tms(3, 5))
    print(dvsn(100, 50))
