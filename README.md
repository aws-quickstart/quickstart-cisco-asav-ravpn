# quickstart-cisco-asav-ravpn
## Cisco Systems on the AWS Cloud

This Quick Start reference deployment guide provides step-by-step instructions for deploying a scalable Cisco Remote Access Virtual Private Network (RA-VPN) on the AWS Cloud. This Quick Start is for users who want to deploy or learn about Cisco AnyConnect RA-VPN services on Cisco Adaptive Security Virtual Appliance (ASAv) firewalls using the AWS Cloud architecture.

### Cisco scalable RA-VPN on AWS
As companies address the ever-increasing demand for secure remote connectivity, the need for a stable and scalable RA-VPN has increased. For many organizations, investing in additional hardware appliances to scale up a network’s infrastructure may not meet timeline objectives and available budgets. But, cloud-based architectures provide computing environments that are highly scalable and flexible in terms of both costs and resources.

**Note:** This deployment can be integrated with both multi-factor authentication (MFA) and authentication, authorization, and accounting (AAA), such as Cisco Duo. For more information, see Duo MFA on AWS.

Please know that we may share who uses AWS Quick Starts with the AWS Partner that collaborated with AWS on the content of the Quick Start.

### Cost and licenses
You are responsible for the cost of the AWS services used while running this Quick Start reference deployment. There is no additional cost for using the Quick Start.

The AWS CloudFormation template for this Quick Start includes configuration parameters that you can customize. Some of these settings, such as instance type, affect the cost of deployment. For cost estimates, see the pricing pages for each AWS service you use. Prices are subject to change.

This Quick Start requires an RA-VPN license from Cisco. The Cisco ASAv virtual firewall provides the following licensing options:

- **Option 1:** Use AWS pay-as-you-go licensing, which is based on hourly billing. This is the default option for this Quick Start.
- **Option 2:** Use Amazon’s Bring Your Own License (BYOL) model in conjunction with Cisco’s Smart Licensing.

To use this Quick Start in a production environment, see [Cisco Adaptive Security Virtual Appliance (ASAv) — Standard Package](https://aws.amazon.com/marketplace/pp/Cisco-Systems-Inc-Cisco-Adaptive-Security-Virtual-/B00WH2LGM0). Ensure that you subscribe to the image using the correct Region. If you want to use option 2, you must use the correct Amazon Machine Image (AMI). For more information, see how to [Deploy the ASAv on the AWS Cloud](https://www.cisco.com/c/en/us/td/docs/security/asa/asa913/asav/getting-started/asav-913-gsg/asav_aws.html).

**Note:** If you don’t have your own license, the ASAv uses a trial license with reduced capacity. It provides 90 days of free usage and up to two AnyConnect VPN sessions within a nonproduction environment where firewall throughput is limited to 100 Kbps. To upgrade to a production license, see the [Cisco documentation](https://www.cisco.com/c/en/us/td/docs/security/asa/asa913/configuration/general/asa-913-general-config/intro-license-smart.html#task_03242D29B58D4DB9B95F4F844973CE2E).

This Quick Start requires a subscription to the Amazon Machine Image (AMI) for Cisco RA VPN, which is available from [AWS Marketplace](https://aws.amazon.com/marketplace/pp/Cisco-Systems-Inc-Cisco-Adaptive-Security-Virtual-/B00WH2LGM0). Additional pricing, terms, and conditions may apply. For more information, see the [deployment guide](https://fwd.aws/Ebm5R).

### Architecture
Deploying this Quick Start with **default parameters** builds the following environment in a specific account and Region in the AWS Cloud.
![quickstart-sumo-logic-security-integrations](https://d0.awsstatic.com/partner-network/QuickStart/datasheets/cisco-asav-ravpn-architecture-diagram.png)

For architectural details, best practices, step-by-step instructions, and customization options, see the [deployment guide](https://fwd.aws/Ebm5R).

To post feedback, submit feature ideas, or report bugs, use the **Issues** section of this GitHub repo.

If you want to submit code for this Quick Start, see the [AWS Quick Start Contributor's Guide](https://aws-quickstart.github.io/).
