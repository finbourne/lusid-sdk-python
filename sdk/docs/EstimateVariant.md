# EstimateVariant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | **str** | The Variant of the Calendar Entry. Together with the valuation point code marks the unique branch for the NavType. | [optional] 
**display_name** | **str** | The name of the Fund Calendar entry. | 
**description** | **str** | A description for the Fund Calendar entry. | [optional] 
**as_at** | **datetime** | The asAt datetime for the Calendar Entry. | 
**holdings_as_at_override** | **datetime** | The optional AsAt Override to use for building holdings in the Valuation Point. Defaults to Latest. | [optional] 
**valuations_as_at_override** | **datetime** | The optional AsAt Override to use for performing valuations in the Valuation Point. Defaults to Latest. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties for the Calendar Entry. These will be from the &#39;ClosedPeriod&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | 
## Example

```python
from lusid.models.estimate_variant import EstimateVariant
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

variant: Optional[StrictStr] = "example_variant"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
as_at: datetime = # Replace with your value
holdings_as_at_override: Optional[datetime] = # Replace with your value
valuations_as_at_override: Optional[datetime] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Version
estimate_variant_instance = EstimateVariant(variant=variant, display_name=display_name, description=description, as_at=as_at, holdings_as_at_override=holdings_as_at_override, valuations_as_at_override=valuations_as_at_override, properties=properties, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

