# VersionSummaryDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**build_version** | **str** |  | [optional] 
**excel_version** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.version_summary_dto import VersionSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of VersionSummaryDto from a JSON string
version_summary_dto_instance = VersionSummaryDto.from_json(json)
# print the JSON string representation of the object
print VersionSummaryDto.to_json()

# convert the object into a dict
version_summary_dto_dict = version_summary_dto_instance.to_dict()
# create an instance of VersionSummaryDto from a dict
version_summary_dto_form_dict = version_summary_dto.from_dict(version_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


