# This is autogenerated code. DO NOT change this manually.
# Run scripts/generate_ast.py to generate this file.


class Node(object):
    __slots__ = ()


class Definition(Node):
    __slots__ = ()


class Document(Node):
    __slots__ = ('loc', 'definitions',)
    _fields = ('definitions',)

    def __init__(self, definitions, loc=None):
        self.loc = loc
        self.definitions = definitions

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, Document) and
                # self.loc == other.loc and
                self.definitions == other.definitions
            )
        )

    def __repr__(self):
        return ('Document('
                'definitions={self.definitions!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.definitions,
            self.loc
        )

    def __hash__(self):
        return id(self)


class OperationDefinition(Definition):
    __slots__ = ('loc', 'operation', 'name', 'variable_definitions', 'directives', 'selection_set',)
    _fields = ('operation', 'name', 'variable_definitions', 'directives', 'selection_set',)

    def __init__(self, operation, selection_set, name=None, variable_definitions=None, directives=None, loc=None):
        self.loc = loc
        self.operation = operation
        self.name = name
        self.variable_definitions = variable_definitions
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, OperationDefinition) and
                # self.loc == other.loc and
                self.operation == other.operation and
                self.name == other.name and
                self.variable_definitions == other.variable_definitions and
                self.directives == other.directives and
                self.selection_set == other.selection_set
            )
        )

    def __repr__(self):
        return ('OperationDefinition('
                'operation={self.operation!r}'
                ', name={self.name!r}'
                ', variable_definitions={self.variable_definitions!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.operation,
            self.selection_set,
            self.name,
            self.variable_definitions,
            self.directives,
            self.loc
        )

    def __hash__(self):
        return id(self)


class VariableDefinition(Node):
    __slots__ = ('loc', 'variable', 'type', 'default_value',)
    _fields = ('variable', 'type', 'default_value',)

    def __init__(self, variable, type, default_value=None, loc=None):
        self.loc = loc
        self.variable = variable
        self.type = type
        self.default_value = default_value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, VariableDefinition) and
                # self.loc == other.loc and
                self.variable == other.variable and
                self.type == other.type and
                self.default_value == other.default_value
            )
        )

    def __repr__(self):
        return ('VariableDefinition('
                'variable={self.variable!r}'
                ', type={self.type!r}'
                ', default_value={self.default_value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.variable,
            self.type,
            self.default_value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class SelectionSet(Node):
    __slots__ = ('loc', 'selections',)
    _fields = ('selections',)

    def __init__(self, selections, loc=None):
        self.loc = loc
        self.selections = selections

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, SelectionSet) and
                # self.loc == other.loc and
                self.selections == other.selections
            )
        )

    def __repr__(self):
        return ('SelectionSet('
                'selections={self.selections!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.selections,
            self.loc
        )

    def __hash__(self):
        return id(self)


class Selection(Node):
    __slots__ = ()


class Field(Selection):
    __slots__ = ('loc', 'alias', 'name', 'arguments', 'directives', 'selection_set',)
    _fields = ('alias', 'name', 'arguments', 'directives', 'selection_set',)

    def __init__(self, name, alias=None, arguments=None, directives=None, selection_set=None, loc=None):
        self.loc = loc
        self.alias = alias
        self.name = name
        self.arguments = arguments
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, Field) and
                # self.loc == other.loc and
                self.alias == other.alias and
                self.name == other.name and
                self.arguments == other.arguments and
                self.directives == other.directives and
                self.selection_set == other.selection_set
            )
        )

    def __repr__(self):
        return ('Field('
                'alias={self.alias!r}'
                ', name={self.name!r}'
                ', arguments={self.arguments!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.alias,
            self.arguments,
            self.directives,
            self.selection_set,
            self.loc
        )

    def __hash__(self):
        return id(self)


class Argument(Node):
    __slots__ = ('loc', 'name', 'value',)
    _fields = ('name', 'value',)

    def __init__(self, name, value, loc=None):
        self.loc = loc
        self.name = name
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, Argument) and
                # self.loc == other.loc and
                self.name == other.name and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('Argument('
                'name={self.name!r}'
                ', value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class FragmentSpread(Selection):
    __slots__ = ('loc', 'name', 'directives',)
    _fields = ('name', 'directives',)

    def __init__(self, name, directives=None, loc=None):
        self.loc = loc
        self.name = name
        self.directives = directives

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, FragmentSpread) and
                # self.loc == other.loc and
                self.name == other.name and
                self.directives == other.directives
            )
        )

    def __repr__(self):
        return ('FragmentSpread('
                'name={self.name!r}'
                ', directives={self.directives!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.directives,
            self.loc
        )

    def __hash__(self):
        return id(self)


