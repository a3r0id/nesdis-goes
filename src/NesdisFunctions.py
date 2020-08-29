
#from selenium import webdriver
from NesdisDataset import GOES
from NesdisErrors import Errors
from requests_html import HTMLSession
from user_agent import generate_navigator
from re import search
from datetime import datetime, timedelta, date
from urllib.parse import urlparse
from os import path, remove
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
DIE_ON_NO_VALID_MATCH = True

# For post-job cleanup :)
class temp:
    stack = {
        "cleanup-files":[]
    }

#indexes = [sector, band]
def parseImages(request, index):
    html = request.text.split("\n")
    parsed = {}
    parsedLines = []

    for line in html:

        PIC_CODE = None
        PIC_TYPE = None
        PIC_DIMENSIONS = []
        PIC_CODE = str()

        if "<a" in line and "../" not in line:
            if "x" in line:
                if "-" in line:
                    PIC_CODE = line.split("-")[0]
                    if len(PIC_CODE) > 5:
                        PIC_TYPE = "default"

            if PIC_TYPE is None:
                PIC_TYPE = "unknown"

            if "0x" in line:
                regexDimensions = search(r'[0-9][0-9][0-9][0-9]x[0-9][0-9][0-9][0-9]', line)
                if regexDimensions is not None:
                    dimBuffer = regexDimensions.group(0)
                    PIC_DIMENSIONS.append(int(dimBuffer.split("x")[0]))
                    PIC_DIMENSIONS.append(int(dimBuffer.split("x")[1]))                  
                else:
                    regexDimensions = search(r'[0-9][0-9][0-9]x[0-9][0-9][0-9]', line)
                    if regexDimensions is not None:
                        dimBuffer = regexDimensions.group(0)
                        PIC_DIMENSIONS.append(int(dimBuffer.split("x")[0]))
                        PIC_DIMENSIONS.append(int(dimBuffer.split("x")[1]))
                    else:
                        PIC_DIMENSIONS = [0,0]
            else:
                PIC_DIMENSIONS = [0,0]            
                
            regexDate = search(r'[0-3][0-9]-[A-Z][a-z][a-z]-[2-9][0-9][0-9][09] [0-9][0-9]:[0-9][0-9]', line)

            regexCode = search(r'\d{11}', line)

            if regexDate is not None:
                PIC_DATE = regexDate.group(0)
            else:
                PIC_DATE = None

            if regexCode is not None:
                PIC_CODE = regexCode.group(0)
            else:
                PIC_CODE = None 
                if "thumbnail" in line:
                    PIC_TYPE = "thumbnail"
                    PIC_CODE = "thumbnail"


            PIC_HREF = line.split("\"")[1].split("\"")[0] 
            
            PIC_FULL_URI = index["uri"] + PIC_HREF    

            parsedLines.append(
                {
                    "type": PIC_TYPE,
                    "code": PIC_CODE,
                    "date": PIC_DATE,
                    "href": PIC_HREF,
                    "full-uri": PIC_FULL_URI,
                    "dimensions": PIC_DIMENSIONS
                }
            )

    parsed["lines"] = parsedLines            
    return parsed      

def DatetimeString(year, month, day, hour, minute):
    return f'{year}-{month}-{day} {hour}:{minute}'

def setDatetimeObj(string):
    return datetime.strptime(string, '%Y-%m-%d %H:%M')

def parseDateTime(this):
    
    day = this.split("-")[0]
    monthString = this.split(day + "-")[1].split("-")[0]
    index = 0
    monthSet = False

    for string in GOES.month_conversion:
        if string[0] in monthString.lower():
            month = GOES.month_conversion[index][1]
            monthSet = True
            break 
        index += 1

    year = this.split(monthString + "-")[1].split(" ")[0]
    hour = this.split(year + " ")[1].split(":")[0]
    minute = this.split(hour + ":")[1]

    out = None
    if not monthSet:
        out = None
    else:
        out = datetime.strptime(f'{year}-{month}-{day} {hour}:{minute}', '%Y-%m-%d %H:%M')
    return out


