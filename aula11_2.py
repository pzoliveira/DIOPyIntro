class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

if __name__ == '__main__':
    while True:
        try:
            inpt = int(input('Please, enter a grade between 0 and 10: '))
            if inpt > 10:
                raise InputError('Grade must be less or equal to 10!')
            elif inpt < 0:
                raise InputError('Grade must be non negative!')
            print(inpt)
            break
        except ValueError:
            print('Invalid value. Please, enter a number between 0 and 10.')
        except InputError as excnm:
            print(excnm)