class InlineFragment(Selection):
    __slots__ = ('loc', 'type_condition', 'directives', 'selection_set',)
    _fields = ('type_condition', 'directives', 'selection_set',)

    def __init__(self, type_condition, selection_set, directives=None, loc=None):
        self.loc = loc
        self.type_condition = type_condition
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, InlineFragment) and
                # self.loc == other.loc and
                self.type_condition == other.type_condition and
                self.directives == other.directives and
                self.selection_set == other.selection_set
            )
        )

    def __repr__(self):
        return ('InlineFragment('
                'type_condition={self.type_condition!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.type_condition,
            self.selection_set,
            self.directives,
            self.loc
        )

    def __hash__(self):
        return id(self)


class FragmentDefinition(Definition):
    __slots__ = ('loc', 'name', 'type_condition', 'directives', 'selection_set',)
    _fields = ('name', 'type_condition', 'directives', 'selection_set',)

    def __init__(self, name, type_condition, selection_set, directives=None, loc=None):
        self.loc = loc
        self.name = name
        self.type_condition = type_condition
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, FragmentDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.type_condition == other.type_condition and
                self.directives == other.directives and
                self.selection_set == other.selection_set
            )
        )

    def __repr__(self):
        return ('FragmentDefinition('
                'name={self.name!r}'
                ', type_condition={self.type_condition!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.type_condition,
            self.selection_set,
            self.directives,
            self.loc
        )

    def __hash__(self):
        return id(self)


class Value(Node):
    __slots__ = ()


class Variable(Value):
    __slots__ = ('loc', 'name',)
    _fields = ('name',)

    def __init__(self, name, loc=None):
        self.loc = loc
        self.name = name

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, Variable) and
                # self.loc == other.loc and
                self.name == other.name
            )
        )

    def __repr__(self):
        return ('Variable('
                'name={self.name!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.loc
        )

    def __hash__(self):
        return id(self)


class IntValue(Value):
    __slots__ = ('loc', 'value',)
    _fields = ('value',)

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, IntValue) and
                # self.loc == other.loc and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('IntValue('
                'value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class FloatValue(Value):
    __slots__ = ('loc', 'value',)
    _fields = ('value',)

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, FloatValue) and
                # self.loc == other.loc and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('FloatValue('
                'value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class StringValue(Value):
    __slots__ = ('loc', 'value',)
    _fields = ('value',)

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, StringValue) and
                # self.loc == other.loc and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('StringValue('
                'value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class BooleanValue(Value):
    __slots__ = ('loc', 'value',)
    _fields = ('value',)

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, BooleanValue) and
                # self.loc == other.loc and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('BooleanValue('
                'value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class EnumValue(Value):
    __slots__ = ('loc', 'value',)
    _fields = ('value',)

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, EnumValue) and
                # self.loc == other.loc and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('EnumValue('
                'value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class ListValue(Value):
    __slots__ = ('loc', 'values',)
    _fields = ('values',)

    def __init__(self, values, loc=None):
        self.loc = loc
        self.values = values

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, ListValue) and
                # self.loc == other.loc and
                self.values == other.values
            )
        )

    def __repr__(self):
        return ('ListValue('
                'values={self.values!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.values,
            self.loc
        )

    def __hash__(self):
        return id(self)


class ObjectValue(Value):
    __slots__ = ('loc', 'fields',)
    _fields = ('fields',)

    def __init__(self, fields, loc=None):
        self.loc = loc
        self.fields = fields

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, ObjectValue) and
                # self.loc == other.loc and
                self.fields == other.fields
            )
        )

    def __repr__(self):
        return ('ObjectValue('
                'fields={self.fields!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.fields,
            self.loc
        )

    def __hash__(self):
        return id(self)


class ObjectField(Node):
    __slots__ = ('loc', 'name', 'value',)
    _fields = ('name', 'value',)

    def __init__(self, name, value, loc=None):
        self.loc = loc
        self.name = name
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, ObjectField) and
                # self.loc == other.loc and
                self.name == other.name and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('ObjectField('
                'name={self.name!r}'
                ', value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class Directive(Node):
    __slots__ = ('loc', 'name', 'arguments',)
    _fields = ('name', 'arguments',)

    def __init__(self, name, arguments=None, loc=None):
        self.loc = loc
        self.name = name
        self.arguments = arguments

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, Directive) and
                # self.loc == other.loc and
                self.name == other.name and
                self.arguments == other.arguments
            )
        )

    def __repr__(self):
        return ('Directive('
                'name={self.name!r}'
                ', arguments={self.arguments!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.arguments,
            self.loc
        )

    def __hash__(self):
        return id(self)


