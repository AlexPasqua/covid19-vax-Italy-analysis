import csv

with open("corrected-punti-somministrazione-latest.csv", 'r', encoding="utf8") as their:
    with open("punti-somministrazione-nome-coordinate.csv", 'r', encoding="utf8") as ours:
        their_reader = csv.reader(their)
        ours_reader = csv.reader(ours)
        their_rows = list(their_reader)
        our_rows = list(ours_reader)

with open("punti-somministrazione-coordinate.csv", 'w', encoding="utf8") as out:
    header = their_rows[0] + our_rows[0][1:]
    out.write(','.join([w for w in header]))
    out.write('\n')

    n_not_found = 0
    for row_their in their_rows[1:]:
        found = False
        for row_our in our_rows[1:]:
            # if the hospital's name is the same, merge the 2 rows and write
            if row_their[3] == row_our[0]:
                found = True
                out_row = row_their + row_our[1:]
                out.write(','.join([w for w in out_row]))
                out.write('\n')
                # break

        if not found:
            n_not_found += 1
            print("Match not found for row:")
            print(row_their, '\n')

print(f"For {n_not_found} rows was not possible to find the coordinates")
