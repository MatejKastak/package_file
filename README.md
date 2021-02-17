# Including data files into a python package

This repo shows an approach how to include data files into a python package that
should be accessible from both source and binary wheel distribution.

In order to create respective distributions use following commands:

1. `python setup.py sdist`
2. `python setup.py bdist_wheel` (dependencies: `pip install wheel`)

The resulting distribution files are placed in the `./dist` folder. In order to
check if the data files are present we can use `unzip` to unpack the wheel and
`tar vxf` to unpack the source distribution.

## Repo organization

Interesting files are marked with `!!!`.

```
├── MANIFEST.in              # !!!
├── package.sh               # Example script
├── README.md
├── setup.py                 # !!!
└── src                      # Package modules
    ├── data                 # Data files
    │   ├── module_info.json
    │   └── test.json
    ├── __init__.py
    └── main.py              # !!!
```

## I want to see this in action.

All the steps are described in the [package.sh](./package.sh).

## How to get files into a source distribution?

`MANIFEST.in` can be used to insert data into the package in the source
distribution. This approach is simple and straight forward. Just declare files
or globs you want to include.

See [file](./MANIFEST.in).

## How to get files into a binary wheel?

This one is a little more tricky.

Use `package_data` keyword argument in the `setup()`.

```
    package_data={
        'src': ['data/*.json'],
    }

```

Good ref: https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html

## How to access the files from python?.

Checkout [main.py](./src/main.py).

Ref: https://setuptools.readthedocs.io/en/latest/pkg_resources.html

## Why did I put data files along side the source code?

I played with placing data files in multiple places, however placing them in the
module works consistently across both options.

## What about `include_package_data=True`?

I played with it but it does not seem to affect those two cases. It works well
even without it. However, we can probably just include it anyways.

## Further testing?

I just tested this on Linux, so probably try this on Windows.
