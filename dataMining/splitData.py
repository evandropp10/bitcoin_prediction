
import pandas as pd

def splitByDate(df, cutDate):
    
    bolOld = df.date < cutDate
    dfOld = df[bolOld]

    bolNew = df.date >= cutDate
    dfNew = df[bolNew]

    return dfOld, dfNew

def splitBySeries(df, cut):

    bolS = df.change + df.change1 + df.change2 + df.change3 + df.change4 + df.change5 < cut
    dfS = df[bolS]

    bolB = df.change + df.change1 + df.change2 + df.change3 + df.change4 + df.change5 >= cut
    dfB = df[bolB]

    return dfS, dfB
