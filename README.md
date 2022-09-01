<p align="center" style="font-size: 103px; font-weight:bold; color: transparent; -webkit-background-clip: text; background-clip: text; background-image: linear-gradient(90deg, red, orange, fuchsia);">
    User filter
</p>


![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) 
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
-----


## Why:
> This project clearly demonstrates the work of `FastAPI` + `MongoDB`. \
> In this project there is one route that can: 

> 1. Filter data by these parameters:
```python
from typing import Optional

from pydantic import BaseModel, Field


class QueryUser(BaseModel):
    ageStart: Optional[int] = Field(description="Start with", default=None)
    ageEnd: Optional[int] = Field(description="Finish on", default=None)
    company: Optional[str] = Field(description="Company", default=None)
    gender: Optional[str] = Field(description="User gender", default=None)
    jobTitle: Optional[str] = Field(description="Job title", default=None)
    joinDateStart: Optional[str] = Field(description="Start with", default=None)
    joinDateEnd: Optional[str] = Field(description="Finish on", default=None)
    salaryStart: Optional[int] = Field(description="Start with", default=None)
    salaryEnd: Optional[int] = Field(description="Finish on", default=None)

```


-----


## Setup:
> ```shell
> # SSH
> git clone git@github.com:xristxgod/USER-FILTER.git
> # HTTPS
> git clone https://github.com/xristxgod/USER-FILTER.git
> ```


-----


## Settings in .prod.env file:
> `MONGODB_NAME` - Database name
> 
> `MONGODB_COLLECTION` - Collection name
> 
> `MONGODB_URL` - Database url


-----


## How to run:
> ```shell
> # Run
> docker-compose -f docker-compose.yml up --build
> # Stop
> docker-compose -f docker-compose.yml stop
> ```


-----


### Screenshot of the work:
![image](https://user-images.githubusercontent.com/84931791/187871247-f20c562f-41be-4630-9683-9a71d230e30a.png)
