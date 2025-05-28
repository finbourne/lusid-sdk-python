# Economics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**lusid_instrument_id** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that economics are for. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the Economic. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**buckets** | [**List[Bucket]**](Bucket.md) | Set of economic data related with each of the side impact of the transaction. | [optional] 

## Example

```python
from lusid.models.economics import Economics

# TODO update the JSON string below
json = "{}"
# create an instance of Economics from a JSON string
economics_instance = Economics.from_json(json)
# print the JSON string representation of the object
print Economics.to_json()

# convert the object into a dict
economics_dict = economics_instance.to_dict()
# create an instance of Economics from a dict
economics_form_dict = economics.from_dict(economics_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


