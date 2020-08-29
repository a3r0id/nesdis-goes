
class Errors:

    class Error(Exception):
        """NESDIS Crawler Exception"""
        pass

    class NoValidMatch(Error):
        """No explicit/implicit match found in query using provided keyword!"""
        pass