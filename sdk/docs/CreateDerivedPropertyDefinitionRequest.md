# CreateDerivedPropertyDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. Not all available values are currently supported, please check the documentation: https://support.lusid.com/knowledgebase/article/KA-01719/. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, Abor, AborConfiguration, Fund, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**property_description** | **str** | Describes the property | [optional] 
**derivation_formula** | **str** | The rule that defines how data is composed for a derived property. | 

## Example

```python
from lusid.models.create_derived_property_definition_request import CreateDerivedPropertyDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDerivedPropertyDefinitionRequest from a JSON string
create_derived_property_definition_request_instance = CreateDerivedPropertyDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateDerivedPropertyDefinitionRequest.to_json()

# convert the object into a dict
create_derived_property_definition_request_dict = create_derived_property_definition_request_instance.to_dict()
# create an instance of CreateDerivedPropertyDefinitionRequest from a dict
create_derived_property_definition_request_form_dict = create_derived_property_definition_request.from_dict(create_derived_property_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


