with open('../input/day_1_data.txt', 'r') as file:
    data = file.read()

list_left = []
list_right = []

for line in data.strip().split("\n"):
    left, right = map(int, line.split())
    list_left.append(left)
    list_right.append(right)

def calculate_total_distance(listl, listr):
    return sum(abs(a - b) for a, b in zip(sorted(listl), sorted(listr)))

def calculate_similarity_score(listl, listr):
    frequency = {num: listr.count(num) for num in listr}
    return sum(num * frequency.get(num, 0) for num in listl)

distance = calculate_total_distance(list_left, list_right)
similarity = calculate_similarity_score(list_left, list_right)

print("Distance:", distance)
print("Similarity:", similarity)
