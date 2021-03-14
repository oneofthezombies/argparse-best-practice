from argparse import Action, ArgumentParser, Namespace
from typing import Any, Optional, Sequence, Text, Union


def best_practice_number() -> None:
    def default_number() -> None:
        parser = ArgumentParser()
        parser.add_argument('--default-number', type=int, default=0)
        parser.add_argument('--default-number-exist', type=int, default=0)
        args = parser.parse_args(['--default-number-exist', '1'])
        assert args.default_number == 0
        assert args.default_number_exist == 1
    default_number()


    def my_number_validation() -> None:
        class MyNumberValidationError(Exception):
            def __init__(self, value: int) -> None:
                self.value = value
                super().__init__()


        class MyNumberValidator(Action):
            def __call__(self, 
                         parser: ArgumentParser, 
                         namespace: Namespace, 
                         values: Union[Text, Sequence[Any], None], 
                         option_string: Optional[Text]) -> None:
                if 0 > values:
                    raise MyNumberValidationError(values)
                setattr(namespace, self.dest, values)


        parser = ArgumentParser()
        parser.add_argument('--my-number-validation', action=MyNumberValidator, type=int, default=0)
        try:
            args = parser.parse_args(['--my-number-validation', '-1'])
        except MyNumberValidationError as e:
            assert MyNumberValidationError(-1).value == e.value
        else:
            assert False
    my_number_validation()
