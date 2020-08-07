import random

NumLooking = 3
vials = 300-28
Time = 22
VialsPerHour = ((60*60)/6)

for h in range(0,Time):
    print(f"hour {h+1}")
    print(f"----------")
    c = min(VialsPerHour, vials)
    for v in range(0,c):
        effect = random.randint(1,100)
        results = []

        counter = 0
        for p in range(0,NumLooking):
            corr = random.randint(1,100)
            if corr <=50:
                results.append(effect)
                if effect==100:
                    counter += 1
            else: 
                incorr = random.randint(1,100)
                results.append(incorr)
                if incorr==100:
                    counter += 1
        print(f"Vial {v}: effect: {effect}. results: {results} Reliability: {counter}")

            

            
