# -*- coding: utf-8 -*-

import time
import timeit
import _thread
import threading

import client

class UploadThread(threading.Thread):

    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end

    def run(self):
        for i in range(self.begin, self.end):
            client.upload('inputs/%d' % i)
        print(i)

size = 10000
step = 1000

def main():

    start_time = timeit.default_timer()

    threads = list()

    for i in range(1, size + 1, step):
        # print(i, i + step)
        thread = UploadThread(i, i + step)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = timeit.default_timer()

    print('Upload {} files: {}'.format(size, end_time - start_time))

if __name__ == '__main__':
    main()
