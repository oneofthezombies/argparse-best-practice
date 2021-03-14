from argparse import Action, ArgumentParser, Namespace
from typing import Any, Optional, Sequence, Text, Union


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
