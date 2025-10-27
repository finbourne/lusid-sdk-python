# FeeTransactionTemplateSpecification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_type_name** | **str** |  | 
**supported_template_fields** | [**List[TemplateField]**](TemplateField.md) |  | 
## Example

```python
from lusid.models.fee_transaction_template_specification import FeeTransactionTemplateSpecification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

specification_type_name: StrictStr = "example_specification_type_name"
supported_template_fields: List[TemplateField] = # Replace with your value
fee_transaction_template_specification_instance = FeeTransactionTemplateSpecification(specification_type_name=specification_type_name, supported_template_fields=supported_template_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

