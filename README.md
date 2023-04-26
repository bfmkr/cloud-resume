# README

Welcome to the GitHub repository for my resume website <https://www.bmkrresume.com> which was built to be highly available and cost efficient using serverless technologies on AWS in the spirit of the original [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/) by [@forrestbrazeal](https://twitter.com/forrestbrazeal).

I embarked on this project to shore up the knowledge gained from studying for the [AWS Certified Cloud Practitioner](https://aws.amazon.com/certification/certified-cloud-practitioner/) qualification.

The following services and technologies were used in this project.

* **Amazon S3**: for static website hosting
* **Amazon Cloudfront**: for content delivery from the S3 bucket with HTTPS
* **Amazon Route 53**: for DNS
* **AWS Certificate Manager**: for the HTTPS certificate
* **Cloudflare**: for registering my domain name and setting up custom email routing.
* **AWS CloudFormation**: for Infrastructure as Code.
* **AWS SAM**: For building the serverless application.
* **Amazon API Gateway**: for the serverless API.
* **Amazon DynamoDB**: for the database storing information for the website's visitor counter.
* **AWS Lambda**: for event management within the serverless API.
* **AWS SDK for Python (Boto3)**: for the backend Lambda functions and testing.
* **GitHub/git**: for source control
* **GitHub Actions**: for automated deploying to AWS in a CI/CD pipeline.
* **HTML/CSS/JavaScript**: for the static website functionality.

It may be of interest to read about [things I would do if I had more time](notes/If%20I%20had more%20time.md), or [parts I found challenging along the way](notes/Challenging%20parts.md).
