class CalcuClass():
    def ComputationForOtherStats(Base,IV,EV,Level,Nature,DS):
        comp1 = EV/4
        comp2 = (2*Base+IV+comp1)
        comp3 = Level/100
        D = comp2*comp3

        stats = ((DS/Nature) - D)*400
        stats1 = ((stats/Level)/4)*4
        return round(stats1,2)
