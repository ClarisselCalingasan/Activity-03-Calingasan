from msilib.schema import Class
import string
import Calingasan_Script_1_Stat as StatsCal
import Calingasan_Script_2_EV as EVCal

def switch(choices):
    if choices == "A" or choices == "a":
        print("Stats")
        Base = int(input("Enter Base HP of Pokemon: "))
        Level = int(input("Enter Level: "))

        print("Enter no. for Nature")
        print("1.Hardy 2.Lonely 3.Brave 4.Adamant 5.Naughty 6.Bold 7.Docile 8.Relaxed 9.Impish 10.Lax")
        print("11.Timid 12.Hasty 13.Serious 14.Jolly 15.Naive 16.Modest 17.Mild 18.Quiet 19.Bashful 20.Rash")
        print("21.Calm 22.Gentle 23.Sassy 24.Careful 25.Quirky")
        Nature = int(input("Enter Nature: "))
        print('\n')

        IVHP = int(input("Enter IV-HP: "))
        if IVHP >= 31:
            print("Max is 31")
            main()
        IVATK = int(input("Enter IV-ATK: "))
        if IVATK >= 31:
            print("Max is 31")
            main()
        IVDEF = int(input("Enter IV-DEF: "))
        if IVDEF >= 31:
            print("Max is 31")
            main()
        IVSATK = int(input("Enter IV-Sp.ATK: "))
        if IVSATK >= 31:
            print("Max is 31")
            main()
        IVSDEF = int(input("Enter IV-Sp.DEF: "))
        if IVSDEF >= 31:
            print("Max is 31")
            main()
        IVSPD = int(input("Enter IV-SPD: "))
        if IVSPD >= 31:
            print("Max is 31")
            main()
        print('\n')



        EVHP = int(input("Enter EV-HP: "))
        if EVHP >= 255:
            print("Max is 255")
            main()
        EVATK = int(input("Enter EV-ATK: "))
        if EVATK >= 255:
            print("Max is 255")
            main()
        EVDEF = int(input("Enter EV-DEF: "))
        if EVDEF >= 255:
            print("Max is 255")
            main()
        EVSATK = int(input("Enter EV-Sp.ATK: "))
        if EVSATK >= 255:
            print("Max is 255")
            main()
        EVSDEF = int(input("Enter EV-Sp.DEF: "))
        if EVSDEF >= 255:
            print("Max is 255")
            main()
        EVSPD = int(input("Enter EV-SPD: "))
        if EVSPD >= 255:
            print("Max is 255")
            main()
        print('\n\n')

        TotalEv = EVHP + EVATK + EVDEF + EVSATK + EVSDEF + EVSPD

        if TotalEv >= 510:
            print("Total EV exceed to max no. PLease input not exceeding total of 510",end="\n")
            main()
        else:
            print("Total HP: ", StatsCal.CalcuClass.ComputationForHP(Base,IVHP,EVHP,Level))
            if Nature == 2 or Nature == 3 or Nature == 4 or Nature == 5:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total ATK: ", StatsCal.CalcuClass.ComputationForOtherStats(Base,IVATK,EVATK,Level,NatureAtt))
            if Nature == 6 or Nature == 8 or Nature == 9 or Nature == 10:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total DEF: ", StatsCal.CalcuClass.ComputationForOtherStats(Base,IVDEF,EVDEF,Level,NatureAtt))
            if Nature == 16 or Nature == 17 or Nature == 18 or Nature == 20:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total Sp.ATK: ", StatsCal.CalcuClass.ComputationForOtherStats(Base,IVSATK,EVSATK,Level,NatureAtt))
            if Nature == 21 or Nature == 22 or Nature == 23 or Nature == 24:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total Sp.DEF: ", StatsCal.CalcuClass.ComputationForOtherStats(Base,IVSDEF,EVSDEF,Level,NatureAtt))
            if Nature == 11 or Nature == 12 or Nature == 14 or Nature == 15:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total SPD: ", StatsCal.CalcuClass.ComputationForOtherStats(Base,IVSPD,EVSPD,Level,NatureAtt), end='\n\n')

            Repeat()

        
    elif choices == "B" or choices == "b":
        print("EV")
        Base = int(input("Enter Base HP of Pokemon: "))
        Level = int(input("Enter Level: "))

        print("Enter no. for Nature")
        print("1.Hardy 2.Lonely 3.Brave 4.Adamant 5.Naughty 6.Bold 7.Docile 8.Relaxed 9.Impish 10.Lax")
        print("11.Timid 12.Hasty 13.Serious 14.Jolly 15.Naive 16.Modest 17.Mild 18.Quiet 19.Bashful 20.Rash")
        print("21.Calm 22.Gentle 23.Sassy 24.Careful 25.Quirky")
        Nature = int(input("Enter Nature: "))
        print('\n')

        IVHP = int(input("Enter IV-HP: "))
        if IVHP >= 31:
            print("Max is 31")
            main()
        IVATK = int(input("Enter IV-ATK: "))
        if IVATK >= 31:
            print("Max is 31")
            main()
        IVDEF = int(input("Enter IV-DEF: "))
        if IVDEF >= 31:
            print("Max is 31")
            main()
        IVSATK = int(input("Enter IV-Sp.ATK: "))
        if IVSATK >= 31:
            print("Max is 31")
            main()
        IVSDEF = int(input("Enter IV-Sp.DEF: "))
        if IVSDEF >= 31:
            print("Max is 31")
            main()
        IVSPD = int(input("Enter IV-SPD: "))
        if IVSPD >= 31:
            print("Max is 31")
            main()
        print('\n')



        EVHP = int(input("Enter EV-HP: "))
        if EVHP >= 255:
            print("Max is 255")
            main()
        EVATK = int(input("Enter EV-ATK: "))
        if EVATK >= 255:
            print("Max is 255")
            main()
        EVDEF = int(input("Enter EV-DEF: "))
        if EVDEF >= 255:
            print("Max is 255")
            main()
        EVSATK = int(input("Enter EV-Sp.ATK: "))
        if EVSATK >= 255:
            print("Max is 255")
            main()
        EVSDEF = int(input("Enter EV-Sp.DEF: "))
        if EVSDEF >= 255:
            print("Max is 255")
            main()
        EVSPD = int(input("Enter EV-SPD: "))
        if EVSPD >= 255:
            print("Max is 255")
            main()
        print('\n\n')

        DSHP = int(input("Enter Desired Increse-HP: "))
        DSATK = int(input("Enter Desired Increse-ATK: "))
        DSDEF = int(input("Enter Desired Increse-DEF: "))
        DSSATK = int(input("Enter Desired Increse-Sp.ATK: "))
        DSSDEF = int(input("Enter Desired Increse-Sp.DEF: "))
        DSSPD = int(input("Enter Desired Increse-SPD: "))
        print('\n\n')

        TotalEv = EVHP + EVATK + EVDEF + EVSATK + EVSDEF + EVSPD

        if TotalEv >= 510:
            print("Total EV exceed to max no. PLease input not exceeding total of 510",end="\n")
            main()
        else:
            print('hp')
            NatureAtt = 1
            print("Total HP: ", EVCal.CalcuClass.ComputationForOtherStats(Base,IVHP,EVHP,Level,NatureAtt,DSHP))
            if Nature == 2 or Nature == 3 or Nature == 4 or Nature == 5:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total ATK: ", EVCal.CalcuClass.ComputationForOtherStats(Base,IVATK,EVATK,Level,NatureAtt,DSATK))
            if Nature == 6 or Nature == 8 or Nature == 9 or Nature == 10:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total DEF: ", EVCal.CalcuClass.ComputationForOtherStats(Base,IVDEF,EVDEF,Level,NatureAtt,DSDEF))
            if Nature == 16 or Nature == 17 or Nature == 18 or Nature == 20:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total Sp.ATK: ", EVCal.CalcuClass.ComputationForOtherStats(Base,IVSATK,EVSATK,Level,NatureAtt,DSSATK))
            if Nature == 21 or Nature == 22 or Nature == 23 or Nature == 24:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total Sp.DEF: ", EVCal.CalcuClass.ComputationForOtherStats(Base,IVSDEF,EVSDEF,Level,NatureAtt,DSSDEF))
            if Nature == 11 or Nature == 12 or Nature == 14 or Nature == 15:
                NatureAtt = 1.1
            else :
                NatureAtt = 0.9
            print("Total SPD: ", EVCal.CalcuClass.ComputationForOtherStats(Base,IVSPD,EVSPD,Level,NatureAtt,DSSPD), end='\n\n')
            
            Repeat()

def main():
    print("Welcome to Stat and EV Calculator",end='\n\n')
    print("Please choose from the following:")
    print("A.Stats B.EV")
    choices = input(":")
    switch(choices)

def Repeat():
    print("Choose 1 to Calculate , 2 for Exit",end="\n")
    choose = int(input(": "))
    if choose == 1:
        main()
    else:
        print("Thank you",end="\n")
        quit()

main()