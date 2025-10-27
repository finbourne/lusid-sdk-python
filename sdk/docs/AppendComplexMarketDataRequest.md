# AppendComplexMarketDataRequest

The details of the point to be appended to a complex market data item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_id** | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | 
**append_market_data** | [**AppendMarketData**](AppendMarketData.md) |  | 
## Example

```python
from lusid.models.append_complex_market_data_request import AppendComplexMarketDataRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

market_data_id: ComplexMarketDataId = # Replace with your value
append_market_data: AppendMarketData = # Replace with your value
append_complex_market_data_request_instance = AppendComplexMarketDataRequest(market_data_id=market_data_id, append_market_data=append_market_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

