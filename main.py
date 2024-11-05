from func_without_return import my_ascending, my_details, say_bool, print_zugi, my_statistics
from func_with_return import my_avg, my_headline, concat_list
my_ascending(-12, 7)
my_details("AI is the best")
say_bool(True)
say_bool(False)
print_zugi([5, 3, 2, 10, 15, 14, 14])
my_statistics([1,8,-9,10,80,100,2])
avg1: float = my_avg(90,99)
print(avg1)
head1: str = my_headline("python has concurred the world")
print(head1)
res_con: list[int] = concat_list([1,2],[3,4,5,6],[7,8,9])
print(f"{res_con} the length of this list is: {len(res_con)}")