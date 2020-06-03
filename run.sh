wget https://www.sbi.co.in/documents/16012/1400784/FOREX_CARD_RATES.pdf -O ~/sbi-tt-rates-historical/$(date '+%Y-%m-%d-%H:%M').pdf
git add .
git commit -m "Daily update $(date '+%Y-%m-%d-%H:%M')"
git push origin master
