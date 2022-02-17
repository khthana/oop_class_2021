class MyClass(object):
    def __enter__(self):
        print('We have entered "with"')
        return self

    def __exit__(self, type, value, traceback):
        print('error type: {0}'.format(type))
        print('error value: {0}'.format(value))
        print('error traceback: {0}'.format(traceback))
        print('We have exit "with"')

    def sayhi(self):
        print('hi, instance %s' % (id(self)))

with MyClass() as cc:
    cc.sayhi()

print('after the "with" block')

