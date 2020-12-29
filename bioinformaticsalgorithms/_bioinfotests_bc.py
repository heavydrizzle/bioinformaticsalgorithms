# -*- coding: utf-8 -*-
"""Abstract Base Classes (ABCs) for testing bioinformatics algorithms, according
to PEP 3119.
"""

from traits.api import HasTraits, Instance, \
    Str

from abc import ABCMeta, abstractmethod
import unittest

__all__ = ["Testable", "BioInformaticsTest", "ORITest",
           "PairwiseAlignmentTest",
        ]

def _check_methods(C, *methods):
    mro = C.__mro__
    for method in methods:
        for B in mro:
            if method in B.__dict__:
                if B.__dict__[method] == None:
                    return NotImplemented
                break
            else:
                return NotImplemented
    return True
  
class Testable(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def __test__(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Testable:
            return _check_methods(C, "__test__")
        return NotImplemented


class BioInformaticsTest(Testable):

    __slots__ = ()
    __test_delegate__ = Instance(unittest.TestCase())

    @abstractmethod
    def __name__(self):
        yield

    @abstractmethod
    def __script__(self):
        yield

    @abstractmethod
    def __input__(self):
        yield

    @classmethod
    def __subclasshook__(cls, C):
        if cls is BioInformaticsTest:
            return _check_methods(C, "__name__", "__script__", "__input__")
        return NotImplemented

class ORITest(BioInformaticsTest):
    __slots__ = ()
    
    @abstractmethod
    def __name__(self):
        pass

    @abstractmethod
    def __script__(self):
        pass

    @abstractmethod
    def __input__(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ORITest:
            return _check_methods(C, "__name__", "__script__", "__input__")
        return NotImplemented
    
class PairwiseAlignmentTest(BioInformaticsTest):
    __slots__ = ()
    
    @abstractmethod
    def __name__(self):
        yield

    @abstractmethod
    def __script__(self):
        yield

    @abstractmethod
    def __input__(self):
        yield

    @classmethod
    def __subclasshook__(cls, C):
        if cls is PairwiseAlignmentTest:
            return _check_methods(C, "__name__", "__script__", "__input__")
        return NotImplemented

