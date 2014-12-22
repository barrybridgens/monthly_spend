# Monthly spend class

class MonthlySpend:

    def __init__(self):
        self.data = []


    def read_input_file(self):
        self.data = [line.rstrip() for line in open('input.txt')]


    def for_month(self, month_number, valid_pattern):
        ret = False

        if ((month_number >= 1) and (month_number <= 12)):
            if (len(valid_pattern) == 12):
                if (valid_pattern[month_number - 1] == '1'):
                    ret = True

        return(ret)
