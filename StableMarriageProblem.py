import numpy as np

n = 4
##### Initialize preference list of n men and women in n #####
m = np.empty((n,n), dtype = int)
w = np.empty((n,n), dtype = int)
for i in range(n):
    m[i] = np.random.choice(n, n, replace = False)
    w[i] = np.random.choice(n, n, replace = False)

# Uncomment this to have own prefernce list.
# m and w each should have distinct values of preferences
w = np.array([ [3,1,2,0],
               [3,2,0,1],
               [0,2,1,3],
               [3,1,0,2] ])

m = np.array([ [3,1,2,0],
               [3,2,0,1],
               [1,0,2,3],
               [2,1,0,3] ])
n = len(m)

##### Initialize matches with zeroes #####
matches = np.empty((n,2), dtype = int)
matches[:, 0] = np.arange(n, dtype = int)
matches[:, 1] = np.full(n, -1, dtype = int)

##### Gale-Shapley Algorithm for stable matching #####
while -1 in matches[:, 1]:
    i = np.where(matches[:, 1] == -1)[0][0] #Find index of men free for pairing
    for j in range(n):
        # Check whether the chosen women is free
        if m[i][j] in matches[:, 1]:
            # -> Women is already matched to someone
            matched_man = np.where( matches[:, 1]  == m[i][j] )[0][0]
            temp_women = m[i][j]

            # Check if women prefers the matched man or not
            new_man_index = np.where( w[temp_women, :] == i )[0][0]
            matched_man_index = np.where( w[temp_women, :] == matched_man )[0][0]
            if new_man_index < matched_man_index: # -> Women prefers new partner more
                matches[matched_man][1] = -1
                matches[i][1] = m[i][j]
                break
        else:
            # -> Women is ready to be paired
            matches[i][1] = m[i][j]
            break

print("Men preferences are:")
for i in range(len(m)):
    print(i, "-", m[i])
print("\nWomen preferences are:")
for i in range(len(w)):
    print(i, "-", w[i])
print("\nMatches obtained are:")
for x, y in matches:
    print("{} -> {}".format(x, y))