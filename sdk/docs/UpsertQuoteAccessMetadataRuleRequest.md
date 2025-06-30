# UpsertQuoteAccessMetadataRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**QuoteAccessMetadataRuleId**](QuoteAccessMetadataRuleId.md) |  | 
**metadata** | **Dict[str, List[AccessMetadataValue]]** | The access control metadata to assign to quotes that match the identifier | 
## Example

```python
from lusid.models.upsert_quote_access_metadata_rule_request import UpsertQuoteAccessMetadataRuleRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

id: QuoteAccessMetadataRuleId = # Replace with your value
metadata: Dict[str, conlist(AccessMetadataValue)] = # Replace with your value
upsert_quote_access_metadata_rule_request_instance = UpsertQuoteAccessMetadataRuleRequest(id=id, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

