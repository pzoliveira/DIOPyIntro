class Television:
    def __init__(self):
        self.isOn = False
        self.chnlnbr = 10

    def power(self):
        if self.isOn:
            self.isOn = False
        else:
            self.isOn = True
        print('TV is ON? {}'.format(self.isOn))

    def chnlpls(self):
        if self.isOn:
            self.chnlnbr += 1
            self.shwchnl()

    def chnlmns(self):
        if self.isOn:
            self.chnlnbr -= 1
            self.shwchnl()

    def shwchnl(self):
        print('TV channel: {}'.format(self.chnlnbr))


tv = Television()
tv.power()
tv.power()
tv.power()
tv.chnlpls()
tv.chnlpls()
tv.chnlmns()
