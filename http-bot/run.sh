#!/bin/bash
url="http://localhost:12345/upload"
worker=1
# docker run download-bot:latest --url "https://ncl-ctf.ctfd.io/files/24b38468d88509cc98f9e83f541c87a3" --filename "Level1.exe" --worker 1 --token "eyJ1c2VyX2lkIjoxMjMsInRlYW1faWQiOjY3LCJmaWxlX2lkIjo2fQ.X-slAQ.2rb93VcU0amV8i8hE7uWD9LiW-8"
# docker run download-bot:latest --url $url --filename $filename --worker $worker --token $token
echo "python3 upload_starter.py  --url $url --filename $filename --token $token --worker $worker --function $function --protocol $protocol
