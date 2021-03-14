# argparse-best-practice

```python
def best_practice_bool() -> None:
    def default_false() -> None:
        parser = ArgumentParser()
        parser.add_argument('--default-false', action=BooleanOptionalAction, default=False)
        parser.add_argument('--default-false-exist', action=BooleanOptionalAction, default=False)
        parser.add_argument('--default-false-exist-with-no', action=BooleanOptionalAction, default=False)
        args = parser.parse_args(['--default-false-exist',
                                  '--no-default-false-exist-with-no'
                                  ])
        assert args.default_false == False
        assert args.default_false_exist == True
        assert args.default_false_exist_with_no == False
    default_false()


    def default_true() -> None:
        parser = ArgumentParser()
        parser.add_argument('--default-true', action=BooleanOptionalAction, default=True)
        parser.add_argument('--default-true-exist', action=BooleanOptionalAction, default=True)
        parser.add_argument('--default-true-exist-with-no', action=BooleanOptionalAction, default=True)
        args = parser.parse_args(['--default-true-exist',
                                  '--no-default-true-exist-with-no'
                                  ])
        assert args.default_true == True
        assert args.default_true_exist == True
        assert args.default_true_exist_with_no == False
    default_true()


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


def best_practice_list() -> None:
    def default_empty_list() -> None:
        parser = ArgumentParser()
        parser.add_argument('--default-empty-list', action='extend', nargs='+', default=[])
        parser.add_argument('--default-empty-list-exist', action='extend', nargs='+', default=[])
        args = parser.parse_args(['--default-empty-list-exist', 'a', 'b'])
        assert args.default_empty_list == []
        assert args.default_empty_list_exist == ['a', 'b']
    default_empty_list()


    def my_unique_list() -> None:
        class MyUniqueListCreator(Action):
            def __call__(self, 
                         parser: ArgumentParser, 
                         namespace: Namespace, 
                         values: Union[Text, Sequence[Any], None], 
                         option_string: Optional[Text]) -> None:
                default = getattr(namespace, self.dest) if hasattr(namespace, self.dest) else []
                default.extend(values)      
                new_value = list(set(default))
                new_value.sort()      
                setattr(namespace, self.dest,  new_value)


        parser = ArgumentParser()    
        parser.add_argument('--my-unique-list', action=MyUniqueListCreator, nargs='+', default=['a'])
        args = parser.parse_args(['--my-unique-list', 'a', 'b'])
        assert args.my_unique_list == ['a', 'b']
    my_unique_list()
```
