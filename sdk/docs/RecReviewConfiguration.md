# RecReviewConfiguration

How the results of a rec definition's runs are reviewed and approved: what needs reviewing, when the  reviewer may submit, and who has to approve the submission.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_exceptions** | [**RecReviewRequirementRule**](RecReviewRequirementRule.md) |  | [optional] 
**closed_exceptions** | [**RecReviewRequirementRule**](RecReviewRequirementRule.md) |  | [optional] 
**matches** | [**RecReviewRequirementRule**](RecReviewRequirementRule.md) |  | [optional] 
**review_submission** | [**RecReviewSubmission**](RecReviewSubmission.md) |  | [optional] 
**required_approvals** | [**List[RecReviewRequiredApproval]**](RecReviewRequiredApproval.md) | The approvals a submitted review has to collect. All are required and may be given in any order, and no user may give more than one of them. Empty means no approvals are required and the reviewer self-approves on submission. | [optional] 
## Example

```python
from lusid.models.rec_review_configuration import RecReviewConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

open_exceptions: Optional[RecReviewRequirementRule] = # Replace with your value
closed_exceptions: Optional[RecReviewRequirementRule] = # Replace with your value
matches: Optional[RecReviewRequirementRule] = None
review_submission: Optional[RecReviewSubmission] = # Replace with your value
required_approvals: Optional[List[RecReviewRequiredApproval]] = # Replace with your value
rec_review_configuration_instance = RecReviewConfiguration(open_exceptions=open_exceptions, closed_exceptions=closed_exceptions, matches=matches, review_submission=review_submission, required_approvals=required_approvals)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

