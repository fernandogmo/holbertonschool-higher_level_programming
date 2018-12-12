#!/usr/bin/python3

def multiple_returns(sentence):
    len_s = len(sentence)
    return len_s, sentence[0] if len_s > 0 else None

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))


sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
