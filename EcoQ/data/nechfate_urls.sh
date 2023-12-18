curl -s https://nechfate.ma/feed/ | grep -oE 'https://nechfate.ma/[a-z-]*/' | grep -Ev 'wp|feed' | sort -u |tee urls.txt
