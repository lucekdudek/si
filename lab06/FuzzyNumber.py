

class FuzzyNumber(dict):

    def __add__(self, other):
        fn = FuzzyNumber()
        for sv, sf in self.items():
            for ov, of in other.items():
                if sv + ov in fn.keys():
                    fn[sv + ov] = max(fn[sv + ov], min(sf, of))
                else:
                    fn[sv + ov] = min(sf, of)
        return fn

if __name__ == "__main__":
    f1 = FuzzyNumber()
    f1[1] = 0.2
    f1[2] = 1.0
    f1[3] = 0.2

    f2 = FuzzyNumber()
    f2[0] = 0.3
    f2[1] = 1.0
    f2[2] = 0.3

    print(f1)
    print(f2)
    print(f1 + f2)
