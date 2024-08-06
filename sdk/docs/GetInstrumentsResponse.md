# GetInstrumentsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, Instrument]**](Instrument.md) | The instrument definitions, keyed by the identifier used to retrieve them. Only instruments that were found will be contained in this collection. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The identifiers that did not resolve to an instrument along with the nature of the failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.get_instruments_response import GetInstrumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInstrumentsResponse from a JSON string
get_instruments_response_instance = GetInstrumentsResponse.from_json(json)
# print the JSON string representation of the object
print GetInstrumentsResponse.to_json()

# convert the object into a dict
get_instruments_response_dict = get_instruments_response_instance.to_dict()
# create an instance of GetInstrumentsResponse from a dict
get_instruments_response_form_dict = get_instruments_response.from_dict(get_instruments_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


