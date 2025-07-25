# BatchAmendCustomDataModelMembershipResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, MembershipAmendmentResponse]**](MembershipAmendmentResponse.md) |  | [optional] 
**staged** | [**Dict[str, MembershipAmendmentResponse]**](MembershipAmendmentResponse.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) |  | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** |  | [optional] 
## Example

```python
from lusid.models.batch_amend_custom_data_model_membership_response import BatchAmendCustomDataModelMembershipResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, conlist

values: Optional[Dict[str, MembershipAmendmentResponse]] = None
staged: Optional[Dict[str, MembershipAmendmentResponse]] = None
failed: Optional[Dict[str, ErrorDetail]] = None
metadata: Optional[Dict[str, conlist(ResponseMetaData)]] = None
batch_amend_custom_data_model_membership_response_instance = BatchAmendCustomDataModelMembershipResponse(values=values, staged=staged, failed=failed, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

