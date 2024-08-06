# DecoratedComplianceRunSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**details** | [**List[ComplianceRuleResultDetail]**](ComplianceRuleResultDetail.md) |  | 

## Example

```python
from lusid.models.decorated_compliance_run_summary import DecoratedComplianceRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DecoratedComplianceRunSummary from a JSON string
decorated_compliance_run_summary_instance = DecoratedComplianceRunSummary.from_json(json)
# print the JSON string representation of the object
print DecoratedComplianceRunSummary.to_json()

# convert the object into a dict
decorated_compliance_run_summary_dict = decorated_compliance_run_summary_instance.to_dict()
# create an instance of DecoratedComplianceRunSummary from a dict
decorated_compliance_run_summary_form_dict = decorated_compliance_run_summary.from_dict(decorated_compliance_run_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


