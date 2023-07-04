# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента.
# (речь идет про **kwargs)
def hashable_dicts(**kwargs) -> dict:

    return dict(map(lambda values: (values[1], values[0])
                if try_hashable(values[1]) else (str(values[1]), values[0]),
                    kwargs.items()))

def try_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

print(hashable_dicts(dog='Jack', cat={'Leopold': 2, 'Murka': 3}, turtle=['bill', 'jack', 'anatoliy'],
                     hamster={'edward', 'homa'}))