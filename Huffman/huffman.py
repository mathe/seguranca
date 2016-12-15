from bitarray import *

def addprefixos(xs, p):
    return dict((k, bitarray(p) + v) for (k,v) in xs.items())

id = 0
class Node:
    def __init__(self, x, f):        
        self.x = x
        self.f = f
        self.l = None
        self.r = None
        global id     
        self.id = id
        id += 1

    def join(self, o):
        n = Node(None, self.f + o.f)
        n.l = self
        n.r = o
        return n    

    
    def coding(self):
        l = {}
        r = {}
        if self.x:
            return {self.x: bitarray()}
        if self.l: 
            l = self.l.coding()
        if self.r:
            r = self.r.coding()
        ret = {}
        ret.update(addprefixos(l, '0'))
        ret.update(addprefixos(r, '1'))
        return ret

    def __lt__(self, o):
        return self.f > o.f        

# l = [a, b, c, d]
#l = [Node('a', 4), Node(' ', 2), Node('c', 1), Node('s', 2), Node('r', 1), Node('o', 1)]
def huffmann(l):        
    while(len(l) > 1):
        l.sort()
        a = l.pop()
        b = l.pop()        
        l.append(a.join(b))
    rt = l.pop()
    return (rt,rt.coding())

def save(node,file):
    if node is None:
        return 0
    #file.write()
    line = str(node.id)+":"
    if node.l is None and node.r is None:
        line += node.x
    else:
        line += str(node.l.id) + "," + str(node.r.id)
    file.write(line+"\n")
    save(node.l,file)
    save(node.r,file)