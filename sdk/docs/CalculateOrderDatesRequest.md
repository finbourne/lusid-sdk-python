# CalculateOrderDatesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifier_type** | **str** |  | 
**instrument_identifier** | **str** |  | 
**instrument_scope** | **str** |  | [optional] 
**received_date** | **datetime** |  | [optional] 
**price_date** | **datetime** |  | [optional] 
**transaction_category** | **str** |  | [optional] 
**liquidating_share_class_identifier** | **str** |  | [optional] 
**liquidating_share_class_identifier_type** | **str** |  | [optional] 
**liquidating_share_class_instrument_scope** | **str** |  | [optional] 
## Example

```python
from lusid.models.calculate_order_dates_request import CalculateOrderDatesRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifier_type: StrictStr = "example_instrument_identifier_type"
instrument_identifier: StrictStr = "example_instrument_identifier"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
received_date: Optional[datetime] = # Replace with your value
price_date: Optional[datetime] = # Replace with your value
transaction_category: Optional[StrictStr] = "example_transaction_category"
liquidating_share_class_identifier: Optional[StrictStr] = "example_liquidating_share_class_identifier"
liquidating_share_class_identifier_type: Optional[StrictStr] = "example_liquidating_share_class_identifier_type"
liquidating_share_class_instrument_scope: Optional[StrictStr] = "example_liquidating_share_class_instrument_scope"
calculate_order_dates_request_instance = CalculateOrderDatesRequest(instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, instrument_scope=instrument_scope, received_date=received_date, price_date=price_date, transaction_category=transaction_category, liquidating_share_class_identifier=liquidating_share_class_identifier, liquidating_share_class_identifier_type=liquidating_share_class_identifier_type, liquidating_share_class_instrument_scope=liquidating_share_class_instrument_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

