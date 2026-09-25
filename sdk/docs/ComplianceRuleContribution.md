# ComplianceRuleContribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The position of this contribution within the compliance run. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument** | **str** | The LUSID instrument identifier (LUID) of the instrument for this contribution. | 
**instrument_type** | **str** | Optional. The economic type of the instrument for this contribution. | [optional] 
**holding_type** | **str** | Optional. The holding type of this contribution. | [optional] 
**holding_id** | **str** | Optional. The internal holding identifier encoding the detail of what the holding includes. | [optional] 
**result_values** | **Dict[str, float]** | Dictionary of AddressKey (as string) and their corresponding decimal valuation results for this contribution. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Dictionary of PropertyKey (as string) and their corresponding property for this contribution. | 
**related_properties** | **Dict[str, Optional[str]]** | Dictionary of related property keys (as string) and their string values, read from related entities across a relationship. | 
## Example

```python
from lusid.models.compliance_rule_contribution import ComplianceRuleContribution
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

index: StrictInt = # Replace with your value
index: StrictInt = 42
portfolio_id: ResourceId = # Replace with your value
order_id: Optional[ResourceId] = # Replace with your value
instrument: StrictStr = "example_instrument"
instrument_type: Optional[StrictStr] = "example_instrument_type"
holding_type: Optional[StrictStr] = "example_holding_type"
holding_id: Optional[StrictStr] = "example_holding_id"
result_values: Dict[str, Union[StrictFloat, StrictInt]] = # Replace with your value
properties: Dict[str, ModelProperty] = # Replace with your value
related_properties: Dict[str, Optional[StrictStr]] = # Replace with your value
compliance_rule_contribution_instance = ComplianceRuleContribution(index=index, portfolio_id=portfolio_id, order_id=order_id, instrument=instrument, instrument_type=instrument_type, holding_type=holding_type, holding_id=holding_id, result_values=result_values, properties=properties, related_properties=related_properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

