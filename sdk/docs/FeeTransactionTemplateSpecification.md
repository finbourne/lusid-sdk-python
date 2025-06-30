# FeeTransactionTemplateSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_type_name** | **str** |  | 
**supported_template_fields** | [**List[TemplateField]**](TemplateField.md) |  | 
## Example

```python
from lusid.models.fee_transaction_template_specification import FeeTransactionTemplateSpecification
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr

specification_type_name: StrictStr = "example_specification_type_name"
supported_template_fields: conlist(TemplateField) = # Replace with your value
fee_transaction_template_specification_instance = FeeTransactionTemplateSpecification(specification_type_name=specification_type_name, supported_template_fields=supported_template_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

