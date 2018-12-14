#!/usr/bin/python3
def search_replace(my_list, sch, rep):
    return [rep if i == sch else i for i in my_list]
