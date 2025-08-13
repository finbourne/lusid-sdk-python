# SettlementConfigurationCategory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The method of settlement for the movements of the relevant type(s). Allowed values: &#39;Automatic&#39; and &#39;Instructed&#39;. A value of &#39;Instructed&#39; means that such movements can only be settled with a SettlementInstruction. A value of &#39;Automatic&#39; means that such movements will settle automatically but a SettlementInstruction will still override automatic settlement. | [optional] 
## Example

```python
from lusid.models.settlement_configuration_category import SettlementConfigurationCategory
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

method: Optional[StrictStr] = "example_method"
settlement_configuration_category_instance = SettlementConfigurationCategory(method=method)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

