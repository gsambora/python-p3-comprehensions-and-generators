#!/usr/bin/env python3

def return_evens(num_list):
    evens_only = [num for num in num_list if num%2 == 0 ]
    return evens_only

def make_exclamation(sentence_list):
    return [sent+"!" for sent in sentence_list ]