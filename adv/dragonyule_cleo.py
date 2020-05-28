from core.advbase import *

def module():
    return Dragonyule_Cleo

class Dragonyule_Cleo(Adv):
    a1 = ('a',0.13,'hp70')
    a3 = ('ecombo',30)
    
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 and cancel or fsc
        `s3, fsc
        `fs, seq=5
    """
    coab = ['Hunter_Sarisse', 'Xander', 'Summer_Estelle']

    def prerun(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
        self.stance = 0

    @staticmethod
    def prerun_skillshare(adv):
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff
        adv.stance = 0

    def s1_proc(self, e):
        self.energy.add(1, team=self.condition('buff all team'))
        if self.stance == 0:
            self.stance = 1
        elif self.stance == 1:
            self.stance = 2
            self.buff_class(e.name,0.1,10).on()
        elif self.stance == 2:
            self.stance = 0
            self.buff_class(e.name,0.1,10).on()
            self.buff_class(f'{e.name}_crit',0.08,10,'crit','chance').on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)