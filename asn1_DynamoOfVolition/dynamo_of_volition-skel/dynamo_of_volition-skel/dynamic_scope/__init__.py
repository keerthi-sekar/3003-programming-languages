from tokenize import Name
from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}
        self.keys()
        self.values()


    """ def __contains__(self, __o: object) -> bool:
        if(super().__contains__(__o) == True):
            return super().__contains__(__o)
        else:
            return NameError

    def keys(self) -> KeysView[_KT]:
        return super().keys()

    def values(self) -> ValuesView[_VT_co]:
        return super().values()  """

def get_dynamic_re() -> DynamicScope:
    data = DynamicScope()
    (data, inspect.stack())
    return data
