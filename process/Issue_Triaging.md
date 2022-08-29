# Issue Triaging

Triaging an issue is a multi-step process that is collaboratively performed by community. Triaging an issue usually takes around one business day but may take longer, for example, when the reviewer is not around. Goal of triaging is to provide you with a clear understanding of what will happen to your issue. For example, after your feature request was triaged you know whether we plan to tackle the issue or whether we'll wait to hear what the broader community thinks about this request.


## Terminologies

* TSC: Technical Steering Committee. An informal group of people who meet on a monthly basis and discuss technical topics related to software development. Everyone is welcome to join the Technical Steering Committee. Refer to the charter for more details.


## Process

The basic process of triaging issues is

|First Step     |Next Step            |Result     |
|---            |---                  |---        |
|TSC review ->  |Accepted, or         |
|               |Community review ->  |Closed, or |
|               |                     |Accepted   |

Please note:
1. TSC reviewers can accept an issue but cannot close an issue before it is being reviewed by the community (the "Community Review" step).
2. Associating PRs to open issues is highly recommended.
3. "Accepted" issues will be added to Github milestones and will get prioritized.

Issues can be at four major states during this process. They are easily identifiable:

|State|What your GitHub issue looks like|
|---|---|
|TSC Review|matches the query `label:"tsc-review"`|
|Community Review|matches the query `milestone:"Backlog Candidates"`|
|Accepted|has any milestone except `Backlog Candidates`|
|Closed|matches the query `is:closed`|

In the rest of this document, we'll go into more detail about each of the activities of triaging.


## TSC Review

TSC rotates a primary and a secondary reviewer every week. The reviewers triage issues by assigning the following labels:

### Categorization Labels

Each issue must have a **type** label. Most type labels are grey, some are yellow. Bugs are grey with a touch of red.

|Type|Description|
|---|---|
|[`needs-more-info`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | not possible to assign a type label due to missing information|
|[`bug`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | the implementation of a feature is not correct|
|[`feature-request`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | request for a new feature|
|[`tech-debt`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | improve the implementation/architecture/engineering efficiency|
|[`*question`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | we should direct questions to StackOverflow|

### Platform Labels

Each issue must have a **platform** label. 

|Platform|Description|
|---|---|
|[`ios-simulator`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | iOS Simulator|
|[`ios-device`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Physical iOS device|
|[`android-simulator`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Android Simulator |
|[`android-device`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Physical Android device|
|[`macos-x86`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Mac OS |
|[`macos-arm`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | M-series chips Mac OS |
|[`linux`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Linux |
|[`qt`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Qt |
|[`node`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Node.JS |
|[`all-platforms`](https://github.com/maplibre/maplibre-gl-native/labels/xx) | Across all platforms |

### Important Issues

The TSC reviewers may add `important` labels to issues that
- Critical security vulnerabilities
- Stability or performance issue that makes a feature unusable

### Other labels

If issues are suitable for beginners we may add the `good-first-issue` label and we add code pointers that help beginners to get started with a PR.

Sometime, we get issues that we can't or don't have the time to reproduce due to the complexity or time requirements of the setup but that we indeed suspect to be issues. We label those issues with `investigation-wanted`. What we are looking for is help in reproducing and analyzing the issue.


## Community Review

### Accepting issue
Community members can "up-vote" an issue (adding a GitHub +1/"👍" reaction to the issue description). If an issue surpasses the 20 up-votes in 60 days, the issue will be accepted.

### Closing issue

Community members can also close an issue after reviewing it, for the following reasons:

|Reason|Label|
|---|---|
|It's a duplicate of another issue. | `*duplicate`|
|What is described is the designed behavior. | `*as-designed`|
|The issue is a developer question, should be direct to Github Discussion or our Slack channel| `*dev-question`|
|The issue is a user question, should be direct to Github Discussion or our Slack channel| `*user-question`|
|Given the information we have we can't reproduce the issue. | `*not-reproducible`|
|The feature request is out of scope.  | `*out-of-scope`|

In this case, other than adding these labels, we also encourage the community members to add explicit and specific comments about the reason of closing this issue.