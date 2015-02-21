class SymbolTable(object):
    def __init__(self):
        scope = dict()
    
    def insert(self, symbol):
        self.scope[symbol.__class__.__name__] = symbol
        
    def delete(self, symbol_class_name):
        try: self.scope.pop(symbol_class_name)
        except: pass
        
    def update(self, old_name, new_object):
        self.scope[old_name] = new_object
        
    def contains(self, name):
        return name in self.scope.keys()
    
    def lookup(self, name):
        return self.scope[name]