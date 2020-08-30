# nesdis-goes
Downloads satellite imagery directly from star.nesdis.noaa.gov. Also compiles gifs and a few other utilities.


## Setup/Usage:
Simply 


```python
  
from NesdisAPI import nesdis

API = nesdis(
    {
        "sector": "virginia state",
        "band": "physics micro",
        "dimensions": [250,250]
    }
)

myGif = "test1.gif"

API.makeGif(myGif)

API.cleanUp()
```
