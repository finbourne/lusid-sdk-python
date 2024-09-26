from typing import Optional

class ConfigurationOptions:
    
    def __init__(
        self, 
        total_timeout_ms: Optional[int] = None, 
        connect_timeout_ms: Optional[int] = None, 
        read_timeout_ms: Optional[int] = None, 
        rate_limit_retries: Optional[int] = None
    ):
        self.total_timeout_ms = total_timeout_ms
        self.connect_timeout_ms = connect_timeout_ms
        self.read_timeout_ms = read_timeout_ms
        self.rate_limit_retries = rate_limit_retries
        
    @property
    def total_timeout_ms(self):
        return self.__total_timeout_ms

    @total_timeout_ms.setter
    def total_timeout_ms(self, value):
        if value:
            if not isinstance(value, int):
                raise TypeError(f"total_timeout_ms must be type int but type '{type(value)}' used")
            if value < 0:
                raise ValueError(f"total_timeout_ms must be an integer greater than or equal to zero")
        self.__total_timeout_ms = value

    @property
    def connect_timeout_ms(self):
        return self.__connect_timeout_ms

    @connect_timeout_ms.setter
    def connect_timeout_ms(self, value):
        if value:
            if not isinstance(value, int):
                raise TypeError(f"connect_timeout_ms must be type int but type '{type(value)}' used")
            if value < 0:
                raise ValueError(f"connect_timeout_ms must be an integer greater than or equal to zero")
        self.__connect_timeout_ms = value

    @property
    def read_timeout_ms(self):
        return self.__read_timeout_ms

    @read_timeout_ms.setter
    def read_timeout_ms(self, value):
        if value:
            if not isinstance(value, int):
                raise TypeError(f"read_timeout_ms must be type int but type '{type(value)}' used")
            if value < 0:
                raise ValueError(f"read_timeout_ms must be an integer greater than or equal to zero")
        self.__read_timeout_ms = value

    @property
    def rate_limit_retries(self):
        return self.__rate_limit_retries

    @rate_limit_retries.setter
    def rate_limit_retries(self, value):
        if value:
            if not isinstance(value, int):
                raise TypeError(f"rate_limit_retries must be type int but type '{type(value)}' used")
            if value < 0:
                raise ValueError(f"rate_limit_retries must be an integer greater than or equal to zero")
        self.__rate_limit_retries = value