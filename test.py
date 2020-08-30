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


