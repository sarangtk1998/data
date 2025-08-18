


# chack a num is prime


def prime_num(start,end):
    prime = []
    for i in range(start,end+1):     #5

        for j in range(2,i):          # 2 5
            if i%j==0:
                break
        else:
            prime.append(i)



