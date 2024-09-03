import csv


# process data
"""
with open('train_ship_segmentations_v2.csv', newline='') as readfile:
    shipreader = csv.reader(readfile, delimiter=',')
    with open('ship_data_bc_proc.csv', 'w', newline='') as writefile:
        shipwriter = csv.writer(writefile, delimiter=',')
        prev = ""
        for i,row in enumerate(shipreader):
            if i == 0:
                shipwriter.writerow(row)
            else:
                curr = row[0]
                pre_class = row[1]              
                if curr == prev:
                    pass
                else:
                    if pre_class == "":
                        shipwriter.writerow([curr, '0'])
                    else:
                        shipwriter.writerow([curr, '1'])
                    prev = curr
"""

# sanity check

with open("ship_data_bc_proc.csv") as f:
    imgs = [row['ImageId'] for row in csv.DictReader(f)]
    print(len(imgs))
    print(len(set(imgs)))

with open("ship_data_bc_proc.csv") as f:   
    classes = [row['ShipPresent'] for row in csv.DictReader(f)]
    print(len(classes))
    print(classes.count('0')/len(classes))
    print(classes.count('1')/len(classes))
