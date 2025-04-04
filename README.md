# ArchiverTools

Using this tool you can easily interact with the archiver server through your Python code. 
Using this library you can easily download raw data starting from a PV name, impute missing values and match data of multiple PVs for a defined timespan.

Note: to use this library (in particular, to download new data) you need to be connected on the lbl network (you might need the VPN if some connection exception are raised).

## Installation

To install this package, first clone or download this repository on your computer. Then, from terminal, move into the `archivertools` folder:
```
cd archivertools
```
and install the package through `pip`:
```
pip install .
```

## Getting started
Interactions with the archiver are managed by the `ArchiverClient` class. Let's see some examples.

### Single PV data downloading
To download the data of a given pv, refer to the `.download_data()` function:

``` python
from datetime import datetime
from archivertools import ArchiverClient

archiver_client = ArchiverClient()
pv = archiver_client.download_data(
    pv_name='SR04C___QFA____AM00',
    precision=100, # this defines the precision of your signal in ms (bounded by the archiving policy)
    start=datetime(year=2023, month=4, day=25, hour=22),
    end=datetime(year=2023, month=4, day=25, hour=23),
    verbose=False,
)
```
it returns a `PV` object which contains the following information:
``` python
pv.name # pv name, string
pv.raw_data # pv raw data as a pandas.DataFrame object
pv.clean_data # pv clean data as a pandas.DataFrame object
pv.properties # pv properties stored on the archiver as a pandas.DataFrame object
pv.first_timestamp # first timestamp of the downloaded timestamp as a datetime object
pv.last_timestamp # last timestamp of the downloaded timestamp as a datetime object
```

### Data matching
For a given `list` of PVs, data can be matched according to their timestamps. The list must be a sequence of `str`.
PVs could have different archiving policy. In order to have a matching on the timestamps, they must follow the same archiving policy (this means that all the archiving policies of the listed PVs must be reduced to a common archiving policy).
The parameter `precision` allows to select the precision of the individual PVs to allow the data matching

Data matching can be done using the `.match_data()` function:

``` python
... # all your fancy code
pv_list ['SR04C___QFA____AM00', 'SR04C___QFA____AC00']
matched_data = archiver_client.match_data(
    pv_list=pv_list,
    precision=100,
    start=datetime(year=2023, month=4, day=25, hour=22),
    end=datetime(year=2023, month=4, day=25, hour=23),
)
``` 

## Roadmap
Until now, only data management (downloading, preprocessing and some transformation) is implemented. The next update will cover the data plotting (Dashboards).

## Author
Andrea Pollastro - email: apollastro@lbl.gov

## Contributing
If you find any bug or if you have any suggestion on functionalities or improvement of this library, please feel free to write me. :)

Any contribution is much appreciated.
