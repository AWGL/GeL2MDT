#!/bin/bash



source activate gel2mdt

cd /home/webapps/gel2mdt/GeL2MDT/gelweb/
python manage.py shell_plus < run_batch_update.py

echo " $(date +'%Y-%m-%d')-$(date +'%s')-upload_attempted" >> logs/upload_log.txt
