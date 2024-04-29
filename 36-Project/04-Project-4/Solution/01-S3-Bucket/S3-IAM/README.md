aws iam list-open-id-connect-providers


aws iam create-policy --policy-name s3-policy-2 --policy-document file://s3-policy.json


aws iam create-role --role-name s3-role-2 --assume-role-policy-document file://demo-role-binding.json"


aws iam attach-role-policy --role-name s3-role-2 --policy-arn=arn:aws:iam::153808439998:policy/s3-policy-2


kubectl annotate serviceaccount demo-sa-s3 eks.amazonaws.com/role-arn=arn:aws:iam::153808439998:role/s3-role-2
