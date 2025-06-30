# ShareClassDealingBreakdown

The breakdown of Dealing for a Share Class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_dealing** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for any &#39;Dealing&#39; specific to the share class that has occured inside the queried period. | 
**class_dealing_units** | [**Dict[str, Amount]**](Amount.md) | Bucket of detail for any &#39;Dealing&#39; units specific to the share class that has occured inside the queried period. | 
## Example

```python
from lusid.models.share_class_dealing_breakdown import ShareClassDealingBreakdown
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

class_dealing: Dict[str, ShareClassAmount] = # Replace with your value
class_dealing_units: Dict[str, Amount] = # Replace with your value
share_class_dealing_breakdown_instance = ShareClassDealingBreakdown(class_dealing=class_dealing, class_dealing_units=class_dealing_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

