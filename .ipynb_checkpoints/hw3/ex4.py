class CollectionItr:
    def __init__(self, collection):
        self.collection = collection
        self.itr = iter(collection)
        self.indx = -1

    def __next__(self):
        if self.indx == len(self.collection):
            raise StopIteration()
        else:
            while self.indx != len(self.collection):
                self.indx += 1
                return self.indx, next(self.itr)

    def __iter__(self):
        return self


collection = CollectionItr(["apple", "mango", "orange", "pineapple","watermelon"])
for i in collection:
    print(i)


