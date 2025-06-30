# Instrument

A list of instruments.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**scope** | **str** | The scope in which the instrument lies. | [optional] 
**lusid_instrument_id** | **str** | The unique LUSID Instrument Identifier (LUID) of the instrument. | 
**version** | [**Version**](Version.md) |  | 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**name** | **str** | The name of the instrument. | 
**identifiers** | **Dict[str, str]** | The set of identifiers that can be used to identify the instrument. | 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The requested instrument properties. These will be from the &#39;Instrument&#39; domain. | [optional] 
**lookthrough_portfolio** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_definition** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**state** | **str** | The state of of the instrument at the asAt datetime of this version of the instrument definition. The available values are: Active, Inactive, Deleted | 
**asset_class** | **str** | The nominal asset class of the instrument, e.g. InterestRates, FX, Inflation, Equities, Credit, Commodities, etc. The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown | [optional] 
**dom_ccy** | **str** | The domestic currency, meaning the currency in which the instrument would typically be expected to pay cashflows, e.g. a share in AAPL being USD. | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the instrument. | [optional] 
**settlement_cycle** | [**SettlementCycle**](SettlementCycle.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument import Instrument
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

href: Optional[StrictStr] = "example_href"
scope: Optional[StrictStr] = "example_scope"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
version: Version = # Replace with your value
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
name: StrictStr = "example_name"
identifiers: Dict[str, StrictStr] = # Replace with your value
properties: Optional[conlist(ModelProperty)] = # Replace with your value
lookthrough_portfolio: Optional[ResourceId] = # Replace with your value
instrument_definition: Optional[LusidInstrument] = # Replace with your value
state: StrictStr = "example_state"
asset_class: Optional[StrictStr] = "example_asset_class"
dom_ccy: Optional[StrictStr] = "example_dom_ccy"
relationships: Optional[conlist(Relationship)] = # Replace with your value
settlement_cycle: Optional[SettlementCycle] = # Replace with your value
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[conlist(Link)] = None
instrument_instance = Instrument(href=href, scope=scope, lusid_instrument_id=lusid_instrument_id, version=version, staged_modifications=staged_modifications, name=name, identifiers=identifiers, properties=properties, lookthrough_portfolio=lookthrough_portfolio, instrument_definition=instrument_definition, state=state, asset_class=asset_class, dom_ccy=dom_ccy, relationships=relationships, settlement_cycle=settlement_cycle, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

