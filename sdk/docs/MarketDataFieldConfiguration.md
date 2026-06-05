# MarketDataFieldConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_data_category** | **str** | The category of market data this configuration applies to. Available values: Quote, Complex. | 
**scope** | **str** | The scope of the market data field configuration. | 
**metadata_field_schema** | [**List[MetadataFieldDefinition]**](MetadataFieldDefinition.md) | The metadata field definitions for this configuration. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.market_data_field_configuration import MarketDataFieldConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

market_data_category: StrictStr = "example_market_data_category"
scope: StrictStr = "example_scope"
metadata_field_schema: List[MetadataFieldDefinition] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[List[Link]] = None
market_data_field_configuration_instance = MarketDataFieldConfiguration(market_data_category=market_data_category, scope=scope, metadata_field_schema=metadata_field_schema, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

