# WithholdingTaxConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**anomaly_dataset** | [**ResourceId**](ResourceId.md) |  | 
**main_dataset** | [**ResourceId**](ResourceId.md) |  | 
**source_priority** | **List[str]** | The rule sources in priority order, most preferred first. Optional: a single-source customer configures none and leaves ruleSource blank on every rate row, in which case no source filter is applied and specificity alone decides. | [optional] 
**value_sources** | [**List[WithholdingTaxValueSource]**](WithholdingTaxValueSource.md) | One declaration per customer-defined matching dimension across both datasets, naming where the engine reads that dimension&#39;s value from. A dataset column name cannot imply a storage location, so a declaration is required for every customer dimension: an unmapped dimension is never supplied by the matching request, so no row ever matches on it and the customer silently gets a broader rate than they configured. No declaration is required for taxCountry or profileType, which the engine fills from the waterfall, nor for ruleSource, which is compared against SourcePriority. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.withholding_tax_configuration import WithholdingTaxConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
id: ResourceId
anomaly_dataset: ResourceId = # Replace with your value
main_dataset: ResourceId = # Replace with your value
source_priority: Optional[List[StrictStr]] = # Replace with your value
value_sources: Optional[List[WithholdingTaxValueSource]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
withholding_tax_configuration_instance = WithholdingTaxConfiguration(href=href, id=id, anomaly_dataset=anomaly_dataset, main_dataset=main_dataset, source_priority=source_priority, value_sources=value_sources, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

