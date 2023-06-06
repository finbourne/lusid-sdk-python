# IDataRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_count** | **int** |  | [optional] [readonly] 

## Example

```python
from lusid.models.i_data_record import IDataRecord

# TODO update the JSON string below
json = "{}"
# create an instance of IDataRecord from a JSON string
i_data_record_instance = IDataRecord.from_json(json)
# print the JSON string representation of the object
print IDataRecord.to_json()

# convert the object into a dict
i_data_record_dict = i_data_record_instance.to_dict()
# create an instance of IDataRecord from a dict
i_data_record_form_dict = i_data_record.from_dict(i_data_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


