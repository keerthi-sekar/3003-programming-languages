from tokenize import Name
from typing import Dict, Any, Iterator, Optional
from collections import abc
from types import FunctionType
import inspect


class DynamicScope(abc.Mapping):
    def __init__(self):
        self.env: Dict[str, Optional[Any]] = {}


def get_dynamic_re() -> DynamicScope:
    print(f"{'       --> Entering  DynamicScope.get_dynamic_re Method'}")
    tuple_var = inspect.stack()
    returnDictionary = dict()

    for f in tuple_var:
        flv= f.frame.f_back.f_locals
        freevars = f.frame.f_code.co_freevars
        flist = list (freevars)
        print (flist)

        #HELP as of 9/18: returnDictionary correct implementation for function ...?
        #HELP as of 9/18: Line 33 - str(value) == str(freevars[0]) comparison not working

        for key, value in flv.items():
            if len(freevars) !=0 and str(value) == str(freevars[0]):
                print(key, freevars[0], value, 'true- REMOVE ME ')
            else:
                print(key, value, 'false')   
                returnDictionary.update({key: value})
                

       # if freevars in flv:
            #returnList= flist
    #print(f"{'   -->    --> within get_dynamic_re'}")
    #return None
    return returnDictionary
