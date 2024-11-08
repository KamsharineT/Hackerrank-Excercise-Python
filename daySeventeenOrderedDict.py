''' Hackerrank : Collections.OrderedDict()
    You are the manager of a supermarket.
    You have a list of N items together with their prices that consumers bought on a particular day.
    Your task is to print each item_name and net_price in order of its first occurrence.

    item_name = Name of the item.
    net_price = Quantity of the item sold multiplied by the price of each item.
'''
from collections import OrderedDict
import re

class testOrderedDict():
    def testUsualDict():
        usual_dictionary = {}
        usual_dictionary['a'] = 1
        usual_dictionary['b'] = 2
        usual_dictionary['c'] = 3
        usual_dictionary['d'] = 4
        usual_dictionary['e'] = 5

        return usual_dictionary
    
    def testOrderedDict():
        ordered_dictionary = OrderedDict()
        ordered_dictionary['a'] = 1
        ordered_dictionary['b'] = 2
        ordered_dictionary['c'] = 3
        ordered_dictionary['d'] = 4
        ordered_dictionary['e'] = 5

        return ordered_dictionary
    

    ''' Hackerrank Solution '''
    def hackerrank():
        N = int(input())
        ordered_dictionary = OrderedDict()

        for i in range(N):
            items = input()
            newstring_part = re.findall(r'[A-Za-z ]+', items)[0].strip()
            newinteger_part = int(re.findall(r'\d+', items)[0])

            
            try:
                if len(ordered_dictionary) == 0:
                    ordered_dictionary[newstring_part] = newinteger_part
                else:
                    val = ordered_dictionary[newstring_part]
                    ordered_dictionary[newstring_part] = val + newinteger_part
            except Exception as e:
                ordered_dictionary[newstring_part] = newinteger_part
        return ordered_dictionary
def main():
    # print(testOrderedDict.testUsualDict())
    # print(testOrderedDict.testOrderedDict())
    output = testOrderedDict.hackerrank()

    for index,(key,value) in enumerate(output.items()):
        print(key,value)

if __name__ == '__main__':
    main()