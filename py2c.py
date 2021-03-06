"""
    py2c
    ~~~~

    Convert simple numeric python code into C code.

    The translate() function works on

    Variables definition in C
    -------------------------
    Defining variables within the translate function is a bit of a guess work,
    using following rules:
    *   By default, a variable is a 'double'.
    *   Variable in a for loop is an int.
    *   Variable that is references with brackets is an array of doubles. The
        variable within the brackets is integer. For example, in the
        reference 'var1[var2]', var1 is a double array, and var2 is an integer.
    *   Assignment to an argument makes that argument an array, and the index
        in that assignment is 0.
        For example, the following python code::
            def func(arg1, arg2):
                arg2 = 17.
        is translated to the following C code::
            double func(double arg1)
            {
                arg2[0] = 17.0;
            }
        For example, the following python code is translated to the
        following C code::

            def func(arg1, arg2):          double func(double arg1) {
                arg2 = 17.                      arg2[0] = 17.0;
                                            }
    *   All functions are defined as double, even if there is no
        return statement.

Based on codegen.py:

    :copyright: Copyright 2008 by Armin Ronacher.
    :license: BSD.
"""
"""
Update Notes
============
11/22/2017, O.E.   Each 'visit_*' method is to build a C statement string. It
                    shold insert 4 blanks per indentation level.
                    The 'body' method will combine all the strings, by adding
                    the 'current_statement' to the c_proc string list
   11/2017, OE: variables, argument definition implemented.
   Note: An argument is considered an array if it is the target of an
        assignment. In that case it is translated to <var>[0]
11/27/2017, OE: 'pow' basicly working
  /12/2017, OE: Multiple assignment: a1,a2,...,an=b1,b2,...bn implemented
  /12/2017, OE: Power function, including special cases of
                square(x)(pow(x,2)) and cube(x)(pow(x,3)), implemented in
                translate_power, called from visit_BinOp
12/07/2017, OE: Translation of integer division, '\\' in python, implemented
                in translate_integer_divide, called from visit_BinOp
12/07/2017, OE: C variable definition handled in 'define_c_vars'
              : Python integer division, '//', translated to C in
                'translate_integer_divide'
12/15/2017, OE: Precedence maintained by writing opening and closing
                parenthesesm '(',')', in procedure 'visit_BinOp'.
12/18/2017, OE: Added call to 'add_current_line()' at the beginning
                of visit_Return
01/4/2018, O.E. Added functions 'get_files_names()', , 'print_usage()'. The get_files_names()
                function retrieves the in/out file names form the command line, and returns
                true/false if the number of parameters is valid. In case of no input
                parameters, usage is prompt and the program terminates.
01/4/2018, O.E. 'translate(functions, constants=None)' returns string, instaed of a list


"""
import ast
import sys
from ast import NodeVisitor

BINOP_SYMBOLS = {}
BINOP_SYMBOLS[ast.Add] = '+'
BINOP_SYMBOLS[ast.Sub] = '-'
BINOP_SYMBOLS[ast.Mult] = '*'
BINOP_SYMBOLS[ast.Div] = '/'
BINOP_SYMBOLS[ast.Mod] = '%'
BINOP_SYMBOLS[ast.Pow] = '**'
BINOP_SYMBOLS[ast.LShift] = '<<'
BINOP_SYMBOLS[ast.RShift] = '>>'
BINOP_SYMBOLS[ast.BitOr] = '|'
BINOP_SYMBOLS[ast.BitXor] = '^'
BINOP_SYMBOLS[ast.BitAnd] = '&'
BINOP_SYMBOLS[ast.FloorDiv] = '//'

BOOLOP_SYMBOLS = {}
BOOLOP_SYMBOLS[ast.And] = '&&'
BOOLOP_SYMBOLS[ast.Or] = '||'

CMPOP_SYMBOLS = {}
CMPOP_SYMBOLS[ast.Eq] = '=='
CMPOP_SYMBOLS[ast.NotEq] = '!='
CMPOP_SYMBOLS[ast.Lt] = '<'
CMPOP_SYMBOLS[ast.LtE] = '<='
CMPOP_SYMBOLS[ast.Gt] = '>'
CMPOP_SYMBOLS[ast.GtE] = '>='
CMPOP_SYMBOLS[ast.Is] = 'is'
CMPOP_SYMBOLS[ast.IsNot] = 'is not'
CMPOP_SYMBOLS[ast.In] = 'in'
CMPOP_SYMBOLS[ast.NotIn] = 'not in'

