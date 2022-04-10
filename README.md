# Overview
-----------------------------------------------------------------------------

pypi_analyser is a Python library to monitor PyPi packages! 

## Package Installer 

    pip install pypi-analyser

## Usage

    from pypi_analyser import pypi_analyser
    '''
      package_name -> string pypi package name.
    '''
    package_name = 'pandas'
    package_details = pypi_analyser(package_name)
    
    print(package_details.package_name)
    print(package_details.latest_version)
    print(package_details.license)
    print(package_details.homepage)
    print(package_details.stars)
    print(package_details.forks)
    print(package_details.dependency_count)
    print(package_details.dependencies)
    
**Utilities**

| Name           | Description  |
| ------------- | -----|
| package_name | Returns the pypi package name! |
| description | Returns the description of pypi package! |
| latest_version | Returns the latest version of pypi package! |
| released | Returns the released date of the pypi package! |
| latest_release | Returns the latest release date of pypi package! |
| license | Returns the license of the pypi package! |
| author | Returns the author of the pypi package! |
| maintainer | Returns the maintainer of the pypi package! |
| homepage | Returns the homepage of the pypi package! |
| repository | Returns the repository of the pypi package! |
| dependency_count | Returns the unique dependency count of the pypi package! |
| dependencies | Returns the list of dependendencies for the pypi package! |
| stars | Returns the github stars count of the pypi package! |
| forks | Returns the github forks count of the pypi package! |


## Requirements

The `requirements.txt` file has details of all Python libraries for this package, and can be installed using 
```
pip install -r requirements.txt
```

## Organization

    ├── src
    │   ├── pypi_analyser
              ├── init             <- init
              ├── pypi_analyser    <- package source code for pypi analyser
    ├── setup.py             <- setup file 
    ├── LICENSE              <- LICENSE
    ├── README.md            <- README
    ├── CONTRIBUTING.md      <- contribution
    ├── test.py              <- test cases for unit testing
    ├── requirements.txt     <- requirements file for reproducing the code package

## License

MIT

## Contributions

For steps on code contribution, please see [CONTRIBUTING](./CONTRIBUTING.md).
