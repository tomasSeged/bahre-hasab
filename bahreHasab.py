
CONST_KIDME_LIDETE_KRISTOS = 5500
CONST_WENGELAWIAN = 4
CONST_DAYS_IN_WEEK = 7
CONST_TINTE_METQI = 19
CONST_TINTE_ABEKTE = 11


CONST_ABIY_TSOM = 14
CONST_DEBREZEIT = 41
CONST_PALM_SUNDAY = 62
CONST_GOOD_FRIDAY = 67
CONST_RESSURECTION_SUNDAY = 69
CONST_RIKBE_KAHINAT = 93
CONST_ASCENSION_DAY = 108
CONST_PENTECOSTE = 118
CONST_TSOME_HAWARYAT = 119
CONST_TSOME_DIHNET = 121


#BAHRE HASAB CALCULATOR
#Inspiration for calculation: https://www.youtube.com/watch?v=wPkP_P2SI5Q&pp=ygULYmFocmUgaGFzYWI%3D

#amete alem + amete mihret
def amete_alem(amete_mihret):
    return CONST_KIDME_LIDETE_KRISTOS + int(amete_mihret)


#1=>Mathew, 2=>Mark, 3=>Luke, 0=>John
def wengelawi(amete_mihret):
    return amete_alem(amete_mihret) % CONST_WENGELAWIAN
 
    
def meteneRabiet(amete_mihret):
        return int(amete_alem(amete_mihret) / CONST_WENGELAWIAN)

#Always starts from Tuesday
# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# 3 - Thursday
# 4 - Friday
# 5 - Saturday
# 6 - Sunday
def tinte_kemer(amete_mihret):
    return (amete_alem(amete_mihret) + meteneRabiet(amete_mihret)) % CONST_DAYS_IN_WEEK

def medeb(amete_mihret):
    return amete_alem(amete_mihret) % CONST_TINTE_METQI

def wenber(amete_mihret):
    if medeb(amete_mihret) == 0:
        return 0
    else:
        return medeb(amete_mihret) - 1

def abekte(amete_mihret):
    abeq = CONST_TINTE_ABEKTE * wenber(amete_mihret)
    
    if abeq > 30:
        return abeq % 30
    else:
        return abeq
        
def metqi(amete_mihret):
    met = CONST_TINTE_METQI * wenber(amete_mihret)
    
    if met > 30:
        return met % 30
    else:
        return met

#Either meskerem(1) or Tikemt(2)
def beale_metqi_month(amete_mihret):
    met = metqi(amete_mihret)
    
    if met < 14:
        return 2

    return 1

def beale_metqi_day(amete_mihret):
    
    month = beale_metqi_month(amete_mihret)
    
    #if meskerem
    if month == 1:
        return (tinte_kemer(amete_mihret) + metqi(amete_mihret) - 1 ) % 7
    
    #If tikemt, add 30 
    return (tinte_kemer(amete_mihret) + metqi(amete_mihret) + 30 - 1) % 7
    

#Map of {day : tewsak of day}
# Sun(6) : 7
# Mon(0) : 6
# Tues(1) : 5
# Wed(2) : 4
# Thurs(3) : 3
# Fri(4) : 2
# Sat(5) : 8
tewsak_dict = {6 : 7,
               0 : 6,
               1 : 5,
               2 : 4,
               3 : 3,
               4 : 2, 
               5 : 8
            }

def mebaja_hamer(amete_mihret):
    
    met = metqi(amete_mihret)
    elet_tewsak = tewsak_dict[beale_metqi_day(amete_mihret)]
    
    toRet = met + elet_tewsak
    
    if toRet > 30:
        toRet = toRet % 30
        
    return toRet 


month_dict = {
    1 : "Meskerem",
    2 : "Tikemt",
    3 : "Hidar",
    4 : "Tahsas",
    5 : "Tir",
    6 : "Yekatit",
    7 : "Megabit",
    8 : "Miyazia",
    9 : "Ginbot",
    10 : "Sene",
    11 : "Hamle",
    12 : "Nehase",
    13 : "Pagume"
}

#Day and Month for tsome nineveh
def tsome_nineveh(amete_mihret):

    met = metqi(amete_mihret)
    mebaja_tewsak = tewsak_dict[beale_metqi_day(amete_mihret)]
    month_toRet = 0
    day_toRet = met + mebaja_tewsak
    
    if beale_metqi_month(amete_mihret) == 1:
        month_toRet = 5
    else:
        month_toRet = 6

    if beale_metqi_month(amete_mihret) == 1 and (met+mebaja_tewsak) > 30:
        month_toRet = 6 
        day_toRet = (met + mebaja_tewsak) - 30
            
    return month_toRet, day_toRet


#Calculate date for rest of the holidays
def beal(const, nineveh):
    day = nineveh[1] + const
    month = nineveh[0]
    
    while(day > 30):
        day -= 30
        month += 1
            
    return month,day
    
def printHelp(xs):
        month = month_dict[xs[0]]
        day = xs[1]
        
        ret = str(month) + " " + str(day)
        return ret
    

def main():
    
    print("**************************************")
    print("BAHIRE HASAB - GE'EZ CALENDAR")
    print("**************************************")

    year = input("Please enter a year(YYYY): ")
    
    nineveh = tsome_nineveh(year)
    
     
    print("****************************************\n")
    print("HOLIDAYS AND FASTING DAYS FOR " + str(year)+ ":\n")
    
    print("Nineveh:", month_dict[nineveh[0]], nineveh[1])
    print("Abiy tsom:", printHelp(beal(CONST_ABIY_TSOM,nineveh)))
    print("Debrezeit:", printHelp(beal(CONST_DEBREZEIT,nineveh)))
    print("Hossana:", printHelp(beal(CONST_PALM_SUNDAY,nineveh)))
    print("Siklet (Good Friday):", printHelp(beal(CONST_GOOD_FRIDAY,nineveh)))
    print("Tinsae(Ressurection Sunday):", printHelp(beal(CONST_RESSURECTION_SUNDAY,nineveh)))
    print("Rikbe Kahinat:", printHelp(beal(CONST_RIKBE_KAHINAT,nineveh)))
    print("Irget (Ascension Day):", printHelp(beal(CONST_ASCENSION_DAY,nineveh)))
    print("Beale Piraklitos (PenteCoste):", printHelp(beal(CONST_PENTECOSTE,nineveh)))
    print("Tsome Hawaryat:", printHelp(beal(CONST_TSOME_HAWARYAT,nineveh)))
    print("Tsome Dihnet:", printHelp(beal(CONST_TSOME_DIHNET,nineveh)))
    print("****************************************")


if __name__ == "__main__":
    main()
   
