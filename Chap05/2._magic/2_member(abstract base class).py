from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, m_id, fname, lname):
        self.m_id = m_id
        self.fname = fname
        self.lname = lname

    @abstractmethod
    def discount(self):
        pass

    def full_name(self):
        return "{} {}".format(self.fname, self.lname)

class Gold(Member):
    def discount(self):
        return .10

class Silver(Member):
    def discount(self):
        return .05


if __name__ == '__main__':
    # m = Member("007", "James", "Bond")
    # print(m)
    g = Gold("123", "Peter", "Parker")
    print(g)
    print(g.discount())
    print(g.full_name())
    s = Silver("888", "Jane", "Mark")
    print(s)
    print(s.full_name())