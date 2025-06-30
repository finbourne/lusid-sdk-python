# AborConfigurationRequest

The request used to create an AborConfiguration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code given for the Abor Configuration. | 
**display_name** | **str** | The name of the Abor Configuration. | [optional] 
**description** | **str** | A description for the Abor Configuration. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**chart_of_accounts_id** | [**ResourceId**](ResourceId.md) |  | 
**posting_module_codes** | **List[str]** | The Posting Module Codes from which the rules to be applied are retrieved. | [optional] 
**cleardown_module_codes** | **List[str]** | The Cleardown Module Codes from which the rules to be applied are retrieved. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Abor Configuration. | [optional] 
## Example

```python
from lusid.models.abor_configuration_request import AborConfigurationRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

code: StrictStr = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
recipe_id: ResourceId = # Replace with your value
chart_of_accounts_id: ResourceId = # Replace with your value
posting_module_codes: Optional[conlist(StrictStr)] = # Replace with your value
cleardown_module_codes: Optional[conlist(StrictStr)] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
abor_configuration_request_instance = AborConfigurationRequest(code=code, display_name=display_name, description=description, recipe_id=recipe_id, chart_of_accounts_id=chart_of_accounts_id, posting_module_codes=posting_module_codes, cleardown_module_codes=cleardown_module_codes, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

