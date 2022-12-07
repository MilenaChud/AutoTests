from subprocess import PIPE, run, call
import re

sp = []
sp1 = {}
sp2 = {}


def run_command():
    t = run(["ps aux >> 07122022.txt"], shell=True)
    print(t)
    return t


def read_and_parsing_file():
    with open("07122022.txt", "r") as f:
        text = f.read().split("\n")
        l = len(text)
        result = None
        pr = 0
        pr1 = 0
        pr2 = 0
        pr3 = 0
        pr4 = 0
        pr5 = 0
        count_pid = 0

        for i in range(l):
            str_before = text[i].split(" ")

            count = 0
            for j in str_before:
                if j == '':
                    count += 1

            for _ in range(count):
                str_before.remove('')

            for k in str_before:
                if k == "USER":
                    index = str_before.index("USER")
                    str_before.clear()
                else:
                    sp.append(str_before[index])
                    result = list(set(sp))

            count_memory = 0
            count_cpu = 0
            for next_index in range(len(str_before)):
                if next_index == 1:
                    count_pid += int(str_before[next_index])

                elif next_index == 2:
                    count_cpu += float(str_before[next_index])

                elif next_index == 3:
                    count_memory += float(str_before[next_index])

            pat1 = "^\w{0,19}\s{0,10}\d{0,3}\s{0,10}\d{0,1}.\d{0,2}\s{0,2}\d{0,1}.\d{0,2}"
            patt1 = re.compile(pat1, re.MULTILINE)
            pattt1 = re.findall(patt1, text[i])

            for h in pattt1:
                if "USER" in h:
                    pattt1.clear()
                else:
                    ko = str(h).split(" ")
                    if "root" in h:
                        koo = int(ko[-5])
                        koo_cu = float(ko[-3])
                        koo_mem = float(ko[-1])
                        pr += koo
                        pr2 += koo_cu
                        pr3 += koo_mem
                    elif "mil" in h:
                        ko1 = int(ko[-5])
                        koo_cu1 = float(ko[-3])
                        koo_mem1 = float(ko[-1])
                        pr1 += ko1
                        pr4 += koo_cu1
                        pr5 += koo_mem1

            if pr2 > pr4:
                print("Больше памяти потребляет root: ", pr2)
            else:
                print("Больше памяти потребляет mil: ", pr4)

            if pr3 > pr5:
                print("Больше всего CPU использует root: ", pr2)
            else:
                print("Больше всего CPU использует mil: ", pr4)


        sp1 = {"root": pr}
        sp2 = {"mil": pr1}

    print("Пользовательских процессов:", sp1)
    print("Пользовательских процессов:", sp2)
    print("Пользователи системы:", result)
    print("Количество запущенных процессов всего:", count_pid)
    print("Всего CPU используется: ", count_cpu)
    print("Всего CPU используется: ", count_memory)


if __name__ == '__main__':
    run_command()
    read_and_parsing_file()
