import ast

class FirstParser(ast.NodeVisitor):

    def __init__(self):
        pass

    def continues(self, stmt):
        '''Helper: parse a node's children'''
        super(FirstParser, self).generic_visit(stmt)

    def parse(self, code):
        '''Parse text into a tree and walk the result'''  
        tree = ast.parse(code)
        self.visit(tree)

    def visit_Import(self, stmt_import):
        # retrieve the name from the returned object
        # normally, there is just a single alias
        for alias in stmt_import.names:
            print 'import name "%s"' % alias.name
            print 'import object %s' % alias

        self.continues(stmt_import)

    def visit_BinOp(self, stmt_binop):
        print 'expression: '
        #for child in ast.iter_fields(stmt_binop):
        #    print '  child %s ' % str(child)
	print ' operator %s ' % str(stmt_binop.op)
	#print ast.dump(stmt_binop)
        self.continues(stmt_binop)


    def visit_Name(self, stmt_name):
        print 'expression: '
        print ' variable %s ' % str(stmt_name.id)
        self.continues(stmt_name)


    def visit_Num(self, stmt_num):
        print 'expression: '
        print ' number %s ' % str(stmt_num.n)
        self.continues(stmt_num)

  

parser = FirstParser()
parser.parse('import foo')
parser.parse('a = b + 5')
