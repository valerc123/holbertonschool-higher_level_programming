#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    if len_sen == 0:
        sentence[0] = None
    return (len_sen, sentence[0])
