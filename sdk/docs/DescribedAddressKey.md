# DescribedAddressKey

An address key with additional data describing what this key is for.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | Address key of some underlying object e.g. Valuation/PV, Instrument/Features | [optional] 
**description** | **str** | Description of the address key. | [optional] 
## Example

```python
from lusid.models.described_address_key import DescribedAddressKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

address_key: Optional[StrictStr] = "example_address_key"
description: Optional[StrictStr] = "example_description"
described_address_key_instance = DescribedAddressKey(address_key=address_key, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

