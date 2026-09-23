# CreateWithholdingTaxDatasetDefinitionsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_dataset** | [**CreateWithholdingTaxDataset**](CreateWithholdingTaxDataset.md) |  | 
**main_dataset** | [**CreateWithholdingTaxDataset**](CreateWithholdingTaxDataset.md) |  | 
## Example

```python
from lusid.models.create_withholding_tax_dataset_definitions_request import CreateWithholdingTaxDatasetDefinitionsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

anomaly_dataset: CreateWithholdingTaxDataset = # Replace with your value
main_dataset: CreateWithholdingTaxDataset = # Replace with your value
create_withholding_tax_dataset_definitions_request_instance = CreateWithholdingTaxDatasetDefinitionsRequest(anomaly_dataset=anomaly_dataset, main_dataset=main_dataset)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

