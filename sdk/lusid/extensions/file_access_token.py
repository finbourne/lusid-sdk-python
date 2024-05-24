import collections
import datetime
import logging

logger = logging.getLogger(__name__)


class FileAccessToken(collections.UserString):
    """Loads access token from file when requested
    Acts as a string so can be concatenated to auth headers
    """

    def __init__(self, access_token_location: str, expiry_time:int = 120):
        if access_token_location is None or access_token_location == "":
            raise ValueError("access_token_location must be a non-empty string")
        self.__access_token_location = access_token_location
        self.__expiry_time = expiry_time 
        self.__token_data = {
            "expires": datetime.datetime.now(),
            "current_access_token": "",
        }

    @property
    def data(self) -> str:
        """load access token from file

        Returns
        -------
        str
            Access token
        """
        if self.__token_data["expires"] <= datetime.datetime.now():
            try:
                with open(self.__access_token_location, "r") as access_token_file:
                    self.__token_data["current_access_token"] = access_token_file.read()
                self.__token_data["expires"] = (
                    datetime.datetime.now() + datetime.timedelta(seconds=self.__expiry_time)
                )
            except OSError:
                logger.error("Could not open access token file")
                raise
        return self.__token_data["current_access_token"]
