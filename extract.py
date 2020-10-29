
def getit(el):
    for l in el:
        if type(l) != list:
            outp.append(l)
        else:
            return getit(l)

outp = []
a = [345,3,[2,[788,[[76899,67,[8,[452,[[[45,123,[5464545645,4566,876,88665,652]]]]]]]]]]]
getit(a)
print(outp)
