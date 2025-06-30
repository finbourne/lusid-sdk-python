# ReferenceList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_list_type** | **str** | The reference list values. The available values are: PortfolioGroupIdList, PortfolioIdList, AddressKeyList, StringList, InstrumentList, DecimalList, PropertyList, FundIdList | 
## Example

```python
from lusid.models.reference_list import ReferenceList
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

reference_list_type: StrictStr = "example_reference_list_type"
reference_list_instance = ReferenceList(reference_list_type=reference_list_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

