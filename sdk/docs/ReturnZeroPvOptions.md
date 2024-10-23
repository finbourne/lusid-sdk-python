# ReturnZeroPvOptions

Options to indicate which errors to ignore when performing valuation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_matured** | **bool** | Indicates whether attempting to value an instrument after its maturity date should produce a failure (false)  or a zero PV (true). | [optional] 

## Example

```python
from lusid.models.return_zero_pv_options import ReturnZeroPvOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnZeroPvOptions from a JSON string
return_zero_pv_options_instance = ReturnZeroPvOptions.from_json(json)
# print the JSON string representation of the object
print ReturnZeroPvOptions.to_json()

# convert the object into a dict
return_zero_pv_options_dict = return_zero_pv_options_instance.to_dict()
# create an instance of ReturnZeroPvOptions from a dict
return_zero_pv_options_form_dict = return_zero_pv_options.from_dict(return_zero_pv_options_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


