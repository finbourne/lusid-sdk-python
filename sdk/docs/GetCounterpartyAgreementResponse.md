# GetCounterpartyAgreementResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**value** | [**CounterpartyAgreement**](CounterpartyAgreement.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The counterparty agreement that could not be retrieved along with a reason for failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_counterparty_agreement_response import GetCounterpartyAgreementResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
value: Optional[CounterpartyAgreement] = None
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
get_counterparty_agreement_response_instance = GetCounterpartyAgreementResponse(href=href, value=value, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

