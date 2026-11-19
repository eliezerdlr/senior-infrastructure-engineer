# Microsoft Entra ID and Active Directory integration

Use current Microsoft documentation for tenant-specific implementation. The links below were reachable when this skill was authored; licensing and feature availability can change.

## Architecture boundary

- Active Directory Domain Services commonly authenticates human users and computers on-premises.
- Microsoft Entra ID provides cloud identities, application registrations, service principals, managed identities and workload identity controls.
- A multi-team application can use OIDC or SAML for user sign-in and map Entra groups or application roles to application RBAC.
- SCIM can automate user/group provisioning when the application supports it.
- LDAP/LDAPS is a compatibility path, not the preferred cloud application integration.
- User authentication and agent workload authentication are separate. Do not give an agent a human user's session or password.

## Workload identity controls

For an agent service principal or managed identity:

1. create separate identities per environment and trust boundary;
2. assign owners and lifecycle metadata;
3. prefer managed identities or workload identity federation;
4. constrain federation issuer, subject and audience exactly;
5. grant resource-specific application permissions rather than broad directory roles;
6. require admin consent only through the approved change path;
7. evaluate Conditional Access for workload identities where supported and licensed;
8. review sign-in, audit, consent and role-assignment logs;
9. schedule access reviews or an equivalent owner attestation;
10. disable, validate dependencies, revoke grants/credentials and then delete on retirement.

Conditional Access for workload identities is not a substitute for least privilege. Access reviews do not automatically prove that a workload still needs every underlying resource permission. Confirm both the identity assignment and downstream authorization.

## Official Microsoft references

- [Workload identities overview](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview)
- [Conditional Access for workload identities](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity)
- [Govern Microsoft Entra service accounts](https://learn.microsoft.com/en-us/entra/architecture/govern-service-accounts)
- [Access reviews overview](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)
- [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)
- [Certificate credentials for application authentication](https://learn.microsoft.com/en-us/entra/identity-platform/certificate-credentials)

These links support design decisions; they do not establish that a tenant has the required licence, configuration or enforcement.
