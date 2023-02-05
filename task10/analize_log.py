from subprocess import PIPE, run, call
from operator import itemgetter, attrgetter, methodcaller
import json

directory = '.'  # если поиск осуществляется в текущей директории
file = '*.log'  # шаблон для всех файлов с .log
file1 = 'access.log'  # нужен конкретный файл - указываем переменную
receive = {}
dict_ip = {}
methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']
finally_list = []
time = {}
final = []


def an_log():
    res = run(['find', directory, '-type', 'f', '-name', file], stdout=PIPE)
    std = res.stdout.decode().split('\n')
    for log in std:
        if not log == '':
            res1 = run(['cat', log], stdout=PIPE)
            res1 = res1.stdout.decode().split('\n')
            counter_receive = len(res1)
            final.append(counter_receive)
            print("Общее количество выполненных запросов: ", counter_receive)

            for method in methods:
                res2 = run(["cat {} | awk '{{print $6}}' | grep '{}' | wc -l".format(log, method)], shell=True, stdout=PIPE)
                res2 = res2.stdout.decode().split('\n')
                receive[method] = res2[0]
            final.append(receive)
            print("Подсчет количества запросов по методам:", receive)

            list_ip = run(["cat {} | awk '{{print $1}}' | sort | uniq -c".format(log)], shell=True, stdout=PIPE)
            list_ip = list_ip.stdout.decode().split('\n')
            list_ip.sort()
            len_list_ip = len(list_ip)
            for k in range(3):
                r = list_ip[len_list_ip-(k+1)].split(' ')
                dict_ip[r[-1]] = r[-2]
            final.append(dict_ip)
            print("Top-3 ip", dict_ip)

            res3 = run(['cat', log], stdout=PIPE)
            res3 = res3.stdout.decode().split('\n')
            for line in res3:
                line = line.split(' ')
                line = list(reversed(line))
                finally_list.append(line)

            finally_list.remove([''])
            finally_list.sort(reverse=True)

            for i in range(3):
                list_one = list(reversed(finally_list[i]))
                time[list_one[-1]] = list_one[0], list_one[3], list_one[5]
                final.append(time)
                print("Top-3 долгих запроса", time)

    with open("result.json", "w") as result:
        json.dump(final, result, indent=4)


if __name__ == '__main__':
    an_log()
