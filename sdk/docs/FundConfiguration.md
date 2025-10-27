# FundConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the FundConfiguration. | [optional] 
**description** | **str** | A description for the FundConfiguration. | [optional] 
**dealing_filters** | [**List[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the dealing. | [optional] 
**pnl_filters** | [**List[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the PnL. | [optional] 
**back_out_filters** | [**List[ComponentFilter]**](ComponentFilter.md) | The set of filters used to decide which JE lines are included in the back outs. | [optional] 
**external_fee_filters** | [**List[ExternalFeeComponentFilter]**](ExternalFeeComponentFilter.md) | The set of filters used to decide which JE lines are used for inputting fees from an external source. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the Fund Configuration. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fund_configuration import FundConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
dealing_filters: Optional[List[ComponentFilter]] = # Replace with your value
pnl_filters: Optional[List[ComponentFilter]] = # Replace with your value
back_out_filters: Optional[List[ComponentFilter]] = # Replace with your value
external_fee_filters: Optional[List[ExternalFeeComponentFilter]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
fund_configuration_instance = FundConfiguration(href=href, id=id, display_name=display_name, description=description, dealing_filters=dealing_filters, pnl_filters=pnl_filters, back_out_filters=back_out_filters, external_fee_filters=external_fee_filters, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

