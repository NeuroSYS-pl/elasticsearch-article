# What is this repo about?

:information_source: In this repository we've contained all

- notebooks,
- results,
- datasets,
- utility files and configs,
- all other files that we've used in our blogposts.

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

:star2: Now you should see that the container started and port with token can be found in the docker logs, app should be located at localhost:8888/"token".

**Teardown**

If, at any point, you would like to stop the containers and clean up any remaining data, run the following command:

```bash
docker-compose down --volumes
```

This will stop the containers and delete any stored data in Elasticsearch node.

**Phonetic Analysis Plugin**

In order to recreate the results of one of the experiments using phonetic analyzer, you have to install phonetic analysis plugin within the Elasticsearch container:

1. Run bash within the container

```bash
 docker exec -it elasticsearch_service /bin/bash
```

2. Install the plugin and exit the container

```bash
bin/elasticsearch-plugin install analysis-phonetic
exit
```

3. Restart the Elasticsearch container

```bash
docker restart elasticsearch_service
```

## Ingredients

### Data

`data` folder contains all the neccessary data for the tests.
That includes:

- **_[SQUAD 2.0 dataset](https://rajpurkar.github.io/SQuAD-explorer/)_**, and all our variations of it.
- SwiftUI dataset, from **_[Stanford SwiftUI courses](https://www.youtube.com/playlist?list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG)_**.

How we changed and used the dataset is described in the [README](data/README.md) file.

### Experiments

`experiments` folder contains all the experiments we ran.
All files are titled `experiment_*` and the second part is the name of the experiment.

All results are stored in the `experiments/results` folder and are reproducible via `experiment.*` notebooks.

#### Utils

We've also included some useful utilities for example for scoring the results or indexing Elasticsearch.

## References

| Name            | Link                                  |
| --------------- | ------------------------------------- |
| Elasticsearch   | https://www.elastic.co/elasticsearch/ |
| Project Jupyter | https://jupyter.org/                  |
| Docker          | https://www.docker.com/               |
