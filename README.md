# awsSupport
Contains firmware form MINTS AWS support

## Create a thing on IOT-Core 
The thing for now is meant to represent all IOT devices which are present. The 'mintsThings' is meant to be representing only PM2.5, latitude and longitude columns representing only information needed to serve sharedairdfw.com. 

### How to 
Create a thing called mintsThings. 
AWSIOT--> Manage --> All devices --> Things and then press Create things. 
create single thing -->
Enter thing name as 'mintsThings"
create thing type as 'mintsThing'
Hit next 
---->
Generate a auto generate certificates
---->
Create a policy (This is an access policy)
--> Policy name can be anything -> 'mintsThingPolicy'
below make sure to attach allow all policy actions and policy resources by putting stars on under both actions and resources 
--> Attach policies to certificate -> attach the recently created policy. 
--> push create thing 
---->
Download certificates and keys
At this point download all the keys. There should be 5 files all togeather. Click done. 
---->
At this point attach the certificates to both the relevant policy and thing. 
-> AWS IOT -> Security -> Certificates 
-> Select relavan policy and from the actions button add it to both the relevant policy and thing. 

---> Add the relevant codes to AWS credentials folder.

https://www.youtube.com/watch?v=adKuyckikuw&t=593s
https://github.com/binaryupdates/aws-raspberrypi/blob/main/pipython.py


---------
Partition Keys 
