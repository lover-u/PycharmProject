def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    values = sorted(keywords.values())
    print keys
    print values
    for kw in keys:
        print kw, ":", keywords[kw]



cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print pairs[0]
print pairs[1]
#def a():
#	b = pa
#print lambda pair: pair[1]
#print
pairs.sort(key=lambda pair: pair[1])
print pairs
pairs.sort(key=lambda pair: pair[0])
print pairs