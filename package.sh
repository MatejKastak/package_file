#!/bin/sh

tmp_env () {
	TMP_DIR=$(mktemp -d venv.XXX --tmpdir)
	echo $TMP_DIR
	python -m venv $TMP_DIR
	source $TMP_DIR/bin/activate
}

# Cleanup
rm -rf ./dist
rm -rf ./build
rm -rf *.egg.info

echo -e "\n\n==============TEST SDIST================="
tmp_env
python setup.py sdist
pip install ./dist/package_file-0.0.1.tar.gz
package_file


echo -e "\n\n=============TEST BDIST_WHEEL============"
tmp_env
pip install wheel
python setup.py bdist_wheel
pip install ./dist/package_file-0.0.1-py3-none-any.whl
package_file
