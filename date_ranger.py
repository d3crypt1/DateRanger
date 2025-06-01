from enum import Enum

class RangeType(Enum):
    BI = "bi"
    QUARTER = "quarter"
    MONTH = "month"
    WEEK = "week"
    DAY = "day"

class DateRanger:
    def __init__(self, year, m_fmt = "MM"):
        self.year = int(year)
        self.m_fmt = m_fmt
        self.__month_days()

    def split_annual(self, split):
        m_range=[]
        counter = 0
        end_temp = len(self.m_days) / split
        end_add = int(end_temp)
        for m in self.m_days:
            if counter % end_add == 0:                
                end_month = counter + end_add - 1
                m_range.append( m[0] + "/01/" + str(self.year) + "~" + self.m_days[end_month][0] + "/" + str(self.m_days[end_month][1]) + "/" + str(self.year))
            counter +=1

        return m_range
    
    def split_month(self, month, split):
        m_range=[]
        counter = 0
        end_temp = self.m_days[int(month)][1] / split
        end_add = int(end_temp)
        m = self.m_days[int(month)]
        days = self.m_days[int(month)][1]
        day_range = range(0, days)
        for d in day_range:
            if counter % end_add == 0:
                start_day = counter + 1                
                end_day = counter + end_add
                if end_day < days:
                    m_range.append(m[0] + "/"+ str(start_day) +"/" + str(self.year) + "~" + m[0] + "/" + str(end_day) + "/" + str(self.year))
                else:
                    m_range.append(m[0] + "/"+ str(start_day) +"/" + str(self.year) + "~" + m[0] + "/" + str(days) + "/" + str(self.year))
                    break
                #m_range.append( m[0] + "/01/" + str(self.year) + "~" + self.m_days[end_month][0] + "/" + str(self.m_days[end_month][1]) + "/" + str(self.year))
            counter +=1
        return m_range
            
    def __month_days(self):
        feb = 28
        if self.year % 4 == 0:
            feb = 29
        self.m_days = (("01",31),("02",feb),("03",31),("04",30),("05",31),("06",30),("07",31),("08",31),("09",30),("10",31),("11",30),("12",31))
        
        if self.m_fmt == "MMM": 
            self.m_days = (("JAN",31),("FEB",feb),("MAR",31),("APR",30),("MAY",31),("JUN",30),("JUL",31),("AUG",31),("SEP",30),("OCT",31),("NOV",30),("DEC",31))
        return self.m_days
    
    def date_ranges(self, range_type = RangeType.MONTH, month = None):
        if not isinstance(range_type, RangeType):
            raise TypeError('Search type must be SearchType.QUARTER|MONTH|WEEK|DAY')
        m_range =[]
            
        match range_type:
            case RangeType.BI:
                if month == None:
                    return self.split_annual(2)
                else:
                    return self.split_month(month, 2)
            case RangeType.QUARTER:
                if month != None:
                    raise TypeError('date_ranges(SearchType.QUARTER, [month=(0-11)]) QUARTER not supported with month=None')
                    
                return self.split_annual(4)
            case RangeType.MONTH:
                if month != None:
                    m = self.m_days[int(month)]
                    m_range.append(m[0] + "/01/" + str(self.year) + "~" + m[0] + "/" + str(m[1]) + "/" + str(self.year))
                    return m_range
                return self.split_annual(12)
            case RangeType.WEEK:
                if month == None:
                    raise TypeError('date_ranges(SearchType.WEEK, [month]), month=None is unsuppoarted must be month=[0-11]')                    
                else:
                    return self.split_month(month, 4)
            case RangeType.DAY:
                if month == None:
                    raise TypeError('date_ranges(SearchType.DAY, [month]), month=None is unsuppoarted month=[0-11]')                    
                else:
                    days = self.m_days[int(month)][1]
                    return self.split_month(month, days)
            case _:
                print("Invalid command.")
        return m_range
        
        
if __name__ == "__main__":
    dateRange = DateRanger(2000, m_fmt = "MMM")

    #print(dateRange.year)
    #print(dateRange.m_days[0])

    #print(dateRange.monthly_range(month=2))
    print(dateRange.date_ranges(RangeType.WEEK, 3))


    m_days = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    print( str(m_days.index("MAR")) )

