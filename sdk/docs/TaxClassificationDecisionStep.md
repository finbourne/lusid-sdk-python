# TaxClassificationDecisionStep

One question the decision tree asked on the way to the leaf.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** | The position of the step in the decision trace, starting at 1. | 
**rule** | **str** | The decision-tree rule the step evaluated. | 
**question** | **str** | The question the rule asked of the inputs. | 
**answer** | **str** | The answer the rule took. | 
## Example

```python
from lusid.models.tax_classification_decision_step import TaxClassificationDecisionStep
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order: StrictInt = # Replace with your value
order: StrictInt = 42
rule: StrictStr = "example_rule"
question: StrictStr = "example_question"
answer: StrictStr = "example_answer"
tax_classification_decision_step_instance = TaxClassificationDecisionStep(order=order, rule=rule, question=question, answer=answer)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

