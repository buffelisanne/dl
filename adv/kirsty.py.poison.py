import adv_test
from adv import *
from slot.a import *

def module():
    return Kirsty

class Kirsty(Adv):
    a3 = ('k',0.3)

    comment = 'always poisoned'

    def prerun(this):
        if this.condition('maintain Dauntless Strength'):
            Timer(this.dauntless_strength).on(15)
            Timer(this.dauntless_strength).on(30)
            Timer(this.dauntless_strength).on(45)

    def dauntless_strength(this, t):
        Selfbuff('a1',0.2,-1).on()

if __name__ == '__main__':
    conf = {}
    conf['slot.a'] = RR()+The_Plaguebringer_Always_Poisoned()
    conf['acl'] = """
        `s1
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

