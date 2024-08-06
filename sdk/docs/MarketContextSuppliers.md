# MarketContextSuppliers

It is possible to control which supplier is used for a given asset class.  This field is deprecated in favour of market data rules, which subsumes its functionality.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodity** | **str** |  | [optional] 
**credit** | **str** |  | [optional] 
**equity** | **str** |  | [optional] 
**fx** | **str** |  | [optional] 
**rates** | **str** |  | [optional] 

## Example

```python
from lusid.models.market_context_suppliers import MarketContextSuppliers

# TODO update the JSON string below
json = "{}"
# create an instance of MarketContextSuppliers from a JSON string
market_context_suppliers_instance = MarketContextSuppliers.from_json(json)
# print the JSON string representation of the object
print MarketContextSuppliers.to_json()

# convert the object into a dict
market_context_suppliers_dict = market_context_suppliers_instance.to_dict()
# create an instance of MarketContextSuppliers from a dict
market_context_suppliers_form_dict = market_context_suppliers.from_dict(market_context_suppliers_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


