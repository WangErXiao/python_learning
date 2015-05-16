import _thread as thread, time


mutex=thread.allocate_lock()
count1=0
def counter(myId,count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        ++count1
        print('[%s] => %s' % (myId,i))
        mutex.release()

for i in range(5):
    thread.start_new_thread(counter,(i,5))

time.sleep(6)
print('Main thread exiting.')
print('Count %s' % (count1))
