from argparse import ArgumentParser, BooleanOptionalAction


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
