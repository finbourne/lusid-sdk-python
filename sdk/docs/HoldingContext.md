# HoldingContext

Holding context node.  Contains settings that control how LUSID handles holdings within portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_lot_level_holdings** | **bool** | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to True. | [optional] 

## Example

```python
from lusid.models.holding_context import HoldingContext

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingContext from a JSON string
holding_context_instance = HoldingContext.from_json(json)
# print the JSON string representation of the object
print HoldingContext.to_json()

# convert the object into a dict
holding_context_dict = holding_context_instance.to_dict()
# create an instance of HoldingContext from a dict
holding_context_form_dict = holding_context.from_dict(holding_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


