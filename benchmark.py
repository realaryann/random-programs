import time
start_time = time.time()
from multiprocessing import Pool
i=0
list1=[]
def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        while len(list1) < 500:
            i=i+1
            if i%2 == 0 and str(i)[-1] == '2':
                list1.append(i)
                print(p.map(f, list1))
#converts time taken into points
a = ((time.time() - start_time))
b = float(a) * 100

time.sleep(3)
start_time = time.time()
list2 = []
j = 0
while len(list2) < 500:
    j=j+1
    list2.append(j)
    print(list2)

c = ((time.time() - start_time))
d = float(c) * 100
print(f'Score for single core test is {int(d)}')
print(f'Score for multicore test is {int(b)}')