class Type(Node):
    __slots__ = ()


class NamedType(Type):
    __slots__ = ('loc', 'name',)
    _fields = ('name',)

    def __init__(self, name, loc=None):
        self.loc = loc
        self.name = name

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, NamedType) and
                # self.loc == other.loc and
                self.name == other.name
            )
        )

    def __repr__(self):
        return ('NamedType('
                'name={self.name!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.loc
        )

    def __hash__(self):
        return id(self)


class ListType(Type):
    __slots__ = ('loc', 'type',)
    _fields = ('type',)

    def __init__(self, type, loc=None):
        self.loc = loc
        self.type = type

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, ListType) and
                # self.loc == other.loc and
                self.type == other.type
            )
        )

    def __repr__(self):
        return ('ListType('
                'type={self.type!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.type,
            self.loc
        )

    def __hash__(self):
        return id(self)


class NonNullType(Type):
    __slots__ = ('loc', 'type',)
    _fields = ('type',)

    def __init__(self, type, loc=None):
        self.loc = loc
        self.type = type

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, NonNullType) and
                # self.loc == other.loc and
                self.type == other.type
            )
        )

    def __repr__(self):
        return ('NonNullType('
                'type={self.type!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.type,
            self.loc
        )

    def __hash__(self):
        return id(self)


class Name(Node):
    __slots__ = ('loc', 'value',)
    _fields = ('value',)

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, Name) and
                # self.loc == other.loc and
                self.value == other.value
            )
        )

    def __repr__(self):
        return ('Name('
                'value={self.value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.value,
            self.loc
        )

    def __hash__(self):
        return id(self)


# Type System Definition

class TypeDefinition(Node):
    pass


class TypeSystemDefinition(TypeDefinition):
    pass


class SchemaDefinition(TypeSystemDefinition):
    __slots__ = ('loc', 'operation_types',)
    _fields = ('operation_types',)

    def __init__(self, operation_types, loc=None):
        self.operation_types = operation_types
        self.loc = loc

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, SchemaDefinition) and
                self.operation_types == other.operation_types
            )
        )

    def __repr__(self):
        return ('SchemaDefinition('
                'operation_types={self.operation_types!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.operation_types,
            self.loc
        )

    def __hash__(self):
        return id(self)


class OperationTypeDefinition(Node):
    __slots__ = ('loc', 'operation', 'type',)
    _fields = ('operation', 'type',)

    def __init__(self, operation, type, loc=None):
        self.operation = operation
        self.type = type
        self.loc = loc

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, OperationTypeDefinition) and
                self.operation == other.operation and
                self.type == other.type
            )
        )

    def __repr__(self):
        return ('OperationTypeDefinition('
                'operation={self.operation!r}'
                ', type={self.type!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.operation,
            self.type,
            self.loc
        )

    def __hash__(self):
        return id(self)


class ObjectTypeDefinition(TypeDefinition):
    __slots__ = ('loc', 'name', 'interfaces', 'fields',)
    _fields = ('name', 'interfaces', 'fields',)

    def __init__(self, name, fields, interfaces=None, loc=None):
        self.loc = loc
        self.name = name
        self.interfaces = interfaces
        self.fields = fields

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, ObjectTypeDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.interfaces == other.interfaces and
                self.fields == other.fields
            )
        )

    def __repr__(self):
        return ('ObjectTypeDefinition('
                'name={self.name!r}'
                ', interfaces={self.interfaces!r}'
                ', fields={self.fields!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.fields,
            self.interfaces,
            self.loc
        )

    def __hash__(self):
        return id(self)


class FieldDefinition(Node):
    __slots__ = ('loc', 'name', 'arguments', 'type',)
    _fields = ('name', 'arguments', 'type',)

    def __init__(self, name, arguments, type, loc=None):
        self.loc = loc
        self.name = name
        self.arguments = arguments
        self.type = type

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, FieldDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.arguments == other.arguments and
                self.type == other.type
            )
        )

    def __repr__(self):
        return ('FieldDefinition('
                'name={self.name!r}'
                ', arguments={self.arguments!r}'
                ', type={self.type!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.arguments,
            self.type,
            self.loc
        )

    def __hash__(self):
        return id(self)


class InputValueDefinition(Node):
    __slots__ = ('loc', 'name', 'type', 'default_value',)
    _fields = ('name', 'type', 'default_value',)

    def __init__(self, name, type, default_value=None, loc=None):
        self.loc = loc
        self.name = name
        self.type = type
        self.default_value = default_value

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, InputValueDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.type == other.type and
                self.default_value == other.default_value
            )
        )

    def __repr__(self):
        return ('InputValueDefinition('
                'name={self.name!r}'
                ', type={self.type!r}'
                ', default_value={self.default_value!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.type,
            self.default_value,
            self.loc
        )

    def __hash__(self):
        return id(self)


