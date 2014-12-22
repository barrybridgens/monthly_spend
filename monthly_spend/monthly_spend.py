# Monthly spend class

import operator, datetime, sys

class MonthlySpend:

    def __init__(self):
        self.data = []
        self.full_list = []


    def read_input_file(self):
        self.data = [line.rstrip() for line in open('input.txt')]


    def parse_data_entry(self, data_entry):
        ret = 'ERROR'

        entry = data_entry.split(' ', 3)

        if (len(entry) == 4):
            if ((int(entry[0]) >= 1) and (int(entry[0]) <= 31)):
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
                    self.full_list.append([month, int(pd[0]), float(pd[2]), pd[3]])
        self.full_list.sort(key = operator.itemgetter(0, 1))


    def calculate(self, month, day, balance=0.0):
        final_balance = balance

        if (day > 20):
            # process two months
            for t in self.full_list:
                if (t[0] == month):
                    if ((t[1] > day) and (t[1] <= 31)):
                        final_balance = final_balance - t[2]
                if (month == 12):
                    next_month = 1
                else:
                    next_month = month + 1
                if (t[0] == next_month):
                    if (t[1] <= 20):
                        final_balance = final_balance - t[2]
        else:
            # process one month
            for t in self.full_list:
                if (t[0] == month):
                    if ((t[1] > day) and (t[1] <= 20)):
                        final_balance = final_balance - t[2]

        return(final_balance)


if __name__ == "__main__":
    ms = MonthlySpend()
    ms.read_input_file()
    ms.create_full_list()

    now = datetime.datetime.now()

    balance = 0.0
    if (len(sys.argv) > 1):
        balance = float(sys.argv[1])

    final_balance = ms.calculate(now.month, now.day, balance)

    print(final_balance)