UNARYOP_SYMBOLS = {}
UNARYOP_SYMBOLS[ast.Invert] = '~'
UNARYOP_SYMBOLS[ast.Not] = 'not'
UNARYOP_SYMBOLS[ast.UAdd] = '+'
UNARYOP_SYMBOLS[ast.USub] = '-'


def to_source(tree, constants=None, fname=None, lineno=0):
    """
    This function can convert a syntax tree into C sourcecode.
    """
    generator = SourceGenerator(constants=constants, fname=fname, lineno=lineno)
    generator.visit(tree)
    c_code = "\n".join(generator.c_proc)
    return (c_code)

def isevaluable(s):
    try:
        eval(s)
        return True
    except Exception:
        return False

class SourceGenerator(NodeVisitor):
    """This visitor is able to transform a well formed syntax tree into python
    sourcecode.  For more details have a look at the docstring of the
    `node_to_source` function.
    """

    def __init__(self, indent_with="    ", add_line_information=False,
                 constants=None, fname=None, lineno=0):
        self.result = []
        self.indent_with = indent_with
        self.add_line_information = add_line_information
        self.indentation = 0
        self.new_lines = 0

        # for C
        self.c_proc = []
        self.signature_line = 0
        self.arguments = []
        self.current_function = ""
        self.fname = fname
        self.lineno_offset = lineno
        self.warnings = []
        self.statements = []
        self.current_statement = ""
        # TODO: use set rather than list for c_vars, ...
        self.c_vars = []
        self.c_int_vars = []
        self.c_pointers = []
        self.c_dcl_pointers = []
        self.c_functions = []
        self.c_vectors = []
        self.c_constants = constants if constants is not None else {}
        self.in_subref = False
        self.in_subscript = False
        self.tuples = []
        self.required_functions = []
        self.is_sequence = False
        self.visited_args = False
        self.inside_if = False

    def write_python(self, x):
        if self.new_lines:
            if self.result:
                self.result.append('\n' * self.new_lines)
            self.result.append(self.indent_with * self.indentation)
            self.new_lines = 0
        self.result.append(x)

    def write_c(self, statement):
        # TODO: build up as a list rather than adding to string
        self.current_statement += statement

    def add_c_line(self, line):
        indentation = self.indent_with * self.indentation
        self.c_proc.append("".join((indentation, line, "\n")))

    def add_current_line(self):
        if self.current_statement:
            self.add_c_line(self.current_statement)
            self.current_statement = ''

    def add_unique_var(self, new_var):
        if new_var not in self.c_vars:
            self.c_vars.append(str(new_var))

    def write_sincos(self, node):
        angle = str(node.args[0].id)
        self.write_c(node.args[1].id + " = sin(" + angle + ");")
        self.add_current_line()
        self.write_c(node.args[2].id + " = cos(" + angle + ");")
        self.add_current_line()
        for arg in node.args:
            self.add_unique_var(arg.id)

    def newline(self, node=None, extra=0):
        self.new_lines = max(self.new_lines, 1 + extra)
        if node is not None and self.add_line_information:
            self.write_c('# line: %s' % node.lineno)
            self.new_lines = 1
        if self.current_statement:
            self.statements.append(self.current_statement)
            self.current_statement = ''

    def body(self, statements):
        if self.current_statement:
            self.add_current_line()
        self.new_line = True
        self.indentation += 1
        for stmt in statements:
            #if hasattr(stmt, 'targets') and hasattr(stmt.targets[0], 'id'):
            #    target_name = stmt.targets[0].id # target name needed for debug only
            self.visit(stmt)
        self.add_current_line() # just for breaking point. to be deleted.
        self.indentation -= 1

    def body_or_else(self, node):
        self.body(node.body)
        if node.orelse:
            self.newline()
            self.write_c('else:')
            self.body(node.orelse)

    def signature(self, node):
        want_comma = []
        def write_comma():
            if want_comma:
                self.write_c(', ')
            else:
                want_comma.append(True)

        # for C
        for arg in node.args:
            # CRUFT: 2.7 uses arg.id, 3.x uses arg.arg
            try:
                arg_name = arg.arg
            except AttributeError:
                arg_name = arg.id
            self.arguments.append(arg_name)

        padding = [None] *(len(node.args) - len(node.defaults))
        for arg, default in zip(node.args, padding + node.defaults):
            if default is not None:
                # CRUFT: 2.7 uses arg.id, 3.x uses arg.arg
                try:
                    arg_name = arg.arg
                except AttributeError:
                    arg_name = arg.id
                w_str = ("Default Parameters are unknown to C: '%s = %s" \
                        % (arg_name, str(default.n)))
                self.warnings.append(w_str)

    def decorators(self, node):
        for decorator in node.decorator_list:
            self.newline(decorator)
            self.write_python('@')
            self.visit(decorator)

    # Statements

    def visit_Assert(self, node):
        self.newline(node)
        self.write_c('assert ')
        self.visit(node.test)
        if node.msg is not None:
            self.write_python(', ')
            self.visit(node.msg)

    def define_c_vars(self, target):
        if hasattr(target, 'id'):
        # a variable is considered an array if it apears in the agrument list
        # and being assigned to. For example, the variable p in the following
        # sniplet is a pointer, while q is not
        # def somefunc(p, q):
        #  p = q + 1
        #  return
        #
            if target.id not in self.c_vars:
                if target.id in self.arguments:
                    idx = self.arguments.index(target.id)
                    new_target = self.arguments[idx] + "[0]"
                    if new_target not in self.c_pointers:
                        target.id = new_target
                        self.c_pointers.append(self.arguments[idx])
                else:
                    self.c_vars.append(target.id)

    def add_semi_colon(self):
        semi_pos = self.current_statement.find(';')
        if semi_pos > 0.0:
            self.current_statement = self.current_statement.replace(';', '')
        self.write_c(';')

    def visit_Assign(self, node):
        self.add_current_line()
        for idx, target in enumerate(node.targets): # multi assign, as in 'a = b = c = 7'
            if idx:
                self.write_c(' = ')
            self.define_c_vars(target)
            self.visit(target)
        # Capture assigned tuple names, if any
        targets = self.tuples[:]
        del self.tuples[:]
        self.write_c(' = ')
        self.is_sequence = False
        self.visited_args = False
        self.visit(node.value)
        self.add_semi_colon()
        self.add_current_line()
        # Assign tuples to tuples, if any
        # TODO: doesn't handle swap:  a,b = b,a
        for target, item in zip(targets, self.tuples):
            self.visit(target)
            self.write_c(' = ')
            self.visit(item)
            self.add_semi_colon()
            self.add_current_line()
        if self.is_sequence and not self.visited_args:
            for target in node.targets:
                if hasattr(target, 'id'):
                    if target.id in self.c_vars and target.id not in self.c_dcl_pointers:
                        if target.id not in self.c_dcl_pointers:
                            self.c_dcl_pointers.append(target.id)
                            if target.id in self.c_vars:
                                self.c_vars.remove(target.id)
        self.current_statement = ''

    def visit_AugAssign(self, node):
        if node.target.id not in self.c_vars:
            if node.target.id not in self.arguments:
                self.c_vars.append(node.target.id)
        self.visit(node.target)
        self.write_c(' ' + BINOP_SYMBOLS[type(node.op)] + '= ')
        self.visit(node.value)
        self.add_semi_colon()
        self.add_current_line()

    def visit_ImportFrom(self, node):
        return  # import ignored
        self.newline(node)
        self.write_python('from %s%s import ' %('.' * node.level, node.module))
        for idx, item in enumerate(node.names):
            if idx:
                self.write_python(', ')
            self.write_python(item)

    def visit_Import(self, node):
        return  # import ignored
        self.newline(node)
        for item in node.names:
            self.write_python('import ')
            self.visit(item)

    def visit_Expr(self, node):
        self.newline(node)
        self.generic_visit(node)

    def write_c_pointers(self, start_var):
        if self.c_dcl_pointers:
            var_list = []
            for c_ptr in self.c_dcl_pointers:
                if c_ptr not in self.arguments:
                    var_list.append("*" + c_ptr)
                if c_ptr in self.c_vars:
                    self.c_vars.remove(c_ptr)
            if var_list:
                c_dcl = "    double " + ", ".join(var_list) + ";\n"
                self.c_proc.insert(start_var, c_dcl)
                start_var += 1
        return start_var

    def insert_c_vars(self, start_var):
        have_decls = False
        start_var = self.write_c_pointers(start_var)
        if self.c_int_vars:
            for var in self.c_int_vars:
                if var in self.c_vars:
                    self.c_vars.remove(var)
            decls = ", ".join(self.c_int_vars)
            self.c_proc.insert(start_var, "    int " + decls + ";\n")
            have_decls = True
            start_var += 1

        if self.c_vars:
            decls = ", ".join(self.c_vars)
            self.c_proc.insert(start_var, "    double " + decls + ";\n")
            have_decls = True
            start_var += 1

        if self.c_vectors:
            for vec_number, vec_value  in enumerate(self.c_vectors):
                name = "vec" + str(vec_number + 1)
                decl = "    double " + name + "[] = {" + vec_value + "};"
                self.c_proc.insert(start_var, decl + "\n")
                start_var += 1

        del self.c_vars[:]
        del self.c_int_vars[:]
        del self.c_vectors[:]
        del self.c_pointers[:]
        del self.c_dcl_pointers[:]
        if have_decls:
            self.c_proc.insert(start_var, "\n")

    def insert_signature(self):
        arg_decls = []
        for arg in self.arguments:
            decl = "double " + arg
            if arg in self.c_pointers:
                decl += "[]"
            arg_decls.append(decl)
        args_str = ", ".join(arg_decls)
        method_sig = 'double ' + self.current_function + '(' + args_str + ")"
        if self.signature_line >= 0:
            self.c_proc.insert(self.signature_line, method_sig)

    def visit_FunctionDef(self, node):
        if self.current_function:
            self.unsupported(node, "function within a function")
        self.current_function = node.name

        self.newline(extra=1)
        self.decorators(node)
        self.newline(node)
        self.arguments = []
        self.visit(node.args)
        # for C
        self.signature_line = len(self.c_proc)
        self.add_c_line("\n{")
        start_vars = len(self.c_proc) + 1
        self.body(node.body)
        self.add_c_line("}\n")
        self.insert_signature()
        self.insert_c_vars(start_vars)
