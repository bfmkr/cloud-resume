# Extensions to the cloud resume challenge

Below are a few extensions I made to the original cloud resume challenge.

* [Back to README](../README.md)

## Email routing

* I decided to leverage the free email routing features from my domain registrar (Cloudflare) in order to receive emails from `ben@bmkrresume.com` to my gmail inbox.

* This involved configuring a combination of MX and TXT records in my DNS settings on Cloudflare.  
  As a catch-all, emails to `<anything-goes-here>@bmkrresume.com` will also forward to my gmail inbox. 
  I simply clicked a checkbox on Cloudflare to set this up.

* To enable *sending* emails from `ben@bmkrresume.com` I had to configure this as an alias in gmail.
  I also needed to add the appropriate spf and dmarc TXT records in Cloudflare to ensure they wouldn't be considered as spam by recipients.
  In gmail:

    ```
    Settings > Accounts and Import > Send mail as: > Add another email address

    Name:          Ben McKeever
    Email Address: ben@bmkrresume.com
    [x] Treat as alias

    SMTP Server: smtp.gmail.com       Port: 465
    Username:    bfmckeever
    Password:    <APP PASSWORD>
    ```

* In Cloudflare:

    ```
    DNS >  Records > Add record

    Type:    TXT
    Name:    bmkrresume.com
    TTL:     auto
    Content: v=spf1 include:_spf.mx.cloudflare.net include:_spf.google.com ~all 

    Type:    TXT
    Name:    _dmarc
    TTL:     auto
    Content: v=DMARC1; p=none;

    Type:    MX
    Name: bmkrresume.com
    Priority 43
    Value: route1.mx.cloudflare.net

    Type:    MX
    Name: bmkrresume.com
    Priority 52
    Value: route2.mx.cloudflare.net

    Type:    MX
    Name: bmkrresume.com
    Priority 50
    Value: route3.mx.cloudflare.net
    ```

## Testing code locally with Docker

* With the command `sam local invoke <Lambda-handler>` I was able to run my individual AWS Lambda handlers written in boto3 python code within a local docker container rather than running them on the cloud. 

    This approach speeds up development time, and all of the docker specific details like pulling images from a registry and running the containers are done under the hood by the aws `sam` command. Very convenient.