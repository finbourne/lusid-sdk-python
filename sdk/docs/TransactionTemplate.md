# TransactionTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | A value that represents the instrument type. | 
**instrument_event_type** | **str** | A value that represents the instrument event type. | 
**description** | **str** | The description of the transaction template. | 
**scope** | **str** | The scope in which the transaction template resides. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the template to be created. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transaction_template import TransactionTemplate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_type: StrictStr = "example_instrument_type"
instrument_event_type: StrictStr = "example_instrument_event_type"
description: StrictStr = "example_description"
scope: StrictStr = "example_scope"
component_transactions: List[ComponentTransaction] = # Replace with your value
links: Optional[List[Link]] = None
transaction_template_instance = TransactionTemplate(instrument_type=instrument_type, instrument_event_type=instrument_event_type, description=description, scope=scope, component_transactions=component_transactions, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