#        self.c_pointers = []
        self.c_pointers.clear()
        self.current_function = ""

    def visit_ClassDef(self, node):
        have_args = []
        def paren_or_comma():
            if have_args:
                self.write_python(', ')
            else:
                have_args.append(True)
                self.write_python('(')

        self.newline(extra=2)
        self.decorators(node)
        self.newline(node)
        self.write_python('class %s' % node.name)
        for base in node.bases:
            paren_or_comma()
            self.visit(base)
        # CRUFT: python 2.6 does not have "keywords" attribute
        if hasattr(node, 'keywords'):
            for keyword in node.keywords:
                paren_or_comma()
                self.write_python(keyword.arg + '=')
                self.visit(keyword.value)
            if node.starargs is not None:
                paren_or_comma()
                self.write_python('*')
                self.visit(node.starargs)
            if node.kwargs is not None:
                paren_or_comma()
                self.write_python('**')
                self.visit(node.kwargs)
        self.write_python(have_args and '):' or ':')
        self.body(node.body)

    def visit_If(self, node):
        self.add_current_line()
        self.inside_if = True
        self.write_c('if ')
        self.visit(node.test)
        self.write_c(' {')
        self.body(node.body)
        self.add_c_line('}')
        while True:
            else_ = node.orelse
            if len(else_) == 0:
                break
            #elif hasattr(else_, 'orelse'):
            elif len(else_) == 1 and isinstance(else_[0], ast.If):
                node = else_[0]
                #self.newline()
                self.write_c('else if ')
                self.visit(node.test)
                self.write_c(' {')
                self.body(node.body)
                self.add_current_line()
                self.add_c_line('}')
                #break
            else:
                self.newline()
                self.write_c('else {')
                self.body(node.body)
                self.add_c_line('}')
                break
        self.inside_if = False

    def get_for_range(self, node):
        stop = ""
        start = '0'
        step = '1'
        for_args = []
        temp_statement = self.current_statement
        self.current_statement = ''
        for arg in node.iter.args:
            self.visit(arg)
            for_args.append(self.current_statement)
            self.current_statement = ''
        self.current_statement = temp_statement
        if len(for_args) == 1:
            stop = for_args[0]
        elif len(for_args) == 2:
            start = for_args[0]
            stop = for_args[1]
        elif len(for_args) == 3:
            start = for_args[0]
            stop = for_args[1]
            start = for_args[2]
        else:
            raise("Ilegal for loop parameters")
        return start, stop, step

    def visit_For(self, node):
        # node: for iterator is stored in node.target.
        # Iterator name is in node.target.id.
        self.add_current_line()
        fForDone = False
        self.current_statement = ''
        if hasattr(node.iter, 'func'):
            if hasattr(node.iter.func, 'id'):
                if node.iter.func.id == 'range':
                    self.visit(node.target)
                    iterator = self.current_statement
                    self.current_statement = ''
                    if iterator not in self.c_int_vars:
                        self.c_int_vars.append(iterator)
                    start, stop, step = self.get_for_range(node)
                    self.write_c("for(" + iterator + "=" + str(start) +
                                 " ; " + iterator + " < " + str(stop) +
                                 " ; " + iterator + " += " + str(step) + ") {")
                    self.body_or_else(node)
                    self.write_c("}")
                    fForDone = True
        if not fForDone:
            # Generate the statement that is causing the error
            self.current_statement = ''
            self.write_c('for ')
            self.visit(node.target)
            self.write_c(' in ')
            self.visit(node.iter)
            self.write_c(':')
            # report the error
            self.unsupported("unsupported " + self.current_statement)

    def visit_While(self, node):
        self.newline(node)
        self.write_c('while ')
        self.visit(node.test)
        self.write_c(':')
        self.body_or_else(node)

    def visit_With(self, node):
        self.unsupported(node)
        self.newline(node)
        self.write_python('with ')
        self.visit(node.context_expr)
        if node.optional_vars is not None:
            self.write_python(' as ')
            self.visit(node.optional_vars)
        self.write_python(':')
        self.body(node.body)

    def visit_Pass(self, node):
        self.newline(node)
        #self.write_python('pass')

    def visit_Print(self, node):
        # TODO: print support would be nice, though hard to do
        self.unsupported(node)
        # CRUFT: python 2.6 only
        self.newline(node)
        self.write_c('print ')
        want_comma = False
        if node.dest is not None:
            self.write_c(' >> ')
            self.visit(node.dest)
            want_comma = True
        for value in node.values:
            if want_comma:
                self.write_c(', ')
            self.visit(value)
            want_comma = True
        if not node.nl:
            self.write_c(',')

    def visit_Delete(self, node):
        self.unsupported(node)
        self.newline(node)
        self.write_python('del ')
        for idx, target in enumerate(node):
            if idx:
                self.write_python(', ')
            self.visit(target)

    def visit_TryExcept(self, node):
        self.unsupported(node)
        self.newline(node)
        self.write_python('try:')
        self.body(node.body)
        for handler in node.handlers:
            self.visit(handler)

    def visit_TryFinally(self, node):
        self.unsupported(node)
        self.newline(node)
        self.write_python('try:')
        self.body(node.body)
        self.newline(node)
        self.write_python('finally:')
        self.body(node.finalbody)

    def visit_Global(self, node):
        self.unsupported(node)
        self.newline(node)
        self.write_python('global ' + ', '.join(node.names))

    def visit_Nonlocal(self, node):
        self.newline(node)
        self.write_python('nonlocal ' + ', '.join(node.names))

    def visit_Return(self, node):
        self.add_current_line()
        if node.value is None:
            self.write_c('return')
        else:
            self.write_c('return(')
            self.visit(node.value)
        self.write_c(')')
        self.add_semi_colon()
        self.add_c_line(self.current_statement)
        self.current_statement = ''

    def visit_Break(self, node):
        self.newline(node)
        self.write_c('break')

    def visit_Continue(self, node):
        self.newline(node)
        self.write_c('continue')

    def visit_Raise(self, node):
        self.unsupported(node)
        # CRUFT: Python 2.6 / 3.0 compatibility
        self.newline(node)
        self.write_python('raise')
        if hasattr(node, 'exc') and node.exc is not None:
            self.write_python(' ')
            self.visit(node.exc)
            if node.cause is not None:
                self.write_python(' from ')
                self.visit(node.cause)
        elif hasattr(node, 'type') and node.type is not None:
            self.visit(node.type)
            if node.inst is not None:
                self.write_python(', ')
                self.visit(node.inst)
            if node.tback is not None:
                self.write_python(', ')
                self.visit(node.tback)

    # Expressions

    def visit_Attribute(self, node):
        self.unsupported(node, "attribute reference a.b not supported")
        self.visit(node.value)
        self.write_python('.' + node.attr)

    def visit_Call(self, node):
        want_comma = []
        def write_comma():
            if want_comma:
                self.write_c(', ')
            else:
                want_comma.append(True)
        if hasattr(node.func, 'id'):
            if node.func.id not in self.c_functions:
                self.c_functions.append(node.func.id)
            if node.func.id == 'abs':
                self.write_c("fabs ")
            elif node.func.id == 'int':
                self.write_c('(int) ')
            elif node.func.id == "SINCOS":
                self.write_sincos(node)
                return
            else:
                self.visit(node.func)
        else:
            self.visit(node.func)
        self.write_c('(')
        for arg in node.args:
            write_comma()
            self.visited_args = True
            self.visit(arg)
        for keyword in node.keywords:
            write_comma()
            self.write_c(keyword.arg + '=')
            self.visit(keyword.value)
        if hasattr(node, 'starargs'):
            if node.starargs is not None:
                write_comma()
                self.write_c('*')
                self.visit(node.starargs)
        if hasattr(node, 'kwargs'):
            if node.kwargs is not None:
                write_comma()
                self.write_c('**')
                self.visit(node.kwargs)
        self.write_c(')')
        if (self.inside_if == False):
            self.write_c(';')

    def visit_Name(self, node):
        self.write_c(node.id)
        if node.id in self.c_pointers and not self.in_subref:
            self.write_c("[0]")
        name = ""
        sub = node.id.find("[")
        if sub > 0:
            name = node.id[0:sub].strip()
        else:
            name = node.id
        # add variable to c_vars if it ins't there yet, not an argument and not a number
        if (name not in self.c_functions and name not in self.c_vars and
                name not in self.c_int_vars and name not in self.arguments and
                name not in self.c_constants and not name.isdigit()):
            if self.in_subscript:
                self.c_int_vars.append(node.id)
            else:
                self.c_vars.append(node.id)

    def visit_Str(self, node):
        self.write_c(repr(node.s))

    def visit_Bytes(self, node):
        self.write_c(repr(node.s))

    def visit_Num(self, node):
        self.write_c(repr(node.n))

    def visit_Tuple(self, node):
        for idx, item in enumerate(node.elts):
            if idx:
                self.tuples.append(item)
            else:
                self.visit(item)

    def sequence_visit(left, right):
        def visit(self, node):
            self.is_sequence = True
            s = ""
            for idx, item in enumerate(node.elts):
                if idx > 0 and s:
                    s += ', '
                if hasattr(item, 'id'):
                    s += item.id
                elif hasattr(item, 'n'):
                    s += str(item.n)
            if s:
                self.c_vectors.append(s)
                vec_name = "vec"  + str(len(self.c_vectors))
                self.write_c(vec_name)
        return visit

    visit_List = sequence_visit('[', ']')
    visit_Set = sequence_visit('{', '}')
    del sequence_visit

    def visit_Dict(self, node):
        self.unsupported(node)
        self.write_python('{')
        for idx, (key, value) in enumerate(zip(node.keys, node.values)):
            if idx:
                self.write_python(', ')
            self.visit(key)
            self.write_python(': ')
            self.visit(value)
        self.write_python('}')

    def get_special_power(self, string):
        function_name = ''
        is_negative_exp = False
        if isevaluable(str(self.current_statement)):
            exponent = eval(string)
            is_negative_exp = exponent < 0
            abs_exponent = abs(exponent)
            if abs_exponent == 2:
                function_name = "square"
            elif abs_exponent == 3:
                function_name = "cube"
            elif abs_exponent == 0.5:
                function_name = "sqrt"
            elif abs_exponent == 1.0/3.0:
                function_name = "cbrt"
        if function_name == '':
            function_name = "pow"
        return function_name, is_negative_exp

    def translate_power(self, node):
        # get exponent by visiting the right hand argument.
        function_name = "pow"
        temp_statement = self.current_statement
        # 'visit' functions write the results to the 'current_statement' class memnber
        # Here, a temporary variable, 'temp_statement', is used, that enables the
        # use of the 'visit' function
        self.current_statement = ''
        self.visit(node.right)
        exponent = self.current_statement.replace(' ', '')
        function_name, is_negative_exp = self.get_special_power(self.current_statement)
        self.current_statement = temp_statement
        if is_negative_exp:
            self.write_c("1.0 /(")
        self.write_c(function_name + "(")
        self.visit(node.left)
        if function_name == "pow":
            self.write_c(", ")
            self.visit(node.right)
        self.write_c(")")
        if is_negative_exp:
            self.write_c(")")
        self.write_c(" ")

    def translate_integer_divide(self, node):
        self.write_c("(int)(")
        self.visit(node.left)
        self.write_c(") /(int)(")
        self.visit(node.right)
        self.write_c(")")

    def visit_BinOp(self, node):
        self.write_c("(")
        if '%s' % BINOP_SYMBOLS[type(node.op)] == BINOP_SYMBOLS[ast.Pow]:
            self.translate_power(node)
        elif '%s' % BINOP_SYMBOLS[type(node.op)] == BINOP_SYMBOLS[ast.FloorDiv]:
            self.translate_integer_divide(node)
        else:
            self.visit(node.left)
            self.write_c(' %s ' % BINOP_SYMBOLS[type(node.op)])
            self.visit(node.right)
        self.write_c(")")

    # for C
    def visit_BoolOp(self, node):
        self.write_c('(')
        for idx, value in enumerate(node.values):
            if idx:
                self.write_c(' %s ' % BOOLOP_SYMBOLS[type(node.op)])
            self.visit(value)
        self.write_c(')')

    def visit_Compare(self, node):
        self.write_c('(')
        self.visit(node.left)
        for op, right in zip(node.ops, node.comparators):
            self.write_c(' %s ' % CMPOP_SYMBOLS[type(op)])
            self.visit(right)
        self.write_c(')')

    def visit_UnaryOp(self, node):
        self.write_c('(')
        op = UNARYOP_SYMBOLS[type(node.op)]
        self.write_c(op)
        if op == 'not':
            self.write_c(' ')
        self.visit(node.operand)
        self.write_c(')')

    def visit_Subscript(self, node):
        if node.value.id not in self.c_constants:
            if node.value.id not in self.c_pointers:
                self.c_pointers.append(node.value.id)
        self.in_subref = True
        self.visit(node.value)
        self.in_subref = False
        self.write_c('[')
        self.in_subscript = True
        self.visit(node.slice)
        self.in_subscript = False
        self.write_c(']')

    def visit_Slice(self, node):
        if node.lower is not None:
            self.visit(node.lower)
        self.write_python(':')
        if node.upper is not None:
            self.visit(node.upper)
        if node.step is not None:
            self.write_python(':')
            if not(isinstance(node.step, Name) and node.step.id == 'None'):
                self.visit(node.step)

    def visit_ExtSlice(self, node):
        for idx, item in node.dims:
            if idx:
                self.write_python(', ')
            self.visit(item)

    def visit_Yield(self, node):
        self.unsupported(node)
        self.write_python('yield ')
        self.visit(node.value)

    def visit_Lambda(self, node):
        self.unsupported(node)
        self.write_python('lambda ')
        self.visit(node.args)
        self.write_python(': ')
        self.visit(node.body)

    def visit_Ellipsis(self, node):
        self.unsupported(node)
        self.write_python('Ellipsis')

    def generator_visit(left, right):
        def visit(self, node):
            self.write_python(left)
            self.write_c(left)
            self.visit(node.elt)
            for comprehension in node.generators:
                self.visit(comprehension)
            self.write_c(right)
            #self.write_python(right)
        return visit

    visit_ListComp = generator_visit('[', ']')
    visit_GeneratorExp = generator_visit('(', ')')
    visit_SetComp = generator_visit('{', '}')
    del generator_visit

    def visit_DictComp(self, node):
        self.unsupported(node)
        self.write_python('{')
        self.visit(node.key)
        self.write_python(': ')
        self.visit(node.value)
        for comprehension in node.generators:
            self.visit(comprehension)
        self.write_python('}')

    def visit_IfExp(self, node):
        self.visit(node.body)
        self.write_c(' if ')
        self.visit(node.test)
        self.write_c(' else ')
        self.visit(node.orelse)

    def visit_Starred(self, node):
        self.write_c('*')
        self.visit(node.value)

    def visit_Repr(self, node):
        # CRUFT: python 2.6 only
        self.write_c('`')
        self.visit(node.value)
        self.write_python('`')

    # Helper Nodes

    def visit_alias(self, node):
        self.unsupported(node)
        self.write_python(node.name)
        if node.asname is not None:
            self.write_python(' as ' + node.asname)

    def visit_comprehension(self, node):
        self.write_c(' for ')
        self.visit(node.target)
        self.write_C(' in ')
        #self.write_python(' in ')
        self.visit(node.iter)
        if node.ifs:
            for if_ in node.ifs:
                self.write_python(' if ')
                self.visit(if_)

    def visit_arguments(self, node):
        self.signature(node)

    def unsupported(self, node, message=None):
        if hasattr(node, "value"):
            lineno = node.value.lineno
        elif hasattr(node, "iter"):
            lineno = node.iter.lineno
        else:
            #print(dir(node))
            lineno = 0

        lineno += self.lineno_offset
        if self.fname:
            location = "%s(%d)" % (self.fname, lineno)
        else:
            location = "%d" % (self.fname, lineno)
        if self.current_function:
            location += ", function %s" % self.current_function
        if message is None:
            message = node.__class__.__name__ + " syntax not supported"
        raise SyntaxError("[%s] %s" % (location, message))

