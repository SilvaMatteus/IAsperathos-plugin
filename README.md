# IAsperathos-plugin

## About it

**NOTE:** This project is being developed as part of the [_Distributed Systems_ course](https://sites.google.com/site/ufcgsd/), so because really the short time to develop, it ins't recommended to be deployed in prodution yet.

The IAsperathos plugin is a plugin developed to make the [Asperathos](https://github.com/bigsea-ufcg/bigsea-manager)
able to handle with AI applications that execute genetic algorithms.

This plugin, as other plugins in Asperathos, needs some changes in
the applications to be submitted. Actually, the plugin only needs
that the application submitted logs the fitness value in `/home/<username>/fitness_status.log`.
