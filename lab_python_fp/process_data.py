import json
import sys
import field
import unique
import gen_random
import cm_timer
from print_result import print_result

path = r"C:\Users\123\Desktop\Study\3 sem\PCPL\data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arr):
    return sorted(unique.Unique.lists(unique.Unique(field.field(arr, 'job-name'), ignore_case=False)), key=lambda x: x.lower())


@print_result
def f2(arr):
    filtered = filter(lambda x: x.startswith('программист') or x.startswith('Программист'), arr)
    return list(filtered)


@print_result
def f3(arr):
    modified = map(lambda x: x + " с опытом Python", arr)
    return list(modified)


@print_result
def f4(arrs):
    salaries = gen_random.gen_random(len(arrs), 100000, 200000)
    combined = [f"{arr}, зарплата {salary} руб." for arr, salary in zip(arrs, salaries)]
    return combined


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))