def print_function(f=None):
    """
    Print out the code for the function
    """
    # Include some comments to see if they get printed
    import ast
    import inspect
    if f is not None:
        tree = ast.parse(inspect.getsource(f))
        tree_source = to_source(tree)
        print(tree_source)

def define_constant(name, value, block_size=1):
    # type: (str, any, int) -> str
    """
    Convert a python constant into a C constant of the same name.

    Returns the C declaration of the constant as a string, possibly containing
    line feeds.  The string will not be indented.

    Supports int, double and sequences of double.
    """
    const = "constant "  # OpenCL needs globals to be constant
    if isinstance(value, int):
        parts = [const + "int ", name, " = ", "%d"%value, ";"]
    elif isinstance(value, float):
        parts = [const + "double ", name, " = ", "%.15g"%value, ";"]
    else:
        try:
            len(value)
        except TypeError:
            raise TypeError("constant %s must be int, float or [float, ...]"%name)
        # extend constant arrays to a multiple of 4; not sure if this
        # is necessary, but some OpenCL targets broke if the number
        # of parameters in the parameter table was not a multiple of 4,
        # so do it for all constant arrays to be safe.
        if len(value)%block_size != 0:
            value = list(value) + [0.]*(block_size - len(value)%block_size)
        elements = ["%.15g"%v for v in value]
        parts = [const + "double ", name, "[]", " = ",
                 "{\n   ", ", ".join(elements), "\n};"]

    return "".join(parts)


