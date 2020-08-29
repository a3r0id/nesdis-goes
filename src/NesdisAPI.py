from NesdisFunctions import getDefaultSlidesByTimeframe, RETRIEVE, multiShow, makegif, cleanUp, gatherImages

# [**i**] LIBRARY TO GRACEFULLY SCRAPE PUBLIC SATELLITE IMAGERY FROM https://star.nesdis.noaa.gov [**i**]
# Python API By github.com/aerobotpro

# API v1
class nesdis(object):   
     
    # MAIN OBJECT
    def __init__(self, QUERY):
        self.query = QUERY  

        # GET SLDES BY TIMEFRAME
        self.job = getDefaultSlidesByTimeframe(RETRIEVE(QUERY["sector"], QUERY["band"]), self.query)

        # SET PAYLOAD WITH COMPLETED JOB
        self.payload = self.job  

    # Show each image received, will cause issues if many results    
    def showimages(self):
        multiShow(gatherImages(self.payload))

    # Make GIF image with results
    def makeGif(self, fileName):
        makegif(gatherImages(self.payload), fileName)

    # Delete all downloaded images, besides created images
    def cleanUp(self):
        cleanUp()  