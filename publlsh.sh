rm -rf dist
rm -rf build
python3.10 setup.py sdist bdist_wheel
twine upload dist/* 