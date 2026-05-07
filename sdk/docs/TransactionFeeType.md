# TransactionFeeType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | The display name of the transaction fee type. | [optional] 
**description** | **str** | A description of the transaction fee type. | [optional] 
**calculation** | [**FeeCalculationRequest**](FeeCalculationRequest.md) |  | [optional] 
**condition** | **str** | The condition that the transaction must meet in order for the fee to be applied. | [optional] 
**txn_property_key** | **str** | The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the transaction fee type. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**is_active** | **bool** | Indicates whether the transaction fee type is currently active and should be applied to transactions. Optional when creating a transaction fee type, defaults to true, if a value is not provided. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.transaction_fee_type import TransactionFeeType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ResourceId] = None
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
calculation: Optional[FeeCalculationRequest] = None
condition: Optional[StrictStr] = "example_condition"
txn_property_key: Optional[StrictStr] = "example_txn_property_key"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
href: Optional[StrictStr] = "example_href"
is_active: Optional[StrictBool] = # Replace with your value
is_active:Optional[StrictBool] = None
links: Optional[List[Link]] = None
transaction_fee_type_instance = TransactionFeeType(id=id, display_name=display_name, description=description, calculation=calculation, condition=condition, txn_property_key=txn_property_key, properties=properties, version=version, href=href, is_active=is_active, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

