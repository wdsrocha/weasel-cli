import random
import string

import click


@click.command()
@click.option('--target', default='METHINKS IT IS LIKE A WEASEL')
@click.option('--population-size', default=100, type=int)
@click.option('--mutation-rate', default=.05, type=float)
def cli(target, population_size, mutation_rate):
    charset = string.ascii_uppercase + ' '
    best_subject = ''.join(random.choices(charset, k=len(target)))

    def mutate(subject):
        return ''.join(
            c if random.random() >= mutation_rate
            else random.choice(charset) for c in subject)

    def evaluate(subject):
        return sum(a == b for a, b in zip(subject, target))

    generation = 0
    while True:
        population = population_size * [best_subject]
        population = map(mutate, population)
        best_subject = max(population, key=evaluate)
        score = evaluate(best_subject)
        click.echo(
            f'{generation}: {best_subject} -- score: {score}/{len(target)}')
        if score == len(target):
            return 0
        generation += 1
