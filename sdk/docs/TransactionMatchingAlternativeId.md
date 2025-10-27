# TransactionMatchingAlternativeId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | An property key (from the &#39;Transaction&#39; domain) that can be used as an alternative to TransactionId when matching transactions to settlement instructions. This property must be pre-defined and must be present on the transaction in order to be used for matching. | 
## Example

```python
from lusid.models.transaction_matching_alternative_id import TransactionMatchingAlternativeId
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
transaction_matching_alternative_id_instance = TransactionMatchingAlternativeId(property_key=property_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

