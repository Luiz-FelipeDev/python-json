import json 

with open ('states.json') as f:
    data = json.load(f)

    
''' Removendo os codigos de area '''
for state in data['states']:
    del state['area_codes']
    print(state)
    
''' Escrevendo um novo arquivo JSon com as Alterações '''

with open('new_file_json_states.json', 'w') as file:
    json.dump(data, file, indent=2)

    
    
    
