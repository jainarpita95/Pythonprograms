class Number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=5:
            x=self.a
            self.a+=1
            return x
        else:
           raise StopIteration#python define exception
num_class=Number()
num_iter=iter(num_class)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
for x in num_iter:
    print(x)
    #print(next(num_iter))
   
