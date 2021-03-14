from . import (
    bool as _bool, 
    string as _string, 
    number as _number, 
    list as _list
)


def best_practice():
    _bool.best_practice_bool()
    _string.best_practice_string()
    _number.best_practice_number()
    _list.best_practice_list()


if __name__ == '__main__':
    best_practice()