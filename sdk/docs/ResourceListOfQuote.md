# ResourceListOfQuote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Quote]**](Quote.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_quote import ResourceListOfQuote

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfQuote from a JSON string
resource_list_of_quote_instance = ResourceListOfQuote.from_json(json)
# print the JSON string representation of the object
print ResourceListOfQuote.to_json()

# convert the object into a dict
resource_list_of_quote_dict = resource_list_of_quote_instance.to_dict()
# create an instance of ResourceListOfQuote from a dict
resource_list_of_quote_form_dict = resource_list_of_quote.from_dict(resource_list_of_quote_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


