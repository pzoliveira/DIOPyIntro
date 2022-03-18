from datetime import time

if __name__ == '__main__':
    hrtm = time(hour=22, minute=45, second=30)
    hrtm_str = hrtm.strftime('%H.%M.%S')
    print(hrtm_str)
