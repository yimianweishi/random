from ctypes import *
class myrandom:
    seed = 0
    multiplier = 0x5DEECE66D
    addend = 0xB
    mask = (1 << 48) - 1
    seedUniquifier = 8682522807148012
    def myrandom(self, seed):
        self.seed  = self.initialScramble(seed)
    def initialScramble(self, seed):
        return (seed ^ self.multiplier) & self.mask
    def _next(self, bits):
        oldseed = 0
        nextseed = 0
        seed = self.seed
        oldseed = seed
        nextseed = (oldseed * self.multiplier + self.addend) & self.mask
        self.seed = nextseed
        return c_int(((nextseed >> (48 - bits)))).value
    def _nextInt(self):
        return self._next(32)
    def _nextInt_bound(self, bound):
        r = self._next(31)
        m = bound - 1
        if bound & m == 0:
            r = (((bound * (r & 0xffffffffffffffff)) >> 31) & 0xffffffff)
        else:
            u = r
            r = u % bound
            while u - r + m < 0:
                r = u % bound
                u = self._next(31)
        return r
tmp = myrandom()
tmp.myrandom(1)
for i in range(50):
    print(tmp._nextInt_bound(10))
    
