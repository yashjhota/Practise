import wikipedia
import click


@click.command()
@click.option("--name", prompt="Enter the name of the company", default="Microsoft")
@click.option("--length", prompt="Enter the number of sentences", default=1)
def summary(name, length):

    result = wikipedia.summary(name, sentences=length)

    click.echo(click.style(result, fg="green", bold=True))
    click.echo(click.style("Summary fetched successfully!", fg="blue", bold=True))
    click.echo(
        click.style(
            "Thank you for using the Wikipedia summary bot!", fg="yellow", bold=True
        )
    )
    click.echo(click.style("Have a great day!", fg="red", bold=True))
    click.echo(click.style("Exiting the program...", fg="magenta", bold=True))
    click.echo(click.style("Goodbye!", fg="cyan", bold=True))


if __name__ == "__main__":
    summary()


# def summary(name="Microsoft",length=1):
#     result = wikipedia.summary(name, sentences=length)
#     return result


# print(summary())
# print(summary("Apple", 3))
# print(summary("Tesla", 4))
# print(summary("Amazon", 5))
# print(summary("Meta", 6))
# print(summary("Netflix", 7))
# print(summary("Twitter", 8))
# print(summary("Snap", 9))
