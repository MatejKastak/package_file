import pathlib

import pkg_resources

MODULES = 'data/module_info.json'
TEST = 'data/test.json'


def main():
    print('Hello, world')

    # Assert that the files exists
    assert pkg_resources.resource_exists(__name__, MODULES)
    assert pkg_resources.resource_exists(__name__, TEST)

    # Check file
    print('=' * 20)
    file_path = pathlib.Path(
        pkg_resources.resource_filename(__name__, MODULES))
    print(file_path)
    assert file_path.exists()
    contents = pkg_resources.resource_string(__name__, MODULES)
    assert contents

    print('=' * 20)
    # We can convert to string from bytes optionally
    print(contents.decode('utf-8'))
    print('=' * 20)

    # Exactly the same check, just to make sure
    print('=' * 20)
    file_path = pathlib.Path(
        pkg_resources.resource_filename(__name__, TEST))
    print(file_path)
    assert file_path.exists()
    contents = pkg_resources.resource_string(__name__, TEST)
    assert contents

    print('=' * 20)
    print(contents)
    print('=' * 20)

    # import pdb
    # pdb.set_trace()
