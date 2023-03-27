## AvailabilityScripts

- Install python 
`brew install python`
!Use python 2.7

- You can use VSCode or Pycharm as Code Editor

- Install Pip 

`python -m ensurepip –upgrade or python3 -m ensurepip –upgrade`

- Install Requirements

`pip install pipreqs`

## To Create New Requests :

- Use postman with the request and : 

>  generate code > python > requests

include that code in the Requests>authorization_request.py file
 
## To Run :

- Run availability tests

`python main.py`

## Cron Creation :

1. Open Terminal.
2. Write crontab -e to create crontab.
3. Press i to launch edit mode;
4. Write the schedule command [reference](https://crontab.guru/#24_17_*_*_1-5)

 `30 8 * * 1-5 cd /<direccion al archivo>/ && python main.py`
 
5. Press esc to exit edit mode;
6. Write :wq to write your crontab

> - To delete the running job:
> - To delete the entire crontab: Run crontab -r
> - To delete a single cron job: Go to crontab -e, press i, press dd and press :wq to write the file. 

[Referencia Creacion de Cron](https://www.jcchouinard.com/python-automation-with-cron-on-mac/)