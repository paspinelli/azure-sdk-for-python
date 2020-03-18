# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AzureResourceBase(Model):
    """Common properties for all Azure resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureResourceBase, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class DeploymentScript(AzureResourceBase):
    """Deployment script object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzurePowerShellScript, AzureCliScript

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param identity: Required. Managed identity to be used for this deployment
     script. Currently, only user-assigned MSI is supported.
    :type identity:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentity
    :param location: Required. The location of the ACI and the storage account
     for the deployment script.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'identity': {'required': True},
        'location': {'required': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'AzurePowerShell': 'AzurePowerShellScript', 'AzureCLI': 'AzureCliScript'}
    }

    def __init__(self, *, identity, location: str, tags=None, **kwargs) -> None:
        super(DeploymentScript, self).__init__(**kwargs)
        self.identity = identity
        self.location = location
        self.tags = tags
        self.kind = None
        self.kind = 'DeploymentScript'


class AzureCliScript(DeploymentScript):
    """Object model for the Azure CLI script.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param identity: Required. Managed identity to be used for this deployment
     script. Currently, only user-assigned MSI is supported.
    :type identity:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentity
    :param location: Required. The location of the ACI and the storage account
     for the deployment script.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param cleanup_preference: The clean up preference when the script
     execution gets in a terminal state. Default setting is 'Always'. Possible
     values include: 'Always', 'OnSuccess', 'OnExpiration'
    :type cleanup_preference: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CleanupOptions
    :ivar provisioning_state: State of the script execution. This only appears
     in the response. Possible values include: 'Creating',
     'ProvisioningResources', 'Running', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptProvisioningState
    :ivar status: Contains the results of script execution.
    :vartype status:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptStatus
    :ivar outputs: List of script outputs.
    :vartype outputs: dict[str, object]
    :param primary_script_uri: Uri for the script. This is the entry point for
     the external script.
    :type primary_script_uri: str
    :param supporting_script_uris: Supporting files for the external script.
    :type supporting_script_uris: list[str]
    :param script_content: Script body.
    :type script_content: str
    :param arguments: Command line arguments to pass to the script. Arguments
     are separated by spaces. ex: -Name blue* -Location 'West US 2'
    :type arguments: str
    :param environment_variables: The environment variables to pass over to
     the script.
    :type environment_variables:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.EnvironmentVariable]
    :param force_update_tag: Gets or sets how the deployment script should be
     forced to execute even if the script resource has not changed. Can be
     current time stamp or a GUID.
    :type force_update_tag: str
    :param retention_interval: Required. Interval for which the service
     retains the script resource after it reaches a terminal state. Resource
     will be deleted when this duration expires. Duration is based on ISO 8601
     pattern (for example P7D means one week).
    :type retention_interval: timedelta
    :param timeout: Maximum allowed script execution time specified in ISO
     8601 format. Default value is PT1H
    :type timeout: timedelta
    :param az_cli_version: Required. Azure CLI module version to be used.
    :type az_cli_version: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'identity': {'required': True},
        'location': {'required': True},
        'kind': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'outputs': {'readonly': True},
        'script_content': {'max_length': 32000},
        'retention_interval': {'required': True},
        'az_cli_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'cleanup_preference': {'key': 'properties.cleanupPreference', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'ScriptStatus'},
        'outputs': {'key': 'properties.outputs', 'type': '{object}'},
        'primary_script_uri': {'key': 'properties.primaryScriptUri', 'type': 'str'},
        'supporting_script_uris': {'key': 'properties.supportingScriptUris', 'type': '[str]'},
        'script_content': {'key': 'properties.scriptContent', 'type': 'str'},
        'arguments': {'key': 'properties.arguments', 'type': 'str'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'retention_interval': {'key': 'properties.retentionInterval', 'type': 'duration'},
        'timeout': {'key': 'properties.timeout', 'type': 'duration'},
        'az_cli_version': {'key': 'properties.azCliVersion', 'type': 'str'},
    }

    def __init__(self, *, identity, location: str, retention_interval, az_cli_version: str, tags=None, cleanup_preference=None, primary_script_uri: str=None, supporting_script_uris=None, script_content: str=None, arguments: str=None, environment_variables=None, force_update_tag: str=None, timeout=None, **kwargs) -> None:
        super(AzureCliScript, self).__init__(identity=identity, location=location, tags=tags, **kwargs)
        self.cleanup_preference = cleanup_preference
        self.provisioning_state = None
        self.status = None
        self.outputs = None
        self.primary_script_uri = primary_script_uri
        self.supporting_script_uris = supporting_script_uris
        self.script_content = script_content
        self.arguments = arguments
        self.environment_variables = environment_variables
        self.force_update_tag = force_update_tag
        self.retention_interval = retention_interval
        self.timeout = timeout
        self.az_cli_version = az_cli_version
        self.kind = 'AzureCLI'


class AzurePowerShellScript(DeploymentScript):
    """Object model for the Azure PowerShell script.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param identity: Required. Managed identity to be used for this deployment
     script. Currently, only user-assigned MSI is supported.
    :type identity:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentity
    :param location: Required. The location of the ACI and the storage account
     for the deployment script.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param cleanup_preference: The clean up preference when the script
     execution gets in a terminal state. Default setting is 'Always'. Possible
     values include: 'Always', 'OnSuccess', 'OnExpiration'
    :type cleanup_preference: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CleanupOptions
    :ivar provisioning_state: State of the script execution. This only appears
     in the response. Possible values include: 'Creating',
     'ProvisioningResources', 'Running', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptProvisioningState
    :ivar status: Contains the results of script execution.
    :vartype status:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptStatus
    :ivar outputs: List of script outputs.
    :vartype outputs: dict[str, object]
    :param primary_script_uri: Uri for the script. This is the entry point for
     the external script.
    :type primary_script_uri: str
    :param supporting_script_uris: Supporting files for the external script.
    :type supporting_script_uris: list[str]
    :param script_content: Script body.
    :type script_content: str
    :param arguments: Command line arguments to pass to the script. Arguments
     are separated by spaces. ex: -Name blue* -Location 'West US 2'
    :type arguments: str
    :param environment_variables: The environment variables to pass over to
     the script.
    :type environment_variables:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.EnvironmentVariable]
    :param force_update_tag: Gets or sets how the deployment script should be
     forced to execute even if the script resource has not changed. Can be
     current time stamp or a GUID.
    :type force_update_tag: str
    :param retention_interval: Required. Interval for which the service
     retains the script resource after it reaches a terminal state. Resource
     will be deleted when this duration expires. Duration is based on ISO 8601
     pattern (for example P7D means one week).
    :type retention_interval: timedelta
    :param timeout: Maximum allowed script execution time specified in ISO
     8601 format. Default value is PT1H
    :type timeout: timedelta
    :param az_power_shell_version: Required. Azure PowerShell module version
     to be used.
    :type az_power_shell_version: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'identity': {'required': True},
        'location': {'required': True},
        'kind': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'outputs': {'readonly': True},
        'script_content': {'max_length': 32000},
        'retention_interval': {'required': True},
        'az_power_shell_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'ManagedServiceIdentity'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'cleanup_preference': {'key': 'properties.cleanupPreference', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'ScriptStatus'},
        'outputs': {'key': 'properties.outputs', 'type': '{object}'},
        'primary_script_uri': {'key': 'properties.primaryScriptUri', 'type': 'str'},
        'supporting_script_uris': {'key': 'properties.supportingScriptUris', 'type': '[str]'},
        'script_content': {'key': 'properties.scriptContent', 'type': 'str'},
        'arguments': {'key': 'properties.arguments', 'type': 'str'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'retention_interval': {'key': 'properties.retentionInterval', 'type': 'duration'},
        'timeout': {'key': 'properties.timeout', 'type': 'duration'},
        'az_power_shell_version': {'key': 'properties.azPowerShellVersion', 'type': 'str'},
    }

    def __init__(self, *, identity, location: str, retention_interval, az_power_shell_version: str, tags=None, cleanup_preference=None, primary_script_uri: str=None, supporting_script_uris=None, script_content: str=None, arguments: str=None, environment_variables=None, force_update_tag: str=None, timeout=None, **kwargs) -> None:
        super(AzurePowerShellScript, self).__init__(identity=identity, location=location, tags=tags, **kwargs)
        self.cleanup_preference = cleanup_preference
        self.provisioning_state = None
        self.status = None
        self.outputs = None
        self.primary_script_uri = primary_script_uri
        self.supporting_script_uris = supporting_script_uris
        self.script_content = script_content
        self.arguments = arguments
        self.environment_variables = environment_variables
        self.force_update_tag = force_update_tag
        self.retention_interval = retention_interval
        self.timeout = timeout
        self.az_power_shell_version = az_power_shell_version
        self.kind = 'AzurePowerShell'


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class DeploymentScriptPropertiesBase(Model):
    """Common properties for the deployment script.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param cleanup_preference: The clean up preference when the script
     execution gets in a terminal state. Default setting is 'Always'. Possible
     values include: 'Always', 'OnSuccess', 'OnExpiration'
    :type cleanup_preference: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.CleanupOptions
    :ivar provisioning_state: State of the script execution. This only appears
     in the response. Possible values include: 'Creating',
     'ProvisioningResources', 'Running', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptProvisioningState
    :ivar status: Contains the results of script execution.
    :vartype status:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptStatus
    :ivar outputs: List of script outputs.
    :vartype outputs: dict[str, object]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'outputs': {'readonly': True},
    }

    _attribute_map = {
        'cleanup_preference': {'key': 'cleanupPreference', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status': {'key': 'status', 'type': 'ScriptStatus'},
        'outputs': {'key': 'outputs', 'type': '{object}'},
    }

    def __init__(self, *, cleanup_preference=None, **kwargs) -> None:
        super(DeploymentScriptPropertiesBase, self).__init__(**kwargs)
        self.cleanup_preference = cleanup_preference
        self.provisioning_state = None
        self.status = None
        self.outputs = None


class DeploymentScriptsError(Model):
    """Deployment scripts error response.

    :param error:
    :type error:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(DeploymentScriptsError, self).__init__(**kwargs)
        self.error = error


class DeploymentScriptsErrorException(HttpOperationError):
    """Server responsed with exception of type: 'DeploymentScriptsError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(DeploymentScriptsErrorException, self).__init__(deserialize, response, 'DeploymentScriptsError', *args)


class DeploymentScriptUpdateParameter(AzureResourceBase):
    """Deployment script parameters to be updated. .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :param tags: Resource tags to be updated.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, tags=None, **kwargs) -> None:
        super(DeploymentScriptUpdateParameter, self).__init__(**kwargs)
        self.tags = tags


class EnvironmentVariable(Model):
    """The environment variable to pass to the script in the container instance.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the environment variable.
    :type name: str
    :param value: The value of the environment variable.
    :type value: str
    :param secure_value: The value of the secure environment variable.
    :type secure_value: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'secure_value': {'key': 'secureValue', 'type': 'str'},
    }

    def __init__(self, *, name: str, value: str=None, secure_value: str=None, **kwargs) -> None:
        super(EnvironmentVariable, self).__init__(**kwargs)
        self.name = name
        self.value = value
        self.secure_value = secure_value


class ErrorAdditionalInfo(Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(Model):
    """The resource management error response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ManagedServiceIdentity(Model):
    """Managed identity generic object.

    :param type: Type of the managed identity. Possible values include:
     'UserAssigned'
    :type type: str or
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ManagedServiceIdentityType
    :param user_assigned_identities: The list of user-assigned managed
     identities associated with the resource. Key is the Azure resource Id of
     the managed identity.
    :type user_assigned_identities: dict[str,
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.UserAssignedIdentity]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserAssignedIdentity}'},
    }

    def __init__(self, *, type=None, user_assigned_identities=None, **kwargs) -> None:
        super(ManagedServiceIdentity, self).__init__(**kwargs)
        self.type = type
        self.user_assigned_identities = user_assigned_identities


class ScriptConfigurationBase(Model):
    """Common configuration settings for both Azure PowerShell and Azure CLI
    scripts.

    All required parameters must be populated in order to send to Azure.

    :param primary_script_uri: Uri for the script. This is the entry point for
     the external script.
    :type primary_script_uri: str
    :param supporting_script_uris: Supporting files for the external script.
    :type supporting_script_uris: list[str]
    :param script_content: Script body.
    :type script_content: str
    :param arguments: Command line arguments to pass to the script. Arguments
     are separated by spaces. ex: -Name blue* -Location 'West US 2'
    :type arguments: str
    :param environment_variables: The environment variables to pass over to
     the script.
    :type environment_variables:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.EnvironmentVariable]
    :param force_update_tag: Gets or sets how the deployment script should be
     forced to execute even if the script resource has not changed. Can be
     current time stamp or a GUID.
    :type force_update_tag: str
    :param retention_interval: Required. Interval for which the service
     retains the script resource after it reaches a terminal state. Resource
     will be deleted when this duration expires. Duration is based on ISO 8601
     pattern (for example P7D means one week).
    :type retention_interval: timedelta
    :param timeout: Maximum allowed script execution time specified in ISO
     8601 format. Default value is PT1H
    :type timeout: timedelta
    """

    _validation = {
        'script_content': {'max_length': 32000},
        'retention_interval': {'required': True},
    }

    _attribute_map = {
        'primary_script_uri': {'key': 'primaryScriptUri', 'type': 'str'},
        'supporting_script_uris': {'key': 'supportingScriptUris', 'type': '[str]'},
        'script_content': {'key': 'scriptContent', 'type': 'str'},
        'arguments': {'key': 'arguments', 'type': 'str'},
        'environment_variables': {'key': 'environmentVariables', 'type': '[EnvironmentVariable]'},
        'force_update_tag': {'key': 'forceUpdateTag', 'type': 'str'},
        'retention_interval': {'key': 'retentionInterval', 'type': 'duration'},
        'timeout': {'key': 'timeout', 'type': 'duration'},
    }

    def __init__(self, *, retention_interval, primary_script_uri: str=None, supporting_script_uris=None, script_content: str=None, arguments: str=None, environment_variables=None, force_update_tag: str=None, timeout=None, **kwargs) -> None:
        super(ScriptConfigurationBase, self).__init__(**kwargs)
        self.primary_script_uri = primary_script_uri
        self.supporting_script_uris = supporting_script_uris
        self.script_content = script_content
        self.arguments = arguments
        self.environment_variables = environment_variables
        self.force_update_tag = force_update_tag
        self.retention_interval = retention_interval
        self.timeout = timeout


class ScriptLog(AzureResourceBase):
    """Script execution log object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar name: Name of this resource.
    :vartype name: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar log: Script execution logs in text format.
    :vartype log: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'log': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'log': {'key': 'properties.log', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ScriptLog, self).__init__(**kwargs)
        self.log = None


class ScriptLogsList(Model):
    """Deployment script execution logs.

    :param value: Deployment scripts logs.
    :type value:
     list[~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ScriptLog]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ScriptLog]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(ScriptLogsList, self).__init__(**kwargs)
        self.value = value


class ScriptStatus(Model):
    """Generic object modeling results of script execution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar container_instance_id: ACI resource Id.
    :vartype container_instance_id: str
    :ivar storage_account_id: Storage account resource Id.
    :vartype storage_account_id: str
    :ivar start_time: Start time of the script execution.
    :vartype start_time: datetime
    :ivar end_time: End time of the script execution.
    :vartype end_time: datetime
    :ivar expiration_time: Time the deployment script resource will expire.
    :vartype expiration_time: datetime
    :param error: Error that is relayed from the script execution.
    :type error:
     ~azure.mgmt.resource.deploymentscripts.v2019_10_preview.models.ErrorResponse
    """

    _validation = {
        'container_instance_id': {'readonly': True},
        'storage_account_id': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'expiration_time': {'readonly': True},
    }

    _attribute_map = {
        'container_instance_id': {'key': 'containerInstanceId', 'type': 'str'},
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'expirationTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ScriptStatus, self).__init__(**kwargs)
        self.container_instance_id = None
        self.storage_account_id = None
        self.start_time = None
        self.end_time = None
        self.expiration_time = None
        self.error = error


class UserAssignedIdentity(Model):
    """User-assigned managed identity.

    :param principal_id: Azure Active Directory principal ID associated with
     this identity.
    :type principal_id: str
    :param client_id: Client App Id associated with this identity.
    :type client_id: str
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, *, principal_id: str=None, client_id: str=None, **kwargs) -> None:
        super(UserAssignedIdentity, self).__init__(**kwargs)
        self.principal_id = principal_id
        self.client_id = client_id
