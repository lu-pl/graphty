import json


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁStructuredMessageǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁStructuredMessageǁ__str____mutmut: MutantDict = {}  # type: ignore


class StructuredMessage:
    """Structured log message class.

    This is taken from the Python logging cookbook:
    https://docs.python.org/3/howto/logging-cookbook.html#implementing-structured-logging;
    jsond.dumps.default is set to str for logging of non-json-serializable objects.
    """

    @_mutmut_mutated(mutants_xǁStructuredMessageǁ__init____mutmut)
    def __init__(self, message: str, **kwargs) -> None:
        self.message = message
        self.kwargs = kwargs

    def xǁStructuredMessageǁ__init____mutmut_orig(self, message: str, **kwargs) -> None:
        self.message = message
        self.kwargs = kwargs

    def xǁStructuredMessageǁ__init____mutmut_1(self, message: str, **kwargs) -> None:
        self.message = None
        self.kwargs = kwargs

    def xǁStructuredMessageǁ__init____mutmut_2(self, message: str, **kwargs) -> None:
        self.message = message
        self.kwargs = None

    @_mutmut_mutated(mutants_xǁStructuredMessageǁ__str____mutmut)
    def __str__(self) -> str:
        return "%s >>> %s" % (self.message, json.dumps(self.kwargs, default=str))

    def xǁStructuredMessageǁ__str____mutmut_orig(self) -> str:
        return "%s >>> %s" % (self.message, json.dumps(self.kwargs, default=str))

    def xǁStructuredMessageǁ__str____mutmut_1(self) -> str:
        return "%s >>> %s" / (self.message, json.dumps(self.kwargs, default=str))

    def xǁStructuredMessageǁ__str____mutmut_2(self) -> str:
        return "XX%s >>> %sXX" % (self.message, json.dumps(self.kwargs, default=str))

    def xǁStructuredMessageǁ__str____mutmut_3(self) -> str:
        return "%S >>> %S" % (self.message, json.dumps(self.kwargs, default=str))

    def xǁStructuredMessageǁ__str____mutmut_4(self) -> str:
        return "%s >>> %s" % (self.message, json.dumps(None, default=str))

    def xǁStructuredMessageǁ__str____mutmut_5(self) -> str:
        return "%s >>> %s" % (self.message, json.dumps(self.kwargs, default=None))

    def xǁStructuredMessageǁ__str____mutmut_6(self) -> str:
        return "%s >>> %s" % (self.message, json.dumps(default=str))

    def xǁStructuredMessageǁ__str____mutmut_7(self) -> str:
        return "%s >>> %s" % (self.message, json.dumps(self.kwargs, ))

mutants_xǁStructuredMessageǁ__init____mutmut['_mutmut_orig'] = StructuredMessage.xǁStructuredMessageǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__init____mutmut['xǁStructuredMessageǁ__init____mutmut_1'] = StructuredMessage.xǁStructuredMessageǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__init____mutmut['xǁStructuredMessageǁ__init____mutmut_2'] = StructuredMessage.xǁStructuredMessageǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁStructuredMessageǁ__str____mutmut['_mutmut_orig'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_orig # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_1'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_1 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_2'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_2 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_3'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_3 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_4'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_4 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_5'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_5 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_6'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_6 # type: ignore # mutmut generated
mutants_xǁStructuredMessageǁ__str____mutmut['xǁStructuredMessageǁ__str____mutmut_7'] = StructuredMessage.xǁStructuredMessageǁ__str____mutmut_7 # type: ignore # mutmut generated
