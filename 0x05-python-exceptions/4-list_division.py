#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        new_list = []

        for i in range(list_length):
                nl = 0
                try:
                        div = my_list_1[i] / my_list_2[i]
                        nl = 1
                except ZeroDivisionError:
                        print("division by 0")
                        new_list.append(0)
                except TypeError:
                        print("wrong type")
                        new_list.append(0)
                except IndexError:
                        print("out of range")
                        new_list.append(0)
                finally:
                        if nl == 1:
                                new_list.append(div)
        return new_list
