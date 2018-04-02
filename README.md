# cf-python-template

A simple template for getting started with a python web service to be deployed in Cloud Foundry.

## Getting Started

THis is a simple example to get started with a python REST service deployed in Cloud Foundry.

### Installing

Archiving the dependencies with the local command:

```
pip download vendor -r ../requirements.txt --no-binary :all:
```

## Deployment

This is a Flask project intended to be uses as a REST API.

To deploy to Cloud Foundry just run the command.

```
cf push cf-python-template
```

## Built With

* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/clbj/cf-python-template/tags). 

## Authors

* **Cloves Langendorf Barcellos Junior** - [clbj](https://github.com/clbj)

See also the list of [contributors](https://github.com/clbj/cf-python-template/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details