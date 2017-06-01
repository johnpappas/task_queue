import redis
import properties


class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    # TODO: refactor namespace assignment below and put in calling code
    def __init__(self, name, namespace=properties.REDIS_QUEUE_LISTING_URL_NAMESPACE, **redis_kwargs):
    #def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        # self.__db= redis.Redis(**redis_kwargs)
        #self.__db= redis.Redis(host='localhost', port=6379, db=0, password=None)
        self.__db= redis.Redis(host=properties.REDIS_HOST, port=properties.REDIS_PORT, db=properties.REDIS_DB, password=properties.REDIS_PASSWORD)
        self.key = '%s:%s' %(namespace, name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)
