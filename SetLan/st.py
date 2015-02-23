class SymbolTable(object):
    def __init__(self):
        self.scope = dict()

    def insert(self, var):
        if not self.contains(var.name): self.scope[var.name] = var

    def delete(self, name):
        if self.contains(name): self.scope.pop(name)

    def update(self, old_varname, new_var):
        if old_varname != new_var.name:
            self.delete(old_varname)
            self[new_var.name] = new_var
        else:
            self[old_varname] = new_var

    def contains(self, name):
        return name in self.scope.keys()

    def lookup(self, name):
        return self.scope[name] if self.contains(name) else None