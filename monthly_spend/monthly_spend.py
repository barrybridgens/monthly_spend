# Monthly spend class

import operator

class MonthlySpend:

    def __init__(self):
        self.data = []
        self.full_list = []


    def read_input_file(self):
        self.data = [line.rstrip() for line in open('input.txt')]


    def parse_data_entry(self, data_entry):
        ret = 'ERROR'

        entry = data_entry.split(' ', 2)

        if (len(entry) == 3):
            if ((int(entry[0]) >= 1) and (int(entry[0]) <= 12)):
                ret = entry

        return(ret)


    def for_month(self, month_number, valid_pattern):
        ret = False

        if ((month_number >= 1) and (month_number <= 12)):
            if (len(valid_pattern) == 12):
                if (valid_pattern[month_number - 1] == '1'):
                    ret = True

        return(ret)


    def create_full_list(self):
        for month in range(1, 13):
            for d in self.data:
                pd = self.parse_data_entry(d)
                if (self.for_month(month, pd[1])):
                    self.full_list.append([month, int(pd[0]), pd[2]])
        self.full_list.sort(key = operator.itemgetter(0, 1))
