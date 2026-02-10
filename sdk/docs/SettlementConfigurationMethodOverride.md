# SettlementConfigurationMethodOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | Property Key to override the settlement method. Allowed values: &#39;Automatic&#39;, &#39;Instructed&#39; and &#39;Default&#39;, property key must be in the &#39;Transaction&#39; domain. For a derived property keys, the derivation formula should resolve one of the of the allowed values. &#39;Default&#39; will be treated the same as no or an invalid derived value, will fall back to use the regular settlement method. | 
## Example

```python
from lusid.models.settlement_configuration_method_override import SettlementConfigurationMethodOverride
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
settlement_configuration_method_override_instance = SettlementConfigurationMethodOverride(property_key=property_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

