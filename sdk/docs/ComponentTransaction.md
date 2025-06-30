# ComponentTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**condition** | **str** |  | [optional] 
**transaction_field_map** | [**TransactionFieldMap**](TransactionFieldMap.md) |  | 
**transaction_property_map** | [**List[TransactionPropertyMap]**](TransactionPropertyMap.md) |  | 
**preserve_tax_lot_structure** | **bool** | Controls if tax lot structure should be preserved when cost base is transferred to a new holding. For example in Spin Off instrument events. | [optional] 
**market_open_time_adjustments** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.component_transaction import ComponentTransaction
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr

display_name: StrictStr = "example_display_name"
condition: Optional[StrictStr] = "example_condition"
transaction_field_map: TransactionFieldMap = # Replace with your value
transaction_property_map: conlist(TransactionPropertyMap) = # Replace with your value
preserve_tax_lot_structure: Optional[StrictBool] = # Replace with your value
preserve_tax_lot_structure:Optional[StrictBool] = None
market_open_time_adjustments: Optional[conlist(StrictStr)] = # Replace with your value
component_transaction_instance = ComponentTransaction(display_name=display_name, condition=condition, transaction_field_map=transaction_field_map, transaction_property_map=transaction_property_map, preserve_tax_lot_structure=preserve_tax_lot_structure, market_open_time_adjustments=market_open_time_adjustments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

