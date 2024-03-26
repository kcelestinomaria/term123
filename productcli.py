import typer
from rich.console import Console
from rich.table import Table


console = Console()

app = typer.Typer()


@app.command(short_help='adds a product')
def add(product: str, category: str):
    typer.echo(f"adding {product}, {category}")
    show()

@app.command(short_help='deletes a product')
def delete(position: int):
    typer.echo(f"deleting {position}")
    show()

@app.command(short_help='updates a product')
def update(position: int, product: str = "", category: str = ""):
    typer.echo(f"updating {position}")
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    show()

@app.command()
def show():
    products = [("Samsung Galaxy Pro Tab", "Tablets"), ("Lenovo Laptop", "Laptops")]
    console.print("[bold magenta]Products[/bold magenta]!", "")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Product", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Purchased", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Smartphones': 'cyan', 'Laptops': 'red', 'Smartwatches': 'cyan', 'Tablets': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, product in enumerate(products, start=1):
        c = get_category_color(product[1])
        is_purchased_str = ':true' if True == 2 else ':false'
        table.add_row(str(idx), product[0], f'[{c}]{product[1]}[/{c}]', is_purchased_str)

    console.print(table)

if __name__ == "__main__":
    app()