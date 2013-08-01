
g = list('''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv z q
''')


t = list('''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up q z
''')


mapping = dict(zip(g, t))


infile = open('../inputs/googlerese.in', 'r')
outfile = open('../outputs/googlerese.out', 'w')


for i in xrange(1, int(infile.readline()) + 1):
    s = ''.join(mapping[c] for c in infile.readline())   
    outfile.write('Case #%s: %s' % (i, s))
