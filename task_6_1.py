ip_counter = {}

def read_file(path): 
    with open(path, 'r') as f: 
        while True: 
            line = f.readline() 
            if line: 
                yield line 
            else: 
                return

def extract_ip(line):
    return line.split()[0]

for line in read_file('nginx_logs.txt'):
    ip_ = extract_ip(line)
    if extract_ip(line) in ip_counter: 
        ip_counter[ip_] += 1
    else:
        ip_counter[ip_] = 1

# sorted_values = sorted(ip_counter.values(), reverse=True) # Sort the values
# sorted_dict = {}

# for i in sorted_values:
#     for k in ip_counter.keys():
#         if ip_counter[k] == i:
#             sorted_dict[k] = ip_counter[k]
#             break

spammer = max(zip(ip_counter.values(), ip_counter.keys()))[1]
print(spammer, ip_counter[spammer])

z=1