# ListComplexMarketDataWithMetaDataResponse

Wraps a ComplexMarketData object with information that was retrieved from storage with it.  In particular,  the scope that the data was stored in,  and an object identifying the market data in that scope.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the listed ComplexMarketData entity is stored in. | [optional] 
**market_data_id** | [**ComplexMarketDataId**](ComplexMarketDataId.md) |  | [optional] 
**market_data** | [**ComplexMarketData**](ComplexMarketData.md) |  | [optional] 
## Example

```python
from lusid.models.list_complex_market_data_with_meta_data_response import ListComplexMarketDataWithMetaDataResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: Optional[StrictStr] = "example_scope"
market_data_id: Optional[ComplexMarketDataId] = # Replace with your value
market_data: Optional[ComplexMarketData] = # Replace with your value
list_complex_market_data_with_meta_data_response_instance = ListComplexMarketDataWithMetaDataResponse(scope=scope, market_data_id=market_data_id, market_data=market_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

