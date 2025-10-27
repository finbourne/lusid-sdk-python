# Reconciliation

Representation of Reconciliation in LUSID Api
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ReconciliationId**](ReconciliationId.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**name** | **str** | The name of the scheduled reconciliation | [optional] 
**description** | **str** | A description of the scheduled reconciliation | [optional] 
**is_portfolio_group** | **bool** | Specifies whether reconciliation is between portfolios or portfolio groups | [optional] 
**left** | [**ResourceId**](ResourceId.md) |  | [optional] 
**right** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transactions** | [**ReconciliationTransactions**](ReconciliationTransactions.md) |  | [optional] 
**positions** | [**ReconciliationConfiguration**](ReconciliationConfiguration.md) |  | [optional] 
**valuations** | [**ReconciliationConfiguration**](ReconciliationConfiguration.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Reconciliation properties | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.reconciliation import Reconciliation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ReconciliationId] = None
href: Optional[StrictStr] = "example_href"
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
is_portfolio_group: Optional[StrictBool] = # Replace with your value
is_portfolio_group:Optional[StrictBool] = None
left: Optional[ResourceId] = None
right: Optional[ResourceId] = None
transactions: Optional[ReconciliationTransactions] = None
positions: Optional[ReconciliationConfiguration] = None
valuations: Optional[ReconciliationConfiguration] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
links: Optional[List[Link]] = None
reconciliation_instance = Reconciliation(id=id, href=href, name=name, description=description, is_portfolio_group=is_portfolio_group, left=left, right=right, transactions=transactions, positions=positions, valuations=valuations, properties=properties, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

