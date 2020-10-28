 ### Elite


## Author
* Noble Mungu

## Project Description
A user of the application should be able to:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects
5. View projects overall score
6. View my profile page

# Setup and installation requirements
You need to have the following installed:
* Python3+
* Pip
* Virtual ```$ python3.7 -m venv virtual```
* Activate the virtual environment ```. virtual/bin/activate```
* Django ```(virtual)$ pip install Django==1.11.17```
* Get all requirements ```pip freeze > requirements.txt```

### Running the server
```python manage.py runserver```

# Behaviour Driven Development

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit awwwards-clone site| Various projects are displayed  | User can review projects |
| Click on image| Image details displayed | Image details displayed |
| Search project | Images for project are displayed | App gets the projects for the searched project |
| Visit profile | Projects posted by user are displayed | App gets projects for user |
| Visit Admin | Prompts for admin credentials | Admin dashboard displayed |
| API projects | api with a list of projects is displayed | api displayed |

## Technologies Used
* Django-a python frame-work
* Javascript
* Html
* Bootstrap
* Postmman for visual representation while building the api

# Development
It would be so great to have your contributions! Just follow the instructions below.
Fork the repo
* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above) git clone
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!

## Known Bugs
Currently cannot rate or review and get the api endpoints; actively working on it.

### LICENSE
MIT License

 Copyright (c) 2020 Noble Mungu

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.