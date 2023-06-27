#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            division_result = dividend / divisor

        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except TypeError:
            print("wrong type")
            division_result = 0
        except IndexError as e:
            print(e)
            division_result = 0
        finally:
            result.append(division_result)
    return result
