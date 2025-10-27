# UpsertComplexMarketDataRequest

The details of the complex market data item to upsert into Lusid.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_id** | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | 
**market_data** | [**ComplexMarketData**](ComplexMarketData.md) |  | 
## Example

```python
from lusid.models.upsert_complex_market_data_request import UpsertComplexMarketDataRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

market_data_id: ComplexMarketDataId = # Replace with your value
market_data: ComplexMarketData = # Replace with your value
upsert_complex_market_data_request_instance = UpsertComplexMarketDataRequest(market_data_id=market_data_id, market_data=market_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

