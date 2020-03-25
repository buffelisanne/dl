import adv.adv_test
from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Eleonora

class Eleonora(Adv):
    a3 = ('prep','50%')
    conf = {}
    conf['acl'] = """
        `s1, fsc
        `s2, fsc
        `s3, fsc
        `fs, seq=4
        """
    conf['slot.a'] = Dear_Diary() + The_Fires_of_Hate()
    conf['slot.d'] = Vayu()
    conf['afflict_res.poison'] = 0
    a1 = ('edge_poison', 50, 'hp100')

    def s1_proc(self, e):
        self.afflics.poison('s1',110,0.53)

    def s2_proc(self, e):
        self.afflics.poison('s2',100,0.396)


if __name__ == '__main__':
    conf = {}
    adv.adv_test.test(module(), conf)
