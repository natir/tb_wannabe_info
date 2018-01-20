import os
import csv
import tb_wannabe_info

work_list = list()
with open(os.path.dirname(tb_wannabe_info.__file__) + "/liste_metier.csv") as f:
    reader = csv.reader(f)
    for l in reader:
        work_list.append(tuple(l))

