# PackageSetRequest

A request to create or update multiple Packages.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PackageRequest]**](PackageRequest.md) | A collection of PackageRequests. | [optional] 
## Example

```python
from lusid.models.package_set_request import PackageSetRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

requests: Optional[List[PackageRequest]] = # Replace with your value
package_set_request_instance = PackageSetRequest(requests=requests)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

