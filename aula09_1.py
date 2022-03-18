def crtfile(txtdata):
    txtfile = open('txtfile.txt', 'w')
    txtfile.write(txtdata)
    txtfile.write('\n')
    txtfile.close()


def updtfile(txtdata):
    txtfile = open('txtfile.txt', 'a')
    txtfile.write(txtdata)
    txtfile.write('\n')
    txtfile.close()


if __name__ == '__main__':
    crtfile('First line')
    updtfile('Second line')
    updtfile('Third line')
