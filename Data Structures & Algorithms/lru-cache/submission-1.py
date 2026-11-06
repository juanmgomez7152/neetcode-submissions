class LRUCache:

    def __init__(self, capacity: int):
        self.max_size=capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.put(key, self.cache[key])
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        temp_cache={}
        

        self.cache.pop(key,None)
        temp_cache[key]=value
        temp_cache = temp_cache | self.cache

        self.cache = temp_cache
        
        self._cache_size_check()


    def _cache_size_check(self)->None:
        while len(self.cache.keys())>self.max_size:
            self.cache.popitem()
            
        
