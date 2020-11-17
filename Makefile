# Raspberry has both python 2 and 3: here 3 is preferred	
install:
	python3 setup.py install
package:
	python3 setup.py sdist
clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info