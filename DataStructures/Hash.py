class CustomHash:
    def __init__(self, size):
        self.buckets = size
        self.container = [[() * self.buckets] * self.buckets]
        self.size = 0

    def hash(self, string_to_hash):
        hash_code = 5381
        char_array_of_input = list(string_to_hash)
        for i in range(len(string_to_hash)):
            character = char_array_of_input[i]
            hash_code = ((hash_code << 5) + hash_code) + character
        return hash_code % self.buckets

    def insert(self, key, value):
        index = self.hash(key)
        if len(self.container) == 0:
            self.container[index].append((key, value))
            self.size += 1
        else:
            bucket = self.container[index]
            for i in range(0, self.buckets):
                if bucket[i][0] == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))
            self.size += 1

    def delete(self, key):
        index = self.hash(key)
        if len(self.container) == 0:
            print("Item not in the hash")
        else:
            bucket = self.container[index]
            for i in range(0, self.buckets):
                if bucket[i][0] == key:
                    item = bucket[i][1]
                    bucket.remove(bucket[i])
                    self.size -= 1
                    return item
        print("Key not in hash table")

    def retrieve(self, key):
        index = self.hash(key)
        if len(self.container[index]) == 0:
            print("Item not in hash table")
        else:
            bucket = self.container[index]
            for i in range(self.buckets):
                if bucket[i][0] == key:
                    return bucket[i][1]
            print("Item not in hash table")
