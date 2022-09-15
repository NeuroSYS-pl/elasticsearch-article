# What is this repo about?
:information_source: In this repository we've contained all notebooks, results, datasets, and other files that we've used in our blogposts.

:ok_hand: Everything is reproducible and contenerized so you don't need to worry about installing anything.


## Installation
**Build and run**
```bash
docker-compose up --build
```
to build all containers and run the application.

Or run it in the background with
```bash
docker-compose up -d --build
```

:star2: Now you can access the application at http://localhost:8080, if prompted for the password, use the password `docker`.


**Teardown**

If, at any point, you would like to stop the containers and clean up any remaining data, run the following command:
```bash
docker-compose down --volumes
```
This will stop the containers and delete any stored data in Elasticsearch node.



## Ingredients
### Data
`data` folder contains all the neccessary data for the tests.
That includes:
 - ***[SQUAD 2.0 dataset](https://rajpurkar.github.io/SQuAD-explorer/)***, and all our variations of it.
 - SwiftUI dataset, from ***[Stanford SwiftUI courses](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG)***.

How we changed and used the dataset is described in the [README](data/README.md) file.

### Experiments
`experiments` folder contains all the experiments we ran.
All files are titled `experiment_*` and the second part is the name of the experiment.

All results are stored in the `experiments/results` folder and are reproducible via `experiment.*` notebooks.


#### Utils
We've also included some useful utilities for example for scoring the results or indexing Elasticsearch.


## References
| Name | Link |
|----------------|-------------|
|Elasticsearch|https://www.elastic.co/elasticsearch/|
|Project Jupyter|https://jupyter.org/|
|Docker|https://www.docker.com/|

