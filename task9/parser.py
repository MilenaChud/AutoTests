from subprocess import PIPE, run, call

sp = []


def read_and_parsing_file():
    max_cpu = 0
    user_cpu = ''
    result = None
    index = None
    count_pid = 0
    count_memory = 0
    count_cpu = 0

    res = run(['ps', 'aux'], stdout=PIPE)
    std = res.stdout.decode().split('\n')
    titles = std[0].split()
    l = len(std)

    for p in std[1:]:
        if not p == '':
            t = p.split(maxsplit=len(titles))
            user_cpu = float(t[titles.index('%CPU')])
            if user_cpu >= max_cpu:
                max_cpu = user_cpu
                user_cpu = t[titles.index('COMMAND')]
    
    for i in range(l):
        str_before = std[i].split(" ")

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

        for next_index in range(len(str_before)):
            if next_index == 1:
                count_pid += int(str_before[next_index])

            elif next_index == 2:
                count_cpu += float(str_before[next_index])

            elif next_index == 3:
                count_memory += float(str_before[next_index])

    print("Пользователи системы:", result)
    print("Количество запущенных процессов всего:", count_pid)
    print("Всего CPU используется: ", count_cpu)
    print("Всего CPU используется: ", count_memory)
    print('Max CPU usage: {} {}'.format(max_cpu, user_cpu))


if __name__ == '__main__':
    read_and_parsing_file()
