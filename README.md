# nesdis-goes
This API downloads satellite imagery directly from star.nesdis.noaa.gov.
Easily access and organize the latest imagery with loose querying allowing 
many user-app possibilities. 
Also compiles gifs and a few other utilities.


## Setup:
> Simply move the contents of `/src` to your project folder.

*Sped up to 8x for first half of gif.*
<br/>
![](https://raw.githubusercontent.com/aerobotpro/nesdis-goes/master/ezgif-1-41d268808025.gif)


## Basic Options:
This API accepts a mixed query (dictionary):

(sector: `string`)
> The group of imagery's region (string of keywords).
``Exapmple: "norther pacific ocean"``

(band: `string`)
> The group of imagery's type or band(string of keywords).
``Example: "cloud weather"``

(dimensions: `list`)
> The desired dimensions of each image in the group of images's.
``Dimensions are limited to [250,250] or [500, 500] or [1000, 1000] or [2000, 2000].``

For all options visit:
[Here for all sectors](https://www.star.nesdis.noaa.gov/goes/index.php)
[Here for all bands](https://www.star.nesdis.noaa.gov/goes/conus.php?sat=G17)

### API Methods:
`API.showimages()`
<br/>
> Opens each image received, will cause issues if many results (buggy).

`API.makeGif(GIFname: string)`
<br/>
> Creates a GIF from each image received.

`API.cleanUp()`
<br/>
> Deletes all downloaded images.

`API.payload`
<br/>
> The final query result object, holds all results from query.
<br/>
> Can be utilized for many applications like Django sites etc.


```python

# Import the API
from NesdisAPI import nesdis

# BASIC USAGE
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


## Advanced Usage:

Accepts same query as *Basic Options* plus:

(time: `dict`)
> Sets either a timeframe from now and minus `x` amount of either hours(`int`) or days(`int`) 

> Example: `"time": {"days": 2}`

**or**

> sets a split time from, essentially a time between **x**(`datetime string`) and **y**(`datetime string`),
we'll use "oldest" and "newest" instead of x/y.

> Example: `"time": {timeframe: {"oldest": "2020-08-01 12:30", "newest": "2020-08-30 23:30"}}`

(type: `string`) 
**Do Not Change** - *for further implementations only*

Sets the type of images to select.
Types are: `default`(defaults to this and really shouldn't be changed), `thumbnail`, `unknown`, `banner`
Note: Not really useful at this point in time, I will use this later to call specific images that are not the default slid images like thumbnails etc.

```python

# Import the API
from NesdisAPI import nesdis

# BASIC USAGE
API = nesdis(
    {
        "sector": "virginia state",
        "band": "physics micro",
        "time": {timeframe: {"oldest": "2020-08-01 12:30", "newest": "2020-08-30 23:30"}},
        "dimensions": [250,250]
    }
)

print(API.payload)

myGif = "test1.gif"

API.makeGif(myGif)

API.cleanUp()
```

Note: I'll eventually move this to a module that way it can be installed easier via PIP and properly imported.
