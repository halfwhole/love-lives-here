import random
import pandas as pd
from names_dataset import NameDataset

ds = NameDataset()
first_names = ds.first_names
last_names  = ds.last_names

df = pd.read_csv('data.csv')
names = sorted(str(name).lower() for name in df['name'])

def match(name):
    any_first_name = any(ds.search_first_name(part) for part in name.split(' '))
    any_last_name  = any(ds.search_last_name(part)  for part in name.split(' '))
    return any_first_name or any_last_name

matched_names   = [name for name in names if match(name)]
unmatched_names = [name for name in names if not match(name)]

print('Real names: %.1f%%' % (len(matched_names) / len(names) * 100))
print('Pseudonyms: %.1f%%' % (len(unmatched_names) / len(names) * 100))
print('Examples of real names: %s' % [random.choice(matched_names) for i in range(7)])
print('Examples of pseudonyms: %s' % [random.choice(unmatched_names) for i in range(7)])

# 'smol bean', 'before sunrise', 'soft universe'
# 'xiao ming' vs 'xiaoming'
# 'daniel' vs 'daniellllll'
