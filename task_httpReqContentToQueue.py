#!/usr/bin/python
import requests
import RedisUtils
import time

#Q_RESULT_PUT_QUEUE = RedisUtils.RedisQueue('result_put_queue')

def count_words_at_url(url, qname):
    put_queue = RedisUtils.RedisQueue(qname)
    resp = requests.get(url)
    #return len(resp.text.split())
    put_queue.put(resp.text)
    #Q_RESULT_PUT_QUEUE.put(resp.text)
    #return resp.text



