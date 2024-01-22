# LineageMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index to demonstrate position of lineage member in overall lineage | 
**label** | **str** | Label of the step corresponding to this lineage member | 
**sub_label** | **str** | SubLabel of the step corresponding to this lineage member | 
**info_type** | **str** | Optional. Type of Information | [optional] 
**information** | **str** | Optional. Information for the step corresponding to this lineage member, of type InfoType | [optional] 

## Example

```python
from lusid.models.lineage_member import LineageMember

# TODO update the JSON string below
json = "{}"
# create an instance of LineageMember from a JSON string
lineage_member_instance = LineageMember.from_json(json)
# print the JSON string representation of the object
print LineageMember.to_json()

# convert the object into a dict
lineage_member_dict = lineage_member_instance.to_dict()
# create an instance of LineageMember from a dict
lineage_member_form_dict = lineage_member.from_dict(lineage_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


