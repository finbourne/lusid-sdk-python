# InvestmentAccount

Representation of an Investment Account on the LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope in which the Investment Account lies. | [optional] 
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Unique client-defined identifiers of the Investment Account. | [optional] 
**display_name** | **str** | The display name of the Investment Account | [optional] 
**description** | **str** | The description of the Investment Account | [optional] 
**account_type** | **str** | The type of the of the Investment Account. | [optional] 
**account_holders** | [**List[AccountHolder]**](AccountHolder.md) | The Account Holders of the Investment Account. | [optional] 
**investment_portfolios** | [**List[InvestmentPortfolio]**](InvestmentPortfolio.md) | The Investment Portfolios of the Investment Account. | [optional] 
**lusid_investment_account_id** | **str** | The unique LUSID Investment Account Identifier of the Investment Account. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties associated to the Investment Account. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the Investment Account. | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.investment_account import InvestmentAccount
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

scope: Optional[StrictStr] = "example_scope"
identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
account_type: Optional[StrictStr] = "example_account_type"
account_holders: Optional[conlist(AccountHolder)] = # Replace with your value
investment_portfolios: Optional[conlist(InvestmentPortfolio)] = # Replace with your value
lusid_investment_account_id: Optional[StrictStr] = "example_lusid_investment_account_id"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
relationships: Optional[conlist(Relationship)] = # Replace with your value
href: Optional[StrictStr] = "example_href"
version: Optional[Version] = None
links: Optional[conlist(Link)] = None
investment_account_instance = InvestmentAccount(scope=scope, identifiers=identifiers, display_name=display_name, description=description, account_type=account_type, account_holders=account_holders, investment_portfolios=investment_portfolios, lusid_investment_account_id=lusid_investment_account_id, properties=properties, relationships=relationships, href=href, version=version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

