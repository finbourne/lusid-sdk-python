# InstrumentDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instrument. | 
**identifiers** | [**Dict[str, InstrumentIdValue]**](InstrumentIdValue.md) | A set of identifiers that can be used to identify the instrument. At least one of these must be configured to be a unique identifier. | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | Set of unique instrument properties and associated values to store with the instrument. Each property must be from the &#39;Instrument&#39; domain. | [optional] 
**look_through_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**settlement_cycle** | [**SettlementCycle**](SettlementCycle.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_definition import InstrumentDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

name: StrictStr = "example_name"
identifiers: Dict[str, InstrumentIdValue] = # Replace with your value
properties: Optional[conlist(ModelProperty)] = # Replace with your value
look_through_portfolio_id: Optional[ResourceId] = # Replace with your value
definition: Optional[LusidInstrument] = None
settlement_cycle: Optional[SettlementCycle] = # Replace with your value
instrument_definition_instance = InstrumentDefinition(name=name, identifiers=identifiers, properties=properties, look_through_portfolio_id=look_through_portfolio_id, definition=definition, settlement_cycle=settlement_cycle)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

