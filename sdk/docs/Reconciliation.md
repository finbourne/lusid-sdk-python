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

# TODO update the JSON string below
json = "{}"
# create an instance of Reconciliation from a JSON string
reconciliation_instance = Reconciliation.from_json(json)
# print the JSON string representation of the object
print Reconciliation.to_json()

# convert the object into a dict
reconciliation_dict = reconciliation_instance.to_dict()
# create an instance of Reconciliation from a dict
reconciliation_form_dict = reconciliation.from_dict(reconciliation_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


