class Freezer(object):
    def __init__(self):
        self._container = []

    def store(self, obj):
        self._container.append(obj)

    def stuff(self):
        return self._container[:]

deepfreezer = Freezer()
deepfreezer.store('fish')
deepfreezer.store('pea')
deepfreezer.store('meat')
print(deepfreezer.stuff())

