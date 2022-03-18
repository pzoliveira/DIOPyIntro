from datetime import date

if __name__ == '__main__':
    currdate = date.today()
    currdate_str = currdate.strftime('%d/%m/%Y')
    print(currdate_str)
