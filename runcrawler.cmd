for /F "tokens=*" %%A in ('type "Redmi 6 Pro.txt"') do scrapy crawl amazon -o out.csv -a url=%%A
rem scrapy crawl amazon -o %1.csv -a File=%1