def getDefaultSlidesByTimeframe(parsedObject, queryObject):

    try:
        timeFrame = queryObject["time"]
    except:
        timeFrame = {"hours": 0}

    dimensions = queryObject["dimensions"]

    masterIndex = 0
    slides = []
    timeNow = datetime.now()

    # TIME OBJECT:
    #{
    #    time: {"days": AMOUNT_OF_DAYS}
    #    `or`
    #    hour: {"hours": AMOUNT_OF_HOURS}
    #    `or`
    #    timeframe: {"oldest": "2020-08-01 12:30", "newest": "2020-08-30 23:30"}
    #}

    if "type" in queryObject:
        imageType = queryObject["type"]
    else:
        imageType = None    
        



    for result in parsedObject["lines"]:       
        if result["dimensions"] == dimensions:
            if imageType is not None and imageType.lower() in GOES.types:
                if imageType != queryObject["type"]:
                    continue

            if "days" in timeFrame:

                # CHECK FOR MULTIPLE METRICS PASSED - DIE IF SO
                if "hours" in timeFrame or "timeframe" in timeFrame:
                    print("Too many time metrics included in time query! (1 max)")
                    raise Errors.NoValidMatch

                date = parseDateTime(result["date"])
                if date > timeNow - timedelta(days=int(timeFrame["days"])):
                    slides.append(result)

            elif "hours" in timeFrame:
                date = parseDateTime(result["date"])
                if date > timeNow - timedelta(hours=int(timeFrame["hours"])):
                    slides.append(result)   

            elif "timeframe" in timeFrame:
            # [**i**] Users can use DatetimeString() to fill this [**i**]
                date = parseDateTime(result["date"])
                oldest = setDatetimeObj(timeFrame["oldest"])
                newest = setDatetimeObj(timeFrame["newest"])

                if date > oldest:
                    if date < newest:
                        slides.append(result)

            else:
                print("Invalid time object: " + str(timeFrame))
                raise Errors.NoValidMatch    


        masterIndex += 1  
             

    return slides    

    

    
# TODO : Query active storms @ https://www.star.nesdis.noaa.gov/GOES/index.php
# For injecting script into selenium - Returns active browser object
#def scriptInjector(url, javascript):
#    browser = webdriver.Firefox()
#    browser.get(url)
#    browser.execute_script(javascript)
#    return browser

# Main Request Thingy - Don't need webdriver for current functionality: remove this.html.render()
def headlessRequest(url, stream=False, allow_redirects=False):
    return HTMLSession().get(url, headers=generate_navigator(), stream=stream, allow_redirects=allow_redirects)

# Compares our set query against our set dataset then returns the index of the [best] match (if found).
def searchDriver(searchableObject, keepRange, query):

    indexOfFinal = 1000
    query = query.lower()
    AttemptRecursion = keepRange
    contin = True

    # Create attempt cycle based on range
    for attempt in range(keepRange):
        if not contin:
            break

        # Create cycle based on dataset size
        for x in range(len(searchableObject)):
            if not contin:
                break

            #Check for explicit formal name
            for z in range(len(searchableObject[x]["formal-names"])):
                if not contin:
                    break

                if query == searchableObject[x]["formal-names"][z]:
                    indexOfFinal = x
                    contin = False
                    break

                if not contin:
                    break

            if not contin:
                break
            
            # Check for keywords->
            hits = 0
            for y in range(len(searchableObject[x]["keywords"])):
                if not contin:
                    break

                if searchableObject[x]["keywords"][y] in query:
                    if AttemptRecursion is 1:
                        if searchableObject[x]["keywords"][y] != "state" or searchableObject[x]["keywords"][y] != "country":
                            hits += 1
                    else:
                        hits += 1

                if not contin:
                    break   

                # <-Accepting positives if hits >= current $attemptRecursion
                if hits >= AttemptRecursion:
                    indexOfFinal = x
                    contin = False
                    break

            # Adjust our keeprange recursively for next attempt cycle
            AttemptRecursion = keepRange - attempt 
            if AttemptRecursion is 0 or not contin:
                break  

    # Return None if we dont find a match    
    if indexOfFinal is 1000:
        indexOfFinal = None
    
    return indexOfFinal  

