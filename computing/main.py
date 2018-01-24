import gengine
import environment


# noinspection PyUnusedLocal
def end_stop_condition(i, result_set):
    return float(result_set.best) <= 0.01


engine = gengine.Engine()
engine.environment = environment.Environment(11, 5)
engine.population_size = 300
engine.make_population()
engine.retained_pct = 75
engine.generation_nbr = 1000
engine.mutation_probability = 0.2
engine.end_stop_condition = end_stop_condition
engine.best_is = engine.SMALLEST
engine.run()
