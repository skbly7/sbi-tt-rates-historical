sudo service tor restart
#sleep 5
#curl --socks5 localhost:9050 https://www.sbi.co.in/documents/16012/1400784/FOREX_CARD_RATES.pdf --output ~/sbi-tt-rates-historical/$(date '+%Y-%m-%d-%H:%M').pdf
curl https://www.sbi.co.in/documents/16012/1400784/FOREX_CARD_RATES.pdf --output ~/sbi-tt-rates-historical/$(date '+%Y-%m-%d-%H:%M').pdf
ls | grep -e 2020 -e 2021 -e 2022 | sed -e "s/-........\.pdf//" | uniq | awk '{print "mkdir " $1}' | bash
ls -1 | grep -e 2020 -e 2021 -e 2022 | awk -F"-" '{print "mv "$0" "$1"-"$2}' | bash
git add .
git config user.email "noreply@shivamkhandelwal.in"
git config user.name "Shivam Khandelwal (auto commit)"
git commit -m "Daily update $(date '+%Y-%m-%d-%H:%M')"
git push origin master
