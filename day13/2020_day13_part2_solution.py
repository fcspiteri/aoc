with open('input13.txt','r') as f_open:
    data = f_open.read()
data = data.split('\n')

earliest_time = int(data[0])
bus_list = data[1].split(',')
in_service = []
for i in range(0, len(bus_list)):
    if bus_list[i] != 'x':
        in_service.append([i, int(bus_list[i])])
    
new_time = 500000000000000
run = True
while run == True:
    for bus in in_service:
            if (new_time + bus[0]) % bus[1] == 0:
                if bus[0] == in_service[-1][0]:
                    print('FOUND', new_time)
                    run = False
            else:
                b = bus[1]
                t = new_time + bus[0]
                print(new_time, new_time + b-t%b)
                new_time = new_time + b - t%b
                break