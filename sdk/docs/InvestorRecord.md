# InvestorRecord

Representation of an Investor Record on the LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_investor_record_id** | **str** | The unique LUSID Investor Record Identifier of the Investor Record. | [optional] 
**display_name** | **str** | The display name of the Investor Record | [optional] 
**description** | **str** | The description of the Investor Record | [optional] 
**investor** | [**Investor**](Investor.md) |  | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investor Record. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investor Record. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Investor Record. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.investor_record import InvestorRecord
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

lusid_investor_record_id: Optional[StrictStr] = "example_lusid_investor_record_id"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
investor: Optional[Investor] = None
identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
relationships: Optional[conlist(Relationship)] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
investor_record_instance = InvestorRecord(lusid_investor_record_id=lusid_investor_record_id, display_name=display_name, description=description, investor=investor, identifiers=identifiers, properties=properties, relationships=relationships, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

