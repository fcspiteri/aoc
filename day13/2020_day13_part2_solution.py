import math

with open('input13.txt','r') as f_open:
    data = f_open.read()
data = data.split('\n')

earliest_time = int(data[0])
bus_list = data[1].split(',')
in_service = []
max_bus = 0
max_bus_pos = 0
for i in range(0, len(bus_list)):
    if bus_list[i] != 'x':
        in_service.append([i, int(bus_list[i])])
        if int(bus_list[i]) > max_bus:
            max_bus = int(bus_list[i])
            max_bus_pos = i

new_time = 700000000000000
run = True
while run == True:
    for bus in in_service:
        if (new_time+max_bus_pos) % max_bus == 0:
            if (new_time + bus[0]) % bus[1] == 0:
                if bus[0] == in_service[-1][0]:
                    print('FOUND', new_time)
                    run = False
            else:
                new_time += max_bus
                break
        else:
            new_time += 1