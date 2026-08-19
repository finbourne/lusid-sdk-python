# lusid.RecsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rec_result_set_approval_decision**](RecsApi.md#add_rec_result_set_approval_decision) | **POST** /api/recs/resultsets/{entityUniqueId}/$decide | [EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision
[**batch_manage_rec_result_comments**](RecsApi.md#batch_manage_rec_result_comments) | **POST** /api/recs/results/$batchManageComments | [EXPERIMENTAL] BatchManageRecResultComments: BatchManageRecResultComments
[**batch_review_rec_results**](RecsApi.md#batch_review_rec_results) | **POST** /api/recs/results/$batchReview | [EXPERIMENTAL] BatchReviewRecResults: BatchReviewRecResults
[**create_matching_ruleset**](RecsApi.md#create_matching_ruleset) | **POST** /api/recs/matchingrulesets | [EXPERIMENTAL] CreateMatchingRuleset: CreateMatchingRuleset
[**create_rec_definition**](RecsApi.md#create_rec_definition) | **POST** /api/recs/definitions | [EXPERIMENTAL] CreateRecDefinition: CreateRecDefinition
[**delete_matching_ruleset**](RecsApi.md#delete_matching_ruleset) | **DELETE** /api/recs/matchingrulesets/{scope}/{code} | [EXPERIMENTAL] DeleteMatchingRuleset: DeleteMatchingRuleset
[**delete_rec_definition**](RecsApi.md#delete_rec_definition) | **DELETE** /api/recs/definitions/{scope}/{code} | [EXPERIMENTAL] DeleteRecDefinition: DeleteRecDefinition
[**get_matching_ruleset**](RecsApi.md#get_matching_ruleset) | **GET** /api/recs/matchingrulesets/{scope}/{code} | [EXPERIMENTAL] GetMatchingRuleset: GetMatchingRuleset
[**get_rec_definition**](RecsApi.md#get_rec_definition) | **GET** /api/recs/definitions/{scope}/{code} | [EXPERIMENTAL] GetRecDefinition: GetRecDefinition
[**get_rec_instance**](RecsApi.md#get_rec_instance) | **GET** /api/recs/instances/{instanceIdType}/{instanceIdValue} | [EXPERIMENTAL] GetRecInstance: GetRecInstance
[**get_rec_result**](RecsApi.md#get_rec_result) | **GET** /api/recs/results/{id} | [EXPERIMENTAL] GetRecResult: GetRecResult
[**get_rec_result_set**](RecsApi.md#get_rec_result_set) | **GET** /api/recs/resultsets/{entityUniqueId} | [EXPERIMENTAL] GetRecResultSet: GetRecResultSet
[**instantiate_rec**](RecsApi.md#instantiate_rec) | **POST** /api/recs/instances | [EXPERIMENTAL] InstantiateRec: InstantiateRec
[**list_matching_rulesets**](RecsApi.md#list_matching_rulesets) | **GET** /api/recs/matchingrulesets | [EXPERIMENTAL] ListMatchingRulesets: ListMatchingRulesets
[**list_rec_definitions**](RecsApi.md#list_rec_definitions) | **GET** /api/recs/definitions | [EXPERIMENTAL] ListRecDefinitions: ListRecDefinitions
[**list_rec_instances**](RecsApi.md#list_rec_instances) | **GET** /api/recs/instances | [EXPERIMENTAL] ListRecInstances: ListRecInstances
[**list_rec_result_sets**](RecsApi.md#list_rec_result_sets) | **GET** /api/recs/resultsets | [EXPERIMENTAL] ListRecResultSets: ListRecResultSets
[**list_rec_results**](RecsApi.md#list_rec_results) | **GET** /api/recs/results | [EXPERIMENTAL] ListRecResults: ListRecResults
[**submit_rec_result_set_review**](RecsApi.md#submit_rec_result_set_review) | **POST** /api/recs/resultsets/{entityUniqueId}/$submit | [EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.
[**transition_rec_instance**](RecsApi.md#transition_rec_instance) | **POST** /api/recs/instances/{instanceIdType}/{instanceIdValue}/$transition | [EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance
[**update_matching_ruleset**](RecsApi.md#update_matching_ruleset) | **PUT** /api/recs/matchingrulesets/{scope}/{code} | [EXPERIMENTAL] UpdateMatchingRuleset: UpdateMatchingRuleset
[**update_rec_definition**](RecsApi.md#update_rec_definition) | **PUT** /api/recs/definitions/{scope}/{code} | [EXPERIMENTAL] UpdateRecDefinition: UpdateRecDefinition


# **add_rec_result_set_approval_decision**
> RecResultSet add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)

[EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision

Add an approver decision (approve or request revisions) to a rec result set.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    entity_unique_id = 'entity_unique_id_example' # str | The entity unique id of the rec result set (its version.entityUniqueId).

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest.from_json("")
    # rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest.from_dict({})
    rec_result_set_approval_decision_request = RecResultSetApprovalDecisionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request, opts=opts)

        # [EXPERIMENTAL] AddRecResultSetApprovalDecision: AddRecResultSetApprovalDecision
        api_response = api_instance.add_rec_result_set_approval_decision(entity_unique_id, rec_result_set_approval_decision_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->add_rec_result_set_approval_decision: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | 
 **rec_result_set_approval_decision_request** | [**RecResultSetApprovalDecisionRequest**](RecResultSetApprovalDecisionRequest.md)| The approval decision request. | 

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_manage_rec_result_comments**
> BatchManageCommentResponse batch_manage_rec_result_comments(request_body, success_mode=success_mode)

[EXPERIMENTAL] BatchManageRecResultComments: BatchManageRecResultComments

Add, edit or delete comments on rec results in a batch.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    request_body = {"add-a-comment":{"recResultId":"rec-result-1","commentText":"Investigating this break."},"delete-a-comment":{"recResultId":"rec-result-1","commentId":"00000000-0000-0000-0000-000000000009"}} # Dict[str, BatchManageCommentRequest] | The batch of comment operations, keyed by a client-supplied correlation key.
    success_mode = 'Partial' # str | Whether the batch fails Atomically or in a Partial fashion. Allowed values: Atomic, Partial. (optional) (default to 'Partial')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_manage_rec_result_comments(request_body, success_mode=success_mode, opts=opts)

        # [EXPERIMENTAL] BatchManageRecResultComments: BatchManageRecResultComments
        api_response = api_instance.batch_manage_rec_result_comments(request_body, success_mode=success_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->batch_manage_rec_result_comments: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, BatchManageCommentRequest]**](BatchManageCommentRequest.md)| The batch of comment operations, keyed by a client-supplied correlation key. | 
 **success_mode** | **str**| Whether the batch fails Atomically or in a Partial fashion. Allowed values: Atomic, Partial. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchManageCommentResponse**](BatchManageCommentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec results, keyed by batch item key. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **batch_review_rec_results**
> BatchReviewRecResultResponse batch_review_rec_results(request_body, success_mode=success_mode)

[EXPERIMENTAL] BatchReviewRecResults: BatchReviewRecResults

Apply a batch of review actions (decisions, assignments, comments, properties) to rec results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    request_body = {"accept-a-break":{"recResultIds":["rec-result-1"],"decision":{"value":"Accept","affirm":false}},"force-match-two":{"recResultIds":["rec-result-2","rec-result-3"],"decision":{"value":"ForceMatch","affirm":false,"coreRulesExcused":["Broker Name"]}}} # Dict[str, BatchReviewRecResultRequest] | The batch of review items, keyed by a client-supplied correlation key.
    success_mode = 'Partial' # str | Whether the batch fails Atomically or in a Partial fashion. Allowed values: Atomic, Partial. (optional) (default to 'Partial')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.batch_review_rec_results(request_body, success_mode=success_mode, opts=opts)

        # [EXPERIMENTAL] BatchReviewRecResults: BatchReviewRecResults
        api_response = api_instance.batch_review_rec_results(request_body, success_mode=success_mode)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->batch_review_rec_results: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, BatchReviewRecResultRequest]**](BatchReviewRecResultRequest.md)| The batch of review items, keyed by a client-supplied correlation key. | 
 **success_mode** | **str**| Whether the batch fails Atomically or in a Partial fashion. Allowed values: Atomic, Partial. | [optional] [default to &#39;Partial&#39;]

### Return type

[**BatchReviewRecResultResponse**](BatchReviewRecResultResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results affected by each batch item. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_matching_ruleset**
> MatchingRuleset create_matching_ruleset(create_matching_ruleset_request)

[EXPERIMENTAL] CreateMatchingRuleset: CreateMatchingRuleset

Create a matching ruleset, describing the core and aggregate rules used to match a reconciliation's two sides.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_matching_ruleset_request = CreateMatchingRulesetRequest.from_json("")
    # create_matching_ruleset_request = CreateMatchingRulesetRequest.from_dict({})
    create_matching_ruleset_request = CreateMatchingRulesetRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_matching_ruleset(create_matching_ruleset_request, opts=opts)

        # [EXPERIMENTAL] CreateMatchingRuleset: CreateMatchingRuleset
        api_response = api_instance.create_matching_ruleset(create_matching_ruleset_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->create_matching_ruleset: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_matching_ruleset_request** | [**CreateMatchingRulesetRequest**](CreateMatchingRulesetRequest.md)| The matching ruleset to create. | 

### Return type

[**MatchingRuleset**](MatchingRuleset.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created matching ruleset. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_rec_definition**
> RecDefinition create_rec_definition(create_rec_definition_request)

[EXPERIMENTAL] CreateRecDefinition: CreateRecDefinition

Create a rec definition, describing the two sides to reconcile and the rules to reconcile them with.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_rec_definition_request = CreateRecDefinitionRequest.from_json("")
    # create_rec_definition_request = CreateRecDefinitionRequest.from_dict({})
    create_rec_definition_request = CreateRecDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_rec_definition(create_rec_definition_request, opts=opts)

        # [EXPERIMENTAL] CreateRecDefinition: CreateRecDefinition
        api_response = api_instance.create_rec_definition(create_rec_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->create_rec_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rec_definition_request** | [**CreateRecDefinitionRequest**](CreateRecDefinitionRequest.md)| The rec definition to create. | 

### Return type

[**RecDefinition**](RecDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created rec definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_matching_ruleset**
> DeletedEntityResponse delete_matching_ruleset(scope, code)

[EXPERIMENTAL] DeleteMatchingRuleset: DeleteMatchingRuleset

Delete a matching ruleset identified by scope and code. The deletion takes effect from the deletion datetime,  i.e. the matching ruleset will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    scope = 'scope_example' # str | The scope of the matching ruleset.
    code = 'code_example' # str | The code of the matching ruleset. Together with the scope this uniquely identifies the matching ruleset.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_matching_ruleset(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteMatchingRuleset: DeleteMatchingRuleset
        api_response = api_instance.delete_matching_ruleset(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->delete_matching_ruleset: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the matching ruleset. | 
 **code** | **str**| The code of the matching ruleset. Together with the scope this uniquely identifies the matching ruleset. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_rec_definition**
> DeletedEntityResponse delete_rec_definition(scope, code)

[EXPERIMENTAL] DeleteRecDefinition: DeleteRecDefinition

Delete a rec definition identified by scope and code. The deletion takes effect from the deletion datetime,  i.e. the rec definition will no longer exist at any asAt datetime after the asAt datetime of deletion.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    scope = 'scope_example' # str | The scope of the rec definition.
    code = 'code_example' # str | The code of the rec definition. Together with the scope this uniquely identifies the rec definition.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.delete_rec_definition(scope, code, opts=opts)

        # [EXPERIMENTAL] DeleteRecDefinition: DeleteRecDefinition
        api_response = api_instance.delete_rec_definition(scope, code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->delete_rec_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the rec definition. | 
 **code** | **str**| The code of the rec definition. Together with the scope this uniquely identifies the rec definition. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted entity metadata. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_matching_ruleset**
> MatchingRuleset get_matching_ruleset(scope, code, as_at=as_at)

[EXPERIMENTAL] GetMatchingRuleset: GetMatchingRuleset

Retrieve a single matching ruleset by scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    scope = 'scope_example' # str | The scope of the matching ruleset.
    code = 'code_example' # str | The code of the matching ruleset. Together with the scope this uniquely identifies the matching ruleset.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the matching ruleset. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_matching_ruleset(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetMatchingRuleset: GetMatchingRuleset
        api_response = api_instance.get_matching_ruleset(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_matching_ruleset: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the matching ruleset. | 
 **code** | **str**| The code of the matching ruleset. Together with the scope this uniquely identifies the matching ruleset. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the matching ruleset. Defaults to latest if not specified. | [optional] 

### Return type

[**MatchingRuleset**](MatchingRuleset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested matching ruleset. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_rec_definition**
> RecDefinition get_rec_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRecDefinition: GetRecDefinition

Retrieve a single rec definition by scope and code.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    scope = 'scope_example' # str | The scope of the rec definition.
    code = 'code_example' # str | The code of the rec definition. Together with the scope this uniquely identifies the rec definition.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rec definition. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_rec_definition(scope, code, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetRecDefinition: GetRecDefinition
        api_response = api_instance.get_rec_definition(scope, code, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_rec_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the rec definition. | 
 **code** | **str**| The code of the rec definition. Together with the scope this uniquely identifies the rec definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rec definition. Defaults to latest if not specified. | [optional] 

### Return type

[**RecDefinition**](RecDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_rec_instance**
> RecInstance get_rec_instance(instance_id_type, instance_id_value, as_at=as_at)

[EXPERIMENTAL] GetRecInstance: GetRecInstance

Retrieve a single rec instance by its identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    instance_id_type = 'instance_id_type_example' # str | How the instance was created: \"WorkflowServiceTaskId\" or \"Manual\". Available values: WorkflowServiceTaskId, Manual.
    instance_id_value = 'instance_id_value_example' # str | The instance identifier value (a GUID).
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instance. Defaults to latest if not specified. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_rec_instance(instance_id_type, instance_id_value, as_at=as_at, opts=opts)

        # [EXPERIMENTAL] GetRecInstance: GetRecInstance
        api_response = api_instance.get_rec_instance(instance_id_type, instance_id_value, as_at=as_at)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_rec_instance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id_type** | **str**| How the instance was created: \&quot;WorkflowServiceTaskId\&quot; or \&quot;Manual\&quot;. Available values: WorkflowServiceTaskId, Manual. | 
 **instance_id_value** | **str**| The instance identifier value (a GUID). | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instance. Defaults to latest if not specified. | [optional] 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec instance. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_rec_result**
> RecResult get_rec_result(id, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetRecResult: GetRecResult

Retrieve a single rec result by its id.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    id = 'id_example' # str | The system-generated id of the rec result.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the result. Defaults to latest if not specified. (optional)
    property_keys = ['property_keys_example'] # List[str] | The property keys to decorate onto the result. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_rec_result(id, as_at=as_at, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] GetRecResult: GetRecResult
        api_response = api_instance.get_rec_result(id, as_at=as_at, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_rec_result: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The system-generated id of the rec result. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the result. Defaults to latest if not specified. | [optional] 
 **property_keys** | [**List[str]**](str.md)| The property keys to decorate onto the result. | [optional] 

### Return type

[**RecResult**](RecResult.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec result. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_rec_result_set**
> RecResultSet get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs)

[EXPERIMENTAL] GetRecResultSet: GetRecResultSet

Retrieve a single rec result set by its entity unique id.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    entity_unique_id = 'entity_unique_id_example' # str | The entity unique id of the rec result set (its version.entityUniqueId).
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the result set. Defaults to latest if not specified. (optional)
    include_previous_runs = False # bool | When true, the previousRuns array is populated with prior run snapshots. Defaults to false. (optional) (default to False)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs, opts=opts)

        # [EXPERIMENTAL] GetRecResultSet: GetRecResultSet
        api_response = api_instance.get_rec_result_set(entity_unique_id, as_at=as_at, include_previous_runs=include_previous_runs)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->get_rec_result_set: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the result set. Defaults to latest if not specified. | [optional] 
 **include_previous_runs** | **bool**| When true, the previousRuns array is populated with prior run snapshots. Defaults to false. | [optional] [default to False]

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **instantiate_rec**
> RecInstance instantiate_rec(instantiate_rec_request)

[EXPERIMENTAL] InstantiateRec: InstantiateRec

Instantiate a new rec instance from a rec definition and start its first run. The run              executes asynchronously; the response returns once the run has started, with the instance Running.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # instantiate_rec_request = InstantiateRecRequest.from_json("")
    # instantiate_rec_request = InstantiateRecRequest.from_dict({})
    instantiate_rec_request = InstantiateRecRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.instantiate_rec(instantiate_rec_request, opts=opts)

        # [EXPERIMENTAL] InstantiateRec: InstantiateRec
        api_response = api_instance.instantiate_rec(instantiate_rec_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->instantiate_rec: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instantiate_rec_request** | [**InstantiateRecRequest**](InstantiateRecRequest.md)| The instantiation request. | 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The instantiated rec instance, in a Running state. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_matching_rulesets**
> PagedResourceListOfMatchingRuleset list_matching_rulesets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListMatchingRulesets: ListMatchingRulesets

List matching rulesets, optionally filtered and sorted. Supports pagination.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the matching rulesets. Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing matching rulesets from a previous call. This value is              returned from the previous call. If a pagination token is provided the sortBy, filter and asAt fields must not have              changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many per page. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_matching_rulesets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListMatchingRulesets: ListMatchingRulesets
        api_response = api_instance.list_matching_rulesets(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_matching_rulesets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the matching rulesets. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing matching rulesets from a previous call. This value is              returned from the previous call. If a pagination token is provided the sortBy, filter and asAt fields must not have              changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many per page. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfMatchingRuleset**](PagedResourceListOfMatchingRuleset.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of matching rulesets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_rec_definitions**
> PagedResourceListOfRecDefinition list_rec_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)

[EXPERIMENTAL] ListRecDefinitions: ListRecDefinitions

List rec definitions, optionally filtered and sorted. Supports pagination.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the rec definitions. Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing rec definitions from a previous call. This value is              returned from the previous call. If a pagination token is provided the sortBy, filter and asAt fields must not have              changed since the original request. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many per page. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here              https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_rec_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, opts=opts)

        # [EXPERIMENTAL] ListRecDefinitions: ListRecDefinitions
        api_response = api_instance.list_rec_definitions(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_rec_definitions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the rec definitions. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing rec definitions from a previous call. This value is              returned from the previous call. If a pagination token is provided the sortBy, filter and asAt fields must not have              changed since the original request. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many per page. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here              https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfRecDefinition**](PagedResourceListOfRecDefinition.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested list of rec definitions. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_rec_instances**
> PagedResourceListOfRecInstance list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRecInstances: ListRecInstances

List rec instances.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list instances. Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing instances from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListRecInstances: ListRecInstances
        api_response = api_instance.list_rec_instances(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_rec_instances: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list instances. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing instances from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfRecInstance**](PagedResourceListOfRecInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec instances. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_rec_result_sets**
> PagedResourceListOfRecResultSet list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRecResultSets: ListRecResultSets

List rec result sets.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list result sets. Defaults to latest if not specified. (optional)
    include_previous_runs = False # bool | When true, each item's previousRuns array is populated with prior run snapshots. Defaults to false. (optional) (default to False)
    page = 'page_example' # str | The pagination token to use to continue listing result sets from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\". (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by, opts=opts)

        # [EXPERIMENTAL] ListRecResultSets: ListRecResultSets
        api_response = api_instance.list_rec_result_sets(as_at=as_at, include_previous_runs=include_previous_runs, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_rec_result_sets: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list result sets. Defaults to latest if not specified. | [optional] 
 **include_previous_runs** | **bool**| When true, each item&#39;s previousRuns array is populated with prior run snapshots. Defaults to false. | [optional] [default to False]
 **page** | **str**| The pagination token to use to continue listing result sets from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 

### Return type

[**PagedResourceListOfRecResultSet**](PagedResourceListOfRecResultSet.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec result sets. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_rec_results**
> PagedResourceListOfRecResult list_rec_results(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)

[EXPERIMENTAL] ListRecResults: ListRecResults

List rec results.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list results. Defaults to latest if not specified. (optional)
    page = 'page_example' # str | The pagination token to use to continue listing results from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. (optional)
    limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names suffixed by \" ASC\" or \" DESC\". (optional)
    property_keys = ['property_keys_example'] # List[str] | The property keys to decorate onto each result. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_rec_results(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys, opts=opts)

        # [EXPERIMENTAL] ListRecResults: ListRecResults
        api_response = api_instance.list_rec_results(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by, property_keys=property_keys)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->list_rec_results: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list results. Defaults to latest if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing results from a previous call. If a pagination token is provided the filter and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **property_keys** | [**List[str]**](str.md)| The property keys to decorate onto each result. | [optional] 

### Return type

[**PagedResourceListOfRecResult**](PagedResourceListOfRecResult.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec results. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **submit_rec_result_set_review**
> RecResultSet submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request)

[EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.

Submit a rec result set review for approval, or resubmit after addressing requested revisions.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    entity_unique_id = 'entity_unique_id_example' # str | The entity unique id of the rec result set (its version.entityUniqueId).

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest.from_json("")
    # submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest.from_dict({})
    submit_rec_result_set_review_request = SubmitRecResultSetReviewRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request, opts=opts)

        # [EXPERIMENTAL] SubmitRecResultSetReview: Submit a rec result set review for approval, or resubmit after addressing requested revisions.
        api_response = api_instance.submit_rec_result_set_review(entity_unique_id, submit_rec_result_set_review_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->submit_rec_result_set_review: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_unique_id** | **str**| The entity unique id of the rec result set (its version.entityUniqueId). | 
 **submit_rec_result_set_review_request** | [**SubmitRecResultSetReviewRequest**](SubmitRecResultSetReviewRequest.md)| The submission request. | 

### Return type

[**RecResultSet**](RecResultSet.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec result set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **transition_rec_instance**
> RecInstance transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request)

[EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance

Apply a lifecycle transition (re-run, lock or unlock) to a rec instance.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    instance_id_type = 'instance_id_type_example' # str | How the instance was created: \"WorkflowServiceTaskId\" or \"Manual\". Available values: WorkflowServiceTaskId, Manual.
    instance_id_value = 'instance_id_value_example' # str | The instance identifier value (a GUID).

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # transition_rec_instance_request = TransitionRecInstanceRequest.from_json("")
    # transition_rec_instance_request = TransitionRecInstanceRequest.from_dict({})
    transition_rec_instance_request = TransitionRecInstanceRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request, opts=opts)

        # [EXPERIMENTAL] TransitionRecInstance: TransitionRecInstance
        api_response = api_instance.transition_rec_instance(instance_id_type, instance_id_value, transition_rec_instance_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->transition_rec_instance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id_type** | **str**| How the instance was created: \&quot;WorkflowServiceTaskId\&quot; or \&quot;Manual\&quot;. Available values: WorkflowServiceTaskId, Manual. | 
 **instance_id_value** | **str**| The instance identifier value (a GUID). | 
 **transition_rec_instance_request** | [**TransitionRecInstanceRequest**](TransitionRecInstanceRequest.md)| The transition request. | 

### Return type

[**RecInstance**](RecInstance.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rec instance in its post-transition state. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_matching_ruleset**
> MatchingRuleset update_matching_ruleset(scope, code, update_matching_ruleset_request)

[EXPERIMENTAL] UpdateMatchingRuleset: UpdateMatchingRuleset

Overwrite an existing matching ruleset identified by scope and code.  The update request has the same required fields as create, apart from the identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    scope = 'scope_example' # str | The scope of the matching ruleset.
    code = 'code_example' # str | The code of the matching ruleset. Together with the scope this uniquely identifies the matching ruleset.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_matching_ruleset_request = UpdateMatchingRulesetRequest.from_json("")
    # update_matching_ruleset_request = UpdateMatchingRulesetRequest.from_dict({})
    update_matching_ruleset_request = UpdateMatchingRulesetRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_matching_ruleset(scope, code, update_matching_ruleset_request, opts=opts)

        # [EXPERIMENTAL] UpdateMatchingRuleset: UpdateMatchingRuleset
        api_response = api_instance.update_matching_ruleset(scope, code, update_matching_ruleset_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->update_matching_ruleset: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the matching ruleset. | 
 **code** | **str**| The code of the matching ruleset. Together with the scope this uniquely identifies the matching ruleset. | 
 **update_matching_ruleset_request** | [**UpdateMatchingRulesetRequest**](UpdateMatchingRulesetRequest.md)| The updated matching ruleset values. | 

### Return type

[**MatchingRuleset**](MatchingRuleset.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated matching ruleset. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_rec_definition**
> RecDefinition update_rec_definition(scope, code, update_rec_definition_request)

[EXPERIMENTAL] UpdateRecDefinition: UpdateRecDefinition

Overwrite an existing rec definition identified by scope and code.  The update request has the same required fields as create, apart from the identifier.

### Example

```python
from lusid.exceptions import ApiException
from lusid.extensions.configuration_options import ConfigurationOptions
from lusid.models import *
from pprint import pprint
from lusid import (
    SyncApiClientFactory,
    RecsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "lusidUrl":"https://<your-domain>.lusid.com/api",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the lusid SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(RecsApi)
    scope = 'scope_example' # str | The scope of the rec definition.
    code = 'code_example' # str | The code of the rec definition. Together with the scope this uniquely identifies the rec definition.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_rec_definition_request = UpdateRecDefinitionRequest.from_json("")
    # update_rec_definition_request = UpdateRecDefinitionRequest.from_dict({})
    update_rec_definition_request = UpdateRecDefinitionRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_rec_definition(scope, code, update_rec_definition_request, opts=opts)

        # [EXPERIMENTAL] UpdateRecDefinition: UpdateRecDefinition
        api_response = api_instance.update_rec_definition(scope, code, update_rec_definition_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RecsApi->update_rec_definition: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the rec definition. | 
 **code** | **str**| The code of the rec definition. Together with the scope this uniquely identifies the rec definition. | 
 **update_rec_definition_request** | [**UpdateRecDefinitionRequest**](UpdateRecDefinitionRequest.md)| The updated rec definition values. | 

### Return type

[**RecDefinition**](RecDefinition.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated rec definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

