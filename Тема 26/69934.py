f = open('69934-1.txt')
N, rows_count, places_in_row = [int(x) for x in f.readline().split()]
min_rows = [rows_count + 1] * (places_in_row + 1)
for i in range(N):
    rad, place = [int(x) for x in f.readline().split()]
    min_rows[place] = min(min_rows[place], rad)
max_row_number = 0
places = []
for i in range(1, places_in_row):
    max_row_number = max(max_row_number, min(min_rows[i] - 1, min_rows[i + 1] - 1))
    if min(min_rows[i] - 1, min_rows[i + 1] - 1) == max_row_number:
        places.append(i + 1)
print(max_row_number, max(places))

