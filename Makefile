# make in
# build it in place
in: pennapprobot.c setup.py settings.json
	python3 setup.py build_ext -i

