import datetime

class Note:

    last_id = 0

    def __init__(self, memo, tags=''):
        self._memo = memo
        self._tags = tags
        self.creation_date = datetime.date.today()
        Note.last_id += 1
        self._id = Note.last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags

    @property
    def id(self):
        return self._id

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, memo):
        self._memo = memo

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags

# n1 = Note("hello first")
# n2 = Note("hello again")
# print(n1.memo)
# print(n2.id)
# print(n1.match('hello'))