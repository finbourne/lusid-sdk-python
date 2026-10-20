# ResolveWithholdingTaxRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Where the dimension values come from. Raw: from Dimensions. InstrumentResolved: from the instrument, through the configuration&#39;s value sources, as in booking. Available values: Raw, InstrumentResolved. | 
**tax_country** | **str** | The tax country of the holder. It is matched like any other dimension. | 
**profile_type** | **str** | The profile type of the holder. It is matched like any other dimension. | 
**dimensions** | **Dict[str, Optional[str]]** | The value of each matching dimension, keyed by its field name in the rate datasets. A dimension left out is null, as in booking. taxCountry, profileType and ruleSource are not allowed here, and a name that neither dataset matches on is refused. With InstrumentResolved, a value here overrides the derived one, or gives one that the lookup cannot derive (see unresolvedDimensions in the response). | [optional] 
**wht_config** | [**ResourceId**](ResourceId.md) |  | [optional] 
**anomaly_dataset** | [**ResourceId**](ResourceId.md) |  | [optional] 
**main_dataset** | [**ResourceId**](ResourceId.md) |  | [optional] 
**source_priority** | **List[str]** | Optional. The source priority, most preferred first: it replaces the configuration&#39;s, or is used on its own when there is no configuration. An empty list applies no source filter. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The identifiers of the instrument, resolved as for a transaction. Required with InstrumentResolved, not allowed with Raw. | [optional] 
**instrument_scope** | **str** | Optional. The scope to resolve the instrument in, before the default scope. Only with InstrumentResolved. | [optional] 
## Example

```python
from lusid.models.resolve_withholding_tax_request import ResolveWithholdingTaxRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

mode: StrictStr = "example_mode"
tax_country: StrictStr = "example_tax_country"
profile_type: StrictStr = "example_profile_type"
dimensions: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
wht_config: Optional[ResourceId] = # Replace with your value
anomaly_dataset: Optional[ResourceId] = # Replace with your value
main_dataset: Optional[ResourceId] = # Replace with your value
source_priority: Optional[List[StrictStr]] = # Replace with your value
instrument_identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
resolve_withholding_tax_request_instance = ResolveWithholdingTaxRequest(mode=mode, tax_country=tax_country, profile_type=profile_type, dimensions=dimensions, wht_config=wht_config, anomaly_dataset=anomaly_dataset, main_dataset=main_dataset, source_priority=source_priority, instrument_identifiers=instrument_identifiers, instrument_scope=instrument_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

