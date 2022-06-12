class CalcuClass():

    def ComputationForHP(Base,IV,EV,Level):

        EV= EV/4
        Comp1 = 2 * Base  + IV + EV
        Comp2 = Comp1 * Level
        Comp3 = Comp2 / 100
        HP = Comp3 + Level + 10 

        return round(HP,2)

    def ComputationForOtherStats(Base,IV,EV,Level,Nature):

        EV= EV/4
        Comp1 = 2 * Base  + IV + EV 
        Comp2 = Comp1 * Level
        Comp3 = Comp2 / 100
        Comp4 = Comp3 + 5
        Other = Comp4 * Nature

        return round(Other,2)
