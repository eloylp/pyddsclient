# Contributing to Scirocco PyClient

## Status
At the momment the project is quite stable, but with a lot of pending work to be a really impresionant software piece.
Theres no exhaustive code docs at this time , but it will be.

## Target
This project is in sync with the [scirocco-server](https://github.com/eloylp/scirocco-server) project (the server side part).
The target is to follow all server side new features, making life easier to other developers to interact with this server part.
Also , it would be fancy if we add improvements based on developers needs.
This client must be coded in a flexible fashion. This means that most of logic must be delegated to the server side. We need to reduce to the max the code maintanance since we need more clients.

## Management
Using "Github projects". Theres one development mainline, but in case of big arriving features it can be splitted in more kanban boards with different teams.
Issues must be clear and concise, with recomendations from the creator, if she/he/it has one. 

## Git flow
The project git flow is based on a traditional merge flow with two main branches protected, master and develop.
On a regular contribution flow yo will fork this repo. [this link](http://nvie.com/posts/a-successful-git-branching-model/) provides a detailed idea.
Commits must be atomic, wrapping small and separate functionalities. Dont worry about the length of commit message, its prefered.

## Continous Integration (CI)
Using Travis CI . See .travis.yml file. Its a requirement to pass all tests before merge.

## About the code
The code must be expressive, easy to read. A code that is understood with less comments is a better quality code. 
Best practices, design principles and patterns are welcome with responsability.

See [this link](https://www.python.org/dev/peps/pep-0008).

## Tests
Unit tests are required using the standard unittest module. Integration tests are also needed.

## Documentation
Using github Wiki.