def spawnURI(sectorQuery, bandQuery, keywordSearchRangeStart):

    bandQuery = bandQuery.lower()
    sectorQuery = sectorQuery.lower()

    # CHECK FOR QUERY MATCH: SECTORS
    indexOfFinalSector = searchDriver(GOES.sectors, 4, sectorQuery)

    # CHECK FOR QUERY MATCH: BANDS
    indexOfFinalBand = searchDriver(GOES.bands, 4, bandQuery)    


    if indexOfFinalBand is not None:
        if indexOfFinalSector is not None:
            a =  GOES.base_url + "/" + GOES.sectors[indexOfFinalSector]['formal-names'][2]
            a += "/ABI/SECTOR/" + GOES.sectors[indexOfFinalSector]['formal-names'][0] + "/"
            a += GOES.bands[indexOfFinalBand]['formal-names'][0] + "/"
        else:
            a = None
            if DIE_ON_NO_VALID_MATCH:
                print("Failed to find a valid match for: SECTOR ")
            raise Errors.NoValidMatch  
    else:
        a = None 
        if DIE_ON_NO_VALID_MATCH:
            print("Failed to find a valid match for: BAND ")
        raise Errors.NoValidMatch  

    outObj = {"uri": a, "sector-index": indexOfFinalSector, "band-index": indexOfFinalBand}
    return outObj

def RETRIEVE(SECTOR_QUERY, BAND_QUERY):
    uriObj = spawnURI(SECTOR_QUERY, BAND_QUERY, 4)
    request = headlessRequest(uriObj["uri"])
    #request.html.render()
    parsed = parseImages(request, {"band": uriObj["band-index"], "sector": uriObj["sector-index"], "uri": uriObj["uri"]})
    #PIC_TYPE(s): default, banner, cover, thumbnail, latest, unknown
    #Parsed = {"type": "PIC_TYPE", "date": "DATE_UPLOADED", "href": "HREF", "dimensions": [300, 300]}
    return parsed


def downloadImage(uri):
    fname = str(path.basename(urlparse(uri).path))   
    if not path.isfile(fname):
        with open(fname, 'wb') as handle:

            response = headlessRequest(uri, stream=True, allow_redirects=True)

            if not response.ok:
                print("[x] - Failed To Download File\nResponse:"+str(response))
                fname = None
                
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)  

            # REMEMBER FILE FOR LATER TO DELETE    
            temp.stack["cleanup-files"].append(fname)    
                
    return fname

def gatherImages(payload):
    downloaded = []
    for line in payload:
        image = downloadImage(line["full-uri"])
        downloaded.append({"file": image, "meta": line})
    return downloaded   

#Rate in seconds
def multiShow(images):
    while True:
        for image in images:
            this = Image.open(image["file"])
            this.show()
            this.close()

def makegif(images, fileName):

    # overwrites if existing
    if path.isfile(fileName):
        remove(fileName)

    gifStack = []
    for image in images:
        fileHandle = image["file"]
        this = Image.open(fileHandle)  
        gifStack.append(this)  
    
    try:
        gifStack[0].save(
            fileName,
            save_all=True, append_images=gifStack[1:], optimize=False, duration=180, loop=0
        )
    except Exception as f:
        print(str(f) 
        + "Invalid dimensions passed. Try [250, 250] or [500, 500] or "
        + "[1000, 1000] or [2000, 2000].\nI am still working on programatically"
        + " grabbing specific thumbnails etc so default is the only type of image for now."
        )
        fileName = None        

    return fileName

def cleanUp():
    for line in temp.stack["cleanup-files"]:
        try:
            remove(line)
        except Exception as f:
            print(f)
            pass        
        