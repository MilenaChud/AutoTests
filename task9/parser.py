from subprocess import PIPE, run, call


def read_and_parsing_file():
    max_cpu = 0
    max_mem = 0
    user_cpu_proc = ''
    max_mem_cpu = ''
    result = None
    k = []
    count_memory = 0
    count_cpu = 0
    count_process = 0
    users = {}

    res = run(['ps', 'aux'], stdout=PIPE)
    std = res.stdout.decode().split('\n')
    print(std)
    titles = std[0].split()
    l = len(std)

    for p in std[1:]:
        if not p == '':
            count_process += 1
            t = p.split(maxsplit=len(titles))
            user_cpu = float(t[titles.index('%CPU')])
            user_mem = float(t[titles.index('%MEM')])
            user = str(t[titles.index('USER')])
            k.append(user)
            result = list(set(k))
            if user_cpu >= max_cpu:
                max_cpu = user_cpu
                user_cpu_proc = t[titles.index('COMMAND')]
            if user_mem >= max_mem:
                max_mem = user_mem
                max_mem_cpu = t[titles.index('COMMAND')]

    for j in result:
        sum = 0
        for r in std[1:]:
            if j in r:
                sum += 1

        users[j] = sum

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
                str_before.clear()

        for next_index in range(len(str_before)):
            if next_index == 2:
                count_cpu += float(str_before[next_index])

            elif next_index == 3:
                count_memory += float(str_before[next_index])

    print("Пользователи системы:", result)
    print("Пользовательских процессов:", users)
    print("Количество запущенных процессов всего:", count_process)
    print("Всего CPU используется: ", round(count_cpu, 1))
    print("Всего RAM используется: ", round(count_memory, 1))
    print('Max CPU usage: {} {}'.format(max_cpu, user_cpu_proc[:20]))
    print('Max RAM usage: {} {}'.format(max_mem, max_mem_cpu[:20]))

    with open('17122022.txt', 'w') as f:
        for user in result:
            f.write("Пользователь системы: " + user + '\n')
        f.write("Пользовательских процессов:" + str(users) + '\n')
        f.write("Количество запущенных процессов всего: " + str(count_process) + '\n')
        f.write("Всего CPU используется: " + str(count_cpu) + '\n')
        f.write("Всего RAM используется: " + str(count_memory) + '\n')
        f.write("Max CPU usage: " + str(max_cpu) + ' ' + str(user_cpu_proc) + '\n')
        f.write("Max RAM usage: " + str(max_mem) + ' ' + str(max_mem_cpu) + '\n')


if __name__ == '__main__':
    read_and_parsing_file()
