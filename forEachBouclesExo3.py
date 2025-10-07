string="En grammaire, une phrase peut être considérée comme un ensemble autonome, réunissant des unités syntaxiques organisées selon différents réseaux de relations plus ou moins complexes appelés subordination, coordination ou juxtaposition."
alphabet="abcdefghijklmnopqrstuvwxyz"
letterArray = list()

for letter in string:
    if letter.lower() in alphabet:
        if letter.lower() in [l['letter'] for l in letterArray]:
            for l in letterArray:
                if l['letter'] == letter.lower():
                    l['numberOfTime'] += 1
                    break
        else:
            letterArray.append({ 'letter': letter.lower(), 'numberOfTime': 1 })

letterArray.sort(key=lambda x: x['numberOfTime'], reverse=True)

for i in letterArray:
    print(f"La lettre '{i['letter']}' apparaît {i['numberOfTime']} fois")