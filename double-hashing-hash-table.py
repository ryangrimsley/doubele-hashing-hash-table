

M1 = 13 #m value for tc1
keys1 = [79, 69, 72, 50, 98, 14] #list of keys for tc1
table1 = ['NIL' for x in range(M1)] #empty table for tc1

M2 = 7 #m value for tc2
keys2 = [10, 82, 40, 35, 15, 21,52] #list of keys for tc2
table2 = ['NIL' for x in range(M2)] #empty table for tc2

#h1 func for test case 1
def tc1_h1(key: int):
    return key % 13

#h2 func for test case 1
def tc1_h2(key: int):
    return 1 + (key % 11)

#h1 func for test case 2
def tc2_h1(key: int):
    return key % 7

#h2 for test case 2
def tc2_h2(key: int):
    return 5 - (key % 5)

#double hash function
def double_hash(key: int, i: int, m: int, tc: int):
    if tc == 1:
        return (tc1_h1(key) + (i * tc1_h2(key))) % m
    elif tc == 2:
        return (tc2_h1(key) + (i * tc2_h2(key))) % m

#insert function
def hash_insert(table: list, key: int, m: int, tc: int):
    i = 0
    index = double_hash(key,i, m, tc)

    #while the index your trying to insert at is filled, look for a new one
    while table[index] != 'NIL':
        i += 1
        index = double_hash(key,i,m, tc)
    table[index] = key

#search function
def hash_search(table: list, key: int, m: int, tc):
    i = 0
    index = double_hash(key,i, m, tc)

    #while the index your trying to find value for != value, keep looking until you search the whole list or find an empty position
    while (table[index] != 'NIL') and (i != m):
        if table[index] == key:
            return index
        i += 1
        index = double_hash(key,i,m, tc)

    return None


for key in keys1:
    hash_insert(table1,key,M1,1)
print("Table 1 after double hashing insertion")
print(table1)    

for key in keys2:
    hash_insert(table2,key,M2,2)
print("Table 2 after double hashing insertion: ")
print(table2)

print(hash_search(table1,66,M1,1))
print(hash_search(table2,52,M2,2))