# Modified from the following:
#
#    http://code.activestate.com/recipes/578272-topological-sort/
#    Copyright (C) 2012 Sam Denton
#    License: MIT
def ordered_dag(dag):
    # type: (Dict[T, Set[T]]) -> Iterator[T]
    """
    Given a dag defined by a dictionary of {k1: [k2, ...]} yield keys
    in order such that every key occurs after the keys it depends upon.

    This is an iterator not a sequence.  To reverse it use::

        reversed(tuple(ordered_dag(dag)))

    Raise an error if there are any cycles.

    Keys are arbitrary hashable values.
    """
    # Local import to make the function stand-alone, and easier to borrow
    from functools import reduce

    dag = dag.copy()

    # make leaves depend on the empty set
    leaves = reduce(set.union, dag.values()) - set(dag.keys())
    dag.update({node: set() for node in leaves})
    while True:
        leaves = set(node for node, links in dag.items() if not links)
        if not leaves:
            break
        for node in leaves:
            yield node
        dag = {node: (links-leaves)
               for node, links in dag.items() if node not in leaves}
    if dag:
        raise ValueError("Cyclic dependes exists amongst these items:\n%s"
                         % ", ".join(str(node) for node in dag.keys()))

def translate(functions, constants=None):
    # type: (List[(str, str, int)], Dict[str, any]) -> List[str]
    """
    Convert a set of functions
    """
    snippets = []
    snippets.append("#include <math.h>")
    snippets.append("")
    for source, fname, lineno in functions:
        line_directive = '#line %d "%s"'%(lineno, fname.replace('\\', '\\\\'))
        snippets.append(line_directive)
        tree = ast.parse(source)
        c_code = to_source(tree, constants=constants, fname=fname, lineno=lineno)
        snippets.append(c_code)
    return "\n".join(snippets)
