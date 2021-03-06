# Useful unit conversions

def secsToDays(s):
    '''Assume s is time in seconds and a positive integer or float.
    Return time in days'''
    days = s / (60 * 60 * 24) 
    return days

def daysToSecs(d):
    '''Assume d is time in days and a positive integer or float.
    Return time in seconds'''
    secs = (60 * 60 * 24) * d
    return secs

def dayToYear(d):
    '''Assume d is time in days and a positive integer or float.
    Return time in years'''
    year = 365.25 / d
    return year

def yearToDay(y):
    '''Assume y is time in years and a positive integer or float.
    Return time in days'''
    day = y * 365.25
    return day

def mPerS(mPerD):
    '''Assume mPerD is a positive integer or float.
    Return mPerS'''
    mPerS = days(mPerD)
    return mPerS

def mPerD(mPerS):
    '''Assume mPerS is a positive integer or float.
    Return mPerD'''
    mPerD = secs(mPerS)
    return mPerD

def kgPerM3(mgl):    # Convert mg/l to kg/m^3
    kgPerM3 = mgl /1000
    return kgPerM3

def mgPerL(kgPerM3):       # Convert kg/m^3 to g/m^3 (same as mg/l)
    mgl = 1000 * kgPerM3
    return mgl
