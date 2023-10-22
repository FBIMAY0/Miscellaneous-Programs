import random


endcount = [0]
del endcount[0]
totalcount = 1
for __count in range(32):
    output = ['==========第', str(totalcount), '轮==========']
    print(''.join(output))
    count = 1
    for __count in range(256):
        result = [str(random.randint(0, 1)), str(random.randint(0, 1)), str(random.randint(0, 1)), str(random.randint(0, 1)), str(random.randint(0, 1)), str(random.randint(0, 1)), str(random.randint(0, 1)), str(random.randint(0, 1))]
        output = ['第', str(totalcount), '轮第', str(count), '次运行，结果为：', ' '.join(result)]
        print(''.join(output))
        if (('0 0 0 0 0 0 0 0' in output) or ('1 1 1 1 1 1 1 1' in output)):
            output = ['在第', str(count), '次运行时出现符合要求的结果，开启下一轮']
            print(''.join(output))
            break
        count += 1
    if (count >= 256):
        print('256次运行内都未出现符合要求的结果，本轮运行结果记为“256+”，开启下一轮')
        endcount.append('256+')
    else:
        endcount.append(str(count))
    totalcount += 1
    print('')
print('==========结 果==========')
print('出现符合要求结果的运行次数分别为：')
print(' '.join(endcount))
