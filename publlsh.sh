rm -rf dist
rm -rf build
python3.11 setup.py sdist bdist_wheel
twine upload dist/* 
pip3.11 uninstall -y code2claude
sleep 10
pip3.11 install code2claude