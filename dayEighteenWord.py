'''This is hackerrank word order excercise

You are given nwords. Some words may repeat. For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
'''

from collections import OrderedDict

class wordOrder():
    def wordOrder():
        ordered_words = {}

        N = int(input())
        cnt = 0
        for i in range(N):
            word = str(input())

            word = word.strip()

            try:
                if len(ordered_words) == 0:
                    ordered_words[word] = 1
                    cnt +=1
                else:
                    val = ordered_words[word]
                    ordered_words[word] = val + 1
            except Exception as e:
                ordered_words[word] = 1
                cnt +=1
        print(cnt)
        return ordered_words


def main():
    output = wordOrder.wordOrder()

    for index,(key,value)in enumerate(output.items()):
        print(value,end="")


if __name__ == "__main__":
    main()