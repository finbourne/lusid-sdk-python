# QuoteAccessMetadataRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**QuoteAccessMetadataRuleId**](QuoteAccessMetadataRuleId.md) |  | 
**metadata** | **Dict[str, List[AccessMetadataValue]]** | The access control metadata to assign to quotes that match the identifier | 
## Example

```python
from lusid.models.quote_access_metadata_rule import QuoteAccessMetadataRule
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

id: QuoteAccessMetadataRuleId = # Replace with your value
metadata: Dict[str, conlist(AccessMetadataValue)] = # Replace with your value
quote_access_metadata_rule_instance = QuoteAccessMetadataRule(id=id, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

