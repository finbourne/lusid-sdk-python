# PackageSetRequest

A request to create or update multiple Packages.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PackageRequest]**](PackageRequest.md) | A collection of PackageRequests. | [optional] 
## Example

```python
from lusid.models.package_set_request import PackageSetRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

requests: Optional[conlist(PackageRequest)] = # Replace with your value
package_set_request_instance = PackageSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

