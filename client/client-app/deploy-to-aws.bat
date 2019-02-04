:: This script builds and deploys the Angular 2 project to an s3 bucket titled "smart-lot.io"
ng build --prod --aot
aws s3 cp ./dist s3://smart-lot.io --recursive --acl public-read