#!/bin/bash -e
coverage run manage.py test
coverage html
open htmlcov/index.html

#RDS情報(マスターユーザ)
#disc_v1
#khN3F6UQYxJvfPXVxLj7
#discriminator-v1-db.cwcfv6dzfauo.ap-northeast-1.rds.amazonaws.com