#    return snippets

def print_usage ():
        print("""\
            Usage: python py2c.py <infile> [<outfile>]
            if outfile is omitted, output file is '<infile>.c'
        """)

def get_files_names ():
    import os
    fname_in = fname_out = ""
    valid_params =  len(sys.argv) > 1
    if (valid_params == False):
        print_usage()
    else:
        fname_in = sys.argv[1]
        if len(sys.argv) == 2:
            fname_base = os.path.splitext(fname_in)[0]
            fname_out = str(fname_base) + '.c'
        else:
            fname_out = sys.argv[2]
    return valid_params, fname_in,fname_out

def main():
    try:
        f = open('debug.txt', 'a+')
        f.write('execute_slurm_script')
        f.close()
    except:
        print("error opening file")
    print("Parsing...using Python" + sys.version)
    valid_params, fname_in, fname_out = get_files_names ()
    if (valid_params == False):
        print("Input parameters error.\nExiting")
        return

    with open(fname_in, "r") as python_file:
        code = python_file.read()
    name = "gauss"
    code = (code
            .replace(name+'.n', 'GAUSS_N')
            .replace(name+'.z', 'GAUSS_Z')
            .replace(name+'.w', 'GAUSS_W'))

    translation = translate([(code, fname_in, 1)])

    with open(fname_out, "w") as file_out:
        file_out.write(str(translation))
    print("...Done")

if __name__ == "__main__":
    try:
        main()
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
