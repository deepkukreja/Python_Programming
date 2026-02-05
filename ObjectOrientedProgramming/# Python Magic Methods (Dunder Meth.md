# Python Magic Methods (Dunder Methods)
Complete Notes + GitHub Ready Reference

---

## 1. Object Creation & Destruction
Used for object lifecycle management.

```python
__new__(cls, ...)
__init__(self, ...)
__del__(self)




2. String Representation

Controls how objects are printed or displayed.

__str__(self)
__repr__(self)
__format__(self, format_spec)





3. Comparison Operators

Used for comparing objects.

__eq__(self, other)      # ==
__ne__(self, other)      # !=
__lt__(self, other)      # <
__le__(self, other)      # <=
__gt__(self, other)      # >
__ge__(self, other)      # >=





4. Arithmetic Operators

Defines behavior of mathematical operators.

__add__(self, other)         # +
__sub__(self, other)         # -
__mul__(self, other)         # *
__truediv__(self, other)    # /
__floordiv__(self, other)   # //
__mod__(self, other)        # %
__pow__(self, other)        # **






5. Reflected Arithmetic Operators

Called when left operand does not support the operation.

__radd__(self, other)
__rsub__(self, other)
__rmul__(self, other)
__rtruediv__(self, other)
__rfloordiv__(self, other)
__rmod__(self, other)
__rpow__(self, other)




6. Augmented Assignment Operators

Used with operators like +=, -=, etc.

__iadd__(self, other)
__isub__(self, other)
__imul__(self, other)
__itruediv__(self, other)
__ifloordiv__(self, other)
__imod__(self, other)
__ipow__(self, other)





7. Unary Operators

Operate on a single operand.

__pos__(self)       # +obj
__neg__(self)       # -obj
__abs__(self)       # abs(obj)
__invert__(self)   # ~obj
__round__(self, n)
__floor__(self)
__ceil__(self)
__trunc__(self)






8. Type Conversion Methods

Convert object to built-in types.

__int__(self)
__float__(self)
__complex__(self)
__bool__(self)




9. Container / Collection Methods

Make object behave like a list, tuple, or dict.

__len__(self)
__getitem__(self, key)
__setitem__(self, key, value)
__delitem__(self, key)
__contains__(self, item)




10. Iteration Methods

Allow object to be iterable.

__iter__(self)
__next__(self)




11. Attribute Handling

Customize attribute access.

__getattr__(self, name)
__getattribute__(self, name)
__setattr__(self, name, value)
__delattr__(self, name)




12. Callable Objects

Make object callable like a function.

__call__(self, ...)



13. Context Manager

Used with with statement.

__enter__(self)
__exit__(self, exc_type, exc_value, traceback)




14. Hashing & Truth Value

Used in sets and dictionaries.

__hash__(self)




15. Copying Objects

Used with copy module.

__copy__(self)
__deepcopy__(self, memo)




16. Miscellaneous Utility Methods
__sizeof__(self)
__dir__(self)








