class GOES:

    base_url = "https://cdn.star.nesdis.noaa.gov"

    sectors = [            
        #Sector Schema:
        #{"formal-names": ["REGION_ID", "NAME_FORMAL", "SAT_ID"], "keywords": ["A", "COUPLE", "OF", "QUERY", "RICH", "TERMS"]},
        #(Terms should be ordered from GREATEST SIGNIFICANCE TO LEAST -> -> )

        # WEST
        {"formal-names": ["CONUS", "PACUS", "GOES17"], "keywords": ["pacific", "northwest", "northern", "ocean", "asia", "polynesia", "conus"]},
        {"formal-names": ["FD", "South Pacific - Full Disk", "GOES17"], "keywords": ["pacific", "south", "southern", "ocean", "full", "disk"]},
        {"formal-names": ["pnw", "Pacific Northwest", "GOES17"], "keywords": [
            "pacific", "northwest", "north", "west", "ocean", "close", "oregon", "washington", "california", "state"
            ]},
        {"formal-names": ["psw", "Pacific Southwest", "GOES17"], "keywords": ["pacific", "southwest", "south", "west", "ocean", "close"]},
        {"formal-names": ["wus", "U.S. West Coast", "GOES17"], "keywords": ["pacific", "coast", "west", "california", "state", "ocean", "francisco", "angeles", "la", "city"]},
        {"formal-names": ["ak", "Alaska", "GOES17"], "keywords": ["alaska", "main", "state", "full"]},
        {"formal-names": ["cak", "Central Alaska", "GOES17"], "keywords": ["alaska", "central", "zoom", "anchorage", "city", "state"]},
        {"formal-names": ["sea", "Southeastern Alaska", "GOES17"], "keywords": ["alaska", "south", "eastern", "southeastern", "east", "state", "canada" , "western"]},
        {"formal-names": ["np", "Northern Pacific Ocean", "GOES17"], "keywords": ["pacific", "north", "northern", "ocean", "west", "peninsula"]},
        {"formal-names": ["hi", "Hawaii", "GOES17"], "keywords": ["hawaii", "state", "islands", "pacific", "maui", "city"]},
        {"formal-names": ["tpw", "Tropical Pacific Ocean", "GOES17"], "keywords": ["pacific", "tropic", "tropical", "ocean"]},
        {"formal-names": ["tsp", "South Pacific", "GOES17"], "keywords": ["pacific", "south", "ocean"]},

        ## EAST
        {"formal-names": ["CONUS", "CONUS", "GOES16"], "keywords": ["conus", "usa", "america", "state", "country"]},
        {"formal-names": ["FD", "South Atlantic - Full Disk", "GOES16"], "keywords": [
            "south", "full", "disk", "america", "contintent", "brazil", "country", "uruguay", "peru", "colombia",
            "argentina", "bolivia", "chile", "ecuador", "french guiana", "guyana", "paraguay", "suriname", "venezuela"
            ]},
        {"formal-names": ["nr", "Northern Rockies", "GOES16"], "keywords": [
            "northern", "us", "rockies", "central", "colorado", "state", "denver", "city", "montana", "boseman", "utah", "wyoming", "idaho", "nevada"
            ]},
        {"formal-names": ["umv", "Upper Mississippi Valley", "GOES16"], "keywords": [
            "northern", "us", "upper", "mississippi", "valley", "kansas", "nebraska", "dakota", "minnesota", "missouri", "kentucky", "state"
            ]},
        {"formal-names": ["cgl", "Great Lakes", "GOES16"], "keywords": [
            "great", "lakes", "northern", "state", "southeastern", "wisconsin", "michigan", "ohio", "indiana", "illinois", "penn", "west vir", "erie"
            ]},
        {"formal-names": ["ne", "Northeast", "GOES16"], "keywords": [
            "us", "north", "northeast", "northeastern", "state", "penn", "mary", "conn", "mass", "maine", "nova", "montreal", "ottawa", "rhode", "york", "ny", "boston"
            ]},
        {"formal-names": ["sr", "Southern Rockies", "GOES16"], "keywords": ["southern", "rockies", "arizona", "new mexico", "state"]},
        {"formal-names": ["sp", "Southern Plains", "GOES16"], "keywords": ["southern", "plains", "texas", "okla", "state", "dallas", "city", "louisi", "gulf"]},
        {"formal-names": ["smv", "Southern Mississippi Valley", "GOES16"], "keywords": [
            "south", "valley", "northern", "southeastern", "mississippi", "arkan", "alabama", "tenne" "kenucky", "state"
            ]},
        {"formal-names": ["se", "Southeast", "GOES16"], "keywords": ["south", "deep", "southeast", "state", "florida", "georgia", "carolina", "tenn", "forida"]},      
        {"formal-names": ["eus", "U.S. Atlantic Coast", "GOES16"], "keywords": [
            "atlantic", "coast", "jersey", "virginia", "delaware", "maine", "eastern", "seaboard", "state"
            ]},
        {"formal-names": ["can", "Northern Atlantic", "GOES16"], "keywords": [
            "atlantic", "north", "ireland", "greenland", "iceland", "nova", "scotia", "labrador", "sea", "quebec", "newfound", "country", "scotland"
            ]},
        {"formal-names": ["car", "Caribbean", "GOES16"], "keywords": ["carribbean", "cuba", "dominican", "venez", "north", "country"]},
        {"formal-names": ["gm", "Gulf of Mexico", "GOES16"], "keywords": ["gulf", "mexico", "of", "south", "sea", "texas", "baja"]},
        {"formal-names": ["pr", "Puerto Rico", "GOES16"], "keywords": [
            "puerto", "rico", "country", "virgin", "island", "guadel", "montserrat", "antigua", "dominica", "lucia", "martini"
            ]},
        {"formal-names": ["taw", "Tropical Atlantic", "GOES16"], "keywords": ["atlantic", "tropical", "ocean", "region", "section", "large"]},
        {"formal-names": ["eep", "Eastern East Pacific", "GOES16"], "keywords": ["pacific", "eastern", "east", "southeast", "central", "american", "coast"]},
        {"formal-names": ["mex", "Mexico", "GOES16"], "keywords": ["mexico", "country", "mex", "city"]},
        {"formal-names": ["cam", "Central America", "GOES16"], "keywords": ["central", "america", "costa", "guata", "nicar", "panama", "honduras", "country", "region"]},
        {"formal-names": ["nsa", "South America - Northern", "GOES16"], "keywords": ["north", "south amer", "region", "large"]},
        {"formal-names": ["ssa", "South America - Southern", "GOES16"], "keywords": ["south", "south amer", "region", "large"]}
    ]

    bands = [
        #Band Schema:
        #{"formal-names": ["ACTUAL_NAME_HANDLE"], "keywords": ["A", "COUPLE", "OF", "QUERY", "RICH", "TERMS"]},
        {"formal-names": ["GEOCOLOR"], "keywords": ["geo", "color", "topo", "spatial"]},
        {"formal-names": ["AirMass"], "keywords": ["air", "mass", "particle", "part"]},
        {"formal-names": ["Sandwich"], "keywords": ["sand", "wich", "thermal", "dynamic"]},
        {"formal-names": ["DayCloudPhase"], "keywords": ["day", "cloud", "phase", "weather"]},
        {"formal-names": ["NightMicrophysics"], "keywords": ["night", "micro", "phys", "rgb", "contrast", "fog"]},
        {"formal-names": ["01"], "keywords": ["band", "01", "1", "-", "blue", "visi"]},
        {"formal-names": ["02"], "keywords": ["band", "02", "2", "-", "red", "visi"]},
        {"formal-names": ["03"], "keywords": ["band", "03", "3", "-", "veggie", "near", "ir", "inf"]},
        {"formal-names": ["04"], "keywords": ["band", "04", "4", "-", "cirrus", "near", "ir", "inf"]},
        {"formal-names": ["05"], "keywords": ["band", "05", "5", "-", "snow", "near", "ice", "ir", "inf"]},
        {"formal-names": ["06"], "keywords": ["band", "06", "6", "-", "cloud", "particle", "near", "ir", "inf"]},
        {"formal-names": ["07"], "keywords": ["band", "07", "7", "-", "short", "wave", "window", "ir", "inf"]},
        {"formal-names": ["08"], "keywords": ["band", "08", "8", "-", "water", "vapor", "inf", "ir", "upper", "level"]},
        {"formal-names": ["09"], "keywords": ["band", "09", "9", "-", "water", "vapor", "inf", "ir", "mid", "level"]},
        {"formal-names": ["10"], "keywords": ["band", "10", "10", "-", "water", "vapor", "inf", "ir", "lower", "level"]},
        {"formal-names": ["11"], "keywords": ["band", "11", "11", "-", "cloud", "top", "inf", "ir"]},
        {"formal-names": ["12"], "keywords": ["band", "12", "12", "-", "ozone", "ir", "inf"]},
        {"formal-names": ["13"], "keywords": ["band", "13", "13", "-", "clean", "long", "wave", "window", "ir", "inf"]},
        {"formal-names": ["14"], "keywords": ["band", "14", "14", "-", "long", "wave", "ir", "inf"]},
        {"formal-names": ["15"], "keywords": ["band", "15", "15", "-", "dirty", "long", "wave", "ir", "inf"]},
        {"formal-names": ["16"], "keywords": ["band", "16", "16", "-", "atmos", "co2", "long", "wave", "oxy", "ir", "inf"]},
    ]

    month_conversion = [
        ["ja", "01"],
        ["fe", "02"],
        ["ma", "03"],
        ["ap", "04"],
        ["ma", "05"],
        ["jun", "06"],
        ["jul", "07"],
        ["au", "08"],
        ["se", "09"],
        ["oc", "10"],
        ["no", "11"],
        ["de", "12"]
    ]

    types = [
        "default",
        #meaning: main image set
        "unknown", 
        #"meaning": "unknown image type
        "thumbnail"
        ]