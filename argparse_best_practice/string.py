from argparse import Action, ArgumentParser, Namespace
from typing import Any, Optional, Sequence, Text, Union


def best_practice_string() -> None:
    def default_string() -> None:
        parser = ArgumentParser()
        parser.add_argument('--default-string', default='a')
        parser.add_argument('--default-string-exist', default='a')
        args = parser.parse_args(['--default-string-exist', 'b'])
        assert args.default_string == 'a'
        assert args.default_string_exist == 'b'
    default_string()


    def my_string_validation() -> None:
        class MyStringValidationError(Exception):
            def __init__(self, value: str) -> None:
                self.value = value
                super().__init__()


        class MyStringValidator(Action):
            def __call__(self, 
                         parser: ArgumentParser, 
                         namespace: Namespace, 
                         values: Union[Text, Sequence[Any], None], 
                         option_string: Optional[Text]) -> None:
                if values.islower():
                    raise MyStringValidationError(values)
                setattr(namespace, self.dest, values)


        parser = ArgumentParser()
        parser.add_argument('--my-string-validation', action=MyStringValidator)
        try:
            args = parser.parse_args(['--my-string-validation', 'a'])
        except MyStringValidationError as e:
            assert MyStringValidationError('a').value == e.value
        else:
            assert False
        args = parser.parse_args(['--my-string-validation', 'A'])
        assert args.my_string_validation == 'A'
    my_string_validation()
