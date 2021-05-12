stuff = []
feats = {'title': '', 'price': '', 'quantity': '', 'measuring': ''}
anltcs = {'title': [], 'price': [], 'quantity': [], 'measuring': []}
nn = 0

while True:
    if input('press Enter to continue, or Q to exit- ').upper() == 'Q':
        break
    nn += 1
    for f in feats.keys():
        prop = input(f"enter the feature's value {f} - ")
        feats[f] = int(prop) if (f == 'price' or f == 'quantity') else prop
        anltcs[f].append(feats[f])
    stuff.append((nn, feats.copy()))
    print(f"\nstructure of the stuff\n{stuff}")
    print(f"\ncurrent analytics of the stuff:\n{'*' * 30}")
    for key, value in anltcs.items():
        print(f"{key[:25]:>30}: {value}")
    print('*' * 30)