l = [[1],[3],[4],[5],[8],[9],[12],[14],[15]]

for f in range(7):
    if any(f in sub_list for sub_list in l):
        print('f:', f)