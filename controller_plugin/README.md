# Controller Plugin
This module process fitness given by monitor endpoint and produces a metric that represent the relation between the behavior of our application and what we expect to be.

### How to use this module?
```python
def some_asperathos_controller_function(args):
    monitor_url = "https://example:8080/monitor" # endpoint of monitor
    spent_time = get_real_time() # Generic function that return timestamp between app initialization and now
    fitness_limit = 80 # Fitness that we want to catch up
	time_limit = 10 # Time limit to catch up expected fitness
	ia_controller = IAsperathosController(time_limit)
	evaluation_value = ia_controller.evaluate_effiency(monitor_url,fitness_limit,spent_time)
```
