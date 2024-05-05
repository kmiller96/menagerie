# Docker Compose for VS Code
Showcases how you can use docker-compose in your development environment for
integration testing.

## Scenario
To showcase the functionality, we are going to go with a pretty basic and simple 
case.

There are three services:

- `service1`: the 'main' application that calls the other applications.
- `service2`: one microservice, which takes an input of N numbers and adds them
    together.
- `service3`: another microservice, which takes an input of N numbers and 
    multiplies them together.