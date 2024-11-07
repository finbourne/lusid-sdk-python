# Strategy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[PerpetualProperty]**](PerpetualProperty.md) |  | 
**value_type** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from lusid.models.strategy import Strategy

# TODO update the JSON string below
json = "{}"
# create an instance of Strategy from a JSON string
strategy_instance = Strategy.from_json(json)
# print the JSON string representation of the object
print Strategy.to_json()

# convert the object into a dict
strategy_dict = strategy_instance.to_dict()
# create an instance of Strategy from a dict
strategy_form_dict = strategy.from_dict(strategy_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


