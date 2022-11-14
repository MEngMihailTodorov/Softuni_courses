n, m = input().split()
n_set = set()
m_set = set()

for i in range(int(n)):
    n_set.add(int(input()))

for j in range(int(m)):
    m_set.add(int(input()))

for element in n_set & m_set:
    print(element)