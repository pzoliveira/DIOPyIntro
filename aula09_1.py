import shutil

def crtfile(flnm, txtdata):
    txtfile = open(flnm, 'w')
    txtfile.write(txtdata)
    txtfile.close()


def updtfile(flnm, txtdata):
    txtfile = open(flnm, 'a')
    txtfile.write(txtdata)
    txtfile.close()


def grdsavrg(flnm):
    grdsfile = open(flnm, 'r')
    cntnt = grdsfile.read()
    linelst = cntnt.split('\n')
    stdgrd = {}
    for line in linelst:
        wrdlst = line.split(',')
        stdntnm = wrdlst.pop(0)
        avggrd = lambda grdlst: sum([int(grd) for grd in grdlst]) / 4
        stdgrd[stdntnm] = avggrd(wrdlst)
    return stdgrd


if __name__ == '__main__':
    crtfile('D:/PycharmProjects/DIOPyIntro/txtfile.txt', 'First line\n')
    updtfile('txtfile.txt', 'Second line\n')
    updtfile('txtfile.txt', 'Third line')
    crtfile('grdsfile.txt', 'Aaron,5,5,5,5\n')
    updtfile('grdsfile.txt', 'Ben,6,6,6,6\n')
    updtfile('grdsfile.txt', 'Charles,7,7,7,7\n')
    updtfile('grdsfile.txt', 'David,8,8,8,8')
    print(grdsavrg('grdsfile.txt'))
    shutil.copy('txtfile.txt', 'D:/PycharmProjects/text_file.txt')
    shutil.move('grdsfile.txt', 'D:/PycharmProjects/grades_file.txt')
