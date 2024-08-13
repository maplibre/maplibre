# MapLibre Security and Vulnerability Reporting Policy

## 1. Services Covered by this Policy

This policy covers all services directly operated by us (MapLibre).
Services can be identified by the following means:

- The website has a .well-known/security.txt that links to this policy.
- The reverse DNS of an IP address resolves to one of the following
 domain (or subdomains): maplibre.org

## 2. Acceptable Use

We generally invite security researchers to search for vulnerabilities
in our services. We kindly ask to not put any actual user data or
production systems at risk.

## 3. Classification of Vulnerabilities

We will consider a vulnerability report most likely as relevant if it
reports one of the following problems:

- Memory-safety issues in any MapLibre project
- The vulnerability can be used to directly access non-public
  information that either reveals further security relevant problems or
  contains user data, credentials, or sensitive data in general.
- The vulnerability can be used to disrupt the orderly operation of a
  service (Denial of Service).
- The vulnerability can be used to manipulate data within the service.
- XSS, CSRF, RCE, authentication/authorization bypass, SQL inections,
  etc are considered relevant.

We will consider a vulnerability report most likely as NOT relevant if
it reports one of the following problems:

- Missing security features, for example HTTP headers, if they are not
  actually preventing a vulnerability.
- Publicly accessible version strings of used software.
- Security vulnerablities that can only be used within the scope of the
  used account.

## 4. Reporting Vulnerabilities

Report vulnerabilities via e-mail to <security@maplibre.org>. MapLibre does not
offer a GPG key for encryption.

Please make sure that you include the following information:

- Which service is affected
- How can the bug be used/exploited
- Explanation of the risk

Reports will be answered within 48 hours. If you have not received an
answer within that time frame, feel free to contact us again.

For used open source software, we recommend to file bug reports and/or
pull requests against the upstream repositories. This includes hardening
instructions in the installation documentation.

## 5. Bug Bounties / Vulnerability Rewards

The MapLibre project does not currently pay rewards.

## 6. Acknowledgement

We list recognized reports of vulnerablities online if the reporting
security researcher agrees.

## 7. About this Policy

This policy is MIT licensed. Feel free to suggest modifications and
additions at <https://github.com/digitalfabrik/security-policy>.