class InterfaceTypeDefinition(TypeDefinition):
    __slots__ = ('loc', 'name', 'fields',)
    _fields = ('name', 'fields',)

    def __init__(self, name, fields, loc=None):
        self.loc = loc
        self.name = name
        self.fields = fields

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, InterfaceTypeDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.fields == other.fields
            )
        )

    def __repr__(self):
        return ('InterfaceTypeDefinition('
                'name={self.name!r}'
                ', fields={self.fields!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.fields,
            self.loc
        )

    def __hash__(self):
        return id(self)


class UnionTypeDefinition(TypeDefinition):
    __slots__ = ('loc', 'name', 'types',)
    _fields = ('name', 'types',)

    def __init__(self, name, types, loc=None):
        self.loc = loc
        self.name = name
        self.types = types

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, UnionTypeDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.types == other.types
            )
        )

    def __repr__(self):
        return ('UnionTypeDefinition('
                'name={self.name!r}'
                ', types={self.types!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.types,
            self.loc
        )

    def __hash__(self):
        return id(self)


class ScalarTypeDefinition(TypeDefinition):
    __slots__ = ('loc', 'name',)
    _fields = ('name',)

    def __init__(self, name, loc=None):
        self.loc = loc
        self.name = name

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, ScalarTypeDefinition) and
                # self.loc == other.loc and
                self.name == other.name
            )
        )

    def __repr__(self):
        return ('ScalarTypeDefinition('
                'name={self.name!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.loc
        )

    def __hash__(self):
        return id(self)


class EnumTypeDefinition(TypeDefinition):
    __slots__ = ('loc', 'name', 'values',)
    _fields = ('name', 'values',)

    def __init__(self, name, values, loc=None):
        self.loc = loc
        self.name = name
        self.values = values

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, EnumTypeDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.values == other.values
            )
        )

    def __repr__(self):
        return ('EnumTypeDefinition('
                'name={self.name!r}'
                ', values={self.values!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.values,
            self.loc
        )

    def __hash__(self):
        return id(self)


class EnumValueDefinition(Node):
    __slots__ = ('loc', 'name',)
    _fields = ('name',)

    def __init__(self, name, loc=None):
        self.loc = loc
        self.name = name

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, EnumValueDefinition) and
                # self.loc == other.loc and
                self.name == other.name
            )
        )

    def __repr__(self):
        return ('EnumValueDefinition('
                'name={self.name!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.loc
        )

    def __hash__(self):
        return id(self)


class InputObjectTypeDefinition(TypeDefinition):
    __slots__ = ('loc', 'name', 'fields',)
    _fields = ('name', 'fields',)

    def __init__(self, name, fields, loc=None):
        self.loc = loc
        self.name = name
        self.fields = fields

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, InputObjectTypeDefinition) and
                # self.loc == other.loc and
                self.name == other.name and
                self.fields == other.fields
            )
        )

    def __repr__(self):
        return ('InputObjectTypeDefinition('
                'name={self.name!r}'
                ', fields={self.fields!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.fields,
            self.loc
        )

    def __hash__(self):
        return id(self)


class TypeExtensionDefinition(TypeSystemDefinition):
    __slots__ = ('loc', 'definition',)
    _fields = ('definition',)

    def __init__(self, definition, loc=None):
        self.loc = loc
        self.definition = definition

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, TypeExtensionDefinition) and
                # self.loc == other.loc and
                self.definition == other.definition
            )
        )

    def __repr__(self):
        return ('TypeExtensionDefinition('
                'definition={self.definition!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.definition,
            self.loc
        )

    def __hash__(self):
        return id(self)


class DirectiveDefinition(TypeSystemDefinition):
    __slots__ = ('loc', 'name', 'arguments', 'locations')
    _fields = ('name', 'locations')

    def __init__(self, name, locations, arguments=None, loc=None):
        self.name = name
        self.locations = locations
        self.loc = loc
        self.arguments = arguments

    def __eq__(self, other):
        return (
            self is other or (
                isinstance(other, DirectiveDefinition) and
                self.name == other.name and
                self.locations == other.locations and
                # self.loc == other.loc and
                self.arguments == other.arguments
            )
        )

    def __repr__(self):
        return ('DirectiveDefinition('
                'name={self.name!r}, '
                'locations={self.locations!r}'
                ')').format(self=self)

    def __copy__(self):
        return type(self)(
            self.name,
            self.locations,
            self.arguments,
            self.loc,
        )

    def __hash__(self):
        return id(self)
