import datetime


class FloatIter:
    def __init__(self, start=1.0, stop=7.0, step=0.5):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __str__(self):
        return str(self.start)

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        else:
            self.start += self.step
            return self


# f_iter = FloatIter(1.3, 4.6, 0.5)
# for i in f_iter:
#     print(i)

class TimeIter:
    def __init__(self, start='20:10:00', hours=1, min=0, sec=0, max=10):
        self.frm = '%H:%M:%S'
        self.start = datetime.datetime.strptime(start, self.frm)
        self.hours = hours
        self.min = min
        self.sec = sec
        self.max_iter = max
        self.iter = 0

    def __iter__(self):
        return self

    def __str__(self):
        return self.start.strftime(self.frm)

    def __next__(self):
        if self.iter == self.max_iter:
            raise StopIteration
        self.start += datetime.timedelta(hours=self.hours, minutes=self.min, seconds=self.sec)
        self.iter += 1
        return self


time_iter = TimeIter("10:50:10", 0, 10, 0)
for i in time_iter:
    print(i)
