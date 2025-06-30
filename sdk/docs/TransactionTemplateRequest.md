# TransactionTemplateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the transaction template. | 
**component_transactions** | [**List[ComponentTransaction]**](ComponentTransaction.md) | A set of component transactions that relate to the template to be created. | 
## Example

```python
from lusid.models.transaction_template_request import TransactionTemplateRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr

description: StrictStr = "example_description"
component_transactions: conlist(ComponentTransaction) = # Replace with your value
transaction_template_request_instance = TransactionTemplateRequest(description=description, component_transactions=component_transactions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

