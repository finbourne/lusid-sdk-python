# LineageMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index to demonstrate position of lineage member in overall lineage | 
**label** | **str** | Label of the step corresponding to this lineage member | 
**sub_label** | **str** | SubLabel of the step corresponding to this lineage member | 
**info_type** | **str** | Optional. Type of Information | [optional] 
**information** | **str** | Optional. Information for the step corresponding to this lineage member, of type InfoType | [optional] 
## Example

```python
from lusid.models.lineage_member import LineageMember
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, constr

index: StrictInt = # Replace with your value
index: StrictInt = 42
label: StrictStr = "example_label"
sub_label: StrictStr = "example_sub_label"
info_type: Optional[StrictStr] = "example_info_type"
information: Optional[StrictStr] = "example_information"
lineage_member_instance = LineageMember(index=index, label=label, sub_label=sub_label, info_type=info_type, information=information)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

