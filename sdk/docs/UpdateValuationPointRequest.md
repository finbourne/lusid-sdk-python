# UpdateValuationPointRequest

A definition for the period you wish to close
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valuation_point_code** | **str** | Unique code for the Valuation Point. | 
**variant** | **str** | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. | [optional] 
**name** | **str** | Identifiable Name assigned to the Valuation Point. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the diary entry. | [optional] 
**apply_clear_down** | **bool** | Defaults to null. Set to true if you want the closed period to have the clear down applied. | [optional] 
**update_inclusion_date_nav_adjustments** | **bool** | Defaults to null. Set to true if you have the required licence and want the InclusionDate property values to be used to determine whether items should be automatically included in the post close activities. | [optional] 
## Example

```python
from lusid.models.update_valuation_point_request import UpdateValuationPointRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

valuation_point_code: StrictStr = "example_valuation_point_code"
variant: Optional[StrictStr] = "example_variant"
name: Optional[StrictStr] = "example_name"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
apply_clear_down: Optional[StrictBool] = # Replace with your value
apply_clear_down:Optional[StrictBool] = None
update_inclusion_date_nav_adjustments: Optional[StrictBool] = # Replace with your value
update_inclusion_date_nav_adjustments:Optional[StrictBool] = None
update_valuation_point_request_instance = UpdateValuationPointRequest(valuation_point_code=valuation_point_code, variant=variant, name=name, properties=properties, apply_clear_down=apply_clear_down, update_inclusion_date_nav_adjustments=update_inclusion_date_nav_adjustments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

