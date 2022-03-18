from datetime import datetime, timedelta

if __name__ == '__main__':
    currdate = datetime.now()
    currdate_str = currdate.strftime('%d/%m/%Y %H:%M:%S')
    currdate_str = currdate.strftime('%c')
    print(currdate_str)
    eng2port = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira',
                'Sábado', 'Domingo')
    print(eng2port[currdate.weekday()])
    borndate = datetime(1971, 12, 4, 0, 30, 45)
    print(borndate)
    mtngdate = '28/02/2015 22:22.22'
    cnvrtdate = datetime.strptime(mtngdate, '%d/%m/%Y %H:%M.%S')
    print(cnvrtdate)
    svnyrsltr = cnvrtdate + timedelta(days=2557, hours=1, minutes=28, seconds=8)
    print(svnyrsltr)
