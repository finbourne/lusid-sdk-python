# JournalEntryLineShareClassBreakdown

The apportionment from overall fund level journal entry Line to the share class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_code** | **str** | The share class identifier. | [optional] 
**apportionment_factor** | **float** | The share class apportionment factor (capital ratio). | [optional] 
**local_value** | **float** | This journal entry line&#39;s local value amount after apportionment is applied. | [optional] 
**base_value** | **float** | This journal entry line&#39;s base value amount after apportionment is applied | [optional] 
## Example

```python
from lusid.models.journal_entry_line_share_class_breakdown import JournalEntryLineShareClassBreakdown
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr

short_code: Optional[StrictStr] = "example_short_code"
apportionment_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
local_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
journal_entry_line_share_class_breakdown_instance = JournalEntryLineShareClassBreakdown(short_code=short_code, apportionment_factor=apportionment_factor, local_value=local_value, base_value=base_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

