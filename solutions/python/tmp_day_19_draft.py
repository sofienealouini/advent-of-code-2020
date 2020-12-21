#!/usr/bin/env python
# coding: utf-8

# In[36]:


from typing import List, Tuple
import numpy as np
import re
from functools import reduce
from itertools import product
from copy import deepcopy


def read_lines(input_file_path: str, line_type: type) -> list:
    with open(input_file_path, 'r') as input_file:
        return [line_type(line) for line in input_file.read().splitlines()]


def read_blocks(input_file_path: str) -> List[str]:
    with open(input_file_path, 'r') as input_file:
        return [block.replace('\n', ' ') for block in input_file.read().split('\n\n')]


def read_list_of_lists(input_file_path: str) -> List[List[str]]:
    with open(input_file_path, 'r') as input_file:
        return [block.split('\n') for block in input_file.read().split('\n\n')]
    
def read_grid(input_file_path: str) -> List[List[str]]:
    with open(input_file_path, 'r') as input_file:
        return [list(line) for line in input_file.read().split('\n')]


# In[2]:


input_list = read_list_of_lists('inputday19.txt')


# In[3]:


raw_rules, messages = input_list[0], input_list[1][:-1]


# In[4]:


raw_rules[:5]


# In[5]:


messages[:5]


# In[6]:


raw_rules_dict = {}
for r in raw_rules:
    k, v = r.split(': ')
    v = v.replace('\"', '')
    if v.isalpha():
        raw_rules_dict[int(k)] = v
    else:
        sequences = v.split(' | ')
        seq_rules = []
        for seq in sequences:
            seq_rules.append(tuple(int(e) for e in seq.split(' ')))
        raw_rules_dict[int(k)] = seq_rules


# In[7]:


raw_rules_dict[121]


# In[8]:


raw_rules_dict[125]


# In[9]:


raw_rules_dict[85]


# In[10]:


raw_rules_dict[54]


# In[11]:


raw_rules_dict[86]


# # Part 1

# In[12]:


clean_rules = {
    121: ['a'],
    125: ['b']
}


while 0 not in clean_rules:
    for r in raw_rules_dict:
        current_rule = raw_rules_dict[r]
        if (r not in clean_rules) and all(e in clean_rules for t in current_rule for e in t):
            new_rule_r = []
            for t in current_rule:
                new_rule_r.extend([''.join(c) for c in product(*map(lambda e: clean_rules[e], t))]) 
            clean_rules[r] = new_rule_r


# In[13]:


rule_0_patterns = clean_rules[0]
print('Number of patterns for rule 0:', len(rule_0_patterns))
rule_0_patterns[:5]


# In[65]:


counter = 0
for message in messages:
    if message in clean_rules[0]:
        counter += 1


# In[66]:


counter


# # Part 2

# In[183]:


clean_rules_regex = {k: r'^(' + '|'.join(v) + ')$' for k, v in clean_rules.items()}


# In[184]:


clean_rules_regex[8] = clean_rules_regex[8].replace(')$', ')+$')
clean_rules_regex[8]


# In[185]:


clean_rules_regex[42]


# In[186]:


clean_rules_regex[31]


# In[187]:


clean_rules_regex[11] = clean_rules_regex[42][:-1] + '+(' + clean_rules_regex[42][1:-1] + clean_rules_regex[31][1:-1] + ')*' + clean_rules_regex[31][1:-1] + '+$'
clean_rules_regex[11]


# In[188]:


clean_rules_regex[0] = clean_rules_regex[8][:-1] + clean_rules_regex[11][1:]
clean_rules_regex[0]


# In[191]:


def pat_0_alt(n):
    pat_42 = clean_rules_regex[42][1:-1]
    pat_31 = clean_rules_regex[31][1:-1]
    pat_11_alt = pat_42 + '{' + str(n) + '}' + pat_31 + '{' + str(n) + '}'
    return clean_rules_regex[8][:-1] + pat_11_alt + '$'


# In[194]:


pat_0_alt(3)


# In[199]:


counter = 0
    
for message in messages:
    for n in range(15, 0, -1):
        if re.match(pat_0_alt(n), message):
            counter += 1
            continue


# In[200]:


counter


# In[198]:


max(len(m) for m in messages)


# In[ ]:




