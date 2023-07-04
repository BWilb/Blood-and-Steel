na = ["canada", "United States", "Cuba", "Mexico"]
europe = ["germany", "britain", "russia", "italy", "serbia", "greece"]
asia = ["japan", "turkey", "iraq", "india", "china"]
print("europe", "asia", "north america")
for i in range(0, len(europe) - 1):
    if len(na) - 1 < i:
        print(europe[i], asia[i], "")
        if len(asia) - 1 < i:
            print(europe[i], "", "")

    else:
        print(europe[i], asia[i], na[i])