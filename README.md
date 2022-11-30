Dear reader,

thanks for taking the time to review my code. There are 2 ways you can run it:

1. In a virtual environment: if you already have a virtual environment with PySpark installed, you can run the code in there. Otherwise, please 
a. create a new virtual environment (e.g. with Pipenv)
b. access it with pipenv shell 
c. move to the folder where the code is located
d. run 'pipenv install' to install all packages from the Pipfile
e. run 'python main.py'
d. the main script will create a folder named 'address_cleansed' in which you will find the json file with street & housenumber

2. This is how you run the code inside a Docker Container (you will need to have Docker installed)
a.	Open a Terminal, go to the directory of the code and run “docker build -t friday-challenge .”
b.	Run "docker images" to get a list of images (there should be one with the name friday-challenge)
c.	Run "docker run -i friday-challenge:latest" (if you gave the image a different name in step 1, use this name instead)
d.	Open a second terminal and run “docker ps”  to see a list of containers
e.	“Docker exec -it <container id> bash” starts shell in container
f.	In the container, enter 'cd src' and run 'python3 main_api.py'
g.  You can check the content of the json file by going to the addresses_cleansed folder and open the json file with the 'cat' command

I also wrote a test_main.py file that runs a few checks on the results of the main script. More detailed descriptions are in the docstrings.

In case you have questions, please reach out to me.
All the best, Moritz