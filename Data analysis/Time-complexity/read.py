# list of strings
aviation_data=[]
with open('AviationData.txt','r') as data:
    for line in data:
        aviation_data.append(line)
        
# list of lists   
aviation_list=[]
for data in aviation_data:
    line = data.split('|')
    words=[]
    for word in line:
        words.append(word.strip())
    aviation_list.append(words)

# quadratic search time 
lax_code=[]
for line in aviation_list:
    for word in line:
        if word == 'LAX94LA336':
            lax_code.append(line)

# linear search time
lax_code=[]
for line in aviation_data:
    if 'LAX94LA336' in line:
        lax_code.append(line)

# hash table
aviation_dict_list=[]
for line in aviation_data[1:]:
    line = line.split('|')
    line_dict={}
    for ind, word in enumerate(line):
        line_dict[aviation_data[0].split('|')[ind].strip()] = word.strip()        
    aviation_dict_list.append(line_dict)

# hash table search
lax_code=[]
for row in aviation_dict_list:
    for key, val in row.items():
        if val == 'LAX94LA336':
            lax_code.append(row)
        
# print(lax_code)

# Accidents by State
accidents_state ={}
for row in aviation_dict_list:
    state_key = row['Location'].split(',')[-1]
    if row['Country'] == 'United States':
        if state_key in accidents_state:
            accidents_state[state_key] += 1
        else:
            accidents_state[state_key] = 1

accidents_sorted = [(val,key) for key, val in accidents_state.items()]
accidents_sorted = sorted(accidents_sorted, reverse=True)  
# print(accidents_sorted)


# Fatalities and serious injuries
injuried={}
for row in aviation_dict_list:
    month = row['Event Date'][:2]
    if row['Total Fatal Injuries'] == '':
        row['Total Fatal Injuries'] = '0'
    if row['Total Serious Injuries'] == '':
        row['Total Serious Injuries'] = '0'
    total = int(row['Total Fatal Injuries']) + int(row['Total Serious Injuries'])
    if month in injuried:
        injuried[month] += total
    else:
        injuried[month] = total

print(injuried)



