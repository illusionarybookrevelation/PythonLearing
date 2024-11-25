list_qt = [[1,2],[3,4],[5,6]]
def qtlb(list_qt):
    for aa in list_qt:
        for bb in aa:
            yield bb

for ns in qtlb(list_qt):
    print(ns)