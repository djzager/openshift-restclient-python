# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1StatefulSetSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pod_management_policy': 'str',
        'replicas': 'int',
        'revision_history_limit': 'int',
        'selector': 'V1LabelSelector',
        'service_name': 'str',
        'template': 'V1PodTemplateSpec',
        'update_strategy': 'V1StatefulSetUpdateStrategy',
        'volume_claim_templates': 'list[V1PersistentVolumeClaim]'
    }

    attribute_map = {
        'pod_management_policy': 'podManagementPolicy',
        'replicas': 'replicas',
        'revision_history_limit': 'revisionHistoryLimit',
        'selector': 'selector',
        'service_name': 'serviceName',
        'template': 'template',
        'update_strategy': 'updateStrategy',
        'volume_claim_templates': 'volumeClaimTemplates'
    }

    def __init__(self, pod_management_policy=None, replicas=None, revision_history_limit=None, selector=None, service_name=None, template=None, update_strategy=None, volume_claim_templates=None):
        """
        V1StatefulSetSpec - a model defined in Swagger
        """

        self._pod_management_policy = None
        self._replicas = None
        self._revision_history_limit = None
        self._selector = None
        self._service_name = None
        self._template = None
        self._update_strategy = None
        self._volume_claim_templates = None
        self.discriminator = None

        if pod_management_policy is not None:
          self.pod_management_policy = pod_management_policy
        if replicas is not None:
          self.replicas = replicas
        if revision_history_limit is not None:
          self.revision_history_limit = revision_history_limit
        self.selector = selector
        self.service_name = service_name
        self.template = template
        if update_strategy is not None:
          self.update_strategy = update_strategy
        if volume_claim_templates is not None:
          self.volume_claim_templates = volume_claim_templates

    @property
    def pod_management_policy(self):
        """
        Gets the pod_management_policy of this V1StatefulSetSpec.
        podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.

        :return: The pod_management_policy of this V1StatefulSetSpec.
        :rtype: str
        """
        return self._pod_management_policy

    @pod_management_policy.setter
    def pod_management_policy(self, pod_management_policy):
        """
        Sets the pod_management_policy of this V1StatefulSetSpec.
        podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.

        :param pod_management_policy: The pod_management_policy of this V1StatefulSetSpec.
        :type: str
        """

        self._pod_management_policy = pod_management_policy

    @property
    def replicas(self):
        """
        Gets the replicas of this V1StatefulSetSpec.
        replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.

        :return: The replicas of this V1StatefulSetSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1StatefulSetSpec.
        replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.

        :param replicas: The replicas of this V1StatefulSetSpec.
        :type: int
        """

        self._replicas = replicas

    @property
    def revision_history_limit(self):
        """
        Gets the revision_history_limit of this V1StatefulSetSpec.
        revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.

        :return: The revision_history_limit of this V1StatefulSetSpec.
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """
        Sets the revision_history_limit of this V1StatefulSetSpec.
        revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet's revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.

        :param revision_history_limit: The revision_history_limit of this V1StatefulSetSpec.
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def selector(self):
        """
        Gets the selector of this V1StatefulSetSpec.
        selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

        :return: The selector of this V1StatefulSetSpec.
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1StatefulSetSpec.
        selector is a label query over pods that should match the replica count. It must match the pod template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

        :param selector: The selector of this V1StatefulSetSpec.
        :type: V1LabelSelector
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")

        self._selector = selector

    @property
    def service_name(self):
        """
        Gets the service_name of this V1StatefulSetSpec.
        serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.

        :return: The service_name of this V1StatefulSetSpec.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this V1StatefulSetSpec.
        serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \"pod-specific-string\" is managed by the StatefulSet controller.

        :param service_name: The service_name of this V1StatefulSetSpec.
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")

        self._service_name = service_name

    @property
    def template(self):
        """
        Gets the template of this V1StatefulSetSpec.
        template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.

        :return: The template of this V1StatefulSetSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1StatefulSetSpec.
        template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet.

        :param template: The template of this V1StatefulSetSpec.
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

    @property
    def update_strategy(self):
        """
        Gets the update_strategy of this V1StatefulSetSpec.
        updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.

        :return: The update_strategy of this V1StatefulSetSpec.
        :rtype: V1StatefulSetUpdateStrategy
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        """
        Sets the update_strategy of this V1StatefulSetSpec.
        updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template.

        :param update_strategy: The update_strategy of this V1StatefulSetSpec.
        :type: V1StatefulSetUpdateStrategy
        """

        self._update_strategy = update_strategy

    @property
    def volume_claim_templates(self):
        """
        Gets the volume_claim_templates of this V1StatefulSetSpec.
        volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.

        :return: The volume_claim_templates of this V1StatefulSetSpec.
        :rtype: list[V1PersistentVolumeClaim]
        """
        return self._volume_claim_templates

    @volume_claim_templates.setter
    def volume_claim_templates(self, volume_claim_templates):
        """
        Sets the volume_claim_templates of this V1StatefulSetSpec.
        volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.

        :param volume_claim_templates: The volume_claim_templates of this V1StatefulSetSpec.
        :type: list[V1PersistentVolumeClaim]
        """

        self._volume_claim_templates = volume_claim_templates

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1StatefulSetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
