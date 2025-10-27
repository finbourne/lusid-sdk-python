# UpdateCheckDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Check Definition. | 
**description** | **str** | A description for the Check Definition. | 
**dataset_schema** | [**CheckDefinitionDatasetSchema**](CheckDefinitionDatasetSchema.md) |  | [optional] 
**rule_sets** | [**List[CheckDefinitionRuleSet]**](CheckDefinitionRuleSet.md) | A collection of rule sets for the Check Definition. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Check Definition. | [optional] 
## Example

```python
from lusid.models.update_check_definition_request import UpdateCheckDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
dataset_schema: Optional[CheckDefinitionDatasetSchema] = # Replace with your value
rule_sets: List[CheckDefinitionRuleSet] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
update_check_definition_request_instance = UpdateCheckDefinitionRequest(display_name=display_name, description=description, dataset_schema=dataset_schema, rule_sets=rule_sets, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

