# DataModelMembership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership** | [**List[Membership]**](Membership.md) | The collection of data models this entity is a member of. | 
**current_model** | [**MembershipAndStatus**](MembershipAndStatus.md) |  | [optional] 
## Example

```python
from lusid.models.data_model_membership import DataModelMembership
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

membership: conlist(Membership) = # Replace with your value
current_model: Optional[MembershipAndStatus] = # Replace with your value
data_model_membership_instance = DataModelMembership(membership=membership, current_model=current_model)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

