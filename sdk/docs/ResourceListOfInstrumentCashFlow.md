# ResourceListOfInstrumentCashFlow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[InstrumentCashFlow]**](InstrumentCashFlow.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_instrument_cash_flow import ResourceListOfInstrumentCashFlow

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfInstrumentCashFlow from a JSON string
resource_list_of_instrument_cash_flow_instance = ResourceListOfInstrumentCashFlow.from_json(json)
# print the JSON string representation of the object
print ResourceListOfInstrumentCashFlow.to_json()

# convert the object into a dict
resource_list_of_instrument_cash_flow_dict = resource_list_of_instrument_cash_flow_instance.to_dict()
# create an instance of ResourceListOfInstrumentCashFlow from a dict
resource_list_of_instrument_cash_flow_form_dict = resource_list_of_instrument_cash_flow.from_dict(resource_list_of_instrument_cash_flow_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


