

# Create a python virtual environment. This should be called venv.

venv:
	@echo "Creating virtual environment"
	python3 -m venv venv

# Create a python requirements.txt file. This should include the packages
# from the beginning of the game_of_life.py file in this directory.
# Specifically, the packages should be: pygame

requirements.txt: game_of_life.py
	@echo "Creating requirements.txt"
	echo "pygame" > requirements.txt

# Install the packages from the requirements.txt file into the virtual
# environment.

install: requirements.txt venv
	@echo "Installing requirements.txt"
	venv/bin/pip install -r requirements.txt


# create a gitignore file including all the common recommendations for python
# and C++ projects.
gitignore:
	@echo "Creating .gitignore"
	echo "venv" > .gitignore
	echo "*.pyc" >> .gitignore
	echo "*.o" >> .gitignore
	echo "*.so" >> .gitignore
	echo "*.dylib" >> .gitignore
	echo "*.dll" >> .gitignore
	echo "*.exe" >> .gitignore
	echo "*.out" >> .gitignore
	echo "*.a" >> .gitignore
	echo "*.lib" >> .gitignore
	echo "*.exp" >> .gitignore
	echo "*.ilk" >> .gitignore
	echo "*.pdb" >> .gitignore
	echo "*.obj" >> .gitignore
	echo "*.sbr" >> .gitignore
	echo "*.ncb" >> .gitignore
	echo "*.suo" >> .gitignore
	echo "*.tlog" >> .gitignore
	echo "*.ipch" >> .gitignore
	echo "*.swp" >> .gitignore
	echo "*.sdf" >> .gitignore
	echo "*.sln" >> .gitignore
	echo "*.suo" >> .gitignore
	echo "*.vcxproj" >> .gitignore
	echo "*.vcxproj.filters" >> .gitignore
	echo "*.vcxproj.user" >> .gitignore
	echo "*.vcxproj.*.user" >> .gitignore
	echo "*.pyc" >> .gitignore
	echo "*.pyo" >> .gitignore
	echo "*.pyd" >> .gitignore
	echo "*.pyw" >> .gitignore
	echo "*.egg-info" >> .gitignore
	echo "*.egg" >> .gitignore
	echo "*.cache" >> .gitignore
	echo "*.log" >> .gitignore
	echo "*.DS_Store" >> .gitignore
	echo "*.idea" >> .gitignore
	echo "*.vscode" >> .gitignore
