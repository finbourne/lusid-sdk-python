# UpsertLegalEntityAccessMetadataRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[AccessMetadataValue]**](AccessMetadataValue.md) | The access control metadata to assign to a Legal Entity that matches the identifier | [optional] 
## Example

```python
from lusid.models.upsert_legal_entity_access_metadata_request import UpsertLegalEntityAccessMetadataRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

metadata: Optional[conlist(AccessMetadataValue)] = # Replace with your value
upsert_legal_entity_access_metadata_request_instance = UpsertLegalEntityAccessMetadataRequest(metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

