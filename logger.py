def primery_key():
    a = False
    with open('keys.csv', 'r+', encoding='utf-8') as kk:
        keys = kk.readline().split()
        key = int(keys[-1]) + 1
        kk.write(f'{key}' + ' ')      
    return key    
primery_key()