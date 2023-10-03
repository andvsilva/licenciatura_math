import json

print("Started Reading JSON file...")
with open("mempool.json", "r") as read_file:
    data = json.load(read_file)
    
    for i in data:
        subset = data[i]
        
        if isinstance(subset, int):
            print(f'{i}: {subset}')

        if isinstance(subset, list):
            newsubset = {key: [i[key] for i in subset] for key in subset[0]}
            for j in newsubset:
                print(f'{j}: {newsubset[j]}')

        if isinstance(subset, dict):
            #print(f'{subset}')
            for isubset in subset:
                print(f'{isubset}: {subset[isubset]}')