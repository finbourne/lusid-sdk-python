# BatchAdjustHoldingsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, HoldingAdjustmentWithDate]**](HoldingAdjustmentWithDate.md) | The holdings which have been successfully adjusted. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The holdings that could not be adjusted along with a reason for their failure. | [optional] 
**metadata** | **Dict[str, List[ResponseMetaData]]** | Contains warnings related to adjusted holdings | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.batch_adjust_holdings_response import BatchAdjustHoldingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAdjustHoldingsResponse from a JSON string
batch_adjust_holdings_response_instance = BatchAdjustHoldingsResponse.from_json(json)
# print the JSON string representation of the object
print BatchAdjustHoldingsResponse.to_json()

# convert the object into a dict
batch_adjust_holdings_response_dict = batch_adjust_holdings_response_instance.to_dict()
# create an instance of BatchAdjustHoldingsResponse from a dict
batch_adjust_holdings_response_form_dict = batch_adjust_holdings_response.from_dict(batch_adjust_holdings